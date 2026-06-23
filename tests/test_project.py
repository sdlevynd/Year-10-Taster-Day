import pytest
from main.main import add, subtract

def test_add():
    assert add(2,2) == 4
    assert add(10,10) == 20

def test_subtract():
    assert subtract(10,5) == 5