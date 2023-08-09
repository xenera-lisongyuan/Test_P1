import pytest, requests
from utilities.yaml_util2 import YamlUtil2

class TestOioApiDailyEnglish:

    @pytest.mark.parametrize('args', YamlUtil2('../Data/test_oioapi_dailyenglish.yaml').read_yaml2())
    def test_oioapi_dailyenglish(self, args):
        """This function covers 2 cases: 1 success, 1 failure. The failure case is due to missing input parameters, which responses error code = 40002"""
        url = args['request']['url']
        # params = args['request']['params']
        res = requests.get(url=url)
        print("Return as behind: ", res.json(), type(res.json()))
        # # Below are assertions
        assert args['request']['validate']['code'] == res.json()['code']
        assert args['request']['validate']['msg'] == res.json()['msg']

if __name__ == '__main__':
    pytest.main(['vs'])