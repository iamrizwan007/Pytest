import pytest
import time
from selenium import webdriver

class TestGoogleSearch:
 @pytest.fixture()
 def setUptearDown(self):
  global driver
  driver = webdriver.Chrome(executable_path='C:\\Users\\mrizwan5\\Desktop\\Python\\Selenium\\chromedriver.exe')
  driver.get("https://www.google.com/")
  driver.maximize_window()
  yield
  time.sleep(10)
  driver.close()

 def test_googlesearch(self,setUptearDown):
   driver.find_element_by_name('q').send_keys('Mahesh Babu')
   time.sleep(2)
   driver.find_element_by_name('btnK').click()
   driver.find_element_by_class_name('LC20lb').click()
   title ='Mahesh Babu - Wikipedia'
   assert title == driver.title