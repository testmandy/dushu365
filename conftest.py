# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:21
# @Author  : Mandy
import os

import pytest

from common.method import Request

PROJECT_DIR2 = os.path.abspath(os.path.dirname(__file__))

project_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(project_dir, 'data')

req = Request()


def get_token():
    data = {"username": 'admin', "password": '123456'}
    r = req.post(url='https://iot-api-dev.yonwan.cn/iot/user/login', data=data)
    return r['data']['token']


@pytest.fixture()
def my_headers():
    return {'OCTOPUS-TOKEN': '{0}'.format(get_token()), 'Content-Type': 'application/json; charset=utf-8'}


items = [{
    "firmStock": 15,
    "goodName": "巴厘岛网红梅子味百事可乐",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565752420581.com/goods/1552440590959_24713",
    "productId": 15338,
    "systemStock": 15
}, {
    "firmStock": 119,
    "goodName": "贤哥辣么脆片系列58g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-12-28/xiangelingshimeishixilie123.png",
    "productId": 119,
    "systemStock": 119
}, {
    "firmStock": 19,
    "goodName": "嘉顿威化饼干花生味50g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565750735780.com/goods/1540690808914_40326",
    "productId": 12742,
    "systemStock": 19
}, {
    "firmStock": 21,
    "goodName": "旺旺挑“豆”海苔花生80g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565751983156.com/goods/1549954427600_43136",
    "productId": 14768,
    "systemStock": 21
}, {
    "firmStock": 11,
    "goodName": "元气森林 可乐味",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/20221020192757/1666265277072/主图-06.jpg",
    "productId": 10000019,
    "systemStock": 11
}, {
    "firmStock": 24,
    "goodName": "黄飞鸿麻辣花生110g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565750656255.com/goods/1538387565302_33909",
    "productId": 12449,
    "systemStock": 24
}, {
    "firmStock": 6,
    "goodName": "哇哈哈苏打水",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-27/01057b5eba2496a80121481472ec79.jpg%403000w_1l_0o_100sh.jpg",
    "productId": 15435,
    "systemStock": 6
}, {
    "firmStock": 14,
    "goodName": "娃哈哈苏打水饮品350ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-07-13/whhsds.png",
    "productId": 11249,
    "systemStock": 14
}, {
    "firmStock": 2,
    "goodName": "水溶cc2",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/2091/1634120173014.png",
    "productId": 1012810,
    "systemStock": 2
}, {
    "firmStock": 3,
    "goodName": "元气森林 清新椰椰乳茶",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/20221020195039/1666266639168/主图-07.jpg",
    "productId": 10000022,
    "systemStock": 3
}, {
    "firmStock": 2,
    "goodName": "巧克力",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/20230221165705/1676969825188.png",
    "productId": 10000037,
    "systemStock": 2
}, {
    "firmStock": 2,
    "goodName": "可口可乐",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/20230116141939/1673849979932.png",
    "productId": 10000035,
    "systemStock": 2
}, {
    "firmStock": 24,
    "goodName": "溜溜果园溜溜梅系列60g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-02-25/1614229467%281%29.jpg",
    "productId": 13764,
    "systemStock": 24
}, {
    "firmStock": 15,
    "goodName": "娃哈哈AD钙奶",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-21/src%3Dhttp---www.ledzx.com.cn-uploads-allimg-tk7510259.jpg%26refer%3Dhttp---www.ledzx.com.cn%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg.jpeg",
    "productId": 11421,
    "systemStock": 15
}, {
    "firmStock": 21,
    "goodName": "张君雅点心面系列100g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-09-11/%E5%BC%A0%E5%90%9B%E9%9B%85%E7%82%B9%E5%BF%83%E9%9D%A2100g.png",
    "productId": 11311,
    "systemStock": 21
}, {
    "firmStock": 17,
    "goodName": "森姆家苏打饼干",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565751963906.com/goods/1548825894292_58647",
    "productId": 14700,
    "systemStock": 17
}, {
    "firmStock": 56,
    "goodName": "火咖咖啡味饮料280ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565750052093.com/goods/1531122523207_46888",
    "productId": 11704,
    "systemStock": 56
}, {
    "firmStock": 15,
    "goodName": "好丽友派系列两枚装",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-21/haoliyoupshuangxlx3232432.png",
    "productId": 79,
    "systemStock": 15
}, {
    "firmStock": 1,
    "goodName": "格力高百醇注心饼干系列盒装48g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-03-01/baichunzhuxinbingganxilie123.png",
    "productId": 10908,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "元気森林燃茶系列500ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565749841680.com/goods/1530086454610_45772",
    "productId": 10984,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "蒙牛早餐原麦牛奶纸袋230ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-22/mengnzaocannai230mlz.png",
    "productId": 11721,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "奥利奥巧脆卷系列盒装55g",
    "pic": "https://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-27/aoliaoqiaocuijxilie231.png",
    "productId": 12849,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "三得利利趣拿铁咖啡饮料",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565751169784.com/goods/1542104209916_32901",
    "productId": 13076,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "乐事无限薯片系列40g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-22/leshiwuxoanshupxil40g.png",
    "productId": 13251,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "洽洽喀吱脆薯脆系列",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-25/qiaqiakazhicuixil35g.png",
    "productId": 13433,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "双汇玉米热狗肠袋装160g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565751425476.com/goods/1544243018584_90827",
    "productId": 13517,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "农夫山泉饮用天然水550ml",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/2144/1637751374896.png",
    "productId": 1012832,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "日清 合味道系列",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/octopus/product/pic/20221020183546/1666262146266/主图-01.jpg",
    "productId": 10000009,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "元气森林系列",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/octopus/product/pic/20221020184159/1666262519154/主图-06.jpg",
    "productId": 10000012,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "星巴克系列",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/octopus/product/pic/20221020192158/1666264918122/主图-01.jpg",
    "productId": 10000017,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "奥利奥巧克力夹心饼干系列",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565749776487.png",
    "productId": 61,
    "systemStock": 1
}, {
    "firmStock": 2,
    "goodName": "丽芝士纳宝帝威化袋装58g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565749793223.com/goods/1524899919333_69537",
    "productId": 118,
    "systemStock": 2
}, {
    "firmStock": 1,
    "goodName": "海之言系列瓶装500ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-10-29/haizhiyanyinpin1.png",
    "productId": 10918,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "维他柠檬茶纸盒250ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-03-29/weitaningmengchezdp250ml.png",
    "productId": 10921,
    "systemStock": 1
}, {
    "firmStock": 21,
    "goodName": "张君雅零食系列80g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-02/24d444f8fd32a79d100480dce3db313.png",
    "productId": 11141,
    "systemStock": 21
}, {
    "firmStock": 1,
    "goodName": "蒙牛真果粒牛奶饮品250g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-14/mengniuzhenguolixil250g.png",
    "productId": 11144,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "喜之郎果粒爽饮料350ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-01/d075f57ce59a6c5cab8c6a64eec7711.jpg",
    "productId": 11187,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "中沃体质能量系列600ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-06/zhongwotizhinenglxil600ml.png",
    "productId": 11281,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "可口可乐细罐装330ml",
    "pic": "https://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-13/kekoukelhant330mlxl.png",
    "productId": 11282,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "娃哈哈八宝粥系列罐装360g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-19/wahahababaozhouypxil3244.png",
    "productId": 11445,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "口水娃兰花豆60g（组图）",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-02/koushuiwalanhuadouxil60g.png",
    "productId": 12702,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "乐事大波浪薯片系列",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-11-14/timg-8.jpeg",
    "productId": 13278,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "卫龙亲嘴烧系列",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-06/weilongqinzuishaoxilie23234.png",
    "productId": 13630,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "今麦郎桶装面系列",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-02/jinmailangtongzmxil105g.png",
    "productId": 13744,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "芬达汽水细罐装330ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-04-13/fendaxiguanz330ml.png",
    "productId": 14077,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "蒙牛纯甄经典原味200g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-12-30/chunzhenjingdiamnyuanwei200g.png",
    "productId": 10928,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "农心辛拉面组图",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-12-24/nongxinlamianxil12345.png",
    "productId": 11013,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "曹操饿了即时拌面系列249.5g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565749878739.com/goods/1524822189181_86846",
    "productId": 11118,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "好丽友呀土豆40g系列",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-11-24/u%3D4066559286%2C696825024%26fm%3D26%26gp%3D0.jpg",
    "productId": 11272,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "农夫山泉NFC果汁300ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565749937473.com/goods/1531383064942_49850",
    "productId": 11285,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "维他奶豆奶系列250ml",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-01-13/weitanaidounaixil250ml.png",
    "productId": 11417,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "格力高百奇装饰饼干60g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-05-25/%E6%9C%AA%E6%A0%87%E9%A2%98-1.jpg",
    "productId": 11451,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "统一藤娇牛肉面桶装105g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565750025626.com/goods/1530264990158_33704",
    "productId": 11607,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "苏菲超熟睡350",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565750041696.com/goods/1530601265753_30255",
    "productId": 11666,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "洽洽瓜子系列",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2021-01-05/32471e397fb18aa3f6f5d6ce67f3ed13_tn.jpeg",
    "productId": 11932,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "格力高菜园小饼装饰饼干",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565750175129.com/goods/1535079258500_81440",
    "productId": 12152,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "好吃点熊字饼干系列115g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-11-17/haochidianxizib11.png",
    "productId": 12168,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "无穷酱卤鸭小腿30g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565750668888.com/goods/1538981596386_31831",
    "productId": 12496,
    "systemStock": 1
}, {
    "firmStock": 1,
    "goodName": "白家重庆酸辣粉方便粉丝85g",
    "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565751203886.com/goods/1542898120716_62141",
    "productId": 13187,
    "systemStock": 1
}, {
    "firmStock": 2,
    "goodName": "卤门家族-芝麻素肥牛袋装80g",
    "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/20230217104728/1676602048982.png",
    "productId": 10000036,
    "systemStock": 2
}]

