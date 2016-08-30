#!/usr/bin/env/ python
from setuptools import setup, find_packages
import os

# retrieve the version
try:
    versionfile = os.path.join('{packagename_file}','__version__.py')
    f = open( versionfile, 'r')
    content = f.readline()
    splitcontent = content.split('\'')
    version = splitcontent[1]
    f.close()
except:
    raise Exception('Could not determine the version from {packagename_file}/__version__.py')


# run the setup command
setup(
    name='{packagename}',
    version=version,
    license='{license}',
    description='{description}',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='{url}',
    author='{author}',
    author_email='{author_email}',
    packages=find_packages(),
    install_requires=[],
    classifiers=['Programming Language :: Python :: 2.7'],
)
