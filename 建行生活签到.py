"""
建行生活签到+自动领奖励脚本&&周五石油200-20和100-10券 微信关注 小白技术社 获取更新脚本
对你有帮助可以打赏，石油券是默认都会领一次，所以信用卡也会自动领取，没信用卡的可以走我下边的办卡链接，支持下开发。
ios 越狱源 https://zhaoboy9692.github.io/repo/
博客：https://zhaoxincheng.com/
办卡链接 http://p0.meituan.net/csc/e391c34a75893d102fde56d92db85269216347.jpg
支持下，会持续更新
转载或者二次开发，必须保留以上信息
"""
import json
import random
import re
from time import sleep
from urllib.parse import quote

import requests

# 这里的数据 抓包全都有
phone = ''  # 手机号
user_id = ''  # userid 或着memberid
token = ''
deviceid = '
appversion = ''

headers = {
    'clientinfo': '',
    'user-agent': '%E5%BB%BA%E8%A1%8C%E7%94%9F%E6%B4%BB/2023031502 CFNetwork/1220.1 Darwin/20.3.0',
    'devicetype': 'iOS',
    'mbc-user-agent': f'MBCLOUDCCB/iPhone/iOS14.4.2/{appversion}/{appversion}/0/chinamworld/750*1334/{appversion}/1.0//iPad13,1/iOS/iOS14.4.2',
    'appversion': appversion,
    'ua': 'IPHONE',
    'clientallver': appversion,
    'accept-language': 'zh-cn',
    'deviceid': deviceid,
    'c-app-id': '03_64e1367661ee4091acc04ce98f3660e6',
    'accept': 'application/json',
    'content-type': 'application/json',
}


# 定义加密函数
def encrypt(text):
    res = requests.post('http://82.157.10.108:8086/get_jhenc', data={'encdata': text})
    return res.text


# 定义解密函数
def decrypt(text):
    res = requests.post('http://82.157.10.108:8086/get_jhdec', data={'decdata': text})
    return res.text


def sign_day(mem_id, token):
    """
    签到
    :return:
    """
    cookie = auto_login(token)
    ck = f'SESSION={cookie.get("SESSION")}'
    headers = {
        'Host': 'yunbusiness.ccb.com',
        'content-type': 'application/json;charset=utf-8',
        'mid': '152',
        'appversion': appversion,
        'clientallver': appversion,
        'accept': 'application/json,text/javascript,*/*',
        'clientinfo': '',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'channel_num': '2',
        'origin': 'file://',
        'mbc-user-agent': f'MBCLOUDCCB/iPhone/iOS15.4.1/2.15/2.1.5/{deviceid}/chinamworld/1170*2532/2.1.5.002/1.0/{deviceid}/iPhone12/iOS/iOS15.4.1',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/CloudMercWebView/UnionPay/1.0 CCBLoongPay',
        'cookie': ck,
    }

    params = {
        'txcode': 'A3341A115',
    }
    d = get_act_id(mem_id, '签到', deviceid)
    ACT_ID = d.get('AD_URL', '').split('=')[1]
    print(ACT_ID)

    json_data = {
        'ACT_ID': ACT_ID,
        'REGION_CODE': '110000',
        'chnlType': '1',
        'regionCode': '110000',
    }

    response = requests.post('https://yunbusiness.ccb.com/clp_coupon/txCtrl', params=params, headers=headers,
                             json=json_data)
    print(response.text)
    deal_sign(user_id, ACT_ID)
    return response.text


