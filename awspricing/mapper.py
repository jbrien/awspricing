REGION_MAP = {
    "us-east"      : "us-east-1",
    "us-west"      : "us-west-1",
    "us-west-2"    : "us-west-2",
    "us-std"       : "us-std",
    "eu-ireland"   : "eu-west-1",
    "eu-central-1" : "eu-central-1",
    "apac-sin"     : "ap-southeast-1",
    "apac-syd"     : "ap-southeast-2",
    "apac-tokyo"   : "ap-northeast-1",
    "sa-east-1"    : "sa-east-1"
}

STORAGE_NAME_MAP = {
    "firstTBstorage"    : "1TB Std",
    "next49TBstorage"   : "50TB Std",
    "next450TBstorage"  : "500TB Std",
    "next500TBstorage"  : "1000TB Std",
    "next4000TBstorage" : "5000TB Std",
    "over5000TBstorage" : "5000TB Plus Std"
}

STORAGE_DESCRIPTION_MAP = {
    "firstTBstorage"    : "First 1 TB/Standard",
    "next49TBstorage"   : "1-50 TB/Standard",
    "next450TBstorage"  : "50-500 TB/Standard",
    "next500TBstorage"  : "500-1,000 TB/Standard",
    "next4000TBstorage" : "1,000-5,000 TB/Standard",
    "over5000TBstorage" : "5000+ TB/Standard"
}

EC2_TYPE_MAP = {
    "uODI"            : "t1",
    "stdODI"          : "m1",
    "hiMemODI"        : "m2",
    "secgenstdODI"    : "m3",
    "clusterGPUI"     : "cg1",
    "clusterComputeI" : "cc1",
    "clusterHiMemODI" : "cr1",
    "hiCPUODI"        : "c1",
    "hiIoODI"         : "hi1",
    "hiStoreODI"      : "hs1"
}

EC2_SIZE_MAP = {
    "u"         : "micro",
    "sm"        : "small",
    "med"       : "medium",
    "lg"        : "large",
    "xl"        : "xlarge",
    "xxl"       : "2xlarge",
    "xxxxl"     : "4xlarge",
    "xxxxxxxxl" : "8xlarge"
}

STORAGE_PRICING_THRESHOLD_MAP = {
    "firstTBstorage"    : 0,
    "next49TBstorage"   : 1000,
    "next450TBstorage"  : 50000,
    "next500TBstorage"  : 500000,
    "next4000TBstorage" : 1000000,
    "over5000TBstorage" : 5000000
}

