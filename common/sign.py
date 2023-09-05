# -*- coding: utf-8 -*-
# @Time    : 2023/3/7 11:03
# @Author  : Mandy
import hashlib
import datetime

# import sys
keyString = "5da525bc7b5126cfc5e30cc1"


# def sort(param):
#     """param参数做处理"""
#     # return sorted(param.items())
#     return sorted(param.items(), key=lambda d: d[0])

def sortedDictValues(adict):
    keys = list(adict.keys())
    keys.sort()
    return list(map(adict.get, keys))


# @sortedDictValues
def format_value(param):
    sort_list = sortedDictValues(param)
    sort_list.append(keyString)
    print('排序后的list： %s' % sort_list)
    d = []
    for i in sort_list:
        parameter = ''.join(str(i))
        d.append(parameter)
    format_value = '|'.join(d)
    print('加密前的dict： %s' % format_value)
    return format_value


def md5_sign(data):
    """
    MD5数据加密
    :param encrypt:  format_parameter返回的字符串
    :return: 返回32位 16进制  大写
    """
    # pre_data = format_value(data)
    md5 = hashlib.md5()
    md5.update(data.encode())
    sign = md5.hexdigest()
    print('加密后的sign：%s' % sign)
    return sign


def new_param(param):
    sign = md5_sign(param)
    param['sign'] = sign
    # print('加密后的param：%s' % param)
    return param


def encry_params(params):
    keyString = "5da525bc7b5126cfc5e30cc1"
    # params根据key重新排序后，取dict中的value
    keys = list(params.keys())
    keys.sort()
    sort_list = list(map(params.get, keys))

    # 加上key
    sort_list.append(keyString)
    # print('排序后的list： %s' % sort_list)

    # 使用分隔符串联
    d = []
    for i in sort_list:
        parameter = ''.join(str(i))
        d.append(parameter)
    format_value = '|'.join(d)
    print('串联后的string： %s' % format_value)

    # md5加密
    sign = md5_sign(format_value)
    params['sign'] = sign
    # print('加密后的param：%s' % params)
    return params


# if __name__ == '__main__':
#     param = {
#         "cabinetNo": 'HB20000097',
#         "replenishmentMode": 'FAST',
#         "adminId": 2
#     }
#     print('加密前的param：%s' % param)
#     encry_params(param)


def Findmd5(args):
    md = args.hashvalue
    starttime = datetime.datetime.now()
    for i in open(args.file):
        md5 = hashlib.md5()  # 获取一个md5加密算法对象
        rs = i.strip()  # 去掉行尾的换行符
        md5.update(rs.encode('utf-8'))  # 指定需要加密的字符串
        newmd5 = md5.hexdigest()  # 获取加密后的16进制字符串
        # print newmd5
        if newmd5 == md:
            print('明文是：' + rs)  # 打印出明文字符串
            break
        else:
            pass

    endtime = datetime.datetime.now()
    print(endtime - starttime)  # 计算用时，非必须


# if __name__ == '__main__':
#     import argparse  # 命令行参数获取模块
#
#     parser = argparse.ArgumentParser(usage='Usage:./findmd5.py -l 密码文件路径 -i 哈希值 ',
#                                      description='help info.')  # 创建一个新的解析对象
#     parser.add_argument("-l", default='wordlist.txt', help="密码文件.", dest="file")  # 向该对象中添加使用到的命令行选项和参数
#     parser.add_argument("-i", dest="hashvalue", help="要解密的哈希值.")
#
#     args = parser.parse_args()  # 解析命令行
#     Findmd5(args)
