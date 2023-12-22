import pytest

@pytest.mark.parametrize("username,password",
                         [
                             ("a","1"),
                             ("b","2"),
                             ("c","3")
                         ])
def test_login(username,password):
    print(username)
    print(password)