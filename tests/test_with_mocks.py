import pytest
# import pytest_mock
from unittest.mock import Mock


class MyClass():
    def name(self):
        return "Johannes"

    def greet(self):
        return "Hello, " + self.name()


@pytest.fixture
def my_object():
    return MyClass()


def test_greet(my_object):
    assert my_object.greet() == "Hello, Johannes"


def test_mocked_method(my_object):
    mocked_name = Mock(return_value="Frank")
    my_object.name = mocked_name
    assert my_object.greet() == "Hello, Frank"


def test_mocked_class():
    mock = Mock(MyClass)
    mock.greet.return_value = "Hello, Frank"
    assert mock.greet() == "Hello, Frank"
    assert isinstance(mock, MyClass)
