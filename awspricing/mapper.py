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

def getRegionID(name):
    return REGION_MAP[name]

def getStorageName(name):
    return STORAGE_NAME_MAP[name]

def getStorageDescription(name):
    return STORAGE_DESCRIPTION_MAP[name]

def getStoragePricingThreshold(name):
    return STORAGE_PRICING_THRESHOLD_MAP[name]
