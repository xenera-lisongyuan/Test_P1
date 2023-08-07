import pytest
import allure

@pytest.mark.run(order=1)
@pytest.mark.slow
@allure.severity("normal")
@allure.story("Story1: test_pytest4_01")
@allure.title("Testcase: test_pytest4_01")
def test_pytest4_01():
    assert 0 == 0

# if __name__ == '__main__':
#     pytest.main()
#     # pytest.main(['/test_pytest2.py', '-s', '-q', '--alluredir', '/report'])
#     # os.system('allure generate ./report -o ./report --clean')