"""
哈罗单车

路径：哈罗单车APP
---------------------
20240529 看视频功能没实现，不知道咋搞
---------------------
用途：签到、看视频得鼓励金，鼓励金兑骑行券、话费
变量名：hello_token
格式： 任意请求头抓 Authorization 值

定时设置：每天一次就行，时间随意
cron: 26 11 * * *
const $ = new Env("哈罗单车");
"""
import os
import random
import re
import time

import requests

from sendNotify import send


class TTCY():
    def __init__(self, token):
        self.token = token
        self.taskCode = ""
        self.taskGuid = ""
        self.taskGroupCode = ""
        self.preTaskCode = ""
        # self.preTaskGuid = ""
        self.preTaskGroupCode = ""
        self.headers = {
            'Host': 'api.hellobike.com',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-site',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/json',
            'Origin': 'https://m.hellobike.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Ariver/1.0.15  NebulaSDK; app=easybike; version=6.62.5 WK RVKType(1) NebulaX/1.0.0',
            'Referer': 'https://m.hellobike.com/',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
        }

    # 签到
    def hello_sign(self):
        json_data = {
            'from': 'h5',
            'systemCode': 61,
            'platform': 4,
            'version': '6.62.5',
            'action': 'common.welfare.signAndRecommend',
            'token': self.token,
        }
        url = 'https://api.hellobike.com/api?common.welfare.signAndRecommend'
        response = requests.post(url, headers=self.headers, json=json_data).json()
        if response['code'] == 0 and response['data']['didSignToday']:
            msg = f'✅签到成功, 奖励金：+{response["data"]["bountyCountToday"]}\n'
        else:
            msg = '❌签到失败， cookie可能已失效!\n'

        print(msg)
        return msg

    # 查询奖励金
    def hello_point(self):
        json_data = {
            'from': 'h5',
            'systemCode': 61,
            'platform': 4,
            'version': '6.63.0',
            'action': 'user.taurus.pointInfo',
            'token': self.token,
            'pointType': 1,
        }
        url = 'https://api.hellobike.com/api?user.taurus.pointInfo'
        response = requests.post(url, headers=self.headers, json=json_data).json()
        if response['code'] == 0:
            msg = f'✅可用奖励金：{response["data"]["amount"]}'
        else:
            msg = '❌查询奖励金失败， cookie可能已失效！'

        print(msg)
        return msg

    def task_list(self):
        headers = {
            'Host': 'marketingapi.hellobike.com',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-site',
            # 'requestId': '4w7f6xU6lV6jDfE',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/json',
            'Origin': 'https://m.hellobike.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Ariver/1.0.15  NebulaSDK; app=easybike; version=6.63.6 WK RVKType(1) NebulaX/1.0.0',
            'Referer': 'https://m.hellobike.com/',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
        }

        json_data = {
            'from': 'h5',
            'systemCode': 61,
            'platform': 4,
            'version': '6.63.6',
            'action': 'mars.task.showTaskList',
            'token': self.token,
            'channelId': 4,
            'sceneNameEn': 'platform_points',
            'subSceneNameEn': 'platform_points_pointshp',
            'taskStatusList': [
                'INIT',
                'RUNNING',
            ],
            'queryUnrewardedTasks': True,
            'adCode': '310117',
            'cityCode': '021',
            'longitude': 121.30650065104167,
            'latitude': 31.136067979600693,
        }

        response = requests.post('https://marketingapi.hellobike.com/api?mars.task.showTaskList', headers=headers,
                                 json=json_data)
        print(response.text)
        if response and response.status_code == 200:
            response_json = response.json()
            if response_json['code'] == 0:
                list = response_json['data']['taskList']
                for task in list:
                    if task['mainTitle'] == '激励视频-任务1':
                        if task['taskStatus'] == 'FINISHED':
                            self.taskCode = task['taskCode']
                            self.taskGuid = task['taskGuid']
                            self.taskGroupCode = task['taskGroupCode']
                        elif task['taskStatus'] == 'INIT':
                            self.preTaskCode = task['taskCode']
                            self.preTaskGroupCode = task['taskGroupCode']

    def accept_task(self):
        json_data = {
            'from': 'h5',
            'systemCode': 61,
            'platform': 4,
            'version': '6.63.6',
            'action': 'mars.task.acceptTaskList',
            'token': self.token,
            'channelId': 4,
            'sceneNameEn': 'platform_points',
            'subSceneNameEn': 'platform_points_pointshp',
            'adCode': '310117',
            'cityCode': '021',
            'longitude': 121.30650065104167,
            'latitude': 31.136067979600693,
            'taskList': [
                {
                    'taskCode': self.preTaskCode,
                    'taskGroupCode': self.preTaskGroupCode,
                },
            ],
        }

        url = 'https://marketingapi.hellobike.com/api?mars.task.acceptTaskList'
        response = requests.post(url, headers=self.headers, json=json_data)
        if response and response.status_code == 200:
            response_json = response.json()
            if response_json['codbe'] == 0:
                print(f"领取视频任务成功")

    def receive_award(self):
        headers = {
            'Host': 'marketingapi.hellobike.com',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-site',
            'requestId': '4w7f7fecPbaHjtw',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/json',
            'Origin': 'https://m.hellobike.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Ariver/1.0.15  NebulaSDK; app=easybike; version=6.63.6 WK RVKType(1) NebulaX/1.0.0',
            'Referer': 'https://m.hellobike.com/',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
        }

        json_data = {
            'from': 'h5',
            'systemCode': 61,
            'platform': 4,
            'version': '6.63.6',
            'action': 'mars.offer.receiveAward',
            'token': self.token,
            'channelId': 4,
            'taskGuid': self.taskGuid,
            'taskGroupCode': self.taskGroupCode,
        }

        response = requests.post('https://marketingapi.hellobike.com/api?mars.offer.receiveAward', headers=headers,
                                 json=json_data)
        print(response.json())

    def main(self):
        msg1 = self.hello_sign()
        msg2 = self.hello_point()
        # 功能未实现
        # self.task_list()
        # self.accept_task()
        # self.receive_award()

        # send("哈啰单车", msg1 + msg2)


if __name__ == '__main__':
    env_name = 'HELLO_TOKEN'
    tokenStr = os.getenv(env_name)
    if not tokenStr:
        print(f'⛔️未获取到token变量：请检查变量 {env_name} 是否填写')
        exit(0)
    tokens = re.split(r'&', tokenStr)
    print(f"哈啰单车共获取到{len(tokens)}个账号")
    for i, token in enumerate(tokens, start=1):
        print(f"\n======== ▷ 第 {i} 个账号 ◁ ========")
        TTCY(token).main()
        print("\n随机等待30-60s进行下一个账号")
        time.sleep(random.randint(30, 60))
