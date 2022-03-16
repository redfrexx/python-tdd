import pytest
# import pytest_mock
from unittest.mock import Mock, patch


class MyClass():
    def name(self):
        return "Johannes"

    def greet(self):
        return "Hello, " + self.name()


@pytest.fixture
def my_object():
    return MyClass()

def test_mocked_class():
    mock = Mock(MyClass)
    mock.greet.return_value = "Hello, Frank"
    assert mock.greet() == "Hello, Frank"

def test_greet(my_object):
    assert my_object.greet() == "Hello, Johannes"

def test_patched_object(my_object):
    with patch.object(my_object, 'greet') as mock_greet:
        def side_effect(a):
            return "Hello, Frank"
        mock_greet.side_effect = side_effect
    # The following does not work. I wonder why.
    # assert my_object.greet() == "Hello, Frank"