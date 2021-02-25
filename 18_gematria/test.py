#!/usr/bin/env python3
"""tests for gematria.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

prg = './gematria.py'


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
def test_statistics():
    """Finding the most common value in File and the corresponding words"""

    out = getoutput(f"{prg} './repeating.txt'")
    expected = "The most frequently occurring value is 300.\n" \
               "It corresponds to words:\ncde\ndce\nbdf"
    assert out.strip() == expected.strip()
