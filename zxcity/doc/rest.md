## 千人报名接口请求列表

### 1.查询海报列表

> POST https://wxappprod.izxcs.com/zxcity_restful/ws/rest

request

```
cmd: shop/selectActivePosterList
data: {"shopId":1892,"pageNo":3,"pageSize":10,"version":1}
version: 1
```

success

```
{
    "total": 26,
    "code": 1,
    "msg": "查询成功",
    "data": [
        {
            "id": 10176,
            "merchantId": 86409,
            "shopId": 1892,
            "activityType": 16,
            "activityName": "dadaz",
            "startTime": "2019-06-19 00:00:00",
            "endTime": "2019-12-01 23:59:59",
            "createTime": "2019-06-19 10:28:18",
            "activityStatus": 1,
            "descTitle": "智xixi",
            "pictureUrl": "https://customer-circulation.oss-cn-hangzhou.aliyuncs.com/template-picture/%E8%81%8C%E5%9C%BA%E5%88%86%E4%BA%AB%E4%BC%9A%E5%85%A5%E5%8F%A35.png",
            "createUser": 86409,
            "goodsNumber": 0,
            "isSetup": 0,
            "isSalesPerformance": 0,
            "activePrice": 0,
            "employeeReward": 0,
            "forwardPrice": 0,
            "frameType": 0,
            "signType": 1,
            "extend1": "[\"dddddddddddddddddddddddddddddd\",\"111111111111111111111111111111\",\"222222222222222222222222222222\",\"dddddddddddddddddddddddddddddd\",\"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\",\"??????????????????????????????\",\"000000000000000000000000000000\"]",
            "extend2": null,
            "extend3": null,
            "descContent": null,
            "itemCategoryList": [],
            "salesPerformance": 0,
            "status": 1,
            "templateId": 49,
            "scCardTemplate": null,
            "activeAddress": "哒哒哒哒哒哒的",
            "sortKey": null,
            "page": null,
            "pageSize": null,
            "buyGiftType": 0,
            "reportingTime": "2019-11-01 10:25:00",
            "sharePosterUUID": "ed2fe915ad754896920bea7e6a64f7e4",
            "shopList": null,
            "scShopInfo": null,
            "signUpCharge": null,
            "contentUrl": "http://zxcity-ma.oss-cn-hangzhou.aliyuncs.com/pop%2Fmp3%2Fbg.mp3"
        }
    ]
}
```

error

```
{
    "total": 0,
    "code": 9,
    "msg": "查询成功",
    "data": null
}
```

### 2.查询是否有报名资格

> POST https://wxappprod.izxcs.com/zxcity_restful/ws/rest

request

```
cmd: shop/selectRecommendQualifications
data: {"userId":86126}
version: 1
```

response

```
{
    "total": 0,
    "code": 1,
    "msg": "查询成功",
    "data": 1             # 是否有推荐资格：0-无 1-有
}
```

### 3.查询活动海报详情页面

> POST https://wxappprod.izxcs.com/zxcity_restful/ws/rest

request

```
cmd: shop/selectActivePosterById
data: {"activeId":"10176"}
version: 1
```

response