def get_act_id(mem_id, key_word, deviceid):
    params = {
        'txcode': 'A3341AB03',
    }

    json_data = {
        'IS_CARE': '0',
        'REGION_CODE': '110000',
        'MEB_ID': mem_id,
        'CHANNEL_TYPE': '14',
        'LGT': '116.2445327671808',
        'LTT': '40.05567999910404',
        'DEVICE_NO': '',
        'REAL_REGION_CODE': '110000',
        'SECOND_AD_TYPE_LIST': [
            {
                'SECOND_AD_TYPE': '6',
            },
            {
                'SECOND_AD_TYPE': '7',
            },
            {
                'SECOND_AD_TYPE': '10',
            },
            {
                'SECOND_AD_TYPE': '11',
            },
            {
                'SECOND_AD_TYPE': '12',
            },
            {
                'SECOND_AD_TYPE': '24',
            },
            {
                'SECOND_AD_TYPE': '25',
            },
            {
                'SECOND_AD_TYPE': '37',
            },
            {
                'SECOND_AD_TYPE': '38',
            },
            {
                'SECOND_AD_TYPE': '39',
            },
            {
                'SECOND_AD_TYPE': '40',
            },
            {
                'SECOND_AD_TYPE': '41',
            },
            {
                'SECOND_AD_TYPE': '42',
            },
            {
                'SECOND_AD_TYPE': '75',
            },
            {
                'SECOND_AD_TYPE': '93',
            },
            {
                'SECOND_AD_TYPE': '94',
            },
            {
                'SECOND_AD_TYPE': '95',
            },
            {
                'SECOND_AD_TYPE': '96',
            },
        ],
        'FEED_AD_SHOW_STATUS': 0,
        'chnlType': '1',
        'regionCode': '110000',
    }
    headers = {
        'clientinfo': '',
        'user-agent': '%E5%BB%BA%E8%A1%8C%E7%94%9F%E6%B4%BB/2023031502 CFNetwork/1220.1 Darwin/20.3.0',
        'devicetype': 'iOS',
        'mbc-user-agent': 'MBCLOUDCCB/iPhone/iOS14.4.2/2.12/2.1.2/0/chinamworld/750*1334/2.1.5.001/1.0//iPad13,1/iOS/iOS14.4.2',
        'appversion': '2.1.5.001',
        'ua': 'IPHONE',
        'clientallver': '2.1.5.001',
        'accept-language': 'zh-cn',
        'deviceid': deviceid,
        'c-app-id': '03_64e1367661ee4091acc04ce98f3660e6',
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    response = requests.post('https://yunbusiness.ccb.com/basic_service/txCtrl', params=params, headers=headers,
                             json=json_data)
    data = response.json().get('data', {})
    info = data.get('GIFT_AD_INFO', [])
    for d in info:
        if key_word in str(d):
            return d


def auto_login(token):
    cookies = {
    }

    headers = {
        'Host': 'yunbusiness.ccb.com',
        'user-agent': '%E5%BB%BA%E8%A1%8C%E7%94%9F%E6%B4%BB/2023031502 CFNetwork/1404.0.5 Darwin/22.3.0',
        'devicetype': 'iOS',
        'mbc-user-agent': f'MBCLOUDCCB/iPhone/iOS15.0.1/2.15/2.1.5/DF7459F6-CC42-443B-BBA4-0E5E1344A847/chinamworld/1125*2436/2.1.5.001/1.0/{deviceid}/iPhone12ProMax/iOS/iOS15.0.1',
        'appversion': '2.1.5.001',
        'ua': 'IPHONE',
        'clientallver': '2.1.5.001',
        'deviceid': deviceid,
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'c-app-id': '03_64e1367661ee4091acc04ce98f3660e6',
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    params = {
        'txcode': 'autoLogin',
    }

    data = {
        "Token": token}
    data = json.dumps(data)
    data = quote(encrypt(data))
    response = requests.post('https://yunbusiness.ccb.com/clp_service/txCtrl', params=params, cookies=cookies,
                             headers=headers, data=data)

    print(response.text)
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookie)
    return cookie


def ge_sign_data(nodeDay, actId):
    cookies = {
    }

    headers = {
        'Host': 'yunbusiness.ccb.com',
        'content-type': 'application/json;charset=utf-8',
        'accept': 'application/json,text/javascript,*/*',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'origin': 'file://',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/CloudMercWebView/UnionPay/1.0 CCBLoongPay',
    }

    params = {
        'txcode': 'A3341A073',
    }

    json_data = {
        'actId': actId,
        'nodeDay': int(nodeDay),
        'chnlType': '1',
    }

    response = requests.post(
        'https://yunbusiness.ccb.com/clp_coupon/txCtrl',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.text)
    return response.json().get('data', [])


def get_sign_dui(nodeDay, mebId, actId, nodeCouponId):
    cookies = {
    }

    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Accept': 'application/json,text/javascript,*/*',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Origin': 'file://',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/CloudMercWebView/UnionPay/1.0 CCBLoongPay',
        'Connection': 'keep-alive',
        'Host': 'yunbusiness.ccb.com',
        'MID': '152',
        'clientInfo': '{"appVersion":"2.1.4.001","resourseBundleVersion":"","deviceId":"BBE400ED-4C18-4587-A81B-A5C2A4A0BF02","deviceModel":"iPhone 12 Pro Max","osType":"iOS","osVersion":"15.0.1","mac":"","dFingerprint":"65d62662-a276-4e37-a7d5-80e00ff55115","gpsCityCode":"110000","cityCode":"610100"}',
        'CHANNEL_NUM': '2',
    }

    params = {
        'txcode': 'A3341C082',
    }

    json_data = {
        'mebId': mebId,
        'actId': actId,
        'nodeDay': nodeDay,
        'couponType': 0,
        'nodeCouponId': nodeCouponId,
        'dccpBscInfSn': '',
        'chnlType': '1',
        'regionCode': '110000',
    }

    response = requests.post(
        'https://yunbusiness.ccb.com/clp_coupon/txCtrl',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.text)


def auto_login(token):
    cookies = {
    }

    headers = {
        'Host': 'yunbusiness.ccb.com',
        'user-agent': '%E5%BB%BA%E8%A1%8C%E7%94%9F%E6%B4%BB/2023031502 CFNetwork/1404.0.5 Darwin/22.3.0',
        'devicetype': 'iOS',
        'mbc-user-agent': f'MBCLOUDCCB/iPhone/iOS16.3.1/2.12/2.1.2/7E1BDB39-5CF8-4B88-BB12-AFF439B6A249/chinamworld/750*1334/2.1.2.001/1.0/{deviceid}/iPhone8Global/iOS/iOS16.3.1',
        'appversion': '2.1.2.001',
        'ua': 'IPHONE',
        'clientallver': '2.1.2.001',
        'deviceid': deviceid,
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'c-app-id': '03_64e1367661ee4091acc04ce98f3660e6',
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    params = {
        'txcode': 'autoLogin',
    }

    data = {
        "Token": token}
    data = json.dumps(data)
    data = quote(encrypt(data))
    response = requests.post('https://yunbusiness.ccb.com/clp_service/txCtrl', params=params, cookies=cookies,
                             headers=headers, data=data)

    print(response.text)
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookie)
    return cookie


def qiangquan_no_pay(USER_ID, phone, coupon_ID, cookie):
    cookies = {

    }
    headers = {
        'Cookie': cookie,
        'user-agent': '%E5%BB%BA%E8%A1%8C%E7%94%9F%E6%B4%BB/2023031502 CFNetwork/1404.0.5 Darwin/22.3.0',
        'mid': '152',
        'devicetype': 'iOS',
        'mbc-user-agent': 'MBCLOUDCCB/iPhone/iOS16.3.1/2.12/2.1.2//chinamworld/750*1334/2.1.2.001/1.0//iPhone8Global/iOS/iOS16.3.1',
        'appversion': '9.1.2.001',
        'channel_num': '2',
        'clientallver': '9.1.2.001',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'accept': 'application/json',
        'content-type': 'application/json',
    }
    params = {
        'txcode': 'A3341C076',
    }

    data = {"MSPS_ENTITY": {"PlatForm_Code": "MCP", "Mblph_No": phone, "coupon_ID": coupon_ID,
                            "Channel_User_ID": USER_ID, "DtSrc": "MCP"}, "MS_FLAG": "0", "COUP_CHNL": "01",
            "Channel_User_ID": USER_ID, "chnlType": "1", "MEB_ID": USER_ID,
            "regionCode": "110000", "CLD_REQ_CHANNEL": "01", "USR_TEL": phone, "PlatForm_Code": "MCP",
            "COUPON_ID": coupon_ID,
            "APPEND_PARAM": deviceid,
            "Mrch_ID": "", "MCT_CTMS": {}, "DtSrc": "MCP", "CLD_SOURCE_CHNL": "01", "coupon_ID": coupon_ID,
            "Mblph_No": phone, "MctGetCoupon_Type": "20", "req_channel_type": "1"}
    data = json.dumps(data)
    data = quote(encrypt(data))

    response = requests.post('https://yunbusiness.ccb.com/clp_coupon/txCtrl', params=params, cookies=cookies,
                             headers=headers, data=data)
    data = json.loads(decrypt(response.text))
    print(data)
    return data


def zhou5shiyou():
    """
    周五石油200-20
    :return:
    """
    cookie = auto_login(token)
    ck = f'SESSION={cookie.get("SESSION")}'
    ss = [
        'https://res.yunbusiness.ccb.com/gbchannel/e_report/CCBLIFE/#/couponDetail/ENFB586C3C45EA139636BEE0BCF3D2A2A8?couponType=msps&START_TIME=0800&SMART_MODE=1&fromPage=webview',
        'https://res.yunbusiness.ccb.com/gbchannel/e_report/CCBLIFE/#/couponDetail/ENB4B903977CAB4BA138F42464BF6EC824?couponType=msps&START_TIME=0800&SMART_MODE=1&fromPage=webview',
        'https://res.yunbusiness.ccb.com/gbchannel/e_report/CCBLIFE/#/couponDetail/ENCEAE35E1D99E38C5AB6C69826E485F0E?couponType=msps&START_TIME=0800&SMART_MODE=1&fromPage=webview', ]
    for contentLink in ss:
        c_id = contentLink[contentLink.find('il/') + 3:contentLink.rfind('?coupon')]
        print(c_id)
        qiangquan_no_pay(user_id, phone, c_id, ck)


def deal_sign(mem_id, ACT_ID):
    """
        领取签到券，couponScene 为要领取全类型，默认价值最高的券，可能会领取信用卡的，无信用卡的情况不清楚
    {
	"errMsg": "",
	"data": [{
		"couponId": "qmJB3XqOPn0=",
		"couponInstanceId": null,
		"couponType": 0,
		"nodeDay": 7,
		"couponName": "连续7天签到满15元减8元外卖券(信用卡专享)",
		"dccpBscInfSn": "",
		"couponImg": "http://img.longpay.ccb.com/cosimg/heroes/api/v1/image/20230626/PIC2306261436249006489296.png",
		"couponPrice": 8,
		"couponBuyPrice": 0,
		"couponScene": "外卖",
		"title": "8元外卖券",
		"subTitle": "限信用卡用户领取"
	}, {
		"couponId": "Q116fqSJNCI=",
		"couponInstanceId": null,
		"couponType": 0,
		"nodeDay": 7,
		"couponName": "连续7天签到满6元减5元骑行券",
		"dccpBscInfSn": "",
		"couponImg": "http://img.longpay.ccb.com/cosimg/heroes/api/v1/image/20230627/PIC2306270905216825321704.png",
		"couponPrice": 5,
		"couponBuyPrice": 0,
		"couponScene": "出行",
		"title": "5元骑行券",
		"subTitle": "满6元可用"
	}, {
		"couponId": "VcinUIMB1Hs=",
		"couponInstanceId": null,
		"couponType": 0,
		"nodeDay": 7,
		"couponName": "连续7天签到满15元减4元外卖券",
		"dccpBscInfSn": "",
		"couponImg": "http://img.longpay.ccb.com/cosimg/heroes/api/v1/image/20230626/PIC2306261432334025307436.png",
		"couponPrice": 4,
		"couponBuyPrice": 0,
		"couponScene": "外卖",
		"title": "4元外卖券",
		"subTitle": "满15元可用"
	}],
}
    :return:
    """
    nodeDay = 3
    couponScene = '外卖'  # 券类型在上边看
    nodeCouponId = ''
    couponPrice = 0
    for d in ge_sign_data(nodeDay, ACT_ID):
        if d.get('couponScene') == couponScene:
            if d.get('couponPrice', 0) >= couponPrice:
                couponPrice = d.get('couponPrice', 0)
                nodeCouponId = d.get('couponId')
    get_sign_dui(nodeDay, mem_id, ACT_ID, nodeCouponId)
    nodeDay = 7
    nodeCouponId = ''
    couponPrice = 0
    for d in ge_sign_data(nodeDay, ACT_ID):
        if d.get('couponScene') == couponScene:
            if d.get('couponPrice', 0) >= couponPrice:
                couponPrice = d.get('couponPrice', 0)
                nodeCouponId = d.get('couponId')
    get_sign_dui(nodeDay, mem_id, ACT_ID, nodeCouponId)


def login_web_token(PLATFORM_ID, token):
    """
    获取cc豆页面登录
    :param token:
    :return:
    """
    cookie = auto_login(token)
    ck = f'SESSION={cookie.get("SESSION")}'
    headers = {
        'Cookie': ck,
        'devicetype': 'iOS',
        'appversion': '2.1.5.001',
        'ua': 'IPHONE',
        'clientallver': '2.1.5.001',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    params = {
        'txcode': 'A3341SB06',
    }

    json_data = {
        "regionCode": "110000",
        "PLATFORM_ID": PLATFORM_ID,
        "chnlType": "1",
        "ENCRYPT_MSG": f"userid={user_id}&mobile={phone}"
    }

    response = requests.post(
        'https://yunbusiness.ccb.com/basic_service/txCtrl',
        params=params,
        headers=headers,
        json=json_data,
    )
    print(response.text)
    ENCRYPTED_MSG = response.json().get('data', {}).get('ENCRYPTED_MSG')
    print(ENCRYPTED_MSG)
    return ENCRYPTED_MSG


def cc_center(ENCRYPTED_MSG):
    """
    cc豆中心登录
    :return:
    """

    headers = {
        'Host': 'cy.cloud.ccb.com',
        'content-type': 'application/json;charset=utf-8',
        'accept': 'application/json, text/plain, */*',
        'channel': 'ccblife',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'origin': 'https://cy.cloud.ccb.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView/UnionPay/1.0 CCBLoongPay',
        'referer': 'https://cy.cloud.ccb.com/qymall/ccbean/ccbean_mall_index?',
    }

    json_data = {
        'data': {
            'ccbParamSJ': ENCRYPTED_MSG,
            'parentChannel': 'JH-0007',
        },
    }

    response = requests.post(
        'https://cy.cloud.ccb.com/gateway/user-server/user/promised/login',
        headers=headers,
        json=json_data,
    )
    print(response.text)
    print(response.headers['token'])
    return response.headers['token']