RDS_MAP = {
    "dbInstClass.db.t1.micro"  : { "product_size": "db.t1.micro",
                               "name"        : "Micro DB Instance",
                               "memory_in_gb": 0.63,
                               "core_count"  : 1,
                               "cpu_power"   : 1.2
                             },
    "dbInstClass.uDBInst"  : { "product_size": "db.t1.micro",
                               "name"        : "Micro DB Instance",
                               "memory_in_gb": 0.63,
                               "core_count"  : 1,
                               "cpu_power"   : 1.2
                             },
    "dbInstClass.db.m1.small" : { "product_size": "db.m1.small",
                               "name"        : "Small DB Instance",
                               "memory_in_gb": 1.7,
                               "core_count"  : 1,
                               "cpu_power"   : 1.2
                             },
    "dbInstClass.db.m1.medium": { "product_size": "db.m1.medium",
                               "name"        : "Medium DB Instance",
                               "memory_in_gb": 3.75,
                               "core_count"  : 1,
                               "cpu_power"   : 2.4
                             },
    "dbInstClass.db.m1.large" : { "product_size": "db.m1.large",
                               "name"        : "Large DB Instance",
                               "memory_in_gb": 7.5,
                               "core_count"  : 2,
                               "cpu_power"   : 2.4
                             },
    "dbInstClass.db.m1.xlarge" : { "product_size": "db.m1.xlarge",
                               "name"        : "Extra Large DB Instance",
                               "memory_in_gb": 15,
                               "core_count"  : 4,
                               "cpu_power"   : 2.4
                             },
    "memDBCurrentGen.db.m2.xlarge": { "product_size": "db.m2.xlarge",
                                   "name"        : "High-Memory Extra Large DB Instance",
                                   "memory_in_gb": 17.1,
                                   "core_count"  : 2,
                                   "cpu_power"   : 3.9
                                 },
    "memDBCurrentGen.db.m2.2xlarge": { "product_size": "db.m2.2xlarge",
                                    "name"        : "High-Memory Double Extra Large DB Instance",
                                    "memory_in_gb": 34,
                                    "core_count"  : 4,
                                    "cpu_power"   : 3.9
                                  },
    "memDBCurrentGen.db.m2.4xlarge": { "product_size": "db.m2.4xlarge",
                                     "name"        : "High-Memory Quadruple Extra Large DB Instance",
                                     "memory_in_gb": 68,
                                     "core_count"  : 8,
                                     "cpu_power"   : 3.9
                                   },
    "memDBCurrentGen.db.cr1.8xl":    { "product_size": "db.cr1.8xlarge",
                                     "name"        : "High-Memory Cluster Eight Extra Large DB Instance",
                                     "memory_in_gb": 244,
                                     "core_count"  : 32,
                                     "cpu_power"   : 3.3
                                   },
    "dbInstClass.db.m3.medium":    { "product_size": "db.m3.medium",
                                     "name"        : "Current Generation Medium DB Instance",
                                     "memory_in_gb": 3.75,
                                     "core_count"  : 1,
                                     "cpu_power"   : 3
                                   },
    "dbInstClass.db.m3.large":     { "product_size": "db.m3.large",
                                     "name"        : "Current Generation Large DB Instance",
                                     "memory_in_gb": 7.5,
                                     "core_count"  : 2,
                                     "cpu_power"   : 6.5
                                   },
    "dbInstClass.db.m3.xlarge":    { "product_size": "db.m3.xlarge",
                                     "name"        : "Current Generation Extra Large DB Instance",
                                     "memory_in_gb": 15,
                                     "core_count"  : 4,
                                     "cpu_power"   : 13
                                   },
    "dbInstClass.db.m3.2xlarge":    { "product_size": "db.m3.2xlarge",
                                     "name"        : "Current Generation Double Extra Large DB Instance",
                                     "memory_in_gb": 30,
                                     "core_count"  : 8,
                                     "cpu_power"   : 26
                                   },
    "hiMemDBInstClass.db.m2.xlarge": { "product_size": "db.m2.xlarge",
                                   "name"        : "High-Memory Extra Large DB Instance",
                                   "memory_in_gb": 17.1,
                                   "core_count"  : 2,
                                   "cpu_power"   : 3.9
                                 },
    "hiMemDBInstClass.db.m2.2xlarge": { "product_size": "db.m2.2xlarge",
                                    "name"        : "High-Memory Double Extra Large DB Instance",
                                    "memory_in_gb": 34,
                                    "core_count"  : 4,
                                    "cpu_power"   : 3.9
                                  },
    "hiMemDBInstClass.db.m2.4xlarge": { "product_size": "db.m2.4xlarge",
                                     "name"        : "High-Memory Quadruple Extra Large DB Instance",
                                     "memory_in_gb": 68,
                                     "core_count"  : 8,
                                     "cpu_power"   : 3.9
                                   },
    "hiMemDBInstClass.db.cr1.8xl":    { "product_size": "db.cr1.8xlarge",
                                     "name"        : "High-Memory Cluster Eight Extra Large DB Instance",
                                     "memory_in_gb": 244,
                                     "core_count"  : 32,
                                     "cpu_power"   : 3.3
                                   },
}

def getRegionID(name):
    """ Returns a region ID from AWS json name.

    Arguments:
    :param name: region name in AWS json.

    :returns: region ID.
    :rtype: str
    """
    return REGION_MAP[name]

def getStorageName(name):
    """ Returns a storage name from AWS json name.

    Arguments:
    :param name: storage name in AWS json.

    :returns: storage name.
    :rtype: str
    """
    return STORAGE_NAME_MAP[name]

def getStorageDescription(name):
    """ Returns a description of the storage.

    Arguments:
    :param name: storage name in AWS json.

    :returns: storage description.
    :rtype: str
    """
    return STORAGE_DESCRIPTION_MAP[name]

def getStoragePricingThreshold(name):
    """ Returns a threshold of the storage.

    Arguments:
    :param name: storage name in AWS json.

    :returns: storage threshold.
    :rtype: int
    """
    return STORAGE_PRICING_THRESHOLD_MAP[name]

#def getRdsSpec(name):
#    """ Returns a speicification of RDS.
#
#    Arguments:
#    :param name: RDS name in AWS json.
#
#    :returns: speicification of RDS.
#    :rtype: dict
#    """
#    return RDS_MAP[name]

def getEC2ProductSize(prefix, suffix):
    """ Returns product_size from AWS json name.

    Arguments:
    :param prefix: EC2 type in AWS json.
    :param suffix: EC2 size in AWS json.

    :returns: product_size.
    :rtype: str
    """
    return EC2_TYPE_MAP[prefix] + "." + EC2_SIZE_MAP[suffix]
