from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar("cat")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit(11)
    with pytest.raises(ValueError):
        jar.deposit("cat")
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(7)
    assert jar.size == 10

def test_withdraw():
    jar = Jar(12)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw(13)
    with pytest.raises(ValueError):
        jar.withdraw("cat")
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size == 4
    
    