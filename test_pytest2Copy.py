import pytest
import allure

@pytest.mark.run(order=13)
@allure.severity("normal")
@allure.story("Story1: test_pytest2_01")
@allure.title("Testcase: test_pytest2_01")
def test_pytest2_01():
    assert 0 == 0


@pytest.mark.run(order=10)
@allure.severity("critical")
@allure.title("title: test_pytest2_03")
def test_pytest2_04():
    assert 3 == 4


# if __name__ == '__main__':
#     pytest.main()
#     # pytest.main(['/test_pytest2.py', '-s', '-q', '--alluredir', '/report'])
#     # os.system('allure generate ./report -o ./report --clean')