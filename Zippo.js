import requests
import os
def gg():
    url = 'https://jihulab.com/Xiaoqinetwork/inform/-/raw/main/gg.txt'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
def Control():
    url = "https://jihulab.com/Xiaoqinetwork/inform/-/raw/main/Control.json"
    response = requests.get(url)
    data = response.json()
    v = data["Zippo"]["v"]
    open_status = data["Zippo"]["open"]
    if open_status == 0:
        print(data["Zippo"]["tz"])
        return False
    print(data["Zippo"]["edition"])
    return True
def sign(authorization):
    url = 'https://wx-center.zippo.com.cn/api/daily-signin'
    headers = {
        'authorization': authorization,
        'charset': 'utf-8',
        'x-app-id': 'zippo',
        'x-platform': 'wxmp'
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 201:
        response_data = response.json()
        rewards = response_data['rewards']
        for reward in rewards:
            count = reward['count']
            print(f"恭喜获得奖励{count}积分")
    elif response.status_code == 400:
        response_data = response.json()
        message = response_data['message']
        print(f"签到失败：{message}")
def Share(authorization):
    url = 'https://wx-center.zippo.com.cn/api/missions/records'
    headers = {
        'authorization': authorization,
        'charset': 'utf-8',
        'x-app-id': 'zippo',
        'x-platform': 'wxmp'
    }
    data = {
        "code": "share"
    }
    response = requests.post(url, headers=headers, data=data)
def Collect(authorization):
    url = 'https://wx-center.zippo.com.cn/api/missions/6/rewards'
    headers = {
        'authorization': authorization,
        'charset': 'utf-8',
        'x-app-id': 'zippo',
        'x-platform': 'wxmp'
    }
    data = {
        "id": 6
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 201:
        response_data = response.json()
        points = response_data['points']
        print(f"恭喜获得奖励{points}积分")
    elif response.status_code == 400:
        response_data = response.json()
        message = response_data['message']
        print(f"领取失败：{message}")
if __name__ == "__main__":
    authorization = os.environ.get('Zippo')
    if not authorization:
        print("请设置Zippo环境变量在运行")
    else:
        cks_list = authorization.split('@')
        num = len(cks_list)
        for num, ck in enumerate(cks_list, start=1):
            gg()
            print(f"=====开始执行第{num}个账号任务=====")
            if Control():
                print("=====开始执行签到任务=====")
                sign(authorization)
                print("=====开始执行分享任务=====")
                for i in range(3):
                    Share(authorization)
                    Collect(authorization)