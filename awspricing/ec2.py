import urllib 
import json
import awspricing.mapper
import awspricing.ec2description as ec2desc
from awspricing.base import Base

class EC2(Base):
    """ Class for EC2 pricing. """
    def __init__(self):
        Base.__init__(self)
        pricing_list = { 'linux-od': "http://aws.amazon.com/ec2/pricing/json/linux-od.json",
                         'rhel-od': "http://aws.amazon.com/ec2/pricing/json/rhel-od.json",
                         'sles-od': "http://aws.amazon.com/ec2/pricing/json/sles-od.json",
                         'mswin-od': "http://aws.amazon.com/ec2/pricing/json/mswin-od.json",
                         'mswinSQL-od': "http://aws.amazon.com/ec2/pricing/json/mswinSQL-od.json",
                         'mswinSQLWeb-od': "http://aws.amazon.com/ec2/pricing/json/mswinSQLWeb-od.json" }
        self.json_data = dict()
        for pricing_type in pricing_list:
            self.json_data[pricing_type] = json.loads(urllib.urlopen(pricing_list[pricing_type]).read())

    def getSQL(self):
        """ Returns a list of SQL statements.

        :returns: a list of SQL statemnets that contains pricing data.
        :rtype: list
        """
        server_product_id = self.start_id
        active = 'Y'
        cpu_power = 1000
        prepayment_term_in_months = 0
        standard_pricing_prepaid  = 0
        software = ''
        queries = []
        for single_json in self.json_data.values():
            currency = single_json['config']['currencies'][0]
            for region in single_json['config']['regions']:
                region_id = awspricing.mapper.getRegionID(region['region'])
                for instanceType in region['instanceTypes']:
                    for size in instanceType['sizes']:
                        product_size = size['size']
                        core_count = ec2desc.getVirtualCores(product_size)
                        disk_in_gb = ec2desc.getStorageSize(product_size)
                        memory_in_gb = ec2desc.getMemorySize(product_size)
                        name = ec2desc.getName(product_size)
                        description = ec2desc.getDescription(product_size)
                        if product_size in ['t1.micro', 'c1.medium', 'm1.small', 'm1.medium']:
                            architectures = ['I32', 'I64']
                        else:
                            architectures = ['I64']
                        for value in size['valueColumns']:
                            if value['name'] == "mswin":
                                platform = "WINDOWS"
                            elif value['name'] == "linux":
                                platform = "UNIX"
                            elif value['name'] == "rhel":
                                platform = "RHEL"
                            elif value['name'] == "sles":
                                platform = "SLES"
                            elif value['name'] == "mswinSQL":
                                platform = "MSWINSQL"
                            elif value['name'] == "mswinSQLWeb":
                                platform = "MSWINSQLWEB"
                            try:
                                pricing_hourly = "%.3f" % float(value['prices'][currency])
                            except ValueError:
                                pricing_hourly = "0"
                            for architecture in architectures:
                                query = "INSERT INTO server_product VALUES(%i, %s, '%s', '%s', '%s', %s, %2.1f, '%s', %s, %2.3f, '%s', '%s', %s, '%s', '%s', '%s', %s, %5.2f);" % (
                                    server_product_id, self.cloud_id, product_size, active, architecture, core_count,
                                    cpu_power, description, disk_in_gb, memory_in_gb, name, platform,
                                    prepayment_term_in_months, region_id, software, currency,
                                    pricing_hourly, standard_pricing_prepaid)
                                queries.append(query)
                                server_product_id = server_product_id + 1
                                if platform == 'UNIX':
                                    query = "INSERT INTO server_product VALUES(%i, %s, '%s', '%s', '%s', %s, %2.1f, '%s', %s, %2.3f, '%s', '%s', %s, '%s', '%s', '%s', %s, %5.2f);" % (
                                        server_product_id, self.cloud_id, product_size, active, architecture, core_count,
                                        cpu_power, description, disk_in_gb, memory_in_gb, name, 'UNKNOWN',
                                        prepayment_term_in_months, region_id, software, currency,
                                        pricing_hourly, standard_pricing_prepaid)
                                    queries.append(query)
                                    server_product_id = server_product_id + 1
        return queries

    def getCSV(self):
        """ Returns a list of CSV.

        :returns: a list of CSV that contains pricing data.
        :rtype: list
        """
        csv = []
        csv.append("Product Size, Platform, Region ID, Currency, Pricing")

        for single_json in self.json_data.values():
            currency = single_json['config']['currencies'][0]
            for region in single_json['config']['regions']:
                region_id = awspricing.mapper.getRegionID(region['region'])
                for instanceType in region['instanceTypes']:
                    for size in instanceType['sizes']:
                        product_size = size['size']
                        for value in size['valueColumns']:
                            platform = value['name']
                            try:
                                pricing_hourly = "%.3f" % float(value['prices'][currency])
                            except ValueError:
                                pricing_hourly = "0"
                            row = "%s, %s, %s, %s, %s" % (product_size, platform, region_id,
                                                          currency, pricing_hourly )
                            csv.append(row)
        return csv
