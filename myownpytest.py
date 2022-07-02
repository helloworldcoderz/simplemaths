import myown
import pytest

def test_add():
    print("calling add ")
    assert myown.add(1,1) == 2
 
def test_sub():
    print("calling sub ")
    assert myown.sub(1,1) == 0


def test_add2():
    print("calling add 2 ")
    assert myown.add(1,5) == 6



