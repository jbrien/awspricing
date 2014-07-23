import urllib 
import json
import awspricing.mapper
from awspricing.base import Base

class S3(Base):
    """ Class for S3 pricing. """
    def __init__(self):
        Base.__init__(self)

        pricing_data = urllib.urlopen("http://a0.awsstatic.com/pricing/1/s3/pricing-storage-s3.min.js").read()
        find = pricing_data.find("callback(")
        pricing_data = pricing_data[find+9:]
        pricing_data = pricing_data[:-2]
        pricing_data = pricing_data.replace('vers:', '"vers":')
        pricing_data = pricing_data.replace('config:', '"config":')
        pricing_data = pricing_data.replace('currencies:', '"currencies":')
        pricing_data = pricing_data.replace('rate:', '"rate":')
        pricing_data = pricing_data.replace('valueColumns:', '"valueColumns":')
        pricing_data = pricing_data.replace('footnotes:', '"footnotes":')
        pricing_data = pricing_data.replace('regions:', '"regions":')
        pricing_data = pricing_data.replace('region:', '"region":')
        pricing_data = pricing_data.replace('tiers:', '"tiers":')
        pricing_data = pricing_data.replace('storageTypes:', '"storageTypes":')
        pricing_data = pricing_data.replace('name:', '"name":')
        pricing_data = pricing_data.replace('values:', '"values":')
        pricing_data = pricing_data.replace('type:', '"type":')
        pricing_data = pricing_data.replace('prices:', '"prices":')
        pricing_data = pricing_data.replace('USD:', '"USD":')
        self.json_data = json.loads(pricing_data)
        self.currency = self.json_data['config']['currencies'][0]
        self.rate = self.json_data['config']['rate']

    def getSQL(self):
        """ Returns a list of SQL statements.

        :returns: a list of SQL statemnets that contains pricing data.
        :rtype: list
        """
        storage_product_id = self.start_id
        queries = []
        for region in self.json_data['config']['regions']:
            region_id = awspricing.mapper.getRegionID(region['region'])
            for tier in region['tiers']:
                name = awspricing.mapper.getStorageName(tier['name'])
                description = awspricing.mapper.getStorageDescription(tier['name'])
                pricing_threshold = awspricing.mapper.getStoragePricingThreshold(tier['name'])
                for storage_type in tier['storageTypes']:
                    if storage_type['type'] == 'storage':
                        try:
                            pricing = "%.3f" % float(storage_type['prices'][self.currency])
                        except ValueError:
                            pricing = "0"
                        if region_id == 'us-std':
                            table_region_id = 'us-east-1'
                            query = "INSERT INTO storage_product VALUES(%i, %i, '%s', '%s', '%s', '%s', '%s', '%s', %i, %s);" %\
                                (storage_product_id, self.cloud_id, table_region_id, 'standard', 'Y', self.currency,
                                 name, description, pricing_threshold, pricing)
                            queries.append(query)
                            storage_product_id = storage_product_id + 1
                            table_region_id = 'us-east-2'    
                            query = "INSERT INTO storage_product VALUES(%i, %i, '%s', '%s', '%s', '%s', '%s', '%s', %i, %s);" %\
                                (storage_product_id, self.cloud_id, table_region_id, 'standard', 'Y', self.currency,
                                 name, description, pricing_threshold, pricing)
                            queries.append(query)
                            storage_product_id = storage_product_id + 1
                        else:
                            query = "INSERT INTO storage_product VALUES(%i, %i, '%s', '%s', '%s', '%s', '%s', '%s', %i, %s);" %\
                                (storage_product_id, self.cloud_id, region_id, 'standard', 'Y', self.currency,
                                 name, description, pricing_threshold, pricing)
                            queries.append(query)
                            storage_product_id = storage_product_id + 1

        return queries

    def getCSV(self, selected_type):
        """ Returns a list of CSV.

        Keyword arguments:
        :param selected_type: the type of the product to be returned. i.e. storage, clacier, rrs.

        :returns: a list of CSV that contains pricing data.
        :rtype: list
        """
        csv = []
        csv.append("RegionID, Storage Type, Currency, Pricing, Rate")
        for region in self.json_data['config']['regions']:
            region_id = awspricing.mapper.getRegionID(region['region'])
            for tier in region['tiers']:
                name = awspricing.mapper.getStorageName(tier['name'])
                description = awspricing.mapper.getStorageDescription(tier['name']).replace(',',"")
                for storage_type in tier['storageTypes']:
                    if storage_type['type'] == selected_type:
                        try:
                            pricing = "%.3f" % float(storage_type['prices'][self.currency])
                        except ValueError:
                            pricing = "N/A"
                        row = "%s, %s, %s, %s, %s" % (region_id, description, self.currency, pricing, self.rate)
                        csv.append(row)

        return csv
