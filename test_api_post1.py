import requests
from pprint import pprint
import allure
import time
import os
import pytest

class Test_Api1():

    @allure.feature("test_api_post1")
    def test_post1(self):
        user_info = {
        "token": "129n8yexqy3om8ryec"
        }
        s = requests.Session()
        r = s.post("https://result.eolink.com/vk17wiAd3a7119b4f476f76f44ddf904c0bdbc6aa6ae800?uri=/user/login_json.php", user_info)
        pprint(r.json())
        for key, value in r.json().items():
            if key == "status":
                assert value == "success"

if __name__ == '__main__':
    test_api1 = Test_Api1()
    test_api1.test_post1()
    time.sleep(2)
    os.system("allure generate ./report -o")

