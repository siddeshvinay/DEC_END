from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import ErrorHandler
from selenium.common.exceptions import *
import unittest

# driver=webdriver.Chrome()
#
# driver.get('http://www.google.com')
# driver.maximize_window()
# #driver.get("https://www.bing.com/")
# if "Google" in driver.title:
#     print("paass")
# assert "Google" in driver.title
# # # el=driver.find_element_by_xpath("//input")
# # # #el=driver.find_element_by_xpath("//a")
# # # el.send_keys("Test")
# # # el.clear()
# # el.send_keys(Keys.RETURN)

class PythonOrg(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()


    def test_launchbrowser(self):
        driver=self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python",driver.title)
        dl=driver.find_element_by_name("q")
        dl.send_keys("Python")
        dl.send_keys(Keys.RETURN)
        assert "No results found" not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
