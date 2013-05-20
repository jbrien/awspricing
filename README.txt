awspricing
==========

Python scripts to retrieve pricing data from Amazon Web Services.


Setup
-----
sudo python setup.py install


Usage
-----

usage: awspricing [-h] [--category {ebs,s3}] [--format {sql}]
                  [--cloudid CLOUDID] [--startid STARTID]

optional arguments:
  -h, --help            show this help message and exit
  --category {ebs,s3}, -c {ebs,s3}
                        Pricing data to print out.
  --format {sql}, -f {sql}
                        Format of the output. sql: Queries to enter pricing
                        data into enstratius database.
  --cloudid CLOUDID     AWS cloud ID for SQL output.
  --startid STARTID     Start number of primary key for SQL output.
