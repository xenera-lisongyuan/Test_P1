import requests
from pprint import pprint
import allure
import time
import os
import pytest

class Test_Api1():

    @allure.feature("test_api_post1")
    def test_post1(self):
        s = requests.Session()
        r = s.post("https://result.eolink.com/vk17wiAd3a7119b4f476f76f44ddf904c0bdbc6aa6ae800?uri=/user/login_json.php")
        pprint(r.json())
        for key, value in r.json().items():
            if key == "status":
                assert value == "success"
            elif key == "user_info":
                for key1, value1 in value.items():
                    assert value1 == "129n8yexqy3om8ryec"

if __name__ == '__main__':
    test_api1 = Test_Api1()
    test_api1.test_post1()
    # time.sleep(2)