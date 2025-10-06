"""
Either before or after you implement count in um.py, additionally implement, in a file called test_um.py, 
three or more functions that collectively test your implementation of count thoroughly, each of whose names should begin with test_
"""
from um import count

def test_count():
    assert count("hello world") == 0
    assert count("yummy") == 0
    assert count("umum") == 0
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2