"""
没毛，没毛，买毛，一分钱也没有
抓包userapi.qiekj.com域名里的token
变量名pgsh=token，多账号用@
执行时间: 0 6-17/1 * * * 胖乖生活.py
"""
import  requests
import  json
import os
import time
accounts = os.getenv('pgsh')
accounts_list = os.environ.get('pgsh').split('@')
num_of_accounts = len(accounts_list)
print(f"获取到 {num_of_accounts} 个账号")
for i, account in enumerate(accounts_list, start=1):
    token = accounts_list[0]
    url="https://userapi.qiekj.com/task/completed"
    headers= {
        "Host": "userapi.qiekj.com",
        "Authorization": token,
        "Version": "1.35.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    print(f"\n=======开始执行账号{i}=======")
    print(f"{'-' * 15}执行看广告{'-' * 15}") 
    for j in range(31):
      data=f"taskType=2&token={token}"
      response=requests.post(url,headers=headers,data=data).json()
      if response['data']=='true':
        print(f"第{j+1}个任务成功")
      else:
        print("广告任务完成")
        break
      time.sleep(2)
    print(f"{'-' * 15}执行日常任务{'-' * 15}") 
    for h in range(1, 21):
      data1=f"taskType={h}&token={token}"
      response=requests.post(url,headers=headers,data=data1).json()
      if response['data']=='true':
        print(f"第{h+1}个任务成功")
      else:
        print("日常任务完成")
        break
      time.sleep(2)
    print(f"{'-' * 15}执行浏览商品{'-' * 15}") 
    url="https://qemyapi.qiekj.com/api/search_item_list"
    headers= {
        "Host": "qemyapi.qiekj.com",
        "Authorization": token,
        "Version": "1.35.0",
        "channel": "android_app",
        "content-length": "60",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9",
    }
    data2=f"keyWord=%E9%98%B2%E6%99%92%E8%A1%A3&page=1&pageSize=20&token={token}"
    response=requests.post(url,headers=headers,data=data2).json()
    task_ids = [taskItem['item_id'] for taskItem in response['data']['data'][:6]]
    for task_id in task_ids:
      url = "https://userapi.qiekj.com/integralUmp/rewardIntegral"
      headers= {
        "Host": "userapi.qiekj.com",
        "Authorization": token,
        "Version": "1.35.0",
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
        print(f"浏览商品获得{score}")
      time.sleep(2)
      
      
    
    
    
