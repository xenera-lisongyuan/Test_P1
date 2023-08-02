from selenium import webdriver
import time
import unittest

class Test_Chrome1(unittest.TestCase):
    def test_chrome1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(2)
        driver.get("https://www.baidu.com")

if __name__ == '__main__':
    Test_Chrome1.test_chrome1()