#!usr/bin/env python3

import os
from subprocess import getstatusoutput

prg = './jump_gf.py'
input_numbers = '566-431'


# --------------------------------------------------
def test_exist():

	assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():

	for flag in ['-h', '--help']:
		st, rv = getstatusoutput(f'{prg} {flag}')
		assert st == 0
		assert rv.startswith('usage')


# --------------------------------------------------
def test_num_input():

	st, rv = getstatusoutput(f"{prg} '566-431'")
	assert st == 0
	assert rv == 'five six six -four three one '


# --------------------------------------------------
def test_alphanum_input():

	st, rv = getstatusoutput(f"{prg} 'Hi, my number is 566-432, call me!'")
	print(st)
	assert st == 0
	assert rv == 'Hi, my number is five six six -four three two , call me!'
