# !/usr/bin/python
# _*_ coding: utf-8 _*_

import yaml

class YamlUtil2:

    def __init__(self, yaml_file):
        """pass yaml file to this class via init function： param yaml_file"""
        self.yaml_file = yaml_file

    # read yaml file
    def read_yaml2(self):
        """read yaml, deserialize yaml file, which can convert yaml file to dictionary format: return"""
        with open(self.yaml_file, encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            # print(value, type(value)) # debug
            return value

if __name__ == '__main__':
    YamlUtil2('../Data/test_oioapi_dailyenglish.yaml').read_yaml2()