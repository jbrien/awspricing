aws-pricing
===========

Python scripts to retrieve pricing data from Amazon Web Services.

Usage
-----

usage: awspricing [-h] [--category {ebs,s3}] [--format {sql}]
                  [--cloudid CLOUDID] [--startid STARTID]

optional arguments:
  -h, --help            show this help message and exit
  --category {ebs,s3}, -c {ebs,s3}
                        Category of the pricing.
  --format {sql}, -f {sql}
                        Format of the output.
  --cloudid CLOUDID     AWS cloud ID for SQL output.
  --startid STARTID     Start number of primary key for SQL output.

