#!/usr/bin/python
# _*_ coding: utf-8 _*_

import pytest, requests
from Test_P1.utilities.yaml_util import YamlUtil

class TestYamlApi:

    @pytest.mark.parametrize('args', YamlUtil('../Data/test_api.yaml').read_yaml())
    def test_api_01(self, args):
        """This function covers 2 cases: 1 success, 1 failure. The failure case is due to missing input parameters, which responses error code = 40002"""
        url = args['request']['url']
        params = args['request']['params']
        res = requests.get(url=url, params=params)
        print("Return as behind: ", res.json(), type(res.json()))
        # # Below are assertions
        if res.json().get('expires_in'):
            # print(res.json()['expires_in']) # debug
            assert args['request']['validate']['expires_in'] == res.json()['expires_in']
        else:
            # print('--response errcode below--') # debug
            # print(res.json()['errcode']) # debug
            # print('--below is expected data--') # debug
            # print(args['request']['validate']['errcode']) # debug
            assert args['request']['validate']['errcode'] == res.json()['errcode']

if __name__ == '__main__':
    pytest.main(['vs'])