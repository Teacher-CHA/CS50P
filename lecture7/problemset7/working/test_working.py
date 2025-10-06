from working import convert_time#自己测试的时候可以看看这个新函数是否正确，但是当提交该函数时，会出现错误
from working import convert
import pytest


def test_convert_time():#自己测试的时候可以看看这个新函数是否正确，但是当提交该函数时，会出现错误
    assert convert_time("9","AM") == "09:00"
    assert convert_time("9:00","AM") == "09:00"
    assert convert_time("12","AM") == "00:00"
    assert convert_time("12:00","AM") == "00:00"
    assert convert_time("1","PM") == "13:00"
    assert convert_time("1:01","PM") == "13:01"


def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")