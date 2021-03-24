import pytest

@pytest.fixture(scope='module')	#to implement setUpClass and tearDownClass
def setUpClasstearDownClass():
 print("setUp method")	#this will act as setUp, can be any name
 yield
 print("tearDown method") #this will act as a tearDown

def test_methodA(setUpClasstearDownClass):
 print("method A execution")

def test_methodB(setUpClasstearDownClass):
 print("method B execution")
