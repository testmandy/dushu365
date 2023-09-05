# -*- coding: utf-8 -*-
# @Time    : 2023/3/6 17:28
# @Author  : Mandy
"""
接口名称：微信支付
实现目标：微信支付sign签名MD5加密
签名算法规则：
1.参数名ASCII码从小到大排序（字典序）
2.如果参数的值为空不参与签名
3.参数名区分大小写
4.验证调用返回或微信主动通知签名时，传送的sign参数不参与签名，将生成的签名与该sign值作校验
5.微信接口可能增加字段，验证签名时必须支持增加的扩展字段

"""

# 导入数据处理加密的包
import hashlib

keyString = "5da525bc7b5126cfc5e30cc1"


def ascll_sort(requests_parm):
    """ASCll码排序"""

    def sort(param):
        """param参数做处理"""
        return requests_parm(sorted(param.items()))

    return sort


@ascll_sort
def format_parameter(sort_data):
    """
    拼接参数
    :param sort_data: 装饰器返回的参数
    :return:   所有参数拼成一个字符串
    """
    arr = []
    for data in sort_data:
        for a in data:
            parameter = ''.join(str(a))
            arr.append(parameter)

    param = keyString + ''.join(arr) + keyString
    return param


def md5_sign(format_parameter):
    """
    MD5数据加密
    :param encrypt:  format_parameter返回的字符串
    :return: 返回32位 16进制  大写
    """

    def str_md5(param):
        md5 = hashlib.md5()
        md5.update(param.encode())
        sign = md5.hexdigest()
        return format_parameter(sign.upper())

    return str_md5


@md5_sign
def sign(sign):
    """请求URL"""
    md5_sign = {'sign': sign}
    return md5_sign

