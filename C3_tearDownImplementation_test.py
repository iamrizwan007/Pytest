import pytest

@pytest.fixture()	#@pytest.yield_fixture deprecated
def setUptearDown():
 print("setUp method")	#this will act as setUp, can be any name
 yield
 print("tearDown method") #this will act as a tearDown

def test_methodA(setUptearDown):
 print("method A execution")

def test_methodB(setUptearDown):
 print("method B execution")



