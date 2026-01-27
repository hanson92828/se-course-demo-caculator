import pytest
from caculator.caculate import add_func
from caculator.caculate import subs_func

def test_add_func():
    assert add_func(1, 2) == 3
    assert add_func(-1, 1) == 0
    assert add_func(0, 0) == 0
    
def test_subs_func():
    assert subs_func(2, 1) == 1
    assert subs_func(-1, 1) == -2
    assert subs_func(0, 0) == 0 