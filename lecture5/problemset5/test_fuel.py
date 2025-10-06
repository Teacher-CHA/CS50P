"""
implement two or more functions that collectively test your implementations of convert and gauge thoroughly, 
each of whose names should begin with test_ 
"""
from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("0/100") == 0
    assert convert("100/100") == 100
    assert convert("99/100") == 99

    with pytest.raises(ValueError):
        convert("a/b")
    
    with pytest.raises(ValueError):
        convert("99/3")

    with pytest.raises(ValueError):
        convert("1.1/4")
    
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("!/?")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"