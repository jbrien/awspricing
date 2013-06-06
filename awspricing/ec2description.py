from BeautifulSoup import BeautifulSoup
import urllib

class EC2Description(object):
    """ Class for EC2 Instance Description. """
    def __init__(self):
        self.instances = dict()
        instanceTypes = urllib.urlopen("http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html").read()
        soup=BeautifulSoup(instanceTypes)
        divs  = soup.findAll('div',attrs={'class':'informaltable'})
        table = divs[1].find('table')
        rows  = table.findAll('tr')

        for row in rows:
            pTags = row.findAll('p')
            if len(pTags) != 0:
                name = pTags[8].text
                compute_units = 2.0 if name == "t1.micro" else float(pTags[2].text)
                virtual_cores = int(pTags[3].text.split()[0])
                if "GiB" in pTags[1].text:
                    memory = float(pTags[1].text.split()[0])
                elif "MiB" in pTags[1].text:
                    memory = float(pTags[1].text.split()[0]) / 1000
                if "GiB" in pTags[4].text:
                    storage = int(pTags[4].text.split()[0])
                elif "TiB" in pTags[4].text:
                    storage = int(pTags[4].text.split()[0]) * 1000
                else:
                    storage = 0

                self.instances[name] = {"compute_units" : compute_units, "memory" : memory, "storage" : storage, "virtual_cores" : virtual_cores}

    def getVirtualCores(self, product_size):
        """ Returns the number of virtual cores of EC2 instance.

        Arguments:
        :param product_size: the type of the product size.

        :returns: virtual core count.
        :rtype: int
        """
        return self.instances[product_size]["virtual_cores"]

    def getComputeUnits(self, product_size):
        """ Returns compute units of EC2 instance.

        Arguments:
        :param product_size: the type of the product size.

        :returns: compute units.
        :rtype: int
        """
        return self.instances[product_size]["compute_units"]

    def getStorageSize(self, product_size):
        """ Returns storage size in GB.

        Arguments:
        :param product_size: the type of the product size.

        :returns: storage size in GB.
        :rtype: int
        """
        return self.instances[product_size]["storage"]

    def getMemorySize(self, product_size):
        """ Returns memory size in GB.

        Arguments:
        :param product_size: the type of the product size.

        :returns: memory size in GB.
        :rtype: float
        """
        return self.instances[product_size]["memory"]
