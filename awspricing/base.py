import urllib
import json
import re

class Base(object):
    """ Base class for pricing classes. """
    def __init__(self):
        self._cloud_id = 1
        self._start_id = 1

    def get_json(self, pricing_js_url):
        p = re.compile("(?<=callback\().+(?=\);$)")
        raw_js = urllib.urlopen(pricing_js_url).read().replace("\n","")
        raw_json = p.search(raw_js).group(0)

        p2 = re.compile("\w+(?=\:)")
        refined_json = p2.sub(lambda x: '"'+x.group(0)+'"', raw_json)
        json_data = json.loads(refined_json)

        return json_data

    @property
    def cloud_id(self):
        """`int` - cloud_id for SQL statements."""
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, x):
        self._cloud_id = x

    @property
    def start_id(self):
        """`int` - start_id for SQL statements. It works as a primary key."""
        return self._start_id

    @start_id.setter
    def start_id(self, x):
        self._start_id = x