def redict_short(cc_tk):
    headers = {
        'Host': 'event.ccbft.com',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://event.ccbft.com',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView/UnionPay/1.0 CCBLoongPay',
        'Referer': 'https://event.ccbft.com/e/ccb_gjb/gNMaA4jqEo9J09pVKJdEyg?CCB_Chnl=1029701&ccbParamSJ=a2k3RllZMm9wTFI2MW9KWllKekhNSVZqSWlVQUZZUVpXU1l1T1RkR3RwMUR5YTA0MFpEb1B6eHR5djBPOGVpRzE2K1NGQzJkd2EvSG02N3Q3RHFoVDRKbkhrMmFuck5zZmpkTWpXVmxJTU9jY08xYlpIaUJXTHdFZURlWTF5bHowVG4vSUlCa282ZDlsM1JBbitTREVMcnF3L2h3YVloVHViZ2lUdnVGeksxVDNtR3MwVVQxMGcxQWcvRUlOWWswM3E3bmN5RDFyZFVKR0hTeFpQOG5pNDRibXJYZml1RmdaNmwvQXJob3B2akpIajVVTFgxaWY5Y3Axb3V1U3pmRDgxY2dDV1o4K0EreEdiNHYvVElFZjNNSUtkandmRHB3dkRObHhVajl5bTNZSjJ5Y3BibWQwcm9GWVZrU2RIVkE3bzc2TGRvM096ZU9jUFo0RFQ5MCtZMzVIU1JOVWZXbGNDMC9FNnlsTXE2MmxPTEJMeDZ6aFFlK1BhN2NIaVMyS1hUZDY3S3hxWk5qT2ZxNmVsWUhUbWdyNEJlNHdTbEhndjZTWGlvd2ZGbDF5bEc3U296bXpaeGNZRVIzNkhScU12bjRmS3NNUGl4bkJYQnNpYkp1M3RXNlR4VWJRRUpraCtnaGlJOXpQWnZ6SWpMTEJhUWVyYStLVnRuajltMmNmUmpCVmtkc1g4NE9XL24xUnZ5Mk5sYUwxcnIxbG0zV0VWMnVuam5FOWRRdXAxUkxBOUU2eStLa0pRSHMxU05lbEgweEtaNVFxcTdWY0NlcWxqV25ISFhYWGJDRkswWFBOWXZ6SVBUbFZTWml6SitqVjVqS3QyT1lqOGhUV2MyRytjTm5LQzBJa0Y3QVVCTDg0blJvYU1yeS9POEhUMFdoajRGZEY2ZG01MkU9&cityid=110000&CITYID=110000&userCityId=110000&USERCITYID=110000',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    }

    json_data = {
        'shortId': 'gNMaA4jqEo9J09pVKJdEyg',
        'archId': 'ccb_gjb',
        'ccbParamSJ': cc_tk,
        'channelId': 'ccbLife',
        'ifCcbLifeFirst': True,
    }

    response = requests.post(
        'https://event.ccbft.com/api/flow/nf/shortLink/redirect/ccb_gjb',
        headers=headers,
        json=json_data,
    )

    print(response.text)
    return response.json().get('data', {}).get('redirectUrl')


