import os
import pytest
import time

if __name__ == '__main__':
    """Please use this main function to start all the test cases. Then the results will be published with Allure Report"""
    os.system("pytest --alluredir=./report  --clean-alluredir")
    pytest.main()
    time.sleep(2)
    os.system("allure generate report -o report\\allure-report -c report\\allure-report")
    os.system("allure open report\\allure-report")

    """Please use this main function to start all the test cases. Then the results will be published with html Report"""
    # pytest.main()