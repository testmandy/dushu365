# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:20
# @Author  : Mandy

import pytest

from common.get_url import TestUrl
from common.method import Request
from common.sign import encry_params


def login():
    """小程序登录new_employee_login"""
    data = {
        "userName": 'FuguiTest',
        "password": 'fugui123',
        "platform": 1,
        "partnerId": 2
    }
    new_data = encry_params(data)
    r = req.post(url=URL.get_url('new_employee_login'), data=new_data)
    token = r['token']
    return token


req = Request()
URL = TestUrl()
token = login()

headers = {'Authorization': '1##186291##b1b8ffb0771b4b71b2abec1f00398cb0',
           'Content-Type': 'application/json; charset=utf-8'}

adminId = 186291
baseCabinetNo = "aHR0cHM6Ly9mZ3dlYmFwcC50ZXN0Lnlvbndhbi5jbi9hcHAvSEIyMjIxMjAxMTAwMDA/ZG9vck51bT0y",
reOrderSn = "20230309090000001"
cabinetNo = "HB222120110000"


@pytest.mark.run
class TestApi(object):
    @pytest.mark.run
    def test_permission_page(self):
        """permission_page"""
        data = {
            "currPage": 1,
            "pageSize": 20
        }
        req.post(url=URL.get_url('permission_page'), data=data, headers=headers)

    @pytest.mark.skip
    def add_permission(self):
        """add_permission"""
        data = {
            "positionIds": [55],
            "adminId": adminId
        }
        req.post(url=URL.get_url('add_permission'), data=data, headers=headers)

    @pytest.mark.skip
    def remove_permission(self):
        """remove_permission"""
        data = {
            "id": 1111
        }
        req.post(url=URL.get_url('remove_permission'), data=data, headers=headers)

    @pytest.mark.run(order=1)
    def test_sweep_code_open_door(self):
        """scan_open_door -- 无补货单"""
        data = {
            "baseCabinetNo": "aHR0cHM6Ly9mZ3dlYmFwcC50ZXN0Lnlvbndhbi5jbi9hcHAvSEIyMjIxMjAxMTAwMDA/ZG9vck51bT0y",
            "adminId": adminId,
            "token": token
        }
        new_data = encry_params(data)
        req.post(url=URL.get_url('sweep_code_open_door'), params=new_data, headers=headers)

    @pytest.mark.run(order=1)
    def test_sav_inventory_adjustment_order(self):
        """scan_open_door -- 无补货单"""
        normalProducts = [
                {
                    "firmStock": 108,
                    "goodName": "元气森林 可乐味",
                    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/20221020192757/1666265277072/主图-06.jpg",
                    "productId": 10000019,
                    "systemStock": 108
                },
                {
                    "firmStock": 170,
                    "goodName": "Lipo面包干",
                    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565751781901.com/goods/1547288739688_68355",
                    "productId": 14063,
                    "systemStock": 170
                },
                {
                    "firmStock": 101,
                    "goodName": "可口可乐细罐装330ml",
                    "pic": "https://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-13/kekoukelhant330mlxl.png",
                    "productId": 11282,
                    "systemStock": 101
                }
            ]
        data = {
            "adminId": adminId,
            "cabinetNo": cabinetNo,
            "checkerRecordId": "1221",
            "remarks": "",
            "token": token,
            "userType": "1"
        }
        new_data = encry_params(data)
        new_data['normalProducts'] = normalProducts
        new_data['differenceProducts'] = []
        req.post(url=URL.get_url('sav_inventory_adjustment_order'), params=new_data, headers=headers)

    @pytest.mark.run(order=2)
    def replenishment_temp_create(self):
        """replenishment_temp_create"""
        data = {
            "cabinetNo": cabinetNo,
            "adminId": adminId
        }
        r = req.post(url=URL.get_url('replenishment_temp_create'), data=data, headers=headers)
        order = r['data']
        return order

    @pytest.mark.run(order=3)
    def test_get_common_open_door(self):
        """fast_open_door：// "replenishmentMode" : "FAST" //FAST 是 快速补货模式，NORMAL 是 补货单开门模式"""
        data = {
            "appType": "android",
            "cabinetNo": cabinetNo,
            "checkerRecordId": "",
            "doorNum": 2,
            "reOrderSn": "20230309110000001",
            "userType": 2,
            "adminId": adminId,
            "token": token,
            "replenishmentMode": "FAST"
        }
        new_data = encry_params(data)
        req.post(url=URL.get_url('get_common_open_door'), params=new_data, headers=headers)

    @pytest.mark.run
    def test_query_replenishment_order(self):
        """check_cabinet_product:返回信息不变，柜内商品字段：cabinetProductNum 为0；"""
        temp_order = self.replenishment_temp_create()
        data = {
            "cabinetNo": cabinetNo,
            "reOrderSn": temp_order,
            "adminId": adminId,
            "replenishmentMode": "FAST",
            "token": token
        }
        new_data = encry_params(data)
        req.post(url=URL.get_url('query_replenishment_order'), params=new_data, headers=headers)

    @pytest.mark.run(order=4)
    def test_submit_replenishment_order(self):
        """确认补货submit_replenishment_order"""
        print('登录接口返回的token：%s' % token)
        normalOrderItem = [
            {
                "downNum": 0,
                "facDownNum": 0,
                "upNum": 1,
                "facUpNum": 3,
                "goodName": "好吃点熊字饼干系列115g",
                "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-11-17/haochidianxizib11.png",
                "productId": 12168,
                "productShelf": 1,
                "realProductShelf": 1
            },
            {
                "downNum": 0,
                "facDownNum": 0,
                "upNum": 1,
                "facUpNum": 4,
                "goodName": "英文字母饼干牛奶味",
                "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565751969546.com/goods/1548827650677_35701",
                "productId": 14719,
                "productShelf": 1,
                "realProductShelf": 1
            },
            {
                "downNum": 0,
                "facDownNum": 0,
                "upNum": 1,
                "facUpNum": 7,
                "goodName": "元气森林 可乐味",
                "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/20221020192757/1666265277072/主图-06.jpg",
                "productId": 10000019,
                "productShelf": 1,
                "realProductShelf": 1
            }
        ]
        data = {
            "adminId": adminId,
            "cabinetNo": cabinetNo,
            "reOrderSn": reOrderSn,
            "token": token
        }
        new_data = encry_params(data)
        new_data['normalOrderItem'] = normalOrderItem
        new_data['differenceOrderItem'] = []
        new_data['replenishmentMode'] = "FAST"

        req.post(url=URL.get_url('submit_replenishment_order'), data=new_data, headers=headers)

    @pytest.mark.run(order=5)
    def test_replenishment_record(self):
        """快补单查询replenishment_record,"type": 1   #新增字段 单据类型，1：扫补；2：快补"""
        data = {
            "reStatus": "",
            "cabinetNo": cabinetNo,
            "reSn": "",
            "adminId": adminId,
            "positionIds": [],
            "cabinetName": "",
            "pageSize": 50,
            "currPage": 1,
            "orderStartTime": "",
            "orderEndTime": "",
            "reStartTime": "",
            "reEndTime": "",
            "type": 2  # 新增字段 单据类型，1：扫补；2：快补
        }
        req.post(url=URL.get_url('replenishment_record'), data=data, headers=headers)

    @pytest.mark.run(order=6)
    def test_replenishment_info(self):
        """replenishment_info"""
        data = {
            "gsReplenishmentOrderId": 141,
            "reSn": reOrderSn
        }
        req.post(url=URL.get_url('replenishment_info'), data=data, headers=headers)
