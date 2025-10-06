import pytest
from plates import is_valid

def test_length():#条件2
    assert is_valid("A") == False
    assert is_valid("ABCDEFGHI") == False
    assert is_valid("ABCD") == True

def test_startswithalpha():#条件1
    assert is_valid("1234") == False
    assert is_valid("A123") == False
    assert is_valid("AB123") == True

def test_lastdigit():#条件3：检验是否数字后还有字母
    assert is_valid("AB12A") == False
    assert is_valid("AB12") == True

def test_firstzero():#条件3*：检验第一个数字是否是0
    assert is_valid("AB01") == False
    assert is_valid("AB1") == True

def test_alphaanddigit():#条件4：检验字符串里的每个元素是否是字母或数字
    assert is_valid("AB!!") == False
    assert is_valid("AB520") == True

