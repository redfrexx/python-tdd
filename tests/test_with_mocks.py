import pytest
import pytest_mock
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
    # How can I mock my_object.name() to return something else?
    assert my_object.greet() == "Hello, Johannes"