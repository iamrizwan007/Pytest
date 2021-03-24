import pytest
import time
from selenium import webdriver

class TestHMS:
 @pytest.fixture(scope = 'module')
 def setUptearDownClass(self):
  global driver
  driver = webdriver.Chrome(executable_path='C:\\Users\\mrizwan5\\Desktop\\Python\\Selenium\\chromedriver.exe')
  driver.get("http://www.seleniumbymahesh.com/")
  driver.maximize_window()
  yield
  time.sleep(5)
  driver.close()

 def test_hms_login(self,setUptearDownClass):
  driver.find_element_by_link_text("HMS").click()
  time.sleep(2)
  driver.find_element_by_name("username").send_keys("admin")
  driver.find_element_by_name("password").send_keys("admin")
  driver.find_element_by_name("submit").click()
  title = "Master Page"
  assert title == driver.title
  time.sleep(5)

 def test_hms_logout(self,setUptearDownClass):
  driver.find_element_by_link_text("Logout").click()
  title = "User Login Page"
  assert title == driver.title
