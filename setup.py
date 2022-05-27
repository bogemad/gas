#!/usr/bin/env python3

from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "gas",
    version = "0.1",
    author = "Daniel Bogema",
    author_email = "daniel.bogema@dpi.nsw.gov.au",
    description = ("GAS (Genbank Annotation Statistics): Basic annotation statistics for eukaryotic genomes from Genbank files."),
    license = "GPL-3.0",
    keywords = "genomics gene annotation statistics",
    url = "https://github.com/bogemad/gas",
    py_modules=['gas/gas.py'],
    scripts=['bin/gas'],
    long_description=read('README.md'),
)
