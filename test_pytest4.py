import pytest
import allure

@pytest.mark.slow
@allure.severity("normal")
@allure.story("Story1: test_pytest4_01")
@allure.title("Testcase: test_pytest4_01")
def test_pytest4_01():
    assert 0 == 0

@pytest.mark.quick
@pytest.mark.skipif(condition=True, reason="test skip")
@allure.severity("normal")
@allure.story("Story1: test_pytest4_02")
@allure.title("Testcase: test_pytest4_02")
def test_pytest4_02():
    assert 1 == 1

@allure.severity("normal")
@allure.story("Story1: test_pytest4_03")
@allure.title("Testcase: test_pytest4_03")
def test_pytest4_03():
    assert 2 == 2

# @pytest.mark.xfail(condition=None, *, reason=None, raises=None, run=True, strict=False)
@allure.story("Story1: test_pytest4_04")
@allure.title("Testcase: test_pytest4_04")
def test_pytest4_04():
    assert 3 == 4

if __name__ == '__main__':
    pytest.main()
    # pytest.main(['/test_pytest2.py', '-s', '-q', '--alluredir', '/report'])
    # os.system('allure generate ./report -o ./report --clean')