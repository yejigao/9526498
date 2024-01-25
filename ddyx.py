"""
cron: 0 8 * * *
new Env('点点优选');
微信捉包new.zzpt.top中的userid
青龙变量 export ddyx="userid@userid" 多账号@隔开
默认助力作者赞
"""
import os
import requests
import time
import random
def sign(token):
    url = "https://new.zzpt.top/mini/task/free"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    code = response_data["code"]
    if code == 0:
        msg = response_data["msg"]
        print(f"签到结果:{msg}")
    else:
        print("已签到")
def unauthorized(token):
    url = "https://new.zzpt.top/mini/unauthorized/info/958893"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    code = response_data["code"]
    if code == 0:
        msg = response_data["msg"]
        print(f"助力结果:{msg}")        
def video(token):
    url = "https://new.zzpt.top/mini/task/video"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    code = response_data["code"]
    if code == 0:
        msg = response_data["msg"]
        print(f"观看结果:{msg}")
    else:
        print("已完成")
def lottery(token):
    url = "https://new.zzpt.top/mini/jigsaw/get"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "38",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, compress, br, deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    data = {
        "messageStatus": "",
        "userToken": "",
        "accessType": "1"
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    msg = response_data["msg"]
    print(f"抽奖结果:{msg}")
def exchange(token):
    url = "https://new.zzpt.top/mini/jigsaw/exchange"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    code = response_data["code"]
    if code == 0:
        msg = response_data["msg"]
        price = response_data["data"]["price"]
        print(f"兑换结果:{msg}, 获得余额:{price}")
    else:
        print("未达到要求兑换失败")
def Exchange(token):
    url = "https://new.zzpt.top/mini/jigsaw/exchangePriceByCard/87"
    headers = {
        "Host": "new.zzpt.top",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160049 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "userid": token,
        "Referer": "https://servicewechat.com/wxda7b83cfd34c7fdf/4/page-frame.html"
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    code = response_data["code"]
    if code == 0:
        msg = response_data["msg"]
        price = response_data["data"]["price"]
        print(f"兑换结果:{msg}, 获得余额:{price}")
    else:
        print("未达到要求兑换失败")
if __name__ == "__main__":
    userid = os.environ.get("ddyx")
    if userid:
        tokens_list = userid.split("@")
        for i, token in enumerate(tokens_list):
            print(f">>>>>开始执行第{i+1}个账号任务<<<<<")  
            print(">>>>>领取抽奖机会<<<<<")
            sign(token)
            print(">>>>>助力作者<<<<<")
            unauthorized(token)
            print(">>>>>开始观看广告<<<<<")    
            for _ in range(2):
                video(token)
                time.sleep(random.randint(15, 30))
            print(">>>>>开始执行抽奖<<<<<")
            for _ in range(4):
                lottery(token)
                time.sleep(random.randint(1, 10))
            print(">>>>>福利红包<<<<<")
            exchange(token)
            print(">>>>>龙卡兑换余额<<<<<")
            Exchange(token)
            print("========================================")  
    else:
        print("未找到环境变量ddyx")