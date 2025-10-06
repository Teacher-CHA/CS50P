from numb3rs import validate

def test_validate_number():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True
    assert validate("275.3.6.28") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False

def test_validate_text():
    assert validate("cat") == False

def test_validate_standard():#加了这一个就能通过测试，不加这个就过不了，我感到很困惑
    assert validate("275.3.6.28") == False
    assert validate("hello") == False
    assert validate("10.0.10") == False
    assert validate("192.168.1.1.1") == False
    assert validate("255.256.256.256") == False

    assert validate("192.168.1.1") == True
    assert validate("10.0.0.1") == True
    assert validate("172.16.0.1") == True
    assert validate("255.255.255.255") == True