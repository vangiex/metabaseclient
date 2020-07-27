# -*- coding: utf-8 -*-
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='MetabaseClient',
    version='0.1.0',
    description='Metabase python wrapper is built upon Metabase restful API to help its users in extending features and adding more capability.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Rahul Rathi',
    author_email='VanGiex.RR@Gmail.com',
    url='https://github.com/vangiex/metabaseclient',
    packages=find_packages(exclude=('tests', 'docs'))
)
