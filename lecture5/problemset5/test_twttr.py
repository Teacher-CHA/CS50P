"""
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with pytest test_twttr.py
"""
import pytest
from twttr import shorten

def test_lowercase():
    for letter in "aeiou":
        assert shorten(letter) == ""

def test_uppercase():
    for letter in "AEIOU":
        assert shorten(letter) == ""
