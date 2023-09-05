# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:21
# @Author  : Mandy
from common.get_url import TestUrl
from common.method import Request

URL = TestUrl(yaml_name='url_iot')


class ReqWithToken(object):
    def __init__(self, account, pwd):
        self.req = Request()
        self.account = account
        self.pwd = pwd
        self.headers = {'Content-Type': 'application/json', 'token': '%s'}
        print(self.headers)

    def get(self, url, params=None):
        res = self.req.get(url, params=params, headers=self.headers)
        return res

    def post(self, url, params=None, json=None):
        res = self.req.post(url, params=params, data=json, headers=self.headers)
        return res

    def get_token(self):
        data = {"username": self.account, "password": self.pwd}
        res = self.req.post(url=URL.get_url('login'), data=data)
        token = res['data']['token']
        return token

