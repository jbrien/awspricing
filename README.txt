awspricing
==========
Written by Sean Kang(@sean_kang)
https://github.com/sean-kang/awspricing

Python scripts to retrieve pricing data from Amazon Web Services.


Setup
-----
sudo python setup.py install


Usage
-----
usage: awspricing [-h] [--category {ec2,ebs,s3,glacier,rrs,rds}]
                  [--format {sql,csv}] [--cloudid CLOUDID] [--startid STARTID]

optional arguments:
  -h, --help            show this help message and exit
  --category {ec2,ebs,s3,glacier,rrs,rds}, -c {ec2,ebs,s3,glacier,rrs,rds}
                        Pricing data to print out. ec2: Elastic Compute Cloud,
                        ebs: Elastic Block Store, s3: Simple Storage Service,
                        glacier: Glacier, rrs: Reduced Redundancy Storage,
                        rds: Cloud Relational Database
  --format {sql,csv}, -f {sql,csv}
                        Format of the output. sql: Queries to enter pricing
                        data into enstratius database. csv: Comma-separated
                        values of pricing data.
  --cloudid CLOUDID     AWS cloud ID for SQL output.
  --startid STARTID     Start number of primary key for SQL output.

Special Thanks
--------------
Original idea was from ec2instancepricing by Eran Sandler(@erans)
https://github.com/erans/ec2instancespricing