```
{
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
        "activityStatus": 1,
        "descTitle": "智xixi",
        "pictureUrl": "https://customer-circulation.oss-cn-hangzhou.aliyuncs.com/template-picture/%E8%81%8C%E5%9C%BA%E5%88%86%E4%BA%AB%E4%BC%9A%E5%85%A5%E5%8F%A35.png",
        "createUser": 86409,
        "goodsNumber": 0,
        "isSetup": 0,
        "isSalesPerformance": 0,
        "activePrice": 0,
        "employeeReward": 0,
        "forwardPrice": 0,
        "frameType": 0,
        "signType": 1,
        "extend1": "悦东方世纪精品酒店呀呀呀呀呀呀呀",
        "extend2": "https://oss-cn-hangzhou.aliyuncs.com/tsnrhapp/store/shop/shop_logo_1560305005809.jpeg",
        "extend3": "[\"dddddddddddddddddddddddddddddd\",\"111111111111111111111111111111\",\"222222222222222222222222222222\",\"dddddddddddddddddddddddddddddd\",\"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\",\"??????????????????????????????\",\"000000000000000000000000000000\"]",
        "descContent": "[\"数百家企业内训——内训师\",\"数千名“小白”职场规划——成功教练\",\"“智享企业联盟”——人力资源专家\",\"XX企业连锁机构——总裁\"]",
        "itemCategoryList": [],
        "salesPerformance": 0,
        "status": 0,
        "templateId": 49,
        "scCardTemplate": null,
        "activeAddress": "哒哒哒哒哒哒的",
        "sortKey": null,
        "page": null,
        "pageSize": null,
        "buyGiftType": 0,
        "reportingTime": "2019-11-01 10:25:00",
        "sharePosterUUID": "ed2fe915ad754896920bea7e6a64f7e4",
        "shopList": null,
        "scShopInfo": null,
        "signUpCharge": null,
        "contentUrl": "http://zxcity-ma.oss-cn-hangzhou.aliyuncs.com/pop%2Fmp3%2Fbg.mp3"
    }
}
```

### 4.查询所有行业

> POST https://wxappprod.izxcs.com/zxcity_restful/ws/rest

request

```
cmd: operations/getAllMerchantTradeList
data: {}
version: 1
```

response

