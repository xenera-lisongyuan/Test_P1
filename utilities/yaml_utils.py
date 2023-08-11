# !/usr/bin/python
# _*_ coding: utf-8 _*_
# Author: Song Yuan, Li
# Date: Aug, 2023

import yaml

class YamlUtils:

    def read_yaml(self, yaml_file):
        """read yaml file data and return content"""
        try:
            with open(yaml_file, "r", encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                # print(data, type(data)) # debug
                return data
        except:
            return None

if __name__ == '__main__':
    yaml_utils = YamlUtils()
    yaml_utils.read_yaml(yaml_file)