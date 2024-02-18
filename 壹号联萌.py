"""
壹号联萌 v1.0

变量 token, 多账户换行
export yhlmck=""

cron: 24 13,18 * * *
const $ = new Env("壹号联萌");
"""

import os
import requests
from datetime import datetime, timezone, timedelta
import json
import time
import random
import sys
import io

# 控制是否启用变量

enable_notification = 1   #0不发送通知   1发送通知
USE_THREADS = 1 # 设置为0启用多线程，设置为1使用单线程

# 只有在需要发送通知时才尝试导入notify模块
if enable_notification == 1:
    try:
        from notify import send
    except ModuleNotFoundError:
        print("警告：未找到notify.py模块。它不是一个依赖项，请勿错误安装。程序将退出。")
        sys.exit(1)

#---------简化的框架--------
# 配置参数
base_url = "https://hxxxy.gov.cn"  # 没有使用


# 获取北京日期的函数
def get_beijing_date():  
    beijing_time = datetime.now(timezone(timedelta(hours=8)))
    return beijing_time.date()

def dq_time():
    # 获取当前时间戳
    dqsj = int(time.time())

    # 将时间戳转换为可读的时间格式
    dysj = datetime.fromtimestamp(dqsj).strftime('%Y-%m-%d %H:%M:%S')
    #print("当前时间戳:", dqsj)
    #print("转换后的时间:", dysj)

    return dqsj, dysj

# 获取环境变量
def get_env_variable(var_name):
    value = os.getenv(var_name)
    if value is None:
        print(f'环境变量{var_name}未设置，请检查。')
        return None
    accounts = value.strip().split('\n')
    num_accounts = len(accounts)
    print(f'-----------本次账号运行数量：{num_accounts}-----------')
    print(f'----------项目：壹号联萌 -1.4----------')
    return accounts


#-------------------------------封装请求-------------


def create_headers():
    headers = {
        'Host': 'tdyhhy.gdlsls.com',
        'Connection': 'keep-alive',
        'Content-Length': '10',  
        'Charset': 'utf-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; ONEPLUS A6000 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160055 MMWEBSDK/20231201 MMWEBID/2695 MicroMessenger/8.0.45.2521(0x28002D3D) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        
    }
    return headers

#-------------------------------封装请求---完成----------

def ck(token):
    url = "https://tdyhhy.gdlsls.com/api/blessing/getreward/"
    headers = create_headers()
    params = {
        'application': 'app',
        'application_client_type': 'weixin',
        'token': token
    }
    data = json.dumps({"id": 1})

    while True:
        try:
            response = requests.post(url, headers=headers, params=params, data=data)
            response.raise_for_status()  # 主动抛出异常，如果状态码不是200
            response_json = response.json()
            #print(response_json)  # 如果需要每次循环都打印响应体，可以取消此行注释

            # 检查响应是否为"上限已达"消息
            if response_json.get('code') == -1 and response_json.get('msg') == '您今日获得神仙卡次数已达上限，请明日再参加~':
                print("已达上限，停止请求。")
                break

            # 成功获取奖品的情况
            if response_json.get('code') == 0 and 'data' in response_json:
                name = response_json['data'].get('name', '未知名称')
                if name == "福":  # 如果奖品名称是“福”
                    prize_type = response_json['data'].get('type', '未知类型')  #
                    print()  
                    print(f"福  奖品数量：{prize_type} 就给你看看，才不给你    ")
                    print()  
                    #print("操作成功且奖品名称为‘福’，完整响应体：")
                    #print(response_json)  # 打印完整响应体
                else:
                    print("操作成功！奖品名称：" + name)  # 如果奖品名称不是“福”，仅打印名称




        except requests.exceptions.HTTPError as http_err:
            print(f"发生HTTP错误: {http_err}")  # 明确地处理HTTP错误
        except requests.exceptions.RequestException as e:
            print(f"请求异常: {e}")  # 处理其他请求相关的异常

        # 不论成功或异常，均等待1-3秒
        time.sleep(random.randint(1, 3))

def xkkp(token):
    url = f"https://tdyhhy.gdlsls.com/api/blessing/mycard/?application=app&application_client_type=weixin&token={token}"
    headers = create_headers()
    data = json.dumps({})

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # 确保响应状态码是 200
        response_data = response.json()
        #print(response_data)  # 打印完整的响应体 JSON

        # 检查是否有 'data' 和 'blessing_data'
        if response_data.get('code') == 0 and 'data' in response_data and 'blessing_data' in response_data['data']:
            if response_data['data']['blessing_data']:
                for item in response_data['data']['blessing_data']:
                    name = item.get('name')
                    card_num = item.get('card_num')
                    print(f"卡: {name}, 数量: {card_num}")
            else:
                print("data 为空")
        else:
            print("响应中没有 data 或 blessing_data")

    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")


#本地测试用 

os.environ['yhlm11ck1111'] = '''


'''
import threading

def main1():  #线程版
    var_name = 'yhlmck'
    tokens = get_env_variable(var_name)
    if not tokens:
        print(f'环境变量{var_name}未设置，请检查。')
        return

    total_accounts = len(tokens)
    threads = []  # 用于存储所有线程的列表

    for i, token in enumerate(tokens):
        parts = token.split('#')
        if len(parts) < 1:
            print("令牌格式不正确。跳过处理。")
            continue

        token = parts[0]  # Token 值
        account_no = parts[1] if len(parts) > 1 else ""  # 备注信息
        #print(f'------账号 {i+1}/{total_accounts} {account_no} 抽奖-------')
        
        # 为每个账号创建一个线程，注意传递参数的方式需要是元组，即使只有一个参数
        t = threading.Thread(target=ck, args=(token,))
        t.start()  # 启动线程
        threads.append(t)

    # 等待所有线程完成
    for t in threads:
        t.join()


# 主函数
def main():   #多余
    var_name = 'yhlmck'
    tokens = get_env_variable(var_name)
    if not tokens:
        print(f'环境变量{var_name}未设置，请检查。')
        return

    total_accounts = len(tokens)
    for i, token in enumerate(tokens):
        parts = token.split('#')
        if len(parts) < 1:
            print("令牌格式不正确。跳过处理。")
            continue

        token = parts[0]  
        account_no = parts[1] if len(parts) > 1 else ""  
        print(f'------账号 {i+1}/{total_accounts} {account_no} 抽奖-------')
        ck(token)  
        #xkkp(token)

class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for file in self.files:
            file.write(obj)
            file.flush()  

    def flush(self):
        for file in self.files:
            file.flush()

def main2():    #发送通知版
    var_name = 'yhlmck'
    tokens = get_env_variable(var_name)  
    if not tokens:
        print(f'环境变量{var_name}未设置，请检查。')
        return

    captured_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = Tee(sys.stdout, captured_output)

    try:
        total_accounts = len(tokens)
        for i, token in enumerate(tokens):
            parts = token.split('#')
            if len(parts) < 1:
                print("令牌格式不正确。跳过处理。")
                continue

            token = parts[0]  
            account_no = parts[1] if len(parts) > 1 else ""  
            print(f'------账号 {i+1}/{total_accounts} {account_no} 查询-------')
            #ck(token)  
            xkkp(token)  
    finally:
    
        sys.stdout = original_stdout 
        output_content = captured_output.getvalue()  
        captured_output.close()

        # 如果需要发送通知
        if enable_notification == 1:
            send("壹号联萌", output_content)  
            print("通知已发送。")


if __name__ == "__main__":
    if USE_THREADS:
        main()
        main2()
    else:
        main1()
        main2()
        