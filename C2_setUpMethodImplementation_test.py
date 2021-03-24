import pytest

@pytest.fixture()
def setUp():
 print("setUp method")	#this will act as setUp, can be any name

def test_methodA(setUp):
 print("method A execution")

def test_methodB(setUp):
 print("method B execution")



