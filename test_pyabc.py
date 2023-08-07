import requests
from pprint import pprint

class Test_Api_Get2():

    def test_get2(self):
        s = requests.Session()
        r = s.get("https://result.eolink.com/vk17wiAd3a7119b4f476f76f44ddf904c0bdbc6aa6ae800?uri=/user/points.php")
        pprint(r.json())
        for key, value in r.json().items():
            if key == "points":
                assert value == 100
            elif key == "status":
                assert value == "success"

if __name__ == '__main__':
    test_api_get2 = Test_Api_Get2()
    test_api_get2.test_get2()