productListJson = {"productListJson": [{"productId": "11249", "goodName": "娃哈哈苏打水饮品350ml",
                                 "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/2020-07-13/whhsds.png",
                                 "upNum": "0", "downNum": "0", "downReason": "1", "id": "2452",
                                 "cabinetProductNum": 118, "customPrice": "0.01", "productShelf": "1",
                                 "fullCabinetNum": "121", "old": "true"},
                                {"productId": "15249", "goodName": "悠哈果汁葡萄味软糖",
                                 "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565752395034.com/goods/1552358740680_34946",
                                 "upNum": "0", "downNum": "0", "downReason": "1", "id": "2465", "cabinetProductNum": 20,
                                 "customPrice": "0.01", "productShelf": "1", "fullCabinetNum": "21", "old": "true"},
                                {"productId": "10000019", "goodName": "元气森林 可乐味",
                                 "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/20221020192757/1666265277072/主图-06.jpg",
                                 "upNum": "0", "downNum": "0", "downReason": "1", "id": "2460", "cabinetProductNum": 40,
                                 "customPrice": "0.01", "productShelf": "1", "fullCabinetNum": "60", "old": "true"},
                                {"productId": "15241", "goodName": "嘉顿梳打饼干",
                                 "pic": "http://fgh5s.oss-cn-hangzhou.aliyuncs.com/product/MKG1565752392892.com/goods/1552358170768_42457",
                                 "upNum": "0", "downNum": "0", "downReason": "1", "id": "2462", "cabinetProductNum": 19,
                                 "customPrice": "0.01", "productShelf": "2", "fullCabinetNum": "20", "old": "true"},
                                {"productId": "1012660", "goodName": "可口可乐柠檬柚子气泡茶",
                                 "pic": "https://testfook.oss-cn-hangzhou.aliyuncs.com/prepose/product/pic/20210826153332/1629963212132.png",
                                 "upNum": "0", "downNum": "0", "downReason": "1", "id": "2471", "cabinetProductNum": 0,
                                 "customPrice": "0.01", "productShelf": "2", "fullCabinetNum": "1", "old": "true"}],
            "id": "59", "adminId": "186293"}
