import pytest

@pytest.fixture(scope='module')	#to implement setUpClass and tearDownClass
def setUpClasstearDownClass():
 print("global setUp method")	#this will act as setUp, can be any name
 yield
 print("global tearDown method") #this will act as a tearDown

@pytest.fixture()	
def setUptearDown():
 print("setUp method")
 yield
 print("tearDown method") 

def test_methodA(setUpClasstearDownClass,setUptearDown):
 print("method A execution")

def test_methodB(setUpClasstearDownClass,setUptearDown):
 print("method B execution")
