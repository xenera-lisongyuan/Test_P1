from selenium import webdriver
import time
import unittest

class Test_P1_UI(unittest.TestCase):

    def test_edge1(self):
        """This function is aim to test Edge Browser"""
        driver = webdriver.Edge()
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://www.baidu.com")
        # # 打印搜索结果的标题
        # print(driver.title)
        assert driver.title == "百度一下，你就知道"
        driver.close()

    def test_chrome1(self):
        """This function is aim to test Chrome Browser"""
        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(1)
        driver.get("https://www.baidu.com")
        # # 打印搜索结果的标题
        # print(driver.title)
        assert driver.title == "百度一下，你就知道"
        driver.close()

if __name__ == '__main__':
    Test_P1_UI.test_edge1()
    Test_P1_UI.test_chrome1()