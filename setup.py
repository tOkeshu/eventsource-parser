from setuptools import setup, find_packages
from eventsource_parser import __version__

with open('README.rst') as f:
    README = f.read()

classifiers = ["Programming Language :: Python",
               "License :: OSI Approved :: Apache Software License",
               "Development Status :: 4 - Beta"]


setup(name='eventsource_parser',
      version=__version__,
      url='https://github.com/tOkeshu/eventsource-parser',
      packages=find_packages(),
      long_description=README,
      description="A pure python, framework agnostic EventSource parser",
      author="Romain Gauthier",
      author_email="romain.gauthier@monkeypatch.me",
      include_package_data=True,
      classifiers=classifiers)