```
{
    "total": 0,
    "code": 1,
    "msg": "获取列表成功",
    "data": [
        {
            "id": 1,
            "name": "美容美发",
            "showname": "智享潮业",
            "status": 1,
            "value": "1",
            "iconPath": "http://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxhds2tWnfJSXz8R5wPS5d4iEH.jpg",
            "createtime": "2017-12-06 09:09:02",
            "updatetime": "2019-07-10 18:13:15",
            "params": null
        },
        {
            "id": 2,
            "name": "教育培训",
            "showname": "智享学堂",
            "status": 1,
            "value": "2",
            "iconPath": "http://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxJYM4MBy3Kp84bmdXMKDNQ5fd.png",
            "createtime": "2017-12-06 09:13:36",
            "updatetime": "2017-12-15 14:47:14",
            "params": null
        },
        {
            "id": 3,
            "name": "农林渔牧",
            "showname": "智享农业",
            "status": 1,
            "value": "3",
            "iconPath": "http://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxYR68jdXCYsBk7dX4FB45RhzG.png",
            "createtime": "2017-12-06 09:14:45",
            "updatetime": "2017-12-08 12:16:49",
            "params": null
        },
        {
            "id": 4,
            "name": "餐饮美食",
            "showname": "智享美食",
            "status": 1,
            "value": "4",
            "iconPath": "http://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxE583FJhZK3NHfKAFTzYX6DWc.png",
            "createtime": "2017-12-06 09:15:14",
            "updatetime": "2017-12-15 14:46:34",
            "params": null
        },
        {
            "id": 5,
            "name": "服装鞋帽",
            "showname": "智享潮人",
            "status": 1,
            "value": "5",
            "iconPath": "http://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxN8SJR47RDS2Nsx6G7w2FDemY.png",
            "createtime": "2017-12-06 09:17:22",
            "updatetime": "2017-12-08 12:17:33",
            "params": null
        },
        {
            "id": 6,
            "name": "健康养生",
            "showname": "智享健康",
            "status": 1,
            "value": "6",
            "iconPath": "http://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxNezYxKzsktB6trpSirSRYWwG.png",
            "createtime": "2017-12-06 09:17:27",
            "updatetime": "2018-08-21 17:39:34",
            "params": null
        },
        {
            "id": 7,
            "name": "婴幼用品",
            "showname": "智享宝宝",
            "status": 1,
            "value": "7",
            "iconPath": "http://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxtFbdfrZXNiQQnyX2cB4nMtYn.png",
            "createtime": "2017-12-06 09:17:29",
            "updatetime": "2017-12-15 14:49:29",
            "params": null
        },
        {
            "id": 8,
            "name": "文化用品",
            "showname": "智享文化",
            "status": 1,
            "value": "8",
            "iconPath": "http://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxaPiMD4cE4FPxSZzHzQkBCQjG.png",
            "createtime": "2017-12-06 09:17:32",
            "updatetime": "2017-12-20 10:21:20",
            "params": null
        },
        {
            "id": 9,
            "name": "休闲娱乐",
            "showname": "智享乐城",
            "status": 1,
            "value": "9",
            "iconPath": "http://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxaMS85Y2Sd3ynT3riw4mnCtje.png",
            "createtime": "2017-12-06 09:17:34",
            "updatetime": "2019-01-09 18:02:52",
            "params": null
        },
        {
            "id": 10,
            "name": "旅游休闲",
            "showname": "智享休闲",
            "status": 1,
            "value": "10",
            "iconPath": "img/upload.png",
            "createtime": "2018-05-31 10:58:54",
            "updatetime": "2018-05-31 10:58:54",
            "params": null
        },
        {
            "id": 11,
            "name": "智享经营",
            "showname": "智享经营",
            "status": 1,
            "value": "11",
            "iconPath": "img/upload.png",
            "createtime": "2018-08-21 10:58:40",
            "updatetime": "2018-08-21 10:58:40",
            "params": null
        },
        {
            "id": 12,
            "name": "医疗保健",
            "showname": "智享医疗",
            "status": 1,
            "value": "12",
            "iconPath": "https://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxr4pzMfBk2yZysQZPPXA3txaj.jpg",
            "createtime": "2018-08-21 17:39:10",
            "updatetime": "2018-08-21 17:39:10",
            "params": null
        },
        {
            "id": 13,
            "name": "绿色旅行",
            "showname": "智享旅行",
            "status": 1,
            "value": "13",
            "iconPath": "img/upload.png",
            "createtime": "2018-08-21 17:40:16",
            "updatetime": "2018-08-21 17:40:16",
            "params": null
        },
        {
            "id": 14,
            "name": "挂饰饰品",
            "showname": "智享饰品",
            "status": 1,
            "value": "14",
            "iconPath": "img/upload.png",
            "createtime": "2018-08-21 17:40:56",
            "updatetime": "2018-08-21 17:40:56",
            "params": null
        },
        {
            "id": 15,
            "name": "服装设计",
            "showname": "智享设计",
            "status": 1,
            "value": "15",
            "iconPath": "img/upload.png",
            "createtime": "2018-08-21 17:41:30",
            "updatetime": "2018-08-21 17:41:30",
            "params": null
        },
        {
            "id": 35,
            "name": "医疗美容",
            "showname": "智享医疗",
            "status": 1,
            "value": "16",
            "iconPath": "https://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zx5YjTMsemEiJ7zGMFXkpE2Yer.JPG",
            "createtime": "2018-09-29 15:52:11",
            "updatetime": "2019-07-02 15:43:41",
            "params": null
        },
        {
            "id": 36,
            "name": "医疗健康",
            "showname": "医疗美容",
            "status": 1,
            "value": "17",
            "iconPath": "https://zxcity-app.oss-cn-hangzhou.aliyuncs.com/user-dir/zxak5mXpdSjwWzHFkkMDTXPGQp.png",
            "createtime": "2018-11-28 16:25:05",
            "updatetime": "2019-07-02 15:43:18",
            "params": null
        }
    ]
}
```

### 5.小程序-（千人报名）智享课堂报名海报-查看报名详情

> POST https://wxappprod.izxcs.com/zxcity_restful/ws/rest

request

