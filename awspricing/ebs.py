import urllib 
import json
import awspricing.mapper
from awspricing.base import Base

class Ebs(Base):
    """ Class for EBS pricing. """
    def __init__(self):
        Base.__init__(self)

        pricing_data = urllib.urlopen("http://a0.awsstatic.com/pricing/1/ebs/pricing-ebs.min.js").read()
        find = pricing_data.find("callback(")
        pricing_data = pricing_data[find+9:]
        pricing_data = pricing_data[:-2]
        pricing_data = pricing_data.replace('vers:', '"vers":')
        pricing_data = pricing_data.replace('config:', '"config":')
        pricing_data = pricing_data.replace('currencies:', '"currencies":')
        pricing_data = pricing_data.replace('rate:', '"rate":')
        pricing_data = pricing_data.replace('regions:', '"regions":')
        pricing_data = pricing_data.replace('region:', '"region":')
        pricing_data = pricing_data.replace('types:', '"types":')
        pricing_data = pricing_data.replace('name:', '"name":')
        pricing_data = pricing_data.replace('values:', '"values":')
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
        queries = []
        volume_product_id = self.start_id
        pricing_threshold = 0
        description=""
        for region in self.json_data['config']['regions']:
            region_id = awspricing.mapper.getRegionID(region['region'])
            for ebs_type in region['types']:
                if ebs_type['name'] == 'Amazon EBS Magnetic volumes':
                    name = ebs_type['name']
                    pricing = float(ebs_type['values'][0]['prices'][self.currency])
                    query = "INSERT INTO volume_product VALUES(%i, %i, '%s', '%s', '%s', '%s', '%s', '%s', %i, %.3f);" %\
                            (volume_product_id, self.cloud_id, region_id, 'standard', 'Y',
                             self.currency, name, "Storage costs for allocated " + name, pricing_threshold, pricing)
                    queries.append(query)
                    volume_product_id = volume_product_id + 1

        return queries

    def getCSV(self, selected_type='Amazon EBS Magnetic volumes'):
        """ Returns a list of CSV.

        Keyword arguments:
        :param selected_type: the type of the product to be returned.

        :returns: a list of CSV that contains pricing data.
        :rtype: list
        """
        csv = []
        name="EBS Storage"
        csv.append("RegionID, Storage Type, Currency, Pricing, Rate")
        for region in self.json_data['config']['regions']:
            region_id = awspricing.mapper.getRegionID(region['region'])
            for ebs_type in region['types']:
                if ebs_type['name'] == selected_type:
                    try:
                        pricing = "%.3f" % float(ebs_type['values'][0]['prices'][self.currency])
                    except ValueError:
                        pricing = "N/A"
                    row = "%s, %s, %s, %s, %s" % (region_id, name, self.currency, pricing, self.rate)
                    csv.append(row)

        return csv
