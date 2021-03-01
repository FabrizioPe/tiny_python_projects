#!/usr/bin/env python3
"""All tests for inputCheck module"""

import pytest
from inputCheck import *


# --------------------------------------------------
def test_check_empty():
    """Test for check_empty function"""

    empty_fh = open('inputs/bad-empty.csv')
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_empty(empty_fh)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code != 0


# --------------------------------------------------
def test_check_headers_only():
    """Test for check_headers_only: taken from
    medium.com/python-pandemonium/
    testing-sys-exit-with-pytest-10c6e5f7726f
    Not understood deeply."""

    headers_only = open('inputs/bad-headers-only.csv')
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_headers_only(headers_only)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code != 0


# --------------------------------------------------
def test_check_bad_headers():
    """Test for check_bad_headers function"""
    bad_headers_fh = open('inputs/bad-headers.csv')
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_bad_headers(bad_headers_fh)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code != 0


# --------------------------------------------------
def test_check_bad_delimiters():
    """Test for check_bad_delimiter"""
    bad_delimiters = open('inputs/bad-delimiter.tab')
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_bad_delimiters(bad_delimiters)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code != 0


# -----------------------------------
def test_well_formatted_reps():
    """Test well_formatted_reps function"""

    badly_formatted = [('Burpees', '20'), ('Situps', 'NA'),
                       ('Squats', '4-90'), ('Ciclette', '40.6-56'),
                       ('Jumps', 'forty-60'), ('Pushups', '')]
    expected = [('Squats', '4-90')]

    assert well_formatted_reps(badly_formatted) == expected


# --------------------------------------------------
def test_random_reps():
    """Test random_reps"""
    state = random.getstate()
    random.seed(1)
    assert random_reps('10-30') == 14
    assert random_reps('50-90') == 86
    assert random_reps('25-50') == 50
    random.setstate(state)
