import os
import pytest
import time

# -------Below are debug os.system("python ./test_pytest.py")-------
# os.system("python ./1test_ui_chrome1.py")
# os.system("python ./test_api_get2.py")
# os.system("python ./1test_api_post1.py")
# os.system("python ./1test_api_post2.py")
# os.system("python ./test_pytest4.py")
# os.system("python ./1test_pytest2.py")

if __name__ == '__main__':
    """Please use this file to start all the test cases. Then the results will be published with Allure Report"""
    pytest.main()
    # time.sleep(2)

    # os.system("pytest --alluredir=./report  --clean-alluredir")
    # os.system("pytest 1test_pytest2.py -vs --alluredir=./report")
    # # os.system("pytest 1test_pytest2.py -vs --alluredir=./report")
    # # os.system("pytest 1test_pytest3.py -vs --alluredir=./report")
    # # os.system("pytest test_pytest4.py -vs --alluredir=./report")
    # # # os.system("pytest test_pytest4.py -vs --alluredir=./report  --clean-alluredir")
    # # # os.system("copy environment.properties report\\")
    # os.system("allure generate report -o report\\allure-report -c report\\allure-report")
    # os.system("allure open report\\allure-report")