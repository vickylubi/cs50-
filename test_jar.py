import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12  # default capacity
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size==3
    jar.deposit(9)
    assert jar.size==12
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(4)
    assert jar.size == 6
    jar.withdraw(6)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(2)