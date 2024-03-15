'''
new Env('Q必达小程序');
注册入口:weixin://dl/business/?t=GEK1Z5MV68f
账号密码登录 账号&密码多号@隔开
'''
import requests
import time
import os
def login(username, password):
    url = "http://xcx.wanhuida888.com/ht/web/login/loginNew?t=" + str(int(time.time() * 1000))
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.8",
        "User-Agent": "okhttp-okgo/jeasonlzy",
        "source": "ANDROID",
        "appId": "com.qsongq.fjqexpress",
        "version": "1835",
        "group": "",
        "token": "",
        "cookie": "group=",
        "Content-Type": "application/json;charset=utf-8",
        "Host": "xcx.wanhuida888.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {
        "password": password,
        "account": username
    }
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    msg = response_data['msg']
    token = response_data['data']['token']
    print(f"账号登录结果:{msg}")
    return token
def sign(token):
    url = "http://a2e403quwt.wuliucps.com/ht/web/mine/signIn?t=" + str(int(time.time() * 1000))
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.8",
        "User-Agent": "okhttp-okgo/jeasonlzy",
        "source": "ANDROID",
        "appId": "com.qsongq.fjqexpress",
        "version": "1835",
        "token": token,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "0",
        "Host": "a2e403quwt.wuliucps.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    response = requests.post(url, headers=headers)
    response_data = response.json()
    msg = response_data['msg']
    print(f"账号签到结果:{msg}")
def Video(token):
    url = "https://xcx.wanhuida888.com/ht/web/task/watchVideo?t=" + str(int(time.time() * 1000))
    headers = {
        "Host": "xcx.wanhuida888.com",
        "Connection": "keep-alive",
        "Content-Length": "2",
        "charset": "utf-8",
        "sharecode": "83NPKAI",
        "appid": "wx92e73ad679eee047",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "source": "MINIAPP",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "version": "108",
        "token": token,
        "Referer": "https://servicewechat.com/wx92e73ad679eee047/70/page-frame.html"
    }
    data = {}
    for i in range(3):
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        msg = response_data['msg']
        print(f"广告获取积分{msg}")
        time.sleep(20 + i * 10)  
if __name__ == "__main__":
    qbd = os.environ.get('qbd')
    if not qbd:
        print("请设置qbd环境变量在运行")
    else:
        qbd_list = qbd.split('@')
        for num, qbd_item in enumerate(qbd_list, start=1):
            username, password = qbd_item.split('&')
            print(f"=====开始执行第{num}个账号任务=====")
            print("---------开始执行账号登录")
            token = login(username, password)
            if token:
                print("---------开始执行签到任务")
                sign(token)
                print("---------开始执行广告任务")
                Video(token)
