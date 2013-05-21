import urllib 
import json
import awspricing.mapper
from awspricing.base import Base

class Rds(Base):
    def __init__(self):
        Base.__init__(self)
        self.rds_json = {
            'mysql_std': json.loads(urllib.urlopen("http://aws.amazon.com/rds/pricing/mysql/pricing-standard-deployments.json").read()),
            'oracle_std': json.loads(urllib.urlopen("http://aws.amazon.com/rds/pricing/oracle/pricing-li-standard-deployments.json").read()),
            'oracle_byol': json.loads(urllib.urlopen("http://aws.amazon.com/rds/pricing/oracle/pricing-byol-standard-deployments.json").read()),
            'mssql_std': json.loads(urllib.urlopen("http://aws.amazon.com/rds/pricing/sqlserver/sqlserver-li-se-ondemand.json").read())
        }
        self.rds_dbengine = {
            'mysql_std': ['MYSQL51', 'MYSQL55'],
            'oracle_std': ['ORACLE11G'],
            'oracle_byol': ['ORACLE11GX', 'ORACLE11GEX'],
            'mssql_std': ['mssql_std']
        }
        self.io_json = json.loads(urllib.urlopen("http://aws.amazon.com/rds/pricing/pricing-provisioned-db-standard-deploy.json").read())
        self.currency = self.rds_json['mysql_std']['config']['currencies'][0]
        self.rate = self.rds_json['mysql_std']['config']['rate']

    def getSQL(self):
        queries = []
        std_storage_rate = dict()
        std_io_rate = dict()
        rdbms_product_id = self.start_id
        for region in self.io_json['config']['regions']:
            region_id = awspricing.mapper.getRegionID(region['region'])
            for rate in region['rates']:
                if rate['type'] == 'ioRate':
                    std_io_rate[region_id] = rate['prices'][self.currency]
                elif rate['type'] == 'storageRate':
                    std_storage_rate[region_id] = rate['prices'][self.currency]
        for pricing_type in self.rds_json:
            for region in self.rds_json[pricing_type]['config']['regions']:
                region_id = awspricing.mapper.getRegionID(region['region'])
                for type in region['types']:
                    for tier in type['tiers']:
                        rds_name = "%s.%s" % (type['name'],tier['name'])
                        rds_spec = awspricing.mapper.getRdsSpec(rds_name)
                        product_size = rds_spec['product_size']
                        name = rds_spec['name']
                        core_count = rds_spec['core_count']
                        cpu_power = rds_spec['cpu_power']
                        memory_in_gb = rds_spec['memory_in_gb']
                        io_units = 1000000
                        maximum_storage_in_gb = 0
                        minimum_storage_in_gb = 5
                        description = "64-bit, %s GB RAM, %s x %s GHz CPU Core" %\
                                      (memory_in_gb, core_count, cpu_power)
                        try:
                            pricing = "%.3f" % float(tier['prices'][self.currency])
                        except ValueError:
                            pricing = "0"
                        for dbengine in self.rds_dbengine[pricing_type]:
                            query = "INSERT INTO rdbms_product VALUES(%i, %i, '%s', '%s', '%s', '%s', %i, %s, '%s', %i, %i, %s, %i, '%s', '%s', '%s', %s, %s, %s, %i);" %\
                                     (rdbms_product_id, self.cloud_id, region_id, dbengine, 'Y', 'I64',
                                      core_count, cpu_power, description, io_units, maximum_storage_in_gb,
                                      memory_in_gb, minimum_storage_in_gb, name, product_size, self.currency,
                                      pricing, std_io_rate[region_id], std_storage_rate[region_id], 1)
                            queries.append(query)
                            rdbms_product_id = rdbms_product_id + 1

        return queries

    def getCSV(self):
        csv = ["To be implemented."]
        return csv
