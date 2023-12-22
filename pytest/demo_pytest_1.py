import sys

import pytest

@pytest.mark.skip
def test1():
    x = 10
    y = 10
    assert x == y

@pytest.mark.skipif(sys.version_info<(3,15),reason="python version is not supported")
def test2():
    name = "selenium"
    title = "selenium for automation"
    assert name in title, "title does not match"

@pytest.mark.xfail
def test3():
    assert False
    print("hello")


def test4():
    assert True
    print("close")
