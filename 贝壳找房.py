"""
 变量 BKZF_TOKEN
 多号&隔开
 抓取全部cookie
"""

import os
import re
import time
import requests
import json

ck = ""  # 本地ck

class BKZF:
    def __init__(self, ck1):
        self.name = None
        self.ck = ck1
        self.token = re.search(r'lianjia_token=([^;]+)', self.ck).group(1)
        self.hd = {
            'User-Agent': "Beike3.01.10;POCO POCO+F2+Pro; Android 14",
            'Connection': "Keep-Alive",
            'Accept': "application/json",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'Lianjia-Im-Version': "2.34.0",
            'Lianjia-Version': "3.01.10",
            'Cookie': self.ck
        }

    def login(self):
        try:
            url = "https://wxapp.api.ke.com/es/ershou-xcx/user/site"
            params = {
                'ts': "1714989892402",
                'sign': ""
            }
            headers = {
                'User-Agent': "Mozilla/5.0 (Linux; Android 14; 23117RK66C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20231202 MMWEBID/7136 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
                'Accept-Encoding': "gzip,compress,br,deflate",
                'charset': "utf-8",
                'wll-kgsa': "LJAPPVI accessKeyId=7dIaKkMkwYnjk8jc; nonce=A4P2aKtWRBZZzStrKFx22Edj8iBDsWH7; timestamp=1714989893; signature=Y8Jm9e9YirMrTwTRY23sYX2r2BqMmFMRwIkJjUie54A=",
                'lianjia-session': self.token
            }
            r = requests.get(url, params=params, headers=headers).json()
            if r['error_code'] == 0:
                self.name = r['data']['name']
                print(f'[{self.name}] 登录成功')
                return True
            else:
                print('登录失败：', r['error_msg'])
                return False
        except Exception as e:
            print(e)

    def rewardlist(self):  # 主页领取列表
        url = "https://apps.api.ke.com/openapi/odyssey/island/init?cityId=110000&source=profile"  # 待领取列表

        self.hd['Authorization'] = "MjAxODAxMTFfYW5kcm9pZDo3ZjU4ZWE1ZDhhYTRjNmJiMTYyNzdlNDFiN2JlZWQzZGU2NjRkZmU4"
        try:
            response = requests.get(url, headers=self.hd).json()
            balloonlist = response['data']['balloon']
            self.Rewardcollection(balloonlist)
        except KeyError:
            print(f'[{self.name}] 主页气球奖励 ===> 无待领取奖励~')

    def Rewardcollection(self, balloonlist):
        if balloonlist is None:
            return
        for balloons in balloonlist:
            gameId = balloons['gameId']
            gameType = balloons['gameType']
            self.Rewardcollections(gameType, gameId)

    def tasks(self):
        url = "https://apps.api.ke.com/openapi/taskcenter/api/task/report"

        # 614看二手房源 556地铁找房 563AI造家 553浏览装修首页 607看装修案例 549了解贝壳装修品牌 596看经纪人探房
        tasklist = {
            '614': 'MjAxODAxMTFfYW5kcm9pZDoxMTgyMWMxY2RlYmJjMjFiMDc5N2JkZTY1NTExMzRkZDMyOTg2YTQ0#1714722565',
            '556': 'MjAxODAxMTFfYW5kcm9pZDpiNDg2ZGEyMmE3YWZlYjNlODI3NjZhNjczNzJhOTVjNDMyYmUxZjNh#1714723094',
            '563': 'MjAxODAxMTFfYW5kcm9pZDpiYjc0NWY3OTBkMTM2MWM0OGUzZmUwYjBkYjY0YTk3MTRmYmQ4NDdm#1714723268',
            '553': 'MjAxODAxMTFfYW5kcm9pZDo1Yjg2ZGNlMzNmZjFiMWVkNzFkMTdiMmEyZDgyZWViOGIyMmZmNjI3#1714723420',
            '607': 'MjAxODAxMTFfYW5kcm9pZDpjZWYzYzM0NDQ2NGQ1NTRmZDVkM2I2OGZmMDRiYzQ4YzZmNGM0ODU1#1714723460',
            '549': 'MjAxODAxMTFfYW5kcm9pZDpjZmZmNzRmZTM3YmNmNjEyZTkwOWM0MjkyMmY2MWUwNzFlOTdjNTdm#1714723495',
            '596': 'MjAxODAxMTFfYW5kcm9pZDpjMzU4NmFmODdhOTFkZTZiYTJmNzI5ZTM0ODI3ZWYwMWIxN2Y1NWJi#1714723554'
        }
        taskids = ['614', '556', '563', '553', '607', '549', '596']
        for taskid in taskids:
            Authorizationort = tasklist[taskid]
            Authorizationorts = Authorizationort.split('#')
            Authorization = Authorizationorts[0]
            t = Authorizationorts[1]
            payload = f"task_id={taskid}&event_id=37&brand_id=1&city_id=110000&client=app&request_ts={t}"
            headers = {
                'User-Agent': "Beike3.01.10;POCO POCO+F2+Pro; Android 14",
                'Connection': "Keep-Alive",
                'Accept-Encoding': "gzip",
                'Content-Type': "application/x-www-form-urlencoded",
                'Lianjia-Version': "3.01.10",
                'Authorization': f'{Authorization}',
                'Cookie': self.ck
            }
            r = requests.post(url, data=payload, headers=headers).json()
            print(f"[{self.name}] 完成任务 ===> {r['data']['toast']}")
            self.rewardtask(taskid)

    def Rewardcollections(self, Gametype, GameId):
        url = "https://apps.api.ke.com/openapi/odyssey/island/game/commit"  # 领取主页气球
        payload = json.dumps({
            "gameType": Gametype,
            "gameId": GameId
        })
        self.hd['Authorization'] = "MjAxODAxMTFfYW5kcm9pZDo0OGI4Mjg4M2NmNDdhYzAyZWQzMmFlZjI0ZmVhNjg0ODUxYzdkYWI5"
        response = requests.post(url, data=payload, headers=self.hd).json()
        print(response)

    def rewardtask(self, taskId):
        url = "https://apps.api.ke.com/openapi/odyssey/island/task/commit"  # 领取任务

        payload = json.dumps({
            "taskId": int(taskId),
            "cityId": "110000"
        })
        
        self.hd['Authorization'] = "MjAxODAxMTFfYW5kcm9pZDo0OGI4Mjg4M2NmNDdhYzAyZWQzMmFlZjI0ZmVhNjg0ODUxYzdkYWI5"
        r = requests.post(url, data=payload, headers=self.hd).json()
        print(f"[{self.name}] 领取任务奖励 ===> {r['data']}")

    def Goingtosea(self):
        url = "https://apps.api.ke.com/openapi/odyssey/island/init"
        params = {
            'cityId': "110000",
            'source': "profile"
        }
        self.hd['Authorization'] = "MjAxODAxMTFfYW5kcm9pZDo3ZjU4ZWE1ZDhhYTRjNmJiMTYyNzdlNDFiN2JlZWQzZGU2NjRkZmU4"
        r = requests.get(url, params=params, headers=self.hd).json()
        expedition = r['data']['expedition']
        expeditionStatusName = expedition['expeditionStatusName']
        gameId = expedition['gameId']
        if int(gameId) <= 3:
            if expeditionStatusName == '出海中':
                print(f"[{self.name}] 出海状态 ===> {expeditionStatusName}")
            elif expeditionStatusName == '可出海':
                url = "https://apps.api.ke.com/openapi/odyssey/island/game/open"  # 出海寻宝
                payload = json.dumps({
                    "gameType": "expedition",
                    "gameId": gameId
                })
                self.hd['Authorization'] = "MjAxODAxMTFfYW5kcm9pZDo0OGI4Mjg4M2NmNDdhYzAyZWQzMmFlZjI0ZmVhNjg0ODUxYzdkYWI5"
                res = requests.post(url, data=payload, headers=self.hd).json()
                a = res['data']
                print(f"[{self.name}] ===> {a}")
            elif expeditionStatusName == '已出海':
                print(f"[{self.name}] 出海状态 ===> {expeditionStatusName}")
            elif expeditionStatusName == '完成出海':
                url = "https://apps.api.ke.com/openapi/odyssey/island/game/info"
                params = {
                    'gameType': "expedition"
                }
                self.hd['Authorization'] = "MjAxODAxMTFfYW5kcm9pZDozODVhMTZhYTRjMjIyNDZkYTkzODdkOWM2MTRjY2UwMmNlMDIwN2Rk"
                res = requests.get(url, params=params, headers=self.hd).json()
                print(f"[{self.name}] 出海获得 ===> {res['data']['expedition']['reward']['wood']}")
            else:
                print(f"[{self.name}] 出海状态 ===> {expeditionStatusName}")
        else:
            print(f"[{self.name}] 出海次数 ===> {gameId}")

    def Games(self):
        url = "https://apps.api.ke.com/openapi/odyssey/island/game/micro/init"

        params = {
            'microGameType': "flappy_bird"
        }
        self.hd['Authorization'] = "MjAxODAxMTFfYW5kcm9pZDo2ZDdkODU2OTc1MGU0NDkwYWZkMzQwZGMyMmE3MDdhMDQ0N2E1ZGE0"
        r = requests.get(url, params=params, headers=self.hd).json()
        microGameId = r['data']['microGameId']
        wood = r['data']['wood']
        step = len(wood)
        num = 0
        for woods in wood:
            if woods == 1:
                num = num + 1
        url = "https://apps.api.ke.com/openapi/odyssey/island/game/micro/commit"

        payload = json.dumps({
            "microGameType": "flappy_bird",
            "microGameId": microGameId,
            "step": step,
            "reward": {
                "wood": num,
                "pieceFurnitureList": []
            }
        })
        self.hd['Authorization'] = "MjAxODAxMTFfYW5kcm9pZDo0OGI4Mjg4M2NmNDdhYzAyZWQzMmFlZjI0ZmVhNjg0ODUxYzdkYWI5"
        response = requests.post(url, data=payload, headers=self.hd).json()
        print(f"[{self.name}] 潜水获得木材 ===> {response['data']['reward']['wood']}")

    def start(self):
        if self.login():
            self.rewardlist()
            self.tasks()
            self.Goingtosea()
            self.Games()

if __name__ == '__main__':
    if 'BKZF_TOKEN' in os.environ:
        cookie = os.environ.get('BKZF_TOKEN')
    else:
        print("环境变量中不存在[BKZF_TOKEN],启用本地变量模式")
        cookie = ck
    if cookie == "":
        print("本地变量为空，请设置其中一个变量后再运行")
        exit(-1)
    cookies = cookie.split("&")
    print(f"贝壳找房共获取到 {len(cookies)} 个账号")
    for i, ck in enumerate(cookies):
        print(f"======开始第{i + 1}个账号======")
        BKZF(ck).start()
        time.sleep(2)