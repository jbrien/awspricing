awspricing
==========
Writeen by Sean Kang(@sean_kang)
https://github.com/sean-kang/awspricing

Python scripts to retrieve pricing data from Amazon Web Services.


Setup
-----
sudo python setup.py install


Usage
-----
usage: awspricing [-h] [--category {ebs,storage,glacier,rrs,rds}]
                  [--format {sql,csv}] [--cloudid CLOUDID] [--startid STARTID]

optional arguments:
  -h, --help            show this help message and exit
  --category {ebs,storage,glacier,rrs,rds}, -c {ebs,storage,glacier,rrs,rds}
                        Pricing data to print out.
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
