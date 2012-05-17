from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'amazonify',
    version = '0.1',
    py_modules = ('amazonify',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = [],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/amazonify',
    keywords = 'amazon affiliate web',
    description = 'The simplest way to build Amazon Affiliate links, in Python.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
