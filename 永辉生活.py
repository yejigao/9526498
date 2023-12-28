''' 
new Env('永辉生活');
果园签到要在七点之后运行抓任意域名的deviceid和access_token(有bug及时反馈)
新增果园浇水其余后期慢慢
'''
import requests
import time
import os
def watering(device_id, access_token):
    print(">>>>>果园浇水<<<<<")
    timestamp = str(int(time.time() * 1000))
    url = f"https://activity.yonghuivip.com/api/web/flow/farm/watering?timestamp={timestamp}&channel=android&platform=android&v=9.12.0.12&sellerid=&deviceid={device_id}&shopid=9637&memberid=962892903519470906&app_version=9.12.0.12&channelSub=&brand=realme&model=RMX3562&os=android&osVersion=android31&networkType=5G&screen=2248*1080&productLine=YhStore&appType=h5&access_token={access_token}"
    headers = {
    "Host": "activity.yonghuivip.com",
    "Connection": "keep-alive",
    "Content-Length": "87",
    "X-YH-Biz-Params": "xdotdy=--&gib=--,0(-$,&gvo=+$0_+)*,+",
    "Accept": "application/json",
    "X-YH-Context": "origin=h5&morse=1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36YhStore/9.12.0.12 cn.yonghui.hyd/2022952001 (client/phone; Android 31; realme/RMX3562)",
    "Content-Type": "application/json",
    "Origin": "https://m.yonghuivip.com",
    "X-Requested-With": "cn.yonghui.hyd",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://m.yonghuivip.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
    "activityCode": "HXNC-QG",
    "shopId": "",
    "channel": "",
    "inviteTicket": "",
    "inviteShopId": ""
    }
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    ladder = response_data["data"]["ladderText"]
    print(f"浇水结果:{ladder}")
def flow(device_id, access_token):
    print(">>>>>果园签到<<<<<")
    timestamp = str(int(time.time() * 1000))    
    url = f"https://activity.yonghuivip.com/api/web/flow/farm/doTask?timestamp={timestamp}&channel=android&platform=android&v=9.12.0.12&sellerid=&deviceid={device_id}&shopid=9637&memberid=962892903519470906&app_version=9.12.0.12&channelSub=&brand=realme&model=RMX3562&os=android&osVersion=android31&networkType=WIFI&screen=2248*1080&productLine=YhStore&appType=h5&access_token={access_token}"
    headers = {
        "X-YH-Biz-Params": "xdotdy=--&gib=--,0(-$,&gvo=+$0_+)*,+",
        "X-YH-Context": "origin=h5&morse=1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36YhStore/9.12.0.12 cn.yonghui.hyd/2022952001 (client/phone; Android 31; realme/RMX3562)",
        "Content-Type": "application/json",
        "Origin": "https://m.yonghuivip.com",
        "X-Requested-With": "cn.yonghui.hyd",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://m.yonghuivip.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    payload = {
        "taskType": "sign",
        "activityCode": "HXNC-QG",
        "shopId": "",
        "channel": ""
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    sign = data["data"]["signText"]
    print(f"果园签到结果:{sign}")
def member(device_id, access_token):
    print(">>>>>首页签到任务<<<<<")
    timestamp = str(int(time.time() * 1000))    
    url = f"https://api.yonghuivip.com/web/coupon/signreward/sign?timestamp={timestamp}&channel=android&platform=android&v=9.12.0.12&app_version=9.12.0.12&sellerid=&channelSub=&jysessionid=9d813fd8-366c-42a6-a409-b5097c14cc5e&brand=realme&model=RMX3562&os=android&osVersion=android31&networkType=WIFI&screen=2248*1080&productLine=YhStore&appType=h5&cityid=11&deviceid={device_id}&shopid=9637&memberid=962892903519470906&access_token={access_token}"
    headers = {
        "Host": "api.yonghuivip.com",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "X-YH-Biz-Params": "ncjkdy=,'+(&nzggzmdy=(&xdotdy=--&gib=--,0(-$,&gvo=+$0_+)*,+&vkkdy=yKWHqna(DlqXsuHhk",
        "Accept": "application/json",
        "X-YH-Context": "origin=h5&morse=1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36YhStore/9.12.0.12 cn.yonghui.hyd/2022952001 (client/phone; Android 31; realme/RMX3562)",
        "Content-Type": "application/json",
        "Origin": "https://m.yonghuivip.com",
        "X-Requested-With": "cn.yonghui.hyd",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://m.yonghuivip.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
        "memberId": "962892903519470906",
        "shopId": "9637",
        "missionid": 39
    }
    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()
    code = response_data["code"]
    if code == 0:
        credit = response_data["data"]["signrewardvo"]["credit"]
        print(f"恭喜获得:{credit}积分")
    else:
        message = response_data["message"]
        print(f"签到失败原因:{message}")
def main():
    tokens_str = os.environ.get('yhsh')
    if not tokens_str:
        print("请设置环境变量yhsh")
        return
    token_pairs = tokens_str.split('@')
    for pair in token_pairs:
        device_id, token = pair.split('&')
        flow(device_id, token)
        watering(device_id, token)
        member(device_id, token)
        time.sleep(5)
        print("----------------------")
if __name__ == "__main__":
    print(">>>>>开始执行所有任务<<<<<")
    main()
    print(">>>>>所有任务执行结束<<<<<")