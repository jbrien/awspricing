from distutils.core import setup

setup(
    name='awspricing',
    version='0.1.0',
    author='Sean Kang',
    author_email='es.guybrush@gmail.com',
    packages=['awspricing'],
    scripts=['bin/awspricing'],
    url='http://github.com/sean-kang/awspricing',
    license='Apache 2.0',
    description='Retrieve pricing data from AWS',
)
