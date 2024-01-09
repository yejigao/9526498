import requests
import json
import os
from urllib.parse import quote
import time as timemodule
from datetime import datetime, timedelta, time
accounts = os.getenv('pgsh')
accounts_list = os.environ.get('pgsh').split('@')
num_of_accounts = len(accounts_list)
print(f"获取到 {num_of_accounts} 个账号,""by小陳网络技术")
for i, account in enumerate(accounts_list, start=1):
    values = account.split('#')
    token, name = values[0], values[1]
    print(f"\n=======执行账号{name}=======")
    url = "https://userapi.qiekj.com/task/completed"
    headers = {
        "Host": "userapi.qiekj.com",
        "Authorization": token,
        "Version": "1.38.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    print(f"--🎃APP广告🎃--")
    for j in range(11):
        data = f"taskType=2&token={token}"
        response = requests.post(url, headers=headers, data=data).json()
        timemodule.sleep(5)
        if response['data'] == True:
            print(f"第{j + 1}个任务成功")
        else:
            print("APP广告任务完成")
            break
    print(f"--🍁支付宝广告🍁--")
    for t in range(11):
        data = f"taskType=9&token={token}"
        response = requests.post(url, headers=headers, data=data).json()
        timemodule.sleep(5)
        if response['data'] == True:
            print(f"第{t + 1}个任务成功")
        else:
            print("支付宝广告任务完成")
            break
    print(f"--🍔招商支付任务🍔--")
    for u in range(6):
        data = f"taskType=6&token={token}"
        response = requests.post(url, headers=headers, data=data).json()
        timemodule.sleep(5)
        if response['data'] == True:
            print(f"第{u + 1}个任务成功")
        else:
            print("支付任务完成")
            break
    print(f"--🍥必做任务广告积分🍥--")
    for m in range(8):
        data = f"taskCode=18893134-715b-4307-af1c-b5737c70f58d&token={token}"
        response = requests.post(url, headers=headers, data=data).json()
        timemodule.sleep(3)
        if response['data'] == True:
            print(f"第{m + 1}个任务成功")
        else:
            print("任务完成")
            break
    print(f"--🍥必做任务浏览商品1🍥--")
    for e in range(1):
        data = f"taskCode=22982c2e-f45e-4bd8-b09d-466d9b79144b&token={token}"
        response = requests.post(url, headers=headers, data=data).json()
        if response['data'] == True:
            print(f"第{e + 1}个任务成功")
        else:
            print("任务完成")
    print(f"--🍥必做任务浏览商品2🍥--")
    for k in range(1):
        data = f"taskCode=b800ab21-6320-4fd6-9ec0-1d5369216cd4&token={token}"
        response = requests.post(url, headers=headers, data=data).json()
        if response['data'] == True:
            print(f"第{k + 1}个任务成功")
        else:
            print("任务完成")
            timemodule.sleep(2)
    print(f"--☃️日常任务☃️--")
    for h in range(0, 21):
        data1 = f"taskType={h}&token={token}"
        response = requests.post(url, headers=headers, data=data1).json()
        if response['data'] == True:
            print(f"第{h + 1}个任务成功")
        else:
            print("日常任务完成")
            timemodule.sleep(3)
    print(f"--⚔️浏览商品⚔️--")
    url = "https://qemyapi.qiekj.com/api/search_item_list"
    headers = {
        "Host": "qemyapi.qiekj.com",
        "Authorization": token,
        "Version": "1.38.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    data2 = f"keyWord=%E9%98%B2%E6%99%92%E8%A1%A3&page=1&pageSize=20&token={token}"
    response = requests.post(url, headers=headers, data=data2).json()
    task_ids = [taskItem['item_id'] for taskItem in response['data']['data'][:6]]
    for task_id in task_ids:
        url = "https://userapi.qiekj.com/integralUmp/rewardIntegral"
        headers = {
            "Host": "userapi.qiekj.com",
            "Authorization": token,
            "Version": "1.38.0",
            "channel": "android_app",
            "content-length": "60",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.14.9",
        }
        data3 = f"itemCode={task_id}&token={token}"
        response = requests.post(url, headers=headers, data=data3).json()
        if response['data'] is None:
            print("浏览完成")
            break
        else:
            score = response['data']['rewardIntegral']
            print(f"获得积分：{score}")
            timemodule.sleep(5)
    print(f"--👻报名积分打卡👻--")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    encoded_current_time = quote(current_time)
    headers = {
        "Host": "userapi.qiekj.com",
        "Authorization": token,
        "Version": "1.38.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    url1 = "https://userapi.qiekj.com/markActivity/queryMarkTaskByStartTime"
    url2 = "https://userapi.qiekj.com/markActivity/doApplyTask"
    data4 = {'startTime': encoded_current_time, 'token': token}
    respones = requests.post(url1, headers=headers, data=data4).json()["data"]["taskCode"]
    data5 = {"taskCode": respones, "token": token, }
    respone = requests.post(url2, headers=headers, data=data5).json()["msg"]
    print(f'积分报名结果：{respone}')
    timemodule.sleep(2)
    print(f"--🐼签到🐼--")
    url = "https://userapi.qiekj.com/signin/signInAcList"
    data6 = {"token": token}
    response = requests.post(url, headers=headers, data=data6).json()["data"]["id"]
    url1 = "https://userapi.qiekj.com/signin/doUserSignIn"
    data7 = {"activityId": response, "token": token}
    qiandao = requests.post(url1, headers=headers, data=data7).json()
    if qiandao["msg"] == '成功':
        print("签到成功获得:", qiandao["data"]["totalIntegral"])
    else:
        print(qiandao["msg"])
        timemodule.sleep(2)
    print(f"--💮瓜分积分💮--")
    url1 = "https://userapi.qiekj.com/markActivity/queryMarkTaskByStartTime"
    url2 = "https://userapi.qiekj.com/markActivity/doMarkTask"
    url3 = "https://userapi.qiekj.com/markActivity/markTaskReward"
    current_datetime = datetime.now()
    yesterday_datetime = current_datetime - timedelta(days=1)
    yesterday_now = yesterday_datetime.replace(hour=current_datetime.hour, minute=current_datetime.minute, second=current_datetime.second)
    k = quote(yesterday_now.strftime("%Y-%m-%d %H:%M:%S"))
    data = {"startTime": k, "token": token}
    respones = requests.post(url1, headers=headers, data=data).json()["data"]["taskCode"]
    data1 = {"taskCode": respones, "token": token,}
    respone = requests.post(url2, headers=headers, data=data1).json()["msg"]
    current_time = datetime.now().time()
    afternoon_two = time(14, 10, 0)
    if current_time > afternoon_two:
        guafen = requests.post(url3, headers=headers, data=data1).json()["data"]
        print("获得:", guafen)
    else:
        print("当前未到瓜分时间")
        timemodule.sleep(2)
    print(f"--🌸查询积分🌸--")
    url = "https://userapi.qiekj.com/signin/getTotalIntegral"
    headers = {
        "Host": "userapi.qiekj.com",
        "Authorization": token,
        "Version": "1.38.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    data8 = f"token={token}"
    response = requests.post(url, headers=headers, data=data8)
    data = response.json()['data']
    if data is not None:
        print(f'账户剩余积分：{data}')
        timemodule.sleep(2)