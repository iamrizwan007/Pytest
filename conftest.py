import pytest

@pytest.fixture(scope='module')
def setUptearDownClass():
 print("setUpClass activity")
 yield
 print("tearDownClass activity")

@pytest.fixture()
def setUptearDown():
 print("setUp activity")
 yield
 print("tearDown activity")