from BeautifulSoup import BeautifulSoup
import urllib

EC2_PRODUCTS = {
    "t1.micro"  : { "name": "Micro",
                    "description": "32-bit or 64-bit, 613 MB RAM, Up to 2 EC2 Compute Units, EBS Storage Only, I/O : Low"},
    "m1.small"  : { "name": "Small",
                    "description": "32-bit or 64-bit, 1.7 GB RAM, 1 EC2 Compute Unit, 160 GB Disk, I/O : Moderate"},
    "m1.medium" : { "name": "Medium",
                    "description": "32-bit or 64-bit, 3.75 GB RAM, 2 EC2 Compute Units, 410 GB Disk, I/O : Moderate"},
    "m1.large"  : { "name": "Large",
                    "description": "64-bit, 7.5 GB RAM, 4 EC2 Compute Units, 850 GB Disk, I/O : High"},
    "m1.xlarge" : { "name": "Extra Large",
                    "description": "64-bit, 15 GB RAM, 8 EC2 Compute Units, 1690 GB Disk, I/O : High"},
    "m2.xlarge": { "name": "High-Memory Extra Large",
                    "description": "64-bit, 17.1 GB RAM, 6.5 EC2 Compute Units, 420 GB Disk, I/O : Moderate"},
    "m2.2xlarge": { "name": "High-Memory Double Extra Large",
                    "description": "64-bit, 34.2 GB RAM, 13 EC2 Compute Units, 850 GB Disk, I/O : High"},
    "m2.4xlarge": { "name": "High-Memory Quadruple Extra Large",
                    "description": "64-bit, 68.4 GB RAM, 26 EC2 Compute Units, 1690 GB Disk, I/O : High"},
    "c1.medium" : { "name": "High-CPU Medium",
                    "description": "32-bit or 64-bit, 1.7 GB RAM, 5 EC2 Compute Units, 350 GB Disk, I/O : Moderate"},
    "c1.xlarge" : { "name": "High-CPU Extra Large",
                    "description": "64-bit, 7 GB RAM, 20 EC2 Compute Units, 1690 GB Disk, I/O : High"},
    "cc1.4xlarge": {"name": "Cluster Compute Quadruple Extra Large",
                    "description": "64-bit, 23 GB RAM, 33.5 EC2 Compute Units, 1690 GB Disk, I/O : Very High (10 Gigabit Ethernet)"},
    "cc2.8xlarge": {"name": "Cluster Compute Eight Extra Large",
                    "description": "64-bit, 60.5 GB RAM, 88 EC2 Compute Units, 3370 GB Disk, I/O : Very High (10 Gigabit Ethernet)"},
    "cg1.4xlarge": {"name": "Cluster GPU Quadruple Extra Large",
                    "description": "64-bit, 22 GB RAM, 33.5 EC2 Compute Units, 1690 GB Disk, I/O : Very High (10 Gigabit Ethernet)"},
    "m3.xlarge"  : {"name": "M3 Extra Large Instance",
                    "description": "64-bit, 15 GB RAM, 13 EC2 Compute Units, EBS Storage Only, I/O: Moderate"},
    "m3.2xlarge" : {"name": "M3 Double Extra Large Instance",
                    "description": "64-bit, 30 GB RAM, 26 EC2 Compute Units, EBS Storage Only, I/O: High"},
    "hi1.4xlarge": {"name": "High I/O Quadruple Extra Large Instance",
                    "description": "64-bit, 60.5 GB RAM, 33 EC2 Compute Units, 1024 GB SSD, I/O Very High (10 Gigabit Ethernet)"},
    "hs1.8xlarge": {"name": "High Storage Eight Extra Large Instance",
                    "description": "64-bit, 117 GB RAM, 35 EC2 Compute Units, 2 TB Disk, I/O Very High (10 Gigabit Ethernet)"},
    "cr1.8xlarge": {"name": "High Memory Cluster Eight Extra Large Instance",
                    "description": "64-bit, 244 GB RAM, 88 EC2 Compute Units, 240 GB SSD, I/O Very High (10 Gigabit Ethernet)"}
}

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

    def getName(self, product_size):
        """ Returns name of the EC2 instance.

        Arguments:
        :param product_size: the type of the product size.

        :returns: name of the instance.
        :rtype: str
        """
        return EC2_PRODUCTS[product_size]["name"]

    def getDescription(self, product_size):
        """ Returns description of the EC2 instance.

        Arguments:
        :param product_size: the type of the product size.

        :returns: description of the instance.
        :rtype: str
        """
        return EC2_PRODUCTS[product_size]["description"]
