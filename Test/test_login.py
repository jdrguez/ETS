import pytest
from login import login

def test_login():
    assert login('Pepe', 1234) == True
    assert login('Fran', 8910) == False
    assert login('Saul', 1290) == False