# Reference: http://aws.amazon.com/ec2/instance-types/

EC2_PRODUCTS = {
    "t1.micro"  : { "name": "T1 Micro",
                    "description": "32-bit or 64-bit, 613 MB RAM, Up to 2 EC2 Compute Units, EBS Storage Only, I/O : Low",
                    "compute_units": 1,
                    "virtual_cores": 1,
                    "memory": 0.615,
                    "storage": 0},
    "t2.micro"  : { "name": "T2 Micro",
                    "description": "64-bit, 1 GiB RAM, 30 Initial CPU Credits, EBS Storage Only, I/O: Low to Moderate",
                    "compute_units": 1,
                    "virtual_cores": 1,
                    "memory": 1,
                    "storage": 0},
    "t2.small"  : { "name": "T2 Small",
                    "description": "64-bit, 2 GiB RAM, 30 Initial CPU Credits, EBS Storage Only, I/O : Low to Moderate",
                    "compute_units": 1,
                    "virtual_cores": 1,
                    "memory": 2,
                    "storage": 0},
    "t2.medium"  : { "name": "Micro",
                    "description": "64-bit, 4 GiB RAM, 60 Initial CPU Credits, EBS Storage Only, I/O : Low to Moderate",
                    "compute_units": 2,
                    "virtual_cores": 2,
                    "memory": 4,
                    "storage": 0},
    "m1.small"  : { "name": "Small",
                    "description": "32-bit or 64-bit, 1.7 GiB RAM, 1 EC2 Compute Unit, 160 GB Disk, I/O : Moderate",
                    "compute_units": 1,
                    "virtual_cores": 1,
                    "memory": 1.7,
                    "storage": 160},                                  
    "m1.medium" : { "name": "Medium",
                    "description": "32-bit or 64-bit, 3.75 GiB RAM, 2 EC2 Compute Units, 410 GB Disk, I/O : Moderate",
                    "compute_units": 2,
                    "virtual_cores": 1,
                    "memory": 3.75,
                    "storage": 410},
    "m1.large"  : { "name": "Large",
                    "description": "64-bit, 7.5 GiB RAM, 4 EC2 Compute Units, 850 GB Disk, I/O : High",
                    "compute_units": 4,
                    "virtual_cores": 2,
                    "memory": 7.5,
                    "storage": 820},
    "m1.xlarge" : { "name": "Extra Large",
                    "description": "64-bit, 15 GiB RAM, 8 EC2 Compute Units, 1690 GB Disk, I/O : High",
                    "compute_units": 8,
                    "virtual_cores": 4,
                    "memory": 15,
                    "storage": 1680},
    "m2.xlarge": { "name": "High-Memory Extra Large",
                    "description": "64-bit, 17.1 GiB RAM, 6.5 EC2 Compute Units, 420 GB Disk, I/O : Moderate",
                    "compute_units": 6.5,
                    "virtual_cores": 2,
                    "memory": 17.1,
                    "storage": 420},
    "m2.2xlarge": { "name": "High-Memory Double Extra Large",
                    "description": "64-bit, 34.2 GiB RAM, 13 EC2 Compute Units, 850 GB Disk, I/O : High",
                    "compute_units": 13,
                    "virtual_cores": 4,
                    "memory": 34.2,
                    "storage": 850},
    "m2.4xlarge": { "name": "High-Memory Quadruple Extra Large",
                    "description": "64-bit, 68.4 GiB RAM, 26 EC2 Compute Units, 1690 GB Disk, I/O : High",
                    "compute_units": 26,
                    "virtual_cores": 8,
                    "memory": 68.4,
                    "storage": 1680},
    "c1.medium" : { "name": "High-CPU Medium",
                    "description": "32-bit or 64-bit, 1.7 GiB RAM, 5 EC2 Compute Units, 350 GB Disk, I/O : Moderate",
                    "compute_units": 5,
                    "virtual_cores": 2,
                    "memory": 1.7,
                    "storage": 350},
    "c1.xlarge" : { "name": "High-CPU Extra Large",
                    "description": "64-bit, 7 GiB RAM, 20 EC2 Compute Units, 1690 GB Disk, I/O : High",
                    "compute_units": 20,
                    "virtual_cores": 8,
                    "memory": 7,
                    "storage": 1680},
    "c3.large"  : { "name": "Compute Optimized Large",
                    "description": "64-bit, 3.75 GiB RAM, 7 EC2 Compute Units, 2 X 16 GB SSD, I/O : Moderate",
                    "compute_units": 7,
                    "virtual_cores": 2,
                    "memory": 3.75,
                    "storage": 32},
    "c3.xlarge" : { "name": "Compute Optimized Extra Large",
                    "description": "64-bit, 7.5 GiB RAM, 14 EC2 Compute Units, 2 X 40 GB SSD, I/O : Moderate",
                    "compute_units": 14,
                    "virtual_cores": 4,
                    "memory": 7.5,
                    "storage": 80},
    "c3.2xlarge" : { "name": "Compute Optimized Double Extra Large",
                    "description": "64-bit, 15 GiB RAM, 28 EC2 Compute Units, 2 X 80 GB SSD, I/O : High",
                    "compute_units": 28,
                    "virtual_cores": 8,
                    "memory": 15,
                    "storage": 160},
    "c3.4xlarge" : { "name": "Compute Optimized Quadruple Extra Large",
                    "description": "64-bit, 30 GiB RAM, 55 EC2 Compute Units, 2 X 160 GB SSD, I/O : High",
                    "compute_units": 55,
                    "virtual_cores": 16,
                    "memory": 30,
                    "storage": 320},
    "c3.8xlarge" : { "name": "Compute Optimized Eight Extra Large",
                    "description": "64-bit, 60 GiB RAM, 108 EC2 Compute Units, 2 X 320 GB SSD, I/O : 10 Gigabit",
                    "compute_units": 108,
                    "virtual_cores": 32,
                    "memory": 60,
                    "storage": 640},
    "cc1.4xlarge": {"name": "Cluster Compute Quadruple Extra Large",
                    "description": "64-bit, 23 GiB RAM, 33.5 EC2 Compute Units, 1690 GB Disk, I/O : Very High (10 Gigabit Ethernet)",
                    "compute_units": 33.5 ,
                    "virtual_cores": 8,
                    "memory": 23,
                    "storage": 1690},
    "cc2.8xlarge": {"name": "Cluster Compute Eight Extra Large",
                    "description": "64-bit, 60.5 GiB RAM, 88 EC2 Compute Units, 3370 GB Disk, I/O : Very High (10 Gigabit Ethernet)",
                    "compute_units": 88,
                    "virtual_cores": 32,
                    "memory": 60.5,
                    "storage": 3360},
    "m3.medium"  : {"name": "M3 Medium Instance",
                    "description": "64-bit, 3.75 GiB RAM, 3 EC2 Compute Units, 4 GB SSD, I/O: Moderate",
                    "compute_units": 3,
                    "virtual_cores": 1,
                    "memory": 3.75,
                    "storage": 4},
    "m3.large"  : {"name": "M3 Large Instance",
                    "description": "64-bit, 7.5 GiB RAM, 6.5 EC2 Compute Units, 32 GB SSD, I/O: Moderate",
                    "compute_units": 6.5,
                    "virtual_cores": 2,
                    "memory": 7.5,
                    "storage": 32},
    "m3.xlarge"  : {"name": "M3 Extra Large Instance",
                    "description": "64-bit, 15 GiB RAM, 13 EC2 Compute Units, 2 X 40 GB SSD, I/O: High",
                    "compute_units": 13,
                    "virtual_cores": 4,
                    "memory": 15,
                    "storage": 80},
    "m3.2xlarge" : {"name": "M3 Double Extra Large Instance",
                    "description": "64-bit, 30 GiB RAM, 26 EC2 Compute Units, 2 X 80 GB SSD, I/O: High",
                    "compute_units": 26,
                    "virtual_cores": 8,
                    "memory": 30,
                    "storage": 160},
    "hi1.4xlarge": {"name": "High I/O Quadruple Extra Large",
                    "description": "64-bit, 60.5 GiB RAM, 33 EC2 Compute Units, 1024 GB SSD, I/O Very High (10 Gigabit Ethernet)",
                    "compute_units": 35,
                    "virtual_cores": 16,
                    "memory": 60.5,
                    "storage": 2048},
    "hs1.8xlarge": {"name": "High Storage Eight Extra Large",
                    "description": "64-bit, 117 GiB RAM, 35 EC2 Compute Units, 2 TB Disk, I/O Very High (10 Gigabit Ethernet)",
                    "compute_units": 35,
                    "virtual_cores": 16,
                    "memory": 117,
                    "storage": 49152},
    "cr1.8xlarge": {"name": "High Memory Cluster Eight Extra Large",
                    "description": "64-bit, 244 GiB RAM, 88 EC2 Compute Units, 240 GB SSD, I/O Very High (10 Gigabit Ethernet)",
                    "compute_units": 88,
                    "virtual_cores": 32,
                    "memory": 244,
                    "storage": 240},
    "g2.2xlarge":  {"name": "GPU Instance Double Extra Large",
                    "description": "64-bit, 15 GiB RAM, 26 EC2 Compute Units, 60 GB SSD, I/O High",
                    "compute_units": 26,
                    "virtual_cores": 8,
                    "memory": 15,
                    "storage": 60},
    "cg1.4xlarge": {"name": "Cluster GPU Instance Quadruple Extra Large",
                    "description": "64-bit, 22.5 GiB RAM, 33.5 EC2 Compute Units, 2 X 840 GB Disk, I/O : Very High (10 Gigabit Ethernet)",
                    "compute_units": 33.5,
                    "virtual_cores": 16,
                    "memory": 22.5,
                    "storage": 1680},
    "r3.large":   { "name": "Memory Optimized Large",
                    "description": "64-bit, 15 GiB RAM, 6.5 EC2 Compute Units, 32 GB SSD, I/O Moderate",
                    "compute_units": 6.5,
                    "virtual_cores": 2,
                    "memory": 15,
                    "storage": 32},
    "r3.xlarge":  { "name": "Memory Optimized Extra Large",
                    "description": "64-bit, 30.5 GiB RAM, 13 EC2 Compute Units, 80 GB SSD, I/O Moderate",
                    "compute_units": 13,
                    "virtual_cores": 4,
                    "memory": 30.5,
                    "storage": 80},
    "r3.2xlarge": { "name": "Memory Optimized Double Extra Large",
                    "description": "64-bit, 61 GiB RAM, 26 EC2 Compute Units, 160 GB SSD, I/O High",
                    "compute_units": 26,
                    "virtual_cores": 8,
                    "memory": 61,
                    "storage": 160},
    "r3.4xlarge": { "name": "Memory Optimized Quadruple Extra Large",
                    "description": "64-bit, 122 GiB RAM, 52 EC2 Compute Units, 320 GB SSD, I/O High",
                    "compute_units": 52,
                    "virtual_cores": 16,
                    "memory": 122,
                    "storage": 320},
    "r3.8xlarge": { "name": "Memory Optimized Eight Extra Large",
                    "description": "64-bit, 244 GiB RAM, 104 EC2 Compute Units, 2 X 320 GB SSD, I/O Very High (10 Gigabit Ethernet)",
                    "compute_units": 104,
                    "virtual_cores": 32,
                    "memory": 244,
                    "storage": 640},
    "i2.xlarge":  { "name": "Storage Optimized Extra Large",
                    "description": "64-bit, 30.5 GiB RAM, 14 EC2 Compute Units, 800 GB SSD, I/O Moderate",
                    "compute_units": 14,
                    "virtual_cores": 4,
                    "memory": 30.5,
                    "storage": 800},
    "i2.2xlarge":  {"name": "Storage Optimized Double Extra Large",
                    "description": "64-bit, 61 GiB RAM, 27 EC2 Compute Units, 2 X 800 GB SSD, I/O High",
                    "compute_units": 27,
                    "virtual_cores": 8,
                    "memory": 61,
                    "storage": 1600},
    "i2.4xlarge":  {"name": "Storage Optimized Quadruple Extra Large",
                    "description": "64-bit, 122 GiB RAM, 53 EC2 Compute Units, 4 X 800 GB SSD, I/O High",
                    "compute_units": 53,
                    "virtual_cores": 16,
                    "memory": 122,
                    "storage": 3200},
    "i2.8xlarge":  {"name": "Storage Optimized Eight Extra Large",
                    "description": "64-bit, 244 GiB RAM, 104 EC2 Compute Units, 8 X 800 GB SSD, I/O High",
                    "compute_units": 104,
                    "virtual_cores": 32,
                    "memory": 244,
                    "storage": 6400},
    "r3.large":    {"name": "Memory Optimized Large",
                    "description": "64-bit, 15.25 GiB RAM, 5 EC2 Compute Units, 1 X 32 GB SSD",
                    "compute_units": 5,
                    "virtual_cores": 2,
                    "memory": 15.25,
                    "storage": 32},
    "r3.xlarge":   {"name": "Memory Optimized Extra Large",
                    "description": "64-bit, 30.5 GiB RAM, 10 EC2 Compute Units, 1 X 80 GB SSD",
                    "compute_units": 10,
                    "virtual_cores": 4,
                    "memory": 30.5,
                    "storage": 80},                                                           
    "r3.2xlarge":  {"name": "Memory Optimized Two Extra Large",
                    "description": "64-bit, 61 GiB RAM, 25 EC2 Compute Units, 1 X 160 GB SSD",
                    "compute_units": 25,
                    "virtual_cores": 8,
                    "memory": 61,
                    "storage": 160},  
    "r3.4xlarge":  {"name": "Memory Optimized Four Extra Large",
                    "description": "64-bit, 122 GiB RAM, 62.5 EC2 Compute Units, 1 X 320 GB SSD",
                    "compute_units": 62.5,
                    "virtual_cores": 16,
                    "memory": 122,
                    "storage": 320},  
    "r3.8xlarge":  {"name": "Memory Optimized Eight Extra Large",
                    "description": "64-bit, 244 GiB RAM, 80 EC2 Compute Units, 2 X 320 GB SSD",
                    "compute_units": 80,
                    "virtual_cores": 32,
                    "memory": 244,
                    "storage": 640}                     
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