def get_dirct_data(url):
    res = requests.get(url)
    csrf_token = re.findall('csrf-token content="(.*?)"', res.text)
    auth = re.findall('name=Authorization content="(.*?)"', res.text)
    cookie = requests.utils.dict_from_cookiejar(res.cookies)
    return csrf_token[0], auth[0], cookie


def cc_choujiang(csrf_token, auth, cookies):
    headers = {
        'Host': 'fission-events.ccbft.com',
        'content-type': 'application/json',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'origin': 'https://fission-events.ccbft.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView/UnionPay/1.0 CCBLoongPay',
        'referer': 'https://fission-events.ccbft.com/a/224/xZ4JKaPl/index?CCB_Chnl=1029701&cityid=110000&CITYID=110000&userCityId=110000&USERCITYID=110000&__dmsp_st=U1Q6Y2NiX2dqYjpjY2JMaWZlOjA0QUU0NTUzMUMwREYzNEM5OTA1Q0U5MjE0QThDODI3OmI0NzU2MGY0YmEzYjQ4M2Q5MDlkY2MyMzdlN2M5ZDRm',
        'x-csrf-token': csrf_token,
        'authorization': f'Bearer {auth}',
    }

    json_data = {
        'pot_id': 3,
    }

    response = requests.post(
        'https://fission-events.ccbft.com/activity/dmspblindbox/draw/224/xZ4JKaPl',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.json())


