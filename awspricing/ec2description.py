EC2_PRODUCTS = {
    "t1.micro"  : { "name": "Micro",
                    "description": "32-bit or 64-bit, 613 MB RAM, Up to 2 EC2 Compute Units, EBS Storage Only, I/O : Low",
                    "compute_units": 1,
                    "virtual_cores": 1,
                    "memory": 0.615,
                    "storage": 0},
    "m1.small"  : { "name": "Small",
                    "description": "32-bit or 64-bit, 1.7 GB RAM, 1 EC2 Compute Unit, 160 GB Disk, I/O : Moderate",
                    "compute_units": 1,
                    "virtual_cores": 1,
                    "memory": 1.7,
                    "storage": 160},
    "m1.medium" : { "name": "Medium",
                    "description": "32-bit or 64-bit, 3.75 GB RAM, 2 EC2 Compute Units, 410 GB Disk, I/O : Moderate",
                    "compute_units": 2,
                    "virtual_cores": 1,
                    "memory": 3.75,
                    "storage": 410},
    "m1.large"  : { "name": "Large",
                    "description": "64-bit, 7.5 GB RAM, 4 EC2 Compute Units, 850 GB Disk, I/O : High",
                    "compute_units": 4,
                    "virtual_cores": 2,
                    "memory": 7.5,
                    "storage": 820},
    "m1.xlarge" : { "name": "Extra Large",
                    "description": "64-bit, 15 GB RAM, 8 EC2 Compute Units, 1690 GB Disk, I/O : High",
                    "compute_units": 8,
                    "virtual_cores": 4,
                    "memory": 15,
                    "storage": 1680},
    "m2.xlarge": { "name": "High-Memory Extra Large",
                    "description": "64-bit, 17.1 GB RAM, 6.5 EC2 Compute Units, 420 GB Disk, I/O : Moderate",
                    "compute_units": 6.5,
                    "virtual_cores": 2,
                    "memory": 17.1,
                    "storage": 420},
    "m2.2xlarge": { "name": "High-Memory Double Extra Large",
                    "description": "64-bit, 34.2 GB RAM, 13 EC2 Compute Units, 850 GB Disk, I/O : High",
                    "compute_units": 13,
                    "virtual_cores": 4,
                    "memory": 34.2,
                    "storage": 850},
    "m2.4xlarge": { "name": "High-Memory Quadruple Extra Large",
                    "description": "64-bit, 68.4 GB RAM, 26 EC2 Compute Units, 1690 GB Disk, I/O : High",
                    "compute_units": 26,
                    "virtual_cores": 8,
                    "memory": 68.4,
                    "storage": 1680},
    "c1.medium" : { "name": "High-CPU Medium",
                    "description": "32-bit or 64-bit, 1.7 GB RAM, 5 EC2 Compute Units, 350 GB Disk, I/O : Moderate",
                    "compute_units": 5,
                    "virtual_cores": 2,
                    "memory": 1.7,
                    "storage": 350},
    "c1.xlarge" : { "name": "High-CPU Extra Large",
                    "description": "64-bit, 7 GB RAM, 20 EC2 Compute Units, 1690 GB Disk, I/O : High",
                    "compute_units": 20,
                    "virtual_cores": 8,
                    "memory": 7,
                    "storage": 1680},
    "cc1.4xlarge": {"name": "Cluster Compute Quadruple Extra Large",
                    "description": "64-bit, 23 GB RAM, 33.5 EC2 Compute Units, 1690 GB Disk, I/O : Very High (10 Gigabit Ethernet)",
                    "compute_units": 33.5 ,
                    "virtual_cores": 8,
                    "memory": 23,
                    "storage": 1690},
    "cc2.8xlarge": {"name": "Cluster Compute Eight Extra Large",
                    "description": "64-bit, 60.5 GB RAM, 88 EC2 Compute Units, 3370 GB Disk, I/O : Very High (10 Gigabit Ethernet)",
                    "compute_units": 88,
                    "virtual_cores": 32,
                    "memory": 60.5,
                    "storage": 3360},
    "cg1.4xlarge": {"name": "Cluster GPU Quadruple Extra Large",
                    "description": "64-bit, 22 GB RAM, 33.5 EC2 Compute Units, 1690 GB Disk, I/O : Very High (10 Gigabit Ethernet)",
                    "compute_units": 33.5,
                    "virtual_cores": 16,
                    "memory": 22.5,
                    "storage": 1680},
    "m3.xlarge"  : {"name": "M3 Extra Large Instance",
                    "description": "64-bit, 15 GB RAM, 13 EC2 Compute Units, EBS Storage Only, I/O: Moderate",
                    "compute_units": 13,
                    "virtual_cores": 4,
                    "memory": 15,
                    "storage": 0},
    "m3.2xlarge" : {"name": "M3 Double Extra Large Instance",
                    "description": "64-bit, 30 GB RAM, 26 EC2 Compute Units, EBS Storage Only, I/O: High",
                    "compute_units": 26,
                    "virtual_cores": 8,
                    "memory": 30,
                    "storage": 0},
    "hi1.4xlarge": {"name": "High I/O Quadruple Extra Large Instance",
                    "description": "64-bit, 60.5 GB RAM, 33 EC2 Compute Units, 1024 GB SSD, I/O Very High (10 Gigabit Ethernet)",
                    "compute_units": 35,
                    "virtual_cores": 16,
                    "memory": 60.5,
                    "storage": 2048},
    "hs1.8xlarge": {"name": "High Storage Eight Extra Large Instance",
                    "description": "64-bit, 117 GB RAM, 35 EC2 Compute Units, 2 TB Disk, I/O Very High (10 Gigabit Ethernet)",
                    "compute_units": 35,
                    "virtual_cores": 16,
                    "memory": 117,
                    "storage": 49152},
    "cr1.8xlarge": {"name": "High Memory Cluster Eight Extra Large Instance",
                    "description": "64-bit, 244 GB RAM, 88 EC2 Compute Units, 240 GB SSD, I/O Very High (10 Gigabit Ethernet)",
                    "compute_units": 88,
                    "virtual_cores": 32,
                    "memory": 244,
                    "storage": 240}
}

def getVirtualCores(product_size):
    """ Returns the number of virtual cores of EC2 instance.

    Arguments:
    :param product_size: the type of the product size.

    :returns: virtual core count.
    :rtype: int
    """
    return EC2_PRODUCTS[product_size]["virtual_cores"]

def getComputeUnits(product_size):
    """ Returns compute units of EC2 instance.

    Arguments:
    :param product_size: the type of the product size.

    :returns: compute units.
    :rtype: int
    """
    return EC2_PRODUCTS[product_size]["compute_units"]

def getStorageSize(product_size):
    """ Returns storage size in GB.

    Arguments:
    :param product_size: the type of the product size.

    :returns: storage size in GB.
    :rtype: int
    """
    return EC2_PRODUCTS[product_size]["storage"]

def getMemorySize(product_size):
    """ Returns memory size in GB.

    Arguments:
    :param product_size: the type of the product size.

    :returns: memory size in GB.
    :rtype: float
    """
    return EC2_PRODUCTS[product_size]["memory"]

def getName(product_size):
    """ Returns name of the EC2 instance.

    Arguments:
    :param product_size: the type of the product size.

    :returns: name of the instance.
    :rtype: str
    """
    return EC2_PRODUCTS[product_size]["name"]

def getDescription(product_size):
    """ Returns description of the EC2 instance.

    Arguments:
    :param product_size: the type of the product size.

    :returns: description of the instance.
    :rtype: str
    """
    return EC2_PRODUCTS[product_size]["description"]
