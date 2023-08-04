import pytest
import os
import time

if __name__ == '__main__':
    # pytest.main(["./", "-sv", "--report", "./report/temp_jsonreport -o ./report/html --clean"])
    pytest.main(["./", "-sv", "--report", "./report -o"])
    time.sleep(2)
    # os.system("allure generate ./report/temp_jsonreport -o ./report/html --clean")
    os.system("allure generate ./report -o")