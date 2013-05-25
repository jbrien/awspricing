class Base(object):
    """ Base class for pricing classes. """
    def __init__(self):
        self._cloud_id = 1
        self._start_id = 1

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
