'''
new Env('六度圈脉');
注册链接:https://liudu.hongbaoquanzi.com/#/?spm=1583.1.0.4.1(27,28行手动内置ps:拉整体会覆盖)
BY:YourAhTzu
日期:2.5 11:04
抓authorization填入ldqm函数多号@
'''
import requests
import os
import time
import random
def click(authorization):
    url = "https://liudu.hongbaoquanzi.com/addons/redbag/redbag/click"
    headers = {
        "Accept": "text/json",
        "platform": "App",
        "token": authorization,
        "user-agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/32.0)",
        "Content-Type": "application/json;charset=UTF-8",
        "Content-Length": "69",
        "Host": "liudu.hongbaoquanzi.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {
        "type": 2,
        "longitude": "",#自己的
        "latitude": "",#自己的
        "id": 1
    }
    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()
    msg = response_data['msg']
    sign = response_data['data']['sign']
    id = response_data['data']['id']
    print(f"获取红包id结果: {msg}")
    return id,sign
def receive(id, sign,authorization):
    url = "https://liudu.hongbaoquanzi.com/addons/redbag/redbag/receive"
    headers = {
        "Accept": "text/json",
        "platform": "App",
        "token": authorization,
        "user-agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/32.0)",
        "Content-Type": "application/json;charset=UTF-8",
        "Content-Length": "69",
        "Host": "liudu.hongbaoquanzi.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {
        "sign": sign,
        "id": id
    }
    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()
    msg = response_data['msg']
    print(f"上报请求结果: {msg}")
def getRedinfo(id,authorization):
    url = "https://liudu.hongbaoquanzi.com/addons/redbag/redbag/getRedinfo"
    headers = {
        "Accept": "text/json",
        "platform": "App",
        "token": authorization,
        "user-agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/32.0)",
        "Content-Type": "application/json;charset=UTF-8",
        "Content-Length": "69",
        "Host": "liudu.hongbaoquanzi.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {
        "id": id,
        "type": "2"
    }
    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()
    msg = response_data['msg']
    user_money = response_data['data']['user_money']
    print(f"上报请求结果: {msg},恭喜获得: {user_money}")
if __name__ == "__main__":
    authorizations = os.environ.get('ldqm') 
    if not authorizations:
        print("获取账号失败，检查是否配置正确")
    else:
        tokens_list = authorizations.split('@')
        num = len(tokens_list)
        print(f"=====成功获取到{num}个账号=====")   
        for num, authorization in enumerate(tokens_list, start=1):
            print(f"=====开始执行第{num}个账号任务=====")
            for i in range(10):  # 循环执行10次
                id_value, sign = click(authorization)
                receive(id_value, sign, authorization)
                getRedinfo(id_value, authorization)
                sleep_time = random.randint(10, 30)  
                print(f"--->>>等待{sleep_time}秒")
                time.sleep(sleep_time)  
            print("==============================")