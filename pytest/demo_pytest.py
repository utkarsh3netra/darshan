import pytest

@pytest.mark.select
def test1():
    x = 10
    y = 10
    assert x == y

@pytest.mark.test
def test2():
    name = "selenium"
    title = "selenium for automation"
    assert name in title, "title does not match"

@pytest.mark.select
def test3():
    print("hello")
