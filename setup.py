#!/usr/bin/env python3

from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "gbk_annotation_stats",
    version = "0.1",
    author = "Daniel Bogema",
    author_email = "daniel.bogema@dpi.nsw.gov.au",
    description = ("GBK annotation stats: Basic annotation statistics for eukaryotic genomes"),
    license = "GPL-3.0",
    keywords = "genomics gene annotation statistics",
    url = "https://github.com/bogemad/gbk_annotation_stats",
    py_modules=['gbk_annotation_stats/gbk_annotation_stats.py'],
    scripts=['bin/gbk_annotation_stats'],
    long_description=read('README.md'),
)
