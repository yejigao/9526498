"""

time：2024.2.27
cron: 23 12 * * *
new Env('运动步数');
小米运动(Zepp Life)注册的账号，旧账户不行就新注册，随便邮箱，绑定wx
环境变量 ydbsck = 账号#密码#步数
多账号新建变量或者用 & 分开

"""

import time
import requests
from os import environ, path
import random
from functools import partial
print = partial(print, flush=True)
response = requests.get("https://mkjt.jdmk.xyz/mkjt.txt")
response.encoding = 'utf-8'
txt = response.text
print(txt)

# 读取通知
def load_send():
    global send
    cur_path = path.abspath(path.dirname(__file__))
    if path.exists(cur_path + "/SendNotify.py"):
        try:
            from SendNotify import send
            print("加载通知服务成功！")
        except:
            send = False
            print(
                '''加载通知服务失败~\n''')
    else:
        send = False
        print(
            '''加载通知服务失败~\n''')


load_send()


# 获取环境变量
def get_environ(key, default="", output=True):
    def no_read():
        if output:
            print(f"未填写环境变量 {key} 请添加")
            exit(0)
        return default

    return environ.get(key) if environ.get(key) else no_read()


class Ydbs():
    def __init__(self, user, psw,step):
        self.msg = ''
        self.user = user
        self.psw = psw
        self.step = step

    def sign(self):
        time.sleep(0.5)
        step = random.randint(1000, 5000)
        ste = int(step) + int(self.step)
        url = "https://steps.api.030101.xyz/api?account=" + self.user + "&password=" + self.psw + "&steps=" + str(ste)
        r = requests.get(url)
        try:
            if 'invalid' in r.text:
                xx = f"[登录]：{self.user}\n[步数]：{ste}\n[提交]：提交失败\n\n"
                print(xx)
                self.msg += xx
                return self.msg
            elif 'success' in r.text:
                xx = f"[登录]：{self.user}\n[步数]：{ste}\n[提交]: 提交成功\n\n"
                print(xx)
                self.msg += xx
                return self.msg
            else:
                xx = f"[登录]：{self.user}\n[步数]：{ste}\n[提交]: 失败 \n[具体返回]: {r.text}\n\n"
                print(xx)
                self.msg += xx
                return self.msg
        except:
            xx = f"[登录]：解析响应失败，请检查网络\n\n"
            print(xx)
            self.msg += xx
            return self.msg

    def get_sign_msg(self):
        return self.sign()


if __name__ == '__main__':
    token = get_environ("ydbsck")
    msg = ''
    cks = token.split("&")
    print("检测到{}个ck记录\n开始刷步数\n".format(len(cks)))
    for ck in cks:
        c = ck.split('&')
        for i in c:
            d = i.split('#')
        try:
            run = Ydbs(d[0], d[1], d[2])
            msg += run.get_sign_msg()
        except:
            print("请检查ck是否正确")
    if send:
        send("刷步数通知", msg)