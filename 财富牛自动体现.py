'''

抓token不拉人一天一毛变量名字cfn
'''
import requests
import time
import json
import os
token = os.environ.get('CFN')
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
    cachSave()