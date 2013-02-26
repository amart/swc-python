#

from code import stuff

def test_empty():
    assert stuff([]) == []

def test_single_value():
    assert stuff([1]) == [2]

def test_negative_value():
    assert stuff([-5]) == []
 
