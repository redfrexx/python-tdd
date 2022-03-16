import pytest
from pytest_mock import MockerFixture
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


def test_mocked_method_with_side_effect(my_object):
    def side_effect(*args, **kwargs):
        return "Catherine"

    mocked_name = Mock(side_effect=side_effect)
    my_object.name = mocked_name
    assert my_object.greet() == "Hello, Catherine"
    mocked_name.assert_called()


def test_mocked_class():
    mock = Mock(MyClass)
    mock.greet.return_value = "Hello, Esra"
    assert mock.greet() == "Hello, Esra"
    assert isinstance(mock, MyClass)
    assert mock.greet.call_count == 1
    mock.greet.assert_called()


# Using mocker fixture (provided by pytest_mock) allows to skip unittest.mock imports
def test_mocked_class_with_pytest_mocker(mocker: MockerFixture):
    mock = mocker.Mock(MyClass)
    mock.greet.return_value = "Hello, Esra"
    assert mock.greet() == "Hello, Esra"
    assert isinstance(mock, MyClass)
    assert mock.greet.call_count == 1
    mock.greet.assert_called()
