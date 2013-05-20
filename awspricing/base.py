class Base(object):
    @property
    def cloud_id(self):
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, x):
        self._cloud_id = x

    @property
    def start_id(self):
        return self._start_id

    @start_id.setter
    def start_id(self, x):
        self._start_id = x

    def __init__(self):
        self._cloud_id = 1
        self._start_id = 1
