import urllib 
import json
import awspricing.mapper
from awspricing.base import Base

class S3(Base):
    def __init__(self):
        Base.__init__(self)
        self.json_data = json.loads(urllib.urlopen("http://aws.amazon.com/s3/pricing/pricing-storage.json").read())
        self.currency = self.json_data['config']['currencies'][0]
        self.rate = self.json_data['config']['rate']

    def getSQL(self):
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
                        query = "INSERT INTO storage_product VALUES(%i, %i, '%s', '%s', '%s', '%s', '%s', '%s', %i, %s);" %\
                                (storage_product_id, self.cloud_id, region_id, 'standard', 'Y', self.currency,
                                 name, description, pricing_threshold, pricing)
                        queries.append(query)
                        storage_product_id = storage_product_id + 1

        return queries

    def getCSV(self, selected_type):
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
