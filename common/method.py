# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:32
# @Author  : Mandy
import json
import re

import pytest
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# proxies = {
#     'https': '192.168.1.85:8888'
# }
proxies = None


class Request(object):
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}

    def get(self, url, params=None, headers=None):
        res = requests.get(url=url, params=params, headers=headers, verify=False, timeout=3, proxies=proxies)
        print('[GET]Request URL: %s\n' % url)
        print('-------------------Request Headers-------------------\n%s\n' % headers)
        print('-------------------Request Body-------------------\n%s\n' % params)
        j = json.loads(res.text)
        json_dicts = json.dumps(j, indent=4, ensure_ascii=False)
        print('-------------------Response-------------------\n%s' % json_dicts)
        self.assert_res(j)
        return j

    def post(self, url, params=None, data=None, headers=None):
        print('[POST]Request URL: %s\n' % url)
        print('-------------------Request Headers-------------------\n%s\n' % headers)
        if params is not None:
            res = requests.post(url=url, params=params, headers=headers, verify=False, timeout=3, proxies=proxies)
            print('-------------------Request Body-------------------\n%s\n' % params)
        else:
            res = requests.post(url=url, json=data, headers=headers, verify=False, timeout=3, proxies=proxies)
            print('-------------------Request Body-------------------\n%s\n' % data)
        j = json.loads(res.text)
        json_dicts = json.dumps(j, indent=4, ensure_ascii=False)
        # print('-------------------Response-------------------\n%s' % json_dicts)
        # self.assert_res(j)
        return j

    def assert_res(self, res):
        # if int(res['code']) in [200, 0] or res['msg'] in ['成功', '操作成功']:
        if int(res['code']) in [200, 0]:
            assert True
        else:
            print('用例执行失败')
            assert False

    def main(self, method=None, url=None, params=None, data=None, is_header=True):
        if method is not None:
            if is_header is True:
                res = self.get(url=url, params=params, headers=self.headers)
            else:
                res = self.get(url=url, params=params)
        else:
            if params is not None:
                if is_header is True:
                    res = self.post(url=url, params=params, headers=self.headers)
                else:
                    res = self.post(url=url, params=params)
            else:
                if is_header is True:
                    res = self.post(url=url, data=data, headers=self.headers)
                else:
                    res = self.post(url=url, data=data)

        print('Request URL: %s' % url)
        print('Response: %s' % res)
        self.assert_res(res)
        print('Response code: %s' % res['code'])
        return res

