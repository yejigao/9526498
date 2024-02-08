'''
new Env("豌豆时尚")
每日5次抽取红包，是否到账未知
入口：小程序首页抽红包
抓包：https://year.xingtuan.net.cn/mini/dragonuser/draw?messageStatus=&userToken=域名里面的 userId:
变量名：wdssck，多号 @ 隔开
cron 0 7 * * *
v1.0
'''




import os
import time
import requests
import random

now = str(round(time.time() * 1000))
cookies = os.getenv("wdssck")

class ml:
    def __init__(self, cookie):
        self.cookie = cookie.split("#")[0]

    def sign(self):
        for j in range(5):
            url = "https://year.xingtuan.net.cn/mini/dragonuser/draw?messageStatus=&userToken="
            headers={
                "Host": "year.xingtuan.net.cn",
                "Connection": "keep-alive",
                "xweb_xhr": "1",
                "userId": self.cookie,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9053 Content-Type: application/x-www-form-urlencoded",
                "Accept": "*/*",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://servicewechat.com/wxf5a12e913e732b18/6/page-frame.html",
                "Accept-Language": "zh-CN,zh;q=0.9"
            }
            response = requests.request("GET", url=url, headers=headers)
            print(f"========开始进行{j+1}次抽取红包:{self.cookie}")
            print(f"抽取成功：{response.text}")
            time.sleep(5)
        print("-" * 50)

if __name__ == "__main__":
    cookies = cookies.split("@")
    print(f"【豌豆时尚】共检测到{len(cookies)}个账号")
    print(f"==========================================")
    for i, cookie in enumerate(cookies):
        print(f"========【账号{i+1}】开始运行脚本========")
        ml(cookie).sign()
        time.sleep(random.randint(5, 10))
        print(f"程序结束")