import urllib 
import json
import awspricing.mapper
from awspricing.base import Base
from awspricing.ec2description import EC2Description

class EC2(Base):
    """ Class for EC2 pricing. """
    def __init__(self):
        Base.__init__(self)
        self.json_data = json.loads(urllib.urlopen("http://aws.amazon.com/ec2/pricing/pricing-on-demand-instances.json").read())
        self.currency = self.json_data['config']['currencies'][0]
        self.rate = self.json_data['config']['rate']

    def getSQL(self):
        """ Returns a list of SQL statements.

        :returns: a list of SQL statemnets that contains pricing data.
        :rtype: list
        """
        server_product_id = self.start_id
        ec2desc = EC2Description()
        active = 'Y'
        cpu_power = 1000
        prepayment_term_in_months = 0
        standard_pricing_prepaid  = 0
        software = ''
        queries = []
        for region in self.json_data['config']['regions']:
            region_id = awspricing.mapper.getRegionID(region['region'])
            for instanceType in region['instanceTypes']:
                prefix = instanceType['type']
                for size in instanceType['sizes']:
                    suffix = size['size']
                    product_size = awspricing.mapper.getEC2ProductSize(prefix, suffix)
                    if product_size == 'cc1.8xlarge':
                        product_size = 'cc2.8xlarge'
                    core_count = ec2desc.getVirtualCores(product_size)
                    disk_in_gb = ec2desc.getStorageSize(product_size)
                    memory_in_gb = ec2desc.getMemorySize(product_size)
                    name = "test"
                    description = "test"
                    if product_size in ['t1.micro', 'c1.medium', 'm1.small', 'm1.medium']:
                        architectures = ['I32', 'I64']
                    else:
                        architectures = ['I64']
                    for value in size['valueColumns']:
                        if value['name'] == "mswin":
                            platform = "WINDOWS"
                        elif value['name'] == "linux":
                            platform = "UNIX"
                        else:
                            platform = "UNKNOWN"
                        try:
                            pricing_hourly = "%.3f" % float(value['prices'][self.currency])
                        except ValueError:
                            pricing_hourly = "0"
                        for architecture in architectures:
                            query = "INSERT INTO server_product VALUES(%i, %s, '%s', '%s', '%s', %s, %2.1f, '%s', %s, %2.3f, '%s', '%s', %s, '%s', '%s', '%s', %s, %5.2f);" % (
                                  server_product_id, self.cloud_id, product_size, active, architecture, core_count,
                                  cpu_power, description, disk_in_gb, memory_in_gb, name, platform,
                                  prepayment_term_in_months, region_id, software, self.currency,
                                  pricing_hourly, standard_pricing_prepaid)
                            queries.append(query)
                            server_product_id = server_product_id + 1
        return queries
