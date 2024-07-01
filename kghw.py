"""
阿慈出品必属精品
辣鸡毛抓refreshToken,openid,appid就可以了(别问怎么抓我也不知道)
本大帅哥库https://github.com/YourAhTzu/ac别for(随缘更新)
"""
import os
import requests
import time
import random

def refresh_token(refreshToken):
    url = "https://www.kugua.com/wxapp/refreshToken"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220099 MMWEBSDK/20240404 MMWEBID/2307 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Content-Type": "application/json"
    }
    data = {
        "refresh_token": refreshToken
    }
    response = requests.post(url, headers=headers, json=data)
    json_response = response.json()
    if json_response.get('status') == "0000":
        token = json_response["data"]["token"]
        codemsg = json_response["codemsg"]
        print(f"token刷新结果{codemsg},开始执行提现任务")
        return token
    else:
        print("刷新失败检查refresh_token是否过期")
        return None

def sign(token, appid, openid):
    url = "https://www.kugua.com/wxapp/inflatedv3/popUpRedEnvelopes"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220099 MMWEBSDK/20240404 MMWEBID/2307 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Content-Type": "application/json"
    }
    data = {
        "token": token,
        "type": 1,
        "invite_id": "",
        "code_ticket": "",
        "count": "",
        "appid": appid,
        "openid": openid
    }
    response = requests.post(url, headers=headers, json=data)
    json_response = response.json()
    if json_response.get('status') == "0000":
        codemsg = json_response["codemsg"]
        print(f"签到结果{codemsg}")
    else:
        codemsg = json_response["codemsg"]
        print(f"签到失败{codemsg}")

def tx(token, openid, appid):
    url = "https://www.kugua.com/wxapp/withdrawal/withdrawal"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220099 MMWEBSDK/20240404 MMWEBID/2307 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Content-Type": "application/json"
    }
    data = {
        "token": token,
        "withdrawalId": 8,
        "appid": appid,
        "openid": openid
    }
    response = requests.post(url, headers=headers, json=data)
    json_response = response.json()
    if json_response.get('status') == "0000":
        amount = json_response["data"]["amount"]
        codemsg = json_response["codemsg"]
        print(f"提现结果{codemsg},提现后余额还剩{amount}")
    else:
        codemsg = json_response["codemsg"]
        print(f"提现失败{codemsg}")

if __name__ == "__main__":
    kghw = os.environ.get('kghw')
    if not kghw:
        print("请设置环境变量在运行")
    else:
        kghw_list = kghw.split('@')
        for num, kghw_item in enumerate(kghw_list, start=1):
            appid, openid, refreshToken = kghw_item.split('&')
            print(f"=====开始执行第{num}个账号任务=====")
            print("---------开始执行账号刷新---------")
            refreshed_token = refresh_token(refreshToken)
            if refreshed_token:
                print("---------开始执行账号签到---------")
                sign(refreshed_token, appid, openid)
                time.sleep(random.randint(10, 30))  
                print("---------开始执行账号提现---------")
                tx(refreshed_token, openid, appid)
                time.sleep(random.randint(10, 30))  
            print("---------账号任务执行完毕---------")