```
cmd: shop/selectSignDetail
data: {"activeId":"10176","shopId":"1892","customerId":86126}
version: 1
```

response

```情况一
{
    "total": 0,
    "code": 9,
    "msg": "无报名记录！",
    "data": null
}
```

```情况二
// TODO:

```

### 6.检查手机号是否已报名

> POST https://wxappprod.izxcs.com/zxcity_restful/ws/rest

request

```
cmd: shop/selectByPhone
data: {"activeId":"10176","phone":"18871482140","shareUserId":"0","recommendUserId":"86126"}
version: 1
```

response

```情景一
{
    "total": 0,
    "code": 9,
    "msg": "该手机号已报名！",
    "data": null
}
```

```情景二
{
    "total": 0,
    "code": 1,
    "msg": "查询成功！",
    "data": {
        "price": 0.02,
        "userType": 1,
        "shareUserName": "",
        "recommendUserName": "☆大左"
    }
}
```

### 7.小程序-（千人报名）智享课堂报名海报-报名、下订单

> POST https://wxappprod.izxcs.com/zxcity_restful/ws/rest

request

```
cmd: shop/activePosterSingup
data: {"activeId":"10176","merchantId":"86409","shopId":"1892","customerId":86126,"shareUserId":"0","recommendUserId":"86126","amount":0.02,"signupShopList":[{"tradeId":1,"tradeName":"美容美发","shopName":"大左的店铺","shopAddress":"湖北省武汉市武昌区中山路237号","shopAddressDetail":"东沙大厦","longitude":114.31599,"latitude":30.55386,"signupUserList":[{"username":"dazuo","phone":"18871482141","signupType":1,"price":0.02}]}]}
version: 1
```

response

```
{
    "total": 0,
    "code": 1,
    "msg": "报名成功！",
    "data": "ZXCSSHOP201908062110515320008"
}
```

### 8.发起支付，拉起支付窗口

> POST https://wxappprod.izxcs.com/zxcity_restful/ws/rest

request

```
cmd: payBoot/wx/pay/cloudShop/unifiedOrder
data: {"openid":"oPL_b4oxExGTrGkqE4cgK0dSnLtY","requestBody":{"body":"云店小程序普通订单","out_trade_no":"ZXCSSHOP201908062110515320008","trade_type":"JSAPI"}}
version: 1
```

response

```
{
    "total": 0,
    "code": 1,
    "msg": "操作成功!",
    "data": {
        "timeStamp": "1565097052",
        "wxResult": {
            "returnCode": "SUCCESS",
            "returnMsg": "OK",
            "resultCode": "SUCCESS",
            "errCode": null,
            "errCodeDes": null,
            "appid": "wxd471bb4262ac7505",
            "mchId": "1509096611",
            "subAppId": null,
            "subMchId": null,
            "nonceStr": "Sw4l6hNF85rSihPQ",
            "sign": "36C28C377109C230C51115E4177025EF",
            "xmlString": "<xml><return_code><![CDATA[SUCCESS]]></return_code>\n<return_msg><![CDATA[OK]]></return_msg>\n<appid><![CDATA[wxd471bb4262ac7505]]></appid>\n<mch_id><![CDATA[1509096611]]></mch_id>\n<nonce_str><![CDATA[Sw4l6hNF85rSihPQ]]></nonce_str>\n<sign><![CDATA[36C28C377109C230C51115E4177025EF]]></sign>\n<result_code><![CDATA[SUCCESS]]></result_code>\n<prepay_id><![CDATA[wx06211052117606bc37a8e2dd1306564500]]></prepay_id>\n<trade_type><![CDATA[JSAPI]]></trade_type>\n</xml>",
            "prepayId": "wx06211052117606bc37a8e2dd1306564500",
            "tradeType": "JSAPI",
            "mwebUrl": null,
            "codeURL": null
        },
        "paySign": "34F686CE9995E59891C9B5FE818888C6"
    }
}
```