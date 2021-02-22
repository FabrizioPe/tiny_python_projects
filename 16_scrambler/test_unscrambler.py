#!/usr/bin/env python3
"""tests for unscrambler.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

prg = './unscrambler.py'
fox = '../inputs/fox.txt'
bustle = '../inputs/the-bustle.txt'
spiders = '../inputs/spiders.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text1():
    """Text"""

    out = getoutput(f'{prg} cihekcn')
    assert out.strip() == 'chicken'


# --------------------------------------------------
def test_text2():
    """Text"""

    text = 'The qicuk bworn fox jmup over the lzay dog.'
    expected = 'The quick brown fox jump over the lazy dog.'
    out = getoutput(f'{prg} "{text}"')
    assert out.strip() == expected
