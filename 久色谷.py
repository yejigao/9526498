"""
变量： jiusegu
变量名： key   (在URL里面)
https://www.jiusegu.ink/cmobile/index.php?app=usercenter&mod=gerUserPointsInfo&key=d775342353gwsd2e651bfb2d9cc&pn=1&page=10

例如 export  jiusegu='d775342353gwsd2e651bfb2d9cc#备注
多账号   换行/回车   
脚本作者: QGh3amllamll  
版本 1.0
------更新记录----  
1.0 测试版


"""
import os
import requests
from datetime import datetime, timezone, timedelta
import json
import time
import io
import sys
import requests
import base64

import random  # 导入random模块以生成随机暂停时间
enable_notification = 0   #0不发送通知   1发送通知


# 只有在需要发送通知时才尝试导入notify模块
if enable_notification == 1:
    try:
        from notify import send
    except ModuleNotFoundError:
        print("警告：未找到notify.py模块。它不是一个依赖项，请勿错误安装。程序将退出。")
        sys.exit(1)

#---------简化的框架 0.7 带通知--------

jbxmmz = "久色谷"
jbxmbb = "1.0"


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

def log(message):
    print(message)

def print_disclaimer():
    log("📢 请认真阅读以下声明")
    log("      【免责声明】         ")
    log("✨ 脚本及其中涉及的任何解密分析程序，仅用于测试和学习研究")
    log("✨ 禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断")
    log("✨ 禁止任何公众号、自媒体进行任何形式的转载、发布")
    log("✨ 本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害")
    log("✨ 脚本文件请在下载试用后24小时内自行删除")
    log("✨ 脚本文件如有不慎被破解或修改由破解或修改者承担")
    log("✨ 如不接受此条款请立即删除脚本文件")
    log("" * 10)
    log("如果喜欢请打赏支持维护和开发    更要钱动力 来 更新/维护脚本")
    log("" * 10)
    log(f'这个是怎么东西？？？')
    log(f'U2FsdGVkX1/F371b27nTzUeMknDFjABXyQBHINWvVPRkUVoUe6ZdZ508DVGF7dMc')
    log("" * 10)
    log("" * 10)
    log(f'-----------{jbxmmz} {jbxmbb}-----------')


# 获取环境变量
def get_env_variable(var_name):
    value = os.getenv(var_name)
    if value is None:
        print(f'环境变量{var_name}未设置，请检查。')
        return None
    accounts = value.strip().split('\n')
    num_accounts = len(accounts)
    print(f'-----------本次账号运行数量：{num_accounts}-----------')
   
    print_disclaimer()
    return accounts


#-------------------------------封装请求-------------


def create_headers():
    headers = {
        'host': 'www.jiusegu.ink',
        #'content-length': '36',
        'xweb_xhr': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9079',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://servicewechat.com/wxe05157d66f98e7ee/17/page-frame.html',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    return headers


#-------------------------------封装请求---完成----------

def sign_in(token):
    url = "https://www.jiusegu.ink/cmobile/index.php?app=usercenter&mod=checkInAction"
    data = {"key": token}  # 定义表单数据
    #print(data)
    headers = create_headers()  # 调用headers生成函数


    try:
        response = requests.post(url, headers=headers, data=data)  # 使用data参数发送表单数据
        response.raise_for_status()  # 确保请求成功
        print("签到成功：", response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP错误：{http_err}")
    except Exception as err:
        print(f"请求异常：{err}")


def jf(token):
    url = f"https://www.jiusegu.ink/cmobile/index.php?app=usercenter&mod=getUserInfoNum&key={token}&fields=point"
    headers = create_headers()  # 调用函数生成头部信息
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 对于错误响应抛出HTTPError
        data = response.json()
        
        if data.get('code') == 200:  # 确保使用正确的状态码
            user_info = data['datas']['member_info']  # 直接访问用户信息
            #print("请求成功：")
            print(f"用户名: {user_info['user_name']}, 积分: {user_info['point']}, 余额: {user_info['predepoit']}")
        else:
            print("请求失败，完整的响应内容如下：")
            print(data)

    except requests.exceptions.HTTPError as http_err:
        print(f"发生HTTP错误：{http_err}")  # 打印HTTP错误
    except Exception as err:
        print(f"发生错误：{err}")  # 打印其他错误

def sign_in1(cookie):
    url = "xxxx"
    create_headers()
    try:
        response = requests.post(url, headers=headers, json={})
        response.raise_for_status()  # 确保请求成功
        print("签到成功：", response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP错误：{http_err}")
    except Exception as err:
        print(f"请求异常：{err}")


#本地测试用 
os.environ['cscs'] = '''

'''




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

def send_notification(enable, content):
    if enable:
        try:
            send(f"{jbxmmz}  {jbxmbb}版", content)  # 尝试发送通知
            print("通知已发送。输出内容为：")
            #print(content)
        except NameError:
            print("通知发送失败，send函数未定义。")

def main():
    var_name = 'jiusegu'
    tokens = get_env_variable(var_name)
    if not tokens:
        print(f'环境变量{var_name}未设置，请检查。')
        return

    captured_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = Tee(sys.stdout, captured_output)

    total_accounts = len(tokens)

    for i, token in enumerate(tokens):
        parts = token.split('#')
        if len(parts) < 1:
            print("令牌格式不正确。跳过处理。")
            continue

        token = parts[0]
        #unionid = parts[1]
        account_no = parts[1] if len(parts) > 1 else ""  # 备注信息
        account_info = f" {account_no}" if account_no else ""  # 如果有备注信息，则附加到账号信息中
        print(f'------账号 {i+1}/{total_accounts} {account_info} -------')

        sign_in(token)
        jf(token)

    sys.stdout = original_stdout
    output_content = captured_output.getvalue()
    captured_output.close()

    # 封装后的发送通知逻辑
    send_notification(enable_notification, output_content)

if __name__ == "__main__":
    main()