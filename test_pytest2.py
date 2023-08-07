import pytest
import allure

@pytest.mark.run(order=13)
@allure.severity("normal")
@allure.story("Story1: test_pytest2_01")
@allure.title("Testcase: test_pytest2_01")
def test_pytest2_01():
    assert 0 == 0

@pytest.mark.run(order=12)
@allure.issue("https://selenium-python-zh.readthedocs.io/en/latest/")
@allure.severity("blocker")
@allure.story("Story1: test_pytest2_02")
@allure.title("Testcase: test_pytest2_02")
def test_pytest2_02():
    assert 1 == 2

@pytest.mark.run(order=11)
@allure.severity("critical")
@allure.epic("epic: test_pytest2_03")
@allure.title("title: test_pytest2_03")
@allure.feature("feature: test_pytest2_03")
@allure.story("story: test_pytest2_03")
def test_pytest2_03():
    assert 2 == 3

@pytest.mark.run(order=10)
@allure.severity("critical")
@allure.title("title: test_pytest2_03")
def test_pytest2_04():
    assert 3 == 4

@pytest.mark.run(order=9)
@allure.severity("minor")
@allure.title("title: test_pytest2_05")
def test_pytest2_05():
    assert 4 == 5

@pytest.mark.run(order=8)
@pytest.mark.failed
@allure.severity("trivial")
@allure.title("title: test_pytest2_06")
def test_pytest2_06():
    assert 5 == 6

# if __name__ == '__main__':
#     pytest.main()
#     # pytest.main(['/test_pytest2.py', '-s', '-q', '--alluredir', '/report'])
#     # os.system('allure generate ./report -o ./report --clean')