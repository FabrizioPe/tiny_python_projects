#!/usr/bin/env python3
"""tests for ransom.py"""

import os
import re
import random
from subprocess import getstatusoutput

prg = './ransom.py'
fox = '../inputs/fox.txt'
now = '../inputs/now.txt'


# --------------------------------------------------
def seed_flag():
    return '-s' if random.randint(0, 1) else '--seed'


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
    """Test"""

    in_text = 'The quick brown fox jumps over the lazy dog.'
    tests = [('1', 'Th3 $$1(k |3r$6n$|=ox$jump5 $ve$$t|-|e |_4z$ d$g$'),
             ('3', 'Th3$qu1(k |3$$wn |=ox j$m|`5$$%3r$the$l4$$$|)$(-.')]

    for seed, expected in tests:
        rv, out = getstatusoutput(f'{prg} {seed_flag()} {seed} "{in_text}"')
        assert rv == 0
        assert out.strip() == expected


# --------------------------------------------------
def test_text2():
    """Test"""

    in_text = 'Now is the time for all good men to come to the aid of the party.'
    tests = [
        ('2',
         'Now$i5$the$+1==3 f$$$4|_l good$me|=| +$$($==e$+o$+|-|3$41|)$o|= +|-|3$|`4r+$.'),
        ('5',
         '|=|$w$is t|-|3 +ime |=$r$all$good men$+o co==3 +$ t|-|e$4i|) $|=$+|-|e$|`ar+y$')
    ]

    for seed, expected in tests:
        rv, out = getstatusoutput(f'{prg} {seed_flag()} {seed} "{in_text}"')
        assert rv == 0
        assert out.strip() == expected


# --------------------------------------------------
def test_file1():
    """Test"""

    tests = [('1', 'Th3 $$1(k |3r$6n$|=ox$jump5 $ve$$t|-|e |_4z$ d$g$'),
             ('3', 'Th3$qu1(k |3$$wn |=ox j$m|`5$$%3r$the$l4$$$|)$(-.')]

    for seed, expected in tests:
        rv, out = getstatusoutput(f'{prg} {seed_flag()} {seed} {fox}')
        assert rv == 0
        assert out.strip() == expected


# --------------------------------------------------
def test_file2():
    """Test"""

    tests = [
        ('2',
         'Now$i5$the$+1==3 f$$$4|_l good$me|=| +$$($==e$+o$+|-|3$41|)$o|= +|-|3$|`4r+$.'),
        ('5',
         '|=|$w$is t|-|3 +ime |=$r$all$good men$+o co==3 +$ t|-|e$4i|) $|=$+|-|e$|`ar+y$')]

    for seed, expected in tests:
        rv, out = getstatusoutput(f'{prg} {seed_flag()} {seed} {now}')
        assert rv == 0
        assert out.strip() == expected
