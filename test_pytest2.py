import pytest
import allure

def test_login_01():
    assert 0 == 0

def test_login_02():
    assert 0 == 1

def test_login_03():
    assert 1 == 2

if __name__ == '__main__':
    pytest.main()
    # pytest.main(['/test_pytest2.py', '-s', '-q', '--alluredir', '/report'])
    # os.system('allure generate ./report -o ./report --clean')