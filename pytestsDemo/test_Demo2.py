#any python file should start with test_
#pytest method should be writing with test_
#metgid should have snese in naming
#-k stans for method execution,-s for logs in o/p,-v more info metadata
#u can write py.test <filename>
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg="Hello"
    assert msg == "Hi","Test failed"


def test_SecondCreditCard():
    a=4
    b=6
    assert a+2 == 6,"Addition Do not match"

@pytest.fixture()
def setup():
    print("I will be executing first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")