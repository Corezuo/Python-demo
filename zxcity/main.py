# -*- coding: utf-8 -*-

"""
接口测试
Created by zfh on 2018/11/21
"""

import utils
import api_list
from logger import Logger

Log = Logger.get_log()


"""
千人报名接口自动化测试
"""

# 1.查询海报列表
def test_select_active_poster_list():
    api = api_list.selectActivePosterList
    result = utils.unified_post(api["cmd"], api["data"], api["succ_callback"])
    print(result)

# 2.查询是否有报名资格
def test_select_recommend_qualifications():
    api = api_list.selectRecommendQualifications
    utils.unified_post(api["cmd"], api["data"], api["succ_callback"])

# 3.查询活动海报详情页面
def test_select_active_poster_byid_callback():
    api = api_list.selectActivePosterById
    utils.unified_post(api["cmd"], api["data"], api["succ_callback"])

# 4.查询所有行业
def test_get_all_merchant_trade_list_callback():
    api = api_list.getAllMerchantTradeList
    utils.unified_post(api["cmd"], api["data"], api["succ_callback"])

# 5.小程序-（千人报名）智享课堂报名海报-查看报名详情
def test_select_sign_detail_callback():
    api = api_list.selectSignDetail
    utils.unified_post(api["cmd"], api["data"], api["succ_callback"])

# 6.检查手机号是否已报名
def test_select_byphone_callback():
    api = api_list.selectByPhone
    utils.unified_post(api["cmd"], api["data"], api["succ_callback"])

# 7.小程序-（千人报名）智享课堂报名海报-报名、下订单
def test_active_poster_singup_callback():
    api = api_list.activePosterSingup
    utils.unified_post(api["cmd"], api["data"], api["succ_callback"])

# 8.发起支付，拉起支付窗口
def test_unified_order_callback():
    api = api_list.unifiedOrder
    utils.unified_post(api["cmd"], api["data"], api["succ_callback"])


if __name__ == '__main__':
    test_select_active_poster_list()
    # test_select_recommend_qualifications()
    # test_select_active_poster_byid_callback()
    # test_get_all_merchant_trade_list_callback()
    # test_select_sign_detail_callback()
    # test_select_byphone_callback()
    # test_active_poster_singup_callback()
    # test_unified_order_callback()

