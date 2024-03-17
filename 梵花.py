'''
外面66开车的项目就是这个平台签到 有了朱雀以后去QQ官方群卖货即可一直14左右
注册链接:http://h5.feifan.art/#/login/singin?uid=1735403 不可料子
new Env('梵花');
'''
import requests
import os
def sign(token):
    url = "http://feifanapi.feifan.art/app/newYearSign/userSign"
    headers = {
        "user-agent": "Dart/3.2 (dart:io)",
        "appdevice": "android",
        "access-control-allow-origin": "*",
        "appversion": "41",
        "accept-encoding": "gzip",
        "content-length": "0",
        "host": "feifanapi.feifan.art",
        "content-type": "application/json",
        "platform": "1",
        "moduletype": "0",
        "token": token
    }
    response = requests.post(url, headers=headers)
    result = response.json()
    if result["ecode"] == 0:
        print("签到成功")
    else:
        print(result["emessage"])
def Info(token):
    url = "http://feifanapi.feifan.art/app/newYearSign/newYearSignInfo"
    headers = {
        "user-agent": "Dart/3.2 (dart:io)",
        "appdevice": "android",
        "access-control-allow-origin": "*",
        "appversion": "41",
        "accept-encoding": "gzip",
        "content-length": "0",
        "host": "feifanapi.feifan.art",
        "content-type": "application/json",
        "platform": "1",
        "moduletype": "0",
        "token": token
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    userTaskOneCoiledSignDays = data["data"]["userTaskOneCoiledSignDays"]
    print(f"您已连续签到{userTaskOneCoiledSignDays}天")
if __name__ == "__main__":
    token = os.environ.get('fhys')
    if not token:
        print("请设环境变量在运行")
    else:
        cks_list = token.split('@')
        num = len(cks_list)
        for num, ck in enumerate(cks_list, start=1):
            print(f"=====开始执行第{num}个用户的任务=====")
            sign(token)
            Info(token)