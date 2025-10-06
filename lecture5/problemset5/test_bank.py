"""
 three or more functions that collectively test your implementation of value thoroughly, 
 each of whose names should begin with test_ 
"""
import pytest
from bank import value

def test_startswithhello():
    assert value("hello") == 0
    assert value("hello, world") == 0

def test_startswithh():
    assert value("hi") == 20
    assert value("hi, world") == 20

def test_startswithelse():
    assert value("nihao") == 100
    assert value("nihao, shijie") == 100