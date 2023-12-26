'''
注册链接http://cfnadd.tuesjf.cn?share_code=QD9SV0
抓token不拉人一天一毛变量名字cfn
'''
import requests
import time
import json
import os
token = os.environ.get('cfn')
def apis():
    print(">>>>>开始观看广告<<<<<")
    url = f'http://cfn.tuesjf.cn/apis/v1/showIndexData?token={token}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/105/YM-RT/',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'http://m.cfn.tuesjf.cn',
        'X-Requested-With': 'com.hjtq',
        'Referer': 'http://m.cfn.tuesjf.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'data' in data and 'in_video_num' in data['data']:
        video = data['data']['in_video_num']
        if video >= 5:
            print("任务已完成，自动跳过任务")
        else:
            lookVideo()
def lookVideo():
    url = 'http://cfn.tuesjf.cn/apis/v1/lookVideo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/105/YM-RT/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://m.cfn.tuesjf.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
        'look_type': '0',
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    msg = result['msg']
    print(f"观看结果:{msg}")
    time.sleep(15)
def receiveVideo():
    print(">>>>>开始领取收益<<<<<")
    url = 'http://cfn.tuesjf.cn/apis/v1/receiveVideo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/105/YM-RT/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://m.cfn.tuesjf.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    msg = result['msg']
    print(f"领取结果:{msg}")
def cachSave():
    print(">>>>>开始提现<<<<<")
    url = 'http://cfn.tuesjf.cn/apis/v1/cachSave'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/105/YM-RT/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://m.cfn.tuesjf.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
        'id': '3',
        'token': token
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    msg = result['msg']
    print(f"提现结果:{msg}")    
if __name__ == "__main__":
    apis()
    receiveVideo()
    cachSave()