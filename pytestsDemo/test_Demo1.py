#any python file should start with test_
#pytest method should be writing with test_

import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)