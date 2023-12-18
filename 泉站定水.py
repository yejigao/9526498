"""
@Qim出品 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
泉站大桶订水_V0.1    入口:微信小程序_泉站大桶订水  (每日签到获获得0.2)
抓包 admin.dtds888.com 取出请求体里面的token
export qztoken=token@微信实名名字
多账号用'===='隔开 例 账号1====账号2
cron：0 2 1 * * ? 
"""


import os
import requests
import time

accounts = os.getenv('qztoken')
response = requests.get('https://gitee.com/shallow-a/qim9898/raw/master/label.txt').text
print(response)
if accounts is None:
    print('你没有填入qztoken，咋运行？')
    exit()
else:
    accounts_list = os.environ.get('qztoken').split('====')
    num_of_accounts = len(accounts_list)
    print(f"获取到 {num_of_accounts} 个账号")
    for i, account in enumerate(accounts_list, start=1):
        values = account.split('@')
        token, name = values[0], values[1]
        print(f"\n=======开始执行账号{i}=======")
        t = int(time.time())
        url = "https://admin.dtds888.com/api/index/user/index"
        data = {
            "deviceType": "wxapp",
            "timestamp": t,
            "token": token,
            "version": "1.00"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8391"
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            nickname = response.json()['data']['user']['user_nickname']
            mobile = response.json()['data']['user']['mobile']
            print(f'{nickname} {mobile}---登录成功')
            url = "https://admin.dtds888.com/api/index/user/SignIn"
            response = requests.post(url, headers, params=data).json()
            if response['code'] == 1:
                print(f"{response['msg']},获得{data}元")
            elif response['code'] == 0:
                print(f"{response['msg']}")
            else:
                print(f"签到失败{response}")
            url = "https://admin.dtds888.com/api/index/index/user_info"
            response = requests.post(url, headers, params=data)
            if response.status_code == 200:
                money = response.json()['data']['user']['balance']
                xx = f'余额: {money}'
                print(xx)
            else:
                print(f'错误{response.json()}')
            url = 'https://admin.dtds888.com/api/index/user/cashPost'
            data = {
                'money': '1',
                'name': name,
                'deviceType': 'wxapp',
                'timestamp': t,
                'token': token,
                'version': '1.00'
            }
            response = requests.post(url, headers=headers, json=data).json()
            if money >= 1:
                response = requests.post(url, headers=headers, json=data)
                msg = response.json()['msg']
                print(msg)
            else:
                print(f"钱包余额不足,跳过提现")

        else:
            print(f"登录失败{response}")
