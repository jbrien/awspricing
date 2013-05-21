REGION_MAP = {
    "us-east"    : "us-east-1",
    "us-west"    : "us-west-1",
    "us-west-2"  : "us-west-2",
    "eu-ireland" : "eu-west-1",
    "apac-sin"   : "ap-southeast-1",
    "apac-syd"   : "ap-southeast-2",
    "apac-tokyo" : "ap-northeast-1",
    "sa-east-1"  : "sa-east-1"
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

STORAGE_PRICING_THRESHOLD_MAP = {
    "firstTBstorage"    : 0,
    "next49TBstorage"   : 1000,
    "next450TBstorage"  : 50000,
    "next500TBstorage"  : 500000,
    "next4000TBstorage" : 1000000,
    "over5000TBstorage" : 5000000
}

RDS_MAP = {
    "dbInstClass.uDBInst"  : { "product_size": "db.t1.micro",
                               "name"        : "Micro DB Instance",
                               "memory_in_gb": 0.63,
                               "core_count"  : 1,
                               "cpu_power"   : 1.2
                             },
    "dbInstClass.smDBInst" : { "product_size": "db.m1.small",
                               "name"        : "Small DB Instance",
                               "memory_in_gb": 1.7,
                               "core_count"  : 1,
                               "cpu_power"   : 1.2
                             },
    "dbInstClass.medDBInst": { "product_size": "db.m1.medium",
                               "name"        : "Medium DB Instance",
                               "memory_in_gb": 3.75,
                               "core_count"  : 1,
                               "cpu_power"   : 2.4
                             },
    "dbInstClass.lgDBInst" : { "product_size": "db.m1.large",
                               "name"        : "Large DB Instance",
                               "memory_in_gb": 7.5,
                               "core_count"  : 2,
                               "cpu_power"   : 2.4
                             },
    "dbInstClass.xlDBInst" : { "product_size": "db.m1.xlarge",
                               "name"        : "Extra Large DB Instance",
                               "memory_in_gb": 15,
                               "core_count"  : 4,
                               "cpu_power"   : 2.4
                             },
    "hiMemDBInstClass.xlDBInst": { "product_size": "db.m2.xlarge",
                                   "name"        : "High-Memory Extra Large DB Instance",
                                   "memory_in_gb": 17.1,
                                   "core_count"  : 2,
                                   "cpu_power"   : 3.9
                                 },
    "hiMemDBInstClass.xxlDBInst": { "product_size": "db.m2.2xlarge",
                                    "name"        : "High-Memory Double Extra Large DB Instance",
                                    "memory_in_gb": 34,
                                    "core_count"  : 4,
                                    "cpu_power"   : 3.9
                                  },
    "hiMemDBInstClass.xxxxDBInst": { "product_size": "db.m2.4xlarge",
                                     "name"        : "High-Memory Quadruple Extra Large DB Instance",
                                     "memory_in_gb": 68,
                                     "core_count"  : 8,
                                     "cpu_power"   : 3.9
                                   }
}

def getRegionID(name):
    return REGION_MAP[name]

def getStorageName(name):
    return STORAGE_NAME_MAP[name]

def getStorageDescription(name):
    return STORAGE_DESCRIPTION_MAP[name]

def getStoragePricingThreshold(name):
    return STORAGE_PRICING_THRESHOLD_MAP[name]

def getRdsSpec(name):
    return RDS_MAP[name]
