'''
new Env('壹米众创');
注册链接:http://ymzc.ihuju.cn/mobile/user/reg/reid/764859.html
手动完成一遍悬赏
BY:YourAhTzu
日期:2.1 13:16
抓Cookie填入ymzc变量多号@
'''
import requests
import os
import time
import random
def ad(ck):
    url = "http://ymzc.ihuju.cn/mobile/Index/ad_status_api.html"
    headers = {
        "Host": "ymzc.ihuju.cn",
        "Connection": "keep-alive",
        "Content-Length": "7",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/112/YM-RT/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://ymzc.ihuju.cn",
        "Referer": "http://ymzc.ihuju.cn/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": ck
    }
    data = {
        "id": "2453",
        "ad_key": "4057f666a20568d68c1f412184c7927a-2453"
    }
    response = requests.post(url, headers=headers, data=data)
    json_data = response.json()
    msg = json_data["msg"]
    print(f"获取广告结果:{msg}")
def Reward(ck):
    url = "http://ymzc.ihuju.cn/mobile/Index/ad_apis.html"
    headers = {
        "Host": "ymzc.ihuju.cn",
        "Connection": "keep-alive",
        "Content-Length": "7",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/112/YM-RT/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://ymzc.ihuju.cn",
        "Referer": "http://ymzc.ihuju.cn/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": ck
    }
    data = {
        "uid": "2453",
        "ad_key": "4057f666a20568d68c1f412184c7927a-2453"
    }
    response = requests.post(url, headers=headers, data=data)
    json_data = response.json()
    money = json_data["money"]
    print(f"提交广告成功，当前账号余额:{money}元")
if __name__ == '__main__':
    cks = os.environ.get('ymzc')
    tokens_list = cks.split('@')
    num = len(tokens_list)
    print(f"=====成功获取到{num}个账号=====")   
    for num, ck in enumerate(tokens_list, start=1):
        print(f"=====开始执行第{num}个账号任务=====")
        for _ in range(10):
            ad(ck)
            time.sleep(random.randint(30, 40))
            Reward(ck)
        print("==============================")