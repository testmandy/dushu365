# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:22
# @Author  : Mandy
import yaml

import conftest


class TestUrl(object):
    def __init__(self, yaml_name='url'):
        self.yaml_name = yaml_name
        self.base_url = self.get_uri(key='base_url')

    def get_uri(self, key=None):
        filename = conftest.data_dir + '/%s.yaml' % self.yaml_name
        data = open(filename, encoding='UTF-8').read()
        yaml_reader = yaml.safe_load(data)
        uri = yaml_reader[key]
        return uri

    def get_url(self, name):
        return self.base_url + self.get_uri(name)
