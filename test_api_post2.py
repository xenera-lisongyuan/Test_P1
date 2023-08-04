import requests
from pprint import pprint

class Test_Api1():

    def test_post2(self):
        url = "https://result.eolink.com/3ziKNLX67ac89f3175df7e1050df2c4549f65a6ccd2dc25?uri=/user/login_json.php"
        datas = {
            "status": "success",
            "user_info": {
                "token": "129n8yexqy3om8ryec"
            }
        }
        headers = {
            'content-type': "application/json",
            'x-api-key': "DEMO-API-KEY"
        }

        s = requests.Session()
        r = s.post(url, data=datas, headers=headers)
        pprint(r.json())
        for key, value in r.json().items():
            if key == "status":
                assert value == "success"
            elif key == "user_info":
                print(r.json().get('user_info').get('token')) # Debug use
                assert r.json().get('user_info').get('token') == '129n8yexqy3om8ryec'

if __name__ == '__main__':
    test_api1 = Test_Api1()
    test_api1.test_post2()
