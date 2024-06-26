# 入口 wx小程序  交个朋友
# 抓包 抓 authorization
# 变量 'jgpy'  格式authorization#备注
# 多账号'&'分割
# 一个半月一张月卡
# 每天定时一次 在6:00之前 5:00左右运行 不然获取不到直播列表

import os
import time
import requests
import json
import datetime
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class JGPY():
    def __init__(self,token):
        self.token = token
        self.time1 = datetime.datetime.now().strftime('%Y/%m/%d')
        self.time2 = datetime.datetime.now().strftime('%Y-%m-%d')
        self.live_list = []
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9105",
            "authorization": self.token,
            "xy-extra-data": "appid=wx78f8425753bf755f;version=2.2.10;envVersion=release;senceId=1000",
            "referer": "https://servicewechat.com/wx78f8425753bf755f/19/page-frame.html",
        }

    def sign(self):
        print('-------🎁签到🎁-------')
        time.sleep(2)
        url = "https://smp-api.iyouke.com/dtapi/pointsSign/user/sign"
        params = {
            "date": self.time1
        }
        res = requests.get(url, headers=self.headers, params=params,verify=False).json()
        if res['error'] == 0:
            print('--🌈签到成功，获得{}积分🌈--'.format(res['data']['signReward']))
            time.sleep(2)
        else:
            print('--❎签到失败，响应信息[{}]❎--'.format(res['errorMsg']))
            time.sleep(2)

    def wish(self):
        url = "https://smp-api.iyouke.com/dtapi/p/myWish/wish"
        data = {
            "wishContent": "卫生巾",
            "pic": "",
            "category": "其他",
            "brand": "卫生巾",
            "prodName": "舒肤佳"
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=self.headers, data=data, verify=False).json()

        print(response)
        time.sleep(2)


    def get_live(self):
        print('----🎁获取直播列表🎁----')
        time.sleep(2)
        url = "https://smp-api.iyouke.com/dtapi/channel/live/page"
        params = {
            "day": self.time2,
            "liveHostId": "283",
            "current": "1",
            "pageSize": "10"
        }
        response = requests.get(url, headers=self.headers, params=params, verify=False).json()
        if response['error'] == 0:
            print('--✅成功获取直播列表✅--')
            for item in response['data']['selectedDayLives']:
                liveId = item['liveId']
                theme = item['theme']
                subscribe = item['subscribe']
                starttime = item['startTime']
                self.live_list.append((liveId, theme, subscribe,starttime))
                time.sleep(2)
            if len(self.live_list) == 0:
                print('❗❗❗未公布直播时间，请5:00再运行❗❗❗')
                return False
            else:
                return True
        else:
            print('--❌获取直播列表失败，请检查变量或者联系作者❌--')
            time.sleep(2)
    def sub(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9105",
            "Content-Type": "application/json",
            "authorization": self.token,
            "xy-extra-data": "appid=wx78f8425753bf755f;version=2.2.10;envVersion=release;senceId=1000",
            "referer": "https://servicewechat.com/wx78f8425753bf755f/19/page-frame.html"
        }
        print('------🎁直播订阅🎁------')
        time.sleep(2)
        url = "https://smp-api.iyouke.com/dtapi/points/task/submit"
        for item in self.live_list:
            if not item[2] :
                if int(datetime.datetime.now().hour) < int(datetime.datetime.strptime(item[3], '%Y-%m-%d %H:%M').hour):
                    data = {
                        "bizId": item[0],
                        "taskType": 3
                    }
                    data = json.dumps(data, separators=(',', ':'))
                    response = requests.post(url, headers=headers, data=data, verify=False)
                    print('--🌈订阅成功，获得5积分🌈--')
                    time.sleep(2)
                else:
                    print('--❎当前已过订阅时间，无法订阅❎--')
                    time.sleep(2)
            else:
                print('--✅{}已订阅✅--'.format(item[1]))
                time.sleep(2)
    def watch(self):
        print('------🎁观看直播🎁------')
        time.sleep(2)
        url = "https://smp-api.iyouke.com/dtapi/points/task/2"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9105",
            "Content-Type": "application/json",
            "authorization": self.token,
            "xy-extra-data": "appid=wx78f8425753bf755f;version=2.2.10;envVersion=release;senceId=1000",
            "referer": "https://servicewechat.com/wx78f8425753bf755f/19/page-frame.html"
        }
        for item in self.live_list:
            if int(datetime.datetime.now().hour) - int(datetime.datetime.strptime(item[3], '%Y-%m-%d %H:%M').hour) < 6:
                url = "https://smp-api.iyouke.com/dtapi/points/task/submit"
                data = {
                    "taskType": 2,
                    "bizId": item[0]
                }
                data = json.dumps(data, separators=(',', ':'))
                response = requests.post(url, headers=headers, data=data,verify=False).json()
                if response['error'] == 0:
                    print('--🌈直播预告观看成功，获得5积分🌈--')
                    time.sleep(2)
                else:
                    print('--❎观看失败，响应信息[{}]❎--'.format(response['errorMsg']))
                    time.sleep(2)
            else:
                print('--❎直播已结束❎--')
                time.sleep(2)

if __name__ == '__main__':
    account = os.getenv('jgpy')
    if not account:
        print('❗❗环境变量未设置，请检查❗❗')
        exit(0)
    account_list = os.environ.get('jgpy').split('&')
    print('--🥝共检测到{}个账号，开始执行交个朋友🥝--'.format(len(account_list)))
    for i, item in enumerate(account_list):
        parts = item.split('#')
        token = parts[0]
        name = parts[1]
        print('--🌀执行第{}个账号[{}]🌀--'.format(i + 1, name))
        jgpy = JGPY(token)
        jgpy.sign()
        # jgpy.wish()
        if jgpy.get_live():
            jgpy.sub()
            jgpy.watch()
        if i+1 < len(account_list):
            msg ='--💤开始执行下个账号💤--' + os.linesep
            print(msg)