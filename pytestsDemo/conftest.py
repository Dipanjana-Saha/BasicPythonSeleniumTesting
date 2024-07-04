import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is created")
    return ["Dipanjana","Saha","nicedipa.com"]

@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return request.param