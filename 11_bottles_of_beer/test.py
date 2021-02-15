#!/usr/bin/env python3
"""tests for bottles.py"""

# import hashlib
import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './bottles.py'


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
def test_bad_int():
    """Bad integer value"""

    bad = random.randint(-10, 0)
    rv, out = getstatusoutput(f'{prg} -n {bad}')
    assert rv != 0
    assert re.search(f'--num "{bad}" must be greater than 0', out)


# --------------------------------------------------
def test_float():
    """float value"""

    bad = round(random.random() * 10, 2)
    rv, out = getstatusoutput(f'{prg} --num {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_str():
    """str value"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -n {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_too_many_beers():
    """The program can handle 10 beers at max when going down"""

    bad = random.randint(11, 99)
    rv, out = getstatusoutput(f'{prg} -n {bad}')
    assert rv != 0
    assert re.search('No more than 10 beers when going down, please!', out)


# --------------------------------------------------
def test_one():
    """One bottle of beer"""

    expected = ('One bottle of beer on the wall,\n'
                'One bottle of beer,\n'
                'Take one down, pass it around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} --num 1')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_two():
    """Two bottles of beer"""

    expected = ('Two bottles of beer on the wall,\n'
                'Two bottles of beer,\n'
                'Take one down, pass it around,\n'
                'One bottle of beer on the wall!\n\n'
                'One bottle of beer on the wall,\n'
                'One bottle of beer,\n'
                'Take one down, pass it around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} -n 2')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_step():
    """Taking down two beers each time"""

    expected = ('Three bottles of beer on the wall,\n'
                'Three bottles of beer,\n'
                'Take two down, pass it around,\n'
                'One bottle of beer on the wall!\n\n'
                'One bottle of beer on the wall,\n'
                'One bottle of beer,\n'
                'Take two down, pass it around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} -n 3 --step 2')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
# def test_random():
#     """Random number"""
#
#     sums = dict(
#         map(lambda x: x.split('\t'),
#             open('sums.txt').read().splitlines()))
#
#     for n in random.choices(list(sums.keys()), k=10):
#         flag = '-n' if random.choice([0, 1]) == 1 else '--num'
#         rv, out = getstatusoutput(f'{prg} {flag} {n}')
#         out += '\n'  # because the last newline is removed
#         assert rv == 0
#         assert hashlib.md5(out.encode('utf-8')).hexdigest() == sums[n]


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
