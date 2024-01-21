'''
📖必看免费小说_1.1     ♻20231220

自动完成金币任务，自动提现至微信（需绑定微信和手机且连续签到）

APP下载地址：https://tinyurl.com/4udwu6e2

青龙环境变量：
抓包sensors.ibreader.com域名下的Cookie，多账号用&隔开
变量名：bkxs     变量值：version=5.2.25.28xxxxxx

定时：45 7 * * *

'''

import requests
import hashlib
import random
import time
import os

withdraws_item_id = '2'  #提现额度id，替换为需要提现的id，默认1元(仅限新用户)。【id1:1元，id2:5元，id3:10元，id4:30元，id5:50元，id6:100元】
money_Withdrawal = 1  #自动提现开关，1开启 0关闭

#执行任务
def finish(taskId):
    timestamp = int(time.time())
    sign = hashlib.md5(f'7b7fpld4roey0e6e&taskId={taskId}&time={timestamp}'.encode()).hexdigest()
    url = f"http://api.ibreader.com/task_api/task/finish"
    headers = {
        'Host': 'api.ibreader.com',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8',
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; PCAM00 Build/NGI77B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.25 Mobile Safari/537.36',
        'X-Client': 'sv=7.1.2;pm=PCAM00;ss=1080*2196;version=5.1.86.18.130500001;vId=60752445880d4366988c18aa9d9f6b80;signVersion=2;webVersion=new;oaid=null;pkv=1;ddid=DUzp43Y2YF9X-5bmS5YXSEZcB3nELTOxTV04RFV6cDQzWTJZRjlYLTVibVM1WVhTRVpjQjNuRUxUT3hUVjA0c2h1;androidosv=25;os=0;muk=ui98HJmkunswcEuBWDlg3A%3D%3D;firm=OPPO;duk=Bv6b4gAgfXcjaj%2BBwEtH32pUNNCFZYDKNOv%2Boplr96Q%3D;',
        'Referer': 'https://api.ibreader.com/task_api/task/getChapterTaskList',
        'Accept-Encoding': 'gzip, deflate',
    }
    data = {
        'time': timestamp,
        'sign': sign,
        'taskId': taskId,
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        result = response.json()
        if result['code'] == 100:
            if result['data']['rewardNum'] > 0:
                print(f"\n恭喜获得:{result['data']['rewardNum']}金币")
        elif result['code'] == 180:
            print("任务已完成")
    except requests.exceptions.RequestException as e:
        print("❗请求异常:", e)
        
#章节阅读        
def readChapter():
    timestamp = int(time.time())
    sign = hashlib.md5(f'7b7fpld4roey0e6e'.encode()).hexdigest()
    url = f"https://api.ibreader.com/api/mission/readChapter"
    headers = {
        'Host': 'api.ibreader.com',
        'Cookie': cookie,
        'X-Client': 'sv=7.1.2;pm=PCAM00;ss=1080*2196;version=5.1.86.18.130500001;vId=60752445880d4366988c18aa9d9f6b80;signVersion=2;webVersion=new;oaid=null;pkv=1;ddid=DUzp43Y2YF9X-5bmS5YXSEZcB3nELTOxTV04RFV6cDQzWTJZRjlYLTVibVM1WVhTRVpjQjNuRUxUT3hUVjA0c2h1;androidosv=25;os=0;muk=ui98HJmkunswcEuBWDlg3A%3D%3D;firm=OPPO;duk=Bv6b4gAgfXcjaj%2BBwEtH32pUNNCFZYDKNOv%2Boplr96Q%3D;',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; PCAM00 Build/NGI77B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.25 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'content-length': '84',
        'accept-encoding': 'gzip'
    }
    data = f'sign={sign}&bookId=4263335&chapterNum=1&time={timestamp}'
    try:
        response = requests.post(url, headers=headers, data=data)
        result = response.json()
        if result['code'] == 100:
            print(f"{result['msg']}")
        elif result['code'] == 180:
            print("任务已完成")
    except requests.exceptions.RequestException as e:
        print("❗请求异常:", e)

#执行提现
def withdraw():
    if money_Withdrawal == 1:
        print("=====开始执行提现=====")
        timestamp = str(int(time.time()))
        sign = hashlib.md5(('7b7fpld4roey0e6e&itemId=' + withdraws_item_id + '&platform=0&time=' + timestamp).encode()).hexdigest()
        url = f"https://increase.ibreader.com/task_api/task/v1/withdraw/valid"
        headers = {
            'Host': 'api.ibreader.com',
            'Connection': 'Keep-Alive',
            'Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8',
            'Accept': '*/*',
            'Accept-Language': 'zh-cn',
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; PCAM00 Build/NGI77B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.25 Mobile Safari/537.36',
            'X-Client': 'sv=7.1.2;pm=PCAM00;ss=1080*2196;version=5.1.86.18.130500001;vId=60752445880d4366988c18aa9d9f6b80;signVersion=2;webVersion=new;oaid=null;pkv=1;ddid=DUzp43Y2YF9X-5bmS5YXSEZcB3nELTOxTV04RFV6cDQzWTJZRjlYLTVibVM1WVhTRVpjQjNuRUxUT3hUVjA0c2h1;androidosv=25;os=0;muk=ui98HJmkunswcEuBWDlg3A%3D%3D;firm=OPPO;duk=Bv6b4gAgfXcjaj%2BBwEtH32pUNNCFZYDKNOv%2Boplr96Q%3D;',
            'Referer': 'https://api.ibreader.com/task_api/task/getChapterTaskList',
            'Accept-Encoding': 'gzip, deflate',
        }
        data = {
        'itemId': withdraws_item_id,
        'platform': '0',
        'sign': sign,
        'time': timestamp,
        }
        response = requests.post(url, headers=headers, data=data)
        try:
            result = response.json()
            if result['code'] == 100:
                print(f"✅ 提现成功: {result['msg']}")
            else:
                print(f"❗提现失败: 原因是：{result['msg']}")
        except Exception as e:
            print(f"❗信息异常: {response.text}, 原因：{e}")
    elif money_Withdrawal == 0:
        print(f"{'=' * 25}\n不执行提现")
    
def notice():
    try:
        print(requests.get("https://tinyurl.com/yndmt3ww", timeout=5).content.decode("utf-8"))
    except requests.RequestException as e:
        print(f"❗获取通知时出错: {e}")

if __name__ == '__main__':
    notice()
    accounts = os.getenv("bkxs")
    if accounts is None:
      print("❗未检测到变量 bkxs")
    else:
        accounts_list = os.environ.get("bkxs").split("&")
        num_of_accounts = len(accounts_list)
        print(f"\n获取到 {num_of_accounts} 个账号")
        for i, account in enumerate(accounts_list, start=1):
            values = account.split()
            cookie = values[0]
            print(f"\n=======开始执行账号{i}=======")
            task_ids = [1,3,8,96, 97, 98, 99, 100, 101, 102, 103, 104, 105,201,202,203,204,205,206,233, 234, 235, 236, 237, 238,490]
            time_interval = random.uniform(5, 15)
            for task_id in task_ids:
                finish(task_id)
                time.sleep(time_interval)
            for _ in range(15):
                readChapter()
                time.sleep(time_interval)
            withdraw()
            
