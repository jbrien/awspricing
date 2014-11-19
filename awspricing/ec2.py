import sys
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
        pricing_list = {
                         'linux-od': "http://a0.awsstatic.com/pricing/1/ec2/linux-od.min.js",
                         'rhel-od': "http://a0.awsstatic.com/pricing/1/ec2/rhel-od.min.js",
                         'sles-od': "http://a0.awsstatic.com/pricing/1/ec2/sles-od.min.js",
                         'mswin-od': "http://a0.awsstatic.com/pricing/1/ec2/mswin-od.min.js",
                         'mswinSQL-od': "http://a0.awsstatic.com/pricing/1/ec2/mswinSQL-od.min.js",
                         'mswinSQLWeb-od': "http://a0.awsstatic.com/pricing/1/ec2/mswinSQLWeb-od.min.js",
                         'old-linux-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/linux-od.min.js",
                         'old-rhel-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/rhel-od.min.js",
                         'old-sles-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/sles-od.min.js",
                         'old-mswinSQL-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/mswinSQL-od.min.js",
                         'old-mswinSQLWeb-od': "http://a0.awsstatic.com/pricing/1/ec2/previous-generation/mswinSQLWeb-od.min.js" }
        self.json_data = dict()
        for pricing_type in pricing_list:
            pricing_data = urllib.urlopen(pricing_list[pricing_type]).read()
            find = pricing_data.find("callback(")
            pricing_data = pricing_data[find+9:]
            pricing_data = pricing_data[:-2]
            pricing_data = pricing_data.replace('vers:', '"vers":')
            pricing_data = pricing_data.replace('config:', '"config":')
            pricing_data = pricing_data.replace('valueColumns:', '"valueColumns":')
            pricing_data = pricing_data.replace('rate:', '"rate":')
            pricing_data = pricing_data.replace('currencies:', '"currencies":')
            pricing_data = pricing_data.replace('regions:', '"regions":')
            pricing_data = pricing_data.replace('region:', '"region":')
            pricing_data = pricing_data.replace('instanceTypes:', '"instanceTypes":')
            pricing_data = pricing_data.replace('type:', '"type":')
            pricing_data = pricing_data.replace('sizes:', '"sizes":')
            pricing_data = pricing_data.replace('size:', '"size":')
            pricing_data = pricing_data.replace('vCPU:', '"vCPU":')
            pricing_data = pricing_data.replace('ECU:', '"ECU":')
            pricing_data = pricing_data.replace('memoryGiB:', '"memoryGiB":')
            pricing_data = pricing_data.replace('storageGB:', '"storageGB":')
            pricing_data = pricing_data.replace('name:', '"name":')
            pricing_data = pricing_data.replace('prices:', '"prices":')
            pricing_data = pricing_data.replace('USD:', '"USD":')

            if pricing_type == 'linux-od':
                pricing_data = pricing_data.replace('"name":"os"', '"name":"linux"')
            elif pricing_type == 'rhel-od':
                pricing_data = pricing_data.replace('"name":"os"', '"name":"rhel"')
            elif pricing_type == 'sles-od':
                pricing_data = pricing_data.replace('"name":"os"', '"name":"sles"')
            elif pricing_type == 'mswin-od':
                pricing_data = pricing_data.replace('"name":"os"', '"name":"mswin"')
            elif pricing_type == 'mswinSQL-od':
                pricing_data = pricing_data.replace('"name":"os"', '"name":"mswinSQL"')
            elif pricing_type == 'mswinSQLWeb-od':
                pricing_data = pricing_data.replace('"name":"os"', '"name":"mswinSQLWeb"')

            self.json_data[pricing_type] = json.loads(pricing_data)

    def getSQL(self):
        """ Returns a list of SQL statements.

        :returns: a list of SQL statemnets that contains pricing data.
        :rtype: list
        """
        server_product_id = self.start_id
        active = 'Y'
        cpu_power = 1000
        prepayment_term_in_months = 0
        pricing_hourly = ''
        standard_pricing_prepaid  = 0
        software = ''
        queries = []
        for key in self.json_data.keys():
            single_json = self.json_data[key]
            currency = single_json['config']['currencies'][0]
            for region in single_json['config']['regions']:
                region_id = awspricing.mapper.getRegionID(region['region'])
                for instanceType in region['instanceTypes']:
                    for size in instanceType['sizes']:
                        product_size = size['size']

                        if product_size not in ec2desc.EC2_PRODUCTS:
                            print >> sys.stderr, "No entry in the ec2description EC2_PRODUCTS hash table for this product size:", product_size
                            continue
                        core_count = ec2desc.getVirtualCores(product_size)
                        disk_in_gb = ec2desc.getStorageSize(product_size)
                        memory_in_gb = ec2desc.getMemorySize(product_size)
                        name = ec2desc.getName(product_size)
                        description = ec2desc.getDescription(product_size)
                        if product_size in ['t1.micro', 't2.micro', 't2.small', 't2.medium', 'c1.medium', 'm1.small', 'm1.medium']:
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
                            elif value['name'] == "os":
                                if key in ["linux-od","old-linux-od"]:
                                    platform = "UNIX"
                                elif key in ["rhel-od","old-rhel-od"]:
                                    platform = "RHEL"
                                elif key in ["sles-od","old-sles-od"]:
                                    platform = "SUSE"
                                elif key in ["mswin-od","old-mswin-od"]:
                                    platform = "WINDOWS"
                                elif key in ["mswinSQL-od","old-mswinSQL-od"]:
                                    platform = "MSWINSQL"
                                elif key in ["mswinSQLWeb-od","old-mswinSQLWeb-od"]:
                                    platform = "MSWINSQLWEB"
                            try:
                                if value['prices'][currency] != None:
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

        for key in self.json_data.keys():
            single_json = self.json_data[key]
            currency = single_json['config']['currencies'][0]
            for region in single_json['config']['regions']:
                region_id = awspricing.mapper.getRegionID(region['region'])
                for instanceType in region['instanceTypes']:
                    for size in instanceType['sizes']:
                        product_size = size['size']
                        for value in size['valueColumns']:
                            if value['name'] == "os":
                                if key in ["linux-od","old-linux-od"]:
                                    platform = "linux"
                                elif key in ["rhel-od","old-rhel-od"]:
                                    platform = "rhel"
                                elif key in ["sles-od","old-sles-od"]:
                                    platform = "sles"
                                elif key in ["mswin-od","old-mswin-od"]:
                                    platform = "mswin"
                                elif key in ["mswinSQL-od","old-mswinSQL-od"]:
                                    platform = "mswinSQL"
                                elif key in ["mswinSQLWeb-od","old-mswinSQLWeb-od"]:
                                    platform = "mswinSQLWeb"
                            else:
                                platform = value['name']
                            try:
                                pricing_hourly = "%.3f" % float(value['prices'][currency])
                            except ValueError:
                                pricing_hourly = "0"
                            row = "%s, %s, %s, %s, %s" % (product_size, platform, region_id,
                                                          currency, pricing_hourly )
                            csv.append(row)
        return csv