def get_lanqiu_id(csrf_token, auth, cookies):
    headers = {
        'Host': 'fission-events.ccbft.com',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'origin': 'https://fission-events.ccbft.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView/UnionPay/1.0 CCBLoongPay',
        'referer': 'https://fission-events.ccbft.com/a/224/eZgpye3y/index',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-csrf-token': csrf_token,
        'authorization': f'Bearer {auth}',
    }

    response = requests.post(
        'https://fission-events.ccbft.com/activity/dmspdunk/start/224/eZgpye3y',
        headers=headers,
        cookies=cookies
    )
    print(response.text)
    print(response.json())
    print(response.json().get('data', {}).get('id'))
    return response.json().get('data', {}).get('id')


def play_lanqiu(lanqiu_id, csrf_token, auth, cookies):
    headers = {
        'Host': 'fission-events.ccbft.com',
        'content-type': 'application/json',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'x-csrf-token': csrf_token,
        'authorization': f'Bearer {auth}',
        'origin': 'https://fission-events.ccbft.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView/UnionPay/1.0 CCBLoongPay',
        'referer': 'https://fission-events.ccbft.com/a/224/eZgpye3y/game?placeId=dmRzYVmD',
    }

    json_data = {
        'id': lanqiu_id,
    }

    response = requests.post(
        'https://fission-events.ccbft.com/activity/dmspdunk/shot/224/eZgpye3y',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.text)
    print(response.json())
    return response.text


