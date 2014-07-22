import urllib 
import json
import awspricing.mapper
from awspricing.base import Base

class Rds(Base):
    """ Class for RDBMS pricing. """

    def __init__(self):
        Base.__init__(self)
        self.rds_json = {
            'mysql_std': self.getJSON("http://a0.awsstatic.com/pricing/1/oracle/pricing-li-standard-deployments.min.js"),
            'oracle_std': self.getJSON("http://a0.awsstatic.com/pricing/1/oracle/pricing-li-standard-deployments.min.js"),
            'oracle_byol': self.getJSON("http://a0.awsstatic.com/pricing/1/oracle/pricing-byol-standard-deployments.min.js"),
            'mssql_std': self.getJSON("http://a0.awsstatic.com/pricing/1/sqlserver/sqlserver-li-se-ondemand.min.js")
        }
        self.rds_dbengine = {
            'mysql_std': ['MYSQL51', 'MYSQL55'],
            'oracle_std': ['ORACLE11G'],
            'oracle_byol': ['ORACLE11GX', 'ORACLE11GEX'],
#            'mssql_std': ['mssql_std']
        }
        self.io_json = self.getJSON("http://a0.awsstatic.com/pricing/1/rds/sqlserver/pricing-provisioned-db-standard-deploy.min.js")
        self.currency = self.rds_json['mysql_std']['config']['currencies'][0]
        self.rate = self.rds_json['mysql_std']['config']['rate']

    def getSQL(self):
        """ Returns a list of SQL statements.

        :returns: a list of SQL statemnets that contains pricing data.
        :rtype: list
        """
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
            if pricing_type != 'mssql_std':
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
        """ Returns a list of CSV.

        :returns: a list of CSV that contains pricing data.
        :rtype: list
        """
        csv = []
        std_storage_rate = dict()
        std_io_rate = dict()
        csv.append("Product Size, DB engine, Region ID, Currency, Pricing, I/O Rate, Storage Rate")
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
                        try:
                            pricing = "%.3f" % float(tier['prices'][self.currency])
                        except ValueError:
                            pricing = "0"
                        row = "%s, %s, %s, %s, %s, %s, %s" % (product_size, pricing_type, region_id,
                                                              self.currency, pricing, std_io_rate[region_id],
                                                              std_storage_rate[region_id])
                        csv.append(row)
        return csv

    def getJSON(this, url):   

        """ Returns JSON from the Javascript
            Ugly but it works
        """
        pricing_data = urllib.urlopen(url).read()
        find = pricing_data.find("callback(")
        pricing_data = pricing_data[find+9:]
        pricing_data = pricing_data[:-2]
        pricing_data = pricing_data.replace('vers:', '"vers":')
        pricing_data = pricing_data.replace('config:', '"config":')
        pricing_data = pricing_data.replace('currencies:', '"currencies":')
        pricing_data = pricing_data.replace('USD:', '"USD":')
        pricing_data = pricing_data.replace('valueColumns:', '"valueColumns":')
        pricing_data = pricing_data.replace('rate:', '"rate":')
        pricing_data = pricing_data.replace('rates:', '"rates":')
        pricing_data = pricing_data.replace('regions:', '"regions":')
        pricing_data = pricing_data.replace('region:', '"region":')
        pricing_data = pricing_data.replace('type:', '"type":')
        pricing_data = pricing_data.replace('types:', '"types":')
        pricing_data = pricing_data.replace('name:', '"name":')
        pricing_data = pricing_data.replace('tiers:', '"tiers":')
        pricing_data = pricing_data.replace('prices:', '"prices":')
        pricing_data = pricing_data.replace('storageRate:', '"storageRate":')
        return json.loads(pricing_data)
