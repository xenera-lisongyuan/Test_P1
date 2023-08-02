import requests
from pprint import pprint

class Test_Api2():

    def test_get2():
        s = requests.Session()
        r = s.get("https://result.eolink.com/vk17wiAd3a7119b4f476f76f44ddf904c0bdbc6aa6ae800?uri=/user/points.php")
        # pprint(r.json())
        for key, value in r.json().items():
            if key == "points":
                assert value == 100
            elif key == "status":
                assert value == "success"

if __name__ == '__main__':
    Test_Api2.test_get2()
