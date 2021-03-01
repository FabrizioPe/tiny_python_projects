#!/usr/bin/env python3
"""Module for functions used in wod.py, a program
for doing practice with csv files. Most funcs are
for checking input csv files"""


import os
import random
import re
import sys


# --------------------------------------------------
def check_empty(fh):
    """Interrupt the program if file is empty"""

    fh.seek(0)
    if os.stat(fh.name).st_size == 0:
        sys.exit(f"'{fh.name}' is empty")


# --------------------------------------------------
def check_headers_only(fh):
    """Interrupt the program if file contains only headers"""

    fh.seek(0)  # rewind the file to the beginning
    fh.readline()  # consume the headers
    if fh.readline() == '':
        sys.exit(f"'{fh.name}' contains headers only")


# --------------------------------------------------
def check_bad_headers(fh, delimiter=','):
    """Interrupt the program if file contains title headers
    (like Exercise instead of exercise)"""

    fh.seek(0)
    headers = fh.readline().rstrip().split(delimiter)
    for header in headers:
        if not header.islower():
            sys.exit(f"'{fh.name}' contains badly-formatted headers")


# --------------------------------------------------
def check_bad_delimiters(fh):
    """Check that the delimiter is the comma"""
    fh.seek(0)
    header = fh.readline().strip()
    match = re.match(r'\w+,.+', header)
    if not match:
        sys.exit(f'{fh.name} has not comma as delimiter')


# -----------------------------------
def well_formatted_reps(exercises: list) -> list:
    """Filter out badly formatted reps from the list of exercises"""

    good_format = lambda exc: re.match(r'\d+-\d+', exc[1])
    return list(filter(good_format, exercises))


# --------------------------------------------------
def random_reps(interval: str) -> int:
    """Randomly determine reps from a given interval:
       Ex: '30-50' -> 42"""

    matches = re.match('([0-9]+)-([0-9]+)', interval)
    return random.randint(int(matches.group(1)), int(matches.group(2)))
