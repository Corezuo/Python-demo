# -*- coding: utf-8 -*-

import json

from logger import Logger

Log = Logger.get_log()

"""
接口列表
"""


def select_active_poster_list_succ_callback(content):
    """
    1.查询海报列表
    海报列表成功的回调
    """
    if content["code"] == 9:
        Log.info("【查询海报列表】发生异常：", content["msg"])
        return False

    # 预期结果校验，检查是否包含指定的报名海报：10176
    poster_list = content["data"]
    for poster in poster_list:
        if poster["id"] == 10176:
            return True

    Log.error("【查询海报列表】发生异常，未能找到指定的千人报名海报！")
    return False


selectActivePosterList = {
    "cmd": "shop/selectActivePosterList",
    "data": {
        "shopId": 1892,
        "pageNo": 3,
        "pageSize": 10,
        "version": 1
    },
    "version": 1,
    "expected": {
        "total": 26,
        "code": 1,
        "msg": "查询成功",
        "data": json.dumps([
            # 第三页，其中的一个千人报名活动
            {
                "id": 10176,
                "merchantId": 86409,
                "shopId": 1892,
                "activityType": 16,
                "activityName": "dadaz",
                "startTime": "2019-06-19 00:00:00",
                "endTime": "2019-12-01 23:59:59",
                "createTime": "2019-06-19 10:28:18",
                "activityStatus": 1
            }
        ])
    },
    "succ_callback": select_active_poster_list_succ_callback
}


def select_recommend_qualifications_callback(content):
    """
    2.查询是否有报名资格
    """
    print(content)


selectRecommendQualifications = {
    "cmd": "shop/selectRecommendQualifications",
    "data": {
        "userId": 86126
    },
    "version": 1,
    "expected": {
        "total": 0,
        "code": 1,
        "msg": "查询成功",
        # 是否有推荐资格：0-无 1-有
        "data": 1
    },
    "succ_callback": select_recommend_qualifications_callback
}


def select_active_poster_byid_callback(content):
    """
    3.查询活动海报详情页面
    """
    print(content)


selectActivePosterById = {
    "cmd": "shop/selectActivePosterById",
    "data": {
        "activeId": "10176"
    },
    "version": 1,
    "expected": {
        "total": 0,
        "code": 1,
        "msg": "查询成功",
        "data": {
            "id": 10176,
            "merchantId": 86409,
            "shopId": 1892,
            "activityType": 16,
            "activityName": "dadaz",
            "startTime": "2019-06-19 00:00:00",
            "endTime": "2019-12-01 23:59:59",
            "createTime": "2019-06-19 10:28:18",
            "activityStatus": 1
        }
    },
    "succ_callback": select_active_poster_byid_callback
}


def get_all_merchant_trade_list_callback(content):
    """
    4.查询所有行业
    """
    print(content)


getAllMerchantTradeList = {
    "cmd": "operations/getAllMerchantTradeList",
    "data": {},
    "version": 1,
    "expected": {
        "total": 0,
        "code": 1,
        "msg": "获取列表成功",
        "data": [
            # 第一个行业
            {
                "id": 1,
                "name": "美容美发",
                "showname": "智享潮业",
                "status": 1,
                "value": "1"
            }
        ]
    },
    "succ_callback": get_all_merchant_trade_list_callback
}


def select_sign_detail_callback(content):
    """
    5.小程序-（千人报名）智享课堂报名海报-查看报名详情
    """
    print(content)


selectSignDetail = {
    "cmd": "shop/selectSignDetail",
    "data": {
        "activeId": "10176",
        "shopId": "1892",
        "customerId": 86126
    },
    "version": 1,
    "expected": {
        "total": 0,
        "code": 1,
        "msg": "查询成功！",
        "data": {
            "shareUserId": 0,
            "recommendUserId": 86126,
            "amount": "0.02",
            "signupShopList": [
                {
                    "tradeId": 1,
                    "tradeName": "美容美发",
                    "shopName": "大左的店铺",
                    "shopAddress": "湖北省武汉市武昌区中山路237号",
                    "shopAddressDetail": "东沙大厦",
                    "longitude": 114.31599,
                    "latitude": 30.55386,
                    "signupUserList": [
                        {
                            "username": "dazuo",
                            "phone": "18871482141",
                            "signupType": 1,
                            "price": 0.02,
                            "recommendUserId": 86126,
                            "recommendUserName": "☆大左",
                            "shareUserId": 0,
                            "shareUserName": ""
                        }
                    ]
                }
            ]
        }
    },
    "succ_callback": select_sign_detail_callback
}


