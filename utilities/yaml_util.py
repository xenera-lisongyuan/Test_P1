#!/usr/bin/python
# _*_ coding: utf-8 _*_

import yaml

class YamlUtil:

    def __init__(self, yaml_file):
        """pass yaml file to this class via init function： param yaml_file"""
        self.yaml_file = yaml_file

    # read yaml file
    def read_yaml(self):
        """read yaml, deserialize yaml file, which can convert yaml file to dictionary format: return"""
        # with open(self.yaml_file, endcoding='utf-8') as f:
        with open(self.yaml_file) as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            # print(value, type(value)) # debug
            return value

if __name__ == '__main__':
    YamlUtil('../Data/test_api.yaml').read_yaml()