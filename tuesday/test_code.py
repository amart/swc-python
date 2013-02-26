#

from code import stuff

def test_empty():
    assert stuff([]) == []

def test_single_value():
    assert stuff([1]) == [2]

def test_negative_value():
    assert stuff([-5]) == []
 
def test_zero_value():
    assert stuff([0]) == [0]

def test_lots_of_values():
    assert stuff([-1,2,-3,4,5,-6,7,-8,9]) == [4,8,10,14,18]

