from distutils.core import setup

setup(
    name='awspricing',
    version='0.1.1',
    author=['Sean Kang', 'John Dilts'],
    author_email=['es.guybrush@gmail.com', "john.dilts@enstratius.com"],
    packages=['awspricing'],
    scripts=['bin/awspricing'],
    url='http://github.com/jbrienawspricing',
    license='Apache 2.0',
    description='Retrieve pricing data from AWS',
)
