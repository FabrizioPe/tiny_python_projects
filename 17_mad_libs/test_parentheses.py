#!/usr/bin/env python3
"""Test for parentheses.py"""

import os
import re
from subprocess import getstatusoutput

prg = './parentheses.py'


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
        assert out.lower().startswith('usage')
        
        
# --------------------------------------------------
def test_bad_file():
    """Test bad input file"""

    bad = 'blargh.txt'
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)
    
    
# --------------------------------------------------
def test_no_paretheses():
    """Test a file with no paretheses"""
    
    rv, out = getstatusoutput(f'{prg} ./inputs/no_blanks.txt')
    assert rv != 0
    assert re.search('"./inputs/no_blanks.txt" has no parentheses.', out)


# --------------------------------------------------
def test_parentheses():
    """Test a file with balanced/unbalanced parentheses"""

    rv, out = getstatusoutput(f'{prg} ./inputs/parentheses.txt')
    assert rv == 0
    assert out.strip() == """The balanced parentheses are: ['(bilanciate)', '[questa]', "{quest'altro}"]
The unbalanced parentheses are: ['((questo)))', '[[non]', '[hello]]', '{questa}}']"""