def get_Cst_ID(ck, deviceid, phone):
    headers = {
        'Host': 'yunbusiness.ccb.com',
        'clientinfo': '{"deviceId":"' + deviceid + '","appVersion":"2.1.5.001","osType":"iOS","mac":"0","osVersion":"iOS15.0.1","dFingerprint":"08c9c2e2-c0b4-4d10-9688-2f8c1dc848c0","gpsCityCode":"110000","cityCode":"110000","deviceModel":"iPhone 12 Pro Max"}',
        'user-agent': '%E5%BB%BA%E8%A1%8C%E7%94%9F%E6%B4%BB/2023082202 CFNetwork/1312 Darwin/21.0.0',
        'devicetype': 'iOS',
        'mbc-user-agent': 'MBCLOUDCCB/iPhone/iOS15.0.1/2.15/2.1.5/DF7459F6-CC42-443B-BBA4-0E5E1344A847/chinamworld/1125*2436/2.1.5.001/1.0/' + deviceid + '/iPhone12ProMax/iOS/iOS15.0.1',
        'appversion': '2.1.5.001',
        'ua': 'IPHONE',
        'Cookie': ck,
        'clientallver': '2.1.5.001',
        'deviceid': deviceid,
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'c-app-id': '03_64e1367661ee4091acc04ce98f3660e6',
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    params = {
        'txcode': 'A3341U018',
    }

    json_data = {
        "IS_CERTIF": "1",
        "USR_TEL": phone,
        "chnlType": "1",

    }

    response = requests.post(
        'https://yunbusiness.ccb.com/clp_service/txCtrl',
        params=params,
        headers=headers,
        json=json_data,
    )

    print(response.text)
    return response.json().get('data', {}).get('Cst_ID')


def get_detail(DcCp_Avy_ID=None, Coupon_id=None):
    """
    获取详情
    :return:
    """

    headers = {
        'Host': 'yunbusiness.ccb.com',
        'content-type': 'application/json;charset=utf-8',
        'accept': 'application/json,text/javascript,*/*',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'channel_num': '2',
        'origin': 'file://',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/CloudMercWebView/UnionPay/1.0 CCBLoongPay',
        'skey': 'X7IgMg',
    }

    params = {
        'txcode': 'A3341C006',
    }
    if DcCp_Avy_ID:
        json_data = {
            "CLD_REQ_CHANNEL": "01",
            "KHHK_ENTITY": {
                "DcCp_Bsc_Inf_SN": f"{random.randint(1, 99999)}",
                "DcCp_Avy_ID": DcCp_Avy_ID
            },
            "REQ_CHANNEL_TYPE": 2,
            "chnlType": "1"
        }
    else:
        json_data = {
            "CLD_REQ_CHANNEL": "01",
            "DtSrc": "MCP",
            "MSPS_ENTITY": {
                "Coupon_id": Coupon_id,
                "PlatForm_Code": "MCP"
            },
            "REQ_CHANNEL_TYPE": "1",
            "chnlType": "1",
            "regionCode": "110000"
        }

    response = requests.post('https://yunbusiness.ccb.com/clp_coupon/txCtrl', params=params, headers=headers,
                             json=json_data)
    return response.json().get('data')


def shiwuyuan20购30元星巴克(phone, user_id, token, SKEY, mbskey_info, deviceid, mbc_user_info):
    """
    20元购买30元星巴克 每天0点
    :return:YHQ2023032996582
    """
    cookie = auto_login(token)
    ck = f'SESSION={cookie.get("SESSION")}'
    CST_ID = get_Cst_ID(ck, deviceid, phone)
    DCCP_AVY_ID = 'YHQ2023073104340'  # 每天20买30
    MCT_NM = "20元购买30元星巴克"
    detail = get_detail(DcCp_Avy_ID=DCCP_AVY_ID)
    print(json.dumps(detail))
    KHHK_ENTITYd = detail.get('KHHK_ENTITY')
    LIST2 = KHHK_ENTITYd.get('LIST2')[0]
    LIST1 = KHHK_ENTITYd.get('LIST1', {})
    DcCp_Issu_Num = KHHK_ENTITYd.get('DcCp_Issu_Num')
    DlyAcmPrchDcCpRst_Num = KHHK_ENTITYd.get("DlyAcmPrchDcCpRst_Num", '')
    EachPsnAcmPhDCpRstNum = KHHK_ENTITYd.get("EachPsnAcmPhDCpRstNum", '')
    DcCp_Sale_Prc = KHHK_ENTITYd.get("DcCp_Sale_Prc", '')
    headers = {
        'Host': 'yunbusiness.ccb.com',
        'user-agent': '%E5%BB%BA%E8%A1%8C%E7%94%9F%E6%B4%BB/2023082202 CFNetwork/1312 Darwin/21.0.0',
        'devicetype': 'iOS',
        'mbc-user-agent': 'MBCLOUDCCB/iPhone/iOS15.0.1/2.15/2.1.5/DF7459F6-CC42-443B-BBA4-0E5E1344A847/chinamworld/1125*2436/2.1.5.001/1.0/' + deviceid + '/iPhone12ProMax/iOS/iOS15.0.1',
        'appversion': '2.1.5.001',
        'ua': 'IPHONE',
        'Cookie': ck,
        'clientallver': '2.1.5.001',
        'deviceid': deviceid,
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'c-app-id': '03_64e1367661ee4091acc04ce98f3660e6',
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    params = {
        'txcode': 'A3341O076',
    }

    json_data = {
        'EachPsnDlyPhDCpRstNum': '10',
        'DlyAcmPrchDcCpRst_Num': DlyAcmPrchDcCpRst_Num,
        'PLATFORM': '0',
        'chnlType': '1',
        'MCT_NM': MCT_NM,
        'regionCode': '110000',
        'DcCp_Avy_EdDt': LIST2.get('Seg_Tm_End_ValSt'),
        'Cst_Ctc_Tel': phone,
        'DcCp_Avy_StDt': LIST2.get('Seg_Tm_Strt_ValSt'),
        'DcCp_Issu_Num': DcCp_Issu_Num,
        'DcCp_Prch_Py_Amt': DcCp_Sale_Prc,
        'APPEND_PARAM': '' + deviceid + '|@|111.204.182.100|@|Wifi|@|116.3135032540834|@|40.04471495938354|@|02|@|15.0.1|@|iPhone 12 Pro Max|@||@|110000|@|110000|@|3fa8125ffac3d7b5501963ea3b5b7444f3c1409a|@|2.1.5.001',
        'DcCp_Avy_EdTm': LIST1.get('Seg_Tm_End_ValSt'),
        'ORDER_TYPE': '9',
        'DcCp_Avy_StTm': '000000',
        'DcCp_Avy_ID': DCCP_AVY_ID,
        'USER_ID': user_id,
        'CST_ID': CST_ID,
        'TOTAL_AMT': DcCp_Sale_Prc,
        'EachPsnAcmPhDCpRstNum': EachPsnAcmPhDCpRstNum,
        'MCT_ID': '',
        'DcCp_Prch_Num': '1',
        'DcCp_Bsc_Inf_SN': KHHK_ENTITYd.get('DcCp_Bsc_Inf_SN'),
    }
    print(json.dumps(json_data))
    index = 20
    while index > 0:
        response = requests.post(
            'https://yunbusiness.ccb.com/clp_order/txCtrl',
            params=params,
            headers=headers,
            json=json_data,
        )
        print(response.text)
        if 'ORDER_ID' in str(response.text):
            break
        sleep(3)
        index -= 1


sign_day(user_id, token)
# # # ## 周五石油券
zhou5shiyou()
# # # # 建行生活cc豆抽奖 1w个抽一次，其他的没必要 不能回本
cc_chou_id = 'YS44000010000078'
cc_tk = login_web_token(cc_chou_id, token)
url = redict_short(cc_tk)
csrf_token, auth, cookie = get_dirct_data(url)
i = 6
while i > 0:
    i -= 1
    cc_choujiang(csrf_token, auth, cookie)
    sleep(5)
# 建行生活篮球
lanqiu_chou_id = 'YS44000010000078'
cc_tk = login_web_token(lanqiu_chou_id, token)
url = redict_short(cc_tk)
csrf_token, auth, cookie = get_dirct_data(url)
index = 5
while index > 0:
    index -= 1
    lanqiu_id = get_lanqiu_id(csrf_token, auth, cookie)
    while 1:
        r = play_lanqiu(lanqiu_id, csrf_token, auth, cookie)
        sleep(2)
        if 'fail' in r:
            print("投篮结束")
            break
