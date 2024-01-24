'''
BY:YourAhTzu
日期:1.5 中午11:21
new Env('奇点积分');
抓access-token变量名字qdjf多号@
'''
import requests
import json
import os
def repairBag(access_token):
    url = "https://qidian.hanhoukeji.com/index.php?s=/api//blebag/repairBag"  # 每日三餐开福袋
    headers = {
        "Host": "qidian.hanhoukeji.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "access-token": access_token,
        "Accept-Encoding": "gzip,compress,br,deflate",
        "version": "1.5.19",
        "platform": "MP-WEIXIN",
        "Referer": "https://servicewechat.com/wx3aa7193831495d74/98/page-frame.html"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    status = data['status']
    message = data['message']
    if status == 200:
        points = data['data']['points']
        print(points)
    else:
        print(message)

def getOrderNo(access_token):
    url = 'https://qidian.hanhoukeji.com/index.php?s=/api/seead/getOrderNo'  # 广告获取
    headers = {
        'Host': 'qidian.hanhoukeji.com',
        'Connection': 'keep-alive',
        'charset': 'utf-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/json',
        'access-token': access_token,
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'version': '1.5.19',
        'platform': 'MP-WEIXIN',
        'Referer': 'https://servicewechat.com/wx3aa7193831495d74/98/page-frame.html'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data.get('status') == 200 and 'order_no' in data.get('data', {}):
            order_no = data['data']['order_no']
            print(f"广告编号:{order_no}")
            return order_no

def points(access_token, order_no):
    url = f"https://qidian.hanhoukeji.com/index.php?s=/api/seead/open&order_no={order_no}"
    headers = {
        "Host": "qidian.hanhoukeji.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C51) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "6c074560213a22e18434c54ec77f2ba8application/json",
        "access-token": access_token,
        "Accept-Encoding": "gzip, compress, br, deflate",
        "version": "1.5.19",
        "platform": "MP-WEIXIN",
        "Referer": "https://servicewechat.com/wx3aa7193831495d74/98/page-frame.html"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    status = data["status"]
    if status == 200:
        points = data["data"]["ponits"]
        print(f"恭喜获得积分:{points}")
    else:
        message = data["message"]
        print(f"获取积分失败，错误信息: {message}")
if __name__ == "__main__":
    access_tokens = os.environ.get('qdjf') 
    tokens_list = access_tokens.split('@')  
    for token in tokens_list:
        repairBag(token)
        order_no = getOrderNo(token)
        points(token, order_no)
        print("==============================")