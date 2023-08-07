import pytest
import allure

class Test_Pytest3:

    @pytest.mark.run(order=7)
    @allure.severity("normal")
    @allure.story("Story1: Test_Pytest3")
    @allure.title("Testcase: test_login_01")
    def test_pytest3_01(self):
        assert 0 == 0
        print("01")

    @pytest.mark.run(order=6)
    @allure.severity("critical")
    @allure.story("Story1: Test_Pytest3")
    @allure.title("Testcase: test_login_02")
    def test_pytest3_02(self):
        assert 0 == 1
        print("02")

    @pytest.mark.run(order=5)
    @allure.severity("normal")
    @allure.story("Story1: Test_Pytest3")
    @allure.title("Testcase: test_login_03")
    def test_pytest3_03(self):
        assert 1 == 1
        print("03")

# if __name__ == '__main__':
#     # pytest.main()
#     Test_Pytest3.test_login_03(self)
#     Test_Pytest3.test_login_02(self)
#     Test_Pytest3.test_login_01(self)
#     # pytest.main(['/test_pytest2.py', '-s', '-q', '--alluredir', '/report'])
#     # os.system('allure generate ./report -o ./report --clean')