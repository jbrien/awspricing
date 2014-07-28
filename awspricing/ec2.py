import urllib 
import json
import re
import awspricing.mapper
import awspricing.ec2description as ec2desc
from awspricing.base import Base

class EC2(Base):
    """ Class for EC2 pricing. """
    def __init__(self):
        Base.__init__(self)
        pricing_list = { 'linux-od': "http://a0.awsstatic.com/pricing/1/ec2/linux-od.min.js",
                         'rhel-od': "http://a0.awsstatic.com/pricing/1/ec2/rhel-od.min.js",
                         'sles-od': "http://a0.awsstatic.com/pricing/1/ec2/sles-od.min.js",
                         'mswin-od': "http://a0.awsstatic.com/pricing/1/ec2/mswin-od.min.js",
                         'mswinSQL-od': "http://a0.awsstatic.com/pricing/1/ec2/mswinSQL-od.min.js",
                         'mswinSQLWeb-od': "http://a0.awsstatic.com/pricing/1/ec2/mswinSQLWeb-od.min.js",
                         'old-linux-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/linux-od.min.js",
                         'old-rhel-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/rhel-od.min.js",
                         'old-sles-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/sles-od.min.js",
                         'old-mswin-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/mswin-od.min.js",
                         'old-mswinSQL-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/mswinSQL-od.min.js",
                         'old-mswinSQLWeb-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/mswinSQLWeb-od.min.js" }
        self.json_data = dict()
        for pricing_type in pricing_list:
            self.json_data[pricing_type] = self.get_json(pricing_list[pricing_type])

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
                            elif value['name'] in ["linux", "os"]:
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
