import pytest
@pytest.mark.run(order=3)
def test_methodC():
 print("test C")

@pytest.mark.run(order=2)
def test_methodB():
 print("test B")

@pytest.mark.run(order=1)
def test_methodA():
 print("test A")