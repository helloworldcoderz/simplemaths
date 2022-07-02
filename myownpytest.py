import myown
import pytest

def test_add():
    assert myown.add(1,1) == 2
 
def test_sub():
    assert myown.sub(1,1) == 0


def test_add2():
    assert myown.add(1,5) == 2