def select_byphone_callback(content):
    """
    6.检查手机号是否已报名
    """
    print(content)


selectByPhone = {
    "cmd": "shop/selectByPhone",
    "data": {
        "activeId": "10176",
        "phone": "18871482140",
        "shareUserId": "0",
        "recommendUserId": "86126"
    },
    "version": 1,
    "expected": {
        "total": 0,
        "code": 1,
        "msg": "查询成功！",
        "data": {
            "price": 0.02,
            "userType": 1,
            "shareUserName": "",
            "recommendUserName": "☆大左"
        }
    },
    "succ_callback": select_byphone_callback
}


def active_poster_singup_callback(content):
    """
    7.小程序-（千人报名）智享课堂报名海报-报名、下订单
    """
    print(content)


activePosterSingup = {
    "cmd": "shop/activePosterSingup",
    "data": {
        "activeId": "10176",
        "merchantId": "86409",
        "shopId": "1892",
        "customerId": 86126,
        "shareUserId": "0",
        "recommendUserId": "86126",
        "amount": 0.02,
        "signupShopList": [
            {
                "tradeId": 1,
                "tradeName": "美容美发",
                "shopName": "大左的店铺",
                "shopAddress": "湖北省武汉市武昌区中山路237号",
                "shopAddressDetail": "东沙大厦",
                "longitude": 114.31599,
                "latitude": 30.55386,
                "signupUserList": [
                    {
                        "username": "dazuo",
                        "phone": "18871482141",
                        "signupType": 1,
                        "price": 0.02
                    }
                ]
            }
        ]
    },
    "version": 1,
    "expected": {
        # 订单号作为下一个接口的入参
        "total": 0,
        "code": 1,
        "msg": "报名成功！",
        "data": "ZXCSSHOP201908062110515320008"
    },
    "succ_callback": active_poster_singup_callback
}


def unified_order_callback(content):
    """
    8.发起支付，拉起支付窗口
    """
    print(content)


unifiedOrder = {
    "cmd": "payBoot/wx/pay/cloudShop/unifiedOrder",
    "data": {
        "openid": "oPL_b4oxExGTrGkqE4cgK0dSnLtY",
        "requestBody": {
            "body": "云店小程序普通订单",
            "out_trade_no": "ZXCSSHOP201908062110515320008",
            "trade_type": "JSAPI"
        }
    },
    "version": 1,
    "expected": {
        "total": 0,
        "code": 1,
        "msg": "操作成功!",
        "data": {
            "timeStamp": "1565097052",
            "wxResult": {
                "returnCode": "SUCCESS",
                "returnMsg": "OK",
                "resultCode": "SUCCESS",
                "appid": "wxd471bb4262ac7505",
                "mchId": "1509096611",
                "nonceStr": "Sw4l6hNF85rSihPQ",
                "sign": "36C28C377109C230C51115E4177025EF",
                "xmlString": "<xml><return_code><![CDATA[SUCCESS]]></return_code>\n<return_msg><![CDATA[OK]]></return_msg>\n<appid><![CDATA[wxd471bb4262ac7505]]></appid>\n<mch_id><![CDATA[1509096611]]></mch_id>\n<nonce_str><![CDATA[Sw4l6hNF85rSihPQ]]></nonce_str>\n<sign><![CDATA[36C28C377109C230C51115E4177025EF]]></sign>\n<result_code><![CDATA[SUCCESS]]></result_code>\n<prepay_id><![CDATA[wx06211052117606bc37a8e2dd1306564500]]></prepay_id>\n<trade_type><![CDATA[JSAPI]]></trade_type>\n</xml>",
                "prepayId": "wx06211052117606bc37a8e2dd1306564500",
                "tradeType": "JSAPI",
            },
            "paySign": "34F686CE9995E59891C9B5FE818888C6"
        }
    },
    "succ_callback": unified_order_callback
}
