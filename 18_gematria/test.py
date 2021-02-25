#!/usr/bin/env python3
"""tests for gematria.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

prg = './gematria.py'
spiders = '../inputs/spiders.txt'
fox = '../inputs/fox.txt'
sonnet = '../inputs/sonnet-29.txt'
devilish = './my_words.txt'


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
def test_devilish():
    """File with words which map to 666"""

    out = getoutput(f'{prg} {devilish}')
    expected = "Devilish words in your text:\nddddddB\ndddBddd"
    assert out.strip() == expected.strip()