"""
 * 设置变量 PGSH_TOKEN,多号使用&隔开，青龙直接新建变量即可 ，网页获取ck：https://bigostk.github.io/pg/
 * cron：0 30 11,14 * * *
"""

import requests
import time
import random
import string
import os
import hashlib
from datetime import datetime, timedelta

##############################

ck = ""  # 本地环境ck

#############################
# -----时间配置区，默认即可------

a = "0"
b = "13"
c = "14"
d = "16"

###########################

class PGSH:
    def __init__(self, cki):
        self.token = cki
        self.phone = None
        self.total_amount = 0
        self.hd = {
            'User-Agent': "okhttp/3.14.9",
            'Accept': 'application/json, text/plain, */*',
            'Version': "1.52.0",
            'Content-Type': "application/x-www-form-urlencoded",
            'Authorization': self.token,
            'channel': "android_app"
        }
        self.listUrl = 'https://userapi.qiekj.com/task/list'
        self.phone_url = 'https://userapi.qiekj.com/user/info'
        self.check_url = 'https://userapi.qiekj.com/user/balance'
        self.rcrw_url = 'https://userapi.qiekj.com/task/completed'
        self.sign_url = 'https://userapi.qiekj.com/signin/doUserSignIn'
        self.jrjf_url = "https://userapi.qiekj.com/integralRecord/pageList"
        self.dkbm_url = 'https://userapi.qiekj.com/markActivity/doApplyTask'
        self.dkbm_url1 = 'https://userapi.qiekj.com/markActivity/doMarkTask'
        self.shop_url = 'https://userapi.qiekj.com/integralUmp/rewardIntegral'
        self.jtjl_url = 'https://userapi.qiekj.com/ladderTask/applyLadderReward'
        self.dkbm_url2 = "https://userapi.qiekj.com/markActivity/markTaskReward"
        self.bmcodeurl = 'https://userapi.qiekj.com/markActivity/queryMarkTaskByStartTime'

    # 签名
    def sg(self, y):
        timestamp = str(int(time.time() * 1000))
        y = self.tqr(y)
        o = "android_app"
        p = "alipay"
        data = f"appSecret=xl8v4s/5qpBLvN+8CzFx7vVjy31NgXXcedU7G0QpOMM=&channel={o}&timestamp={timestamp}&token={self.token}&version=1.52.0&{y}"
        data1 = f"appSecret=xl8v4s/5qpBLvN+8CzFx7vVjy31NgXXcedU7G0QpOMM=&channel={p}&timestamp={timestamp}&token={self.token}&version=1.52.0&{y}"
        sign = hashlib.sha256(data.encode()).hexdigest()
        sign1 = hashlib.sha256(data1.encode()).hexdigest()
        return sign, sign1, timestamp

    # 提取参数
    def tqr(self, y):
        start = y.find('https://') + len('https://')
        end = y.find('/', start)
        return y[end:]

    # 检测token有效性
    def name(self):
        try:
            data = {'token': self.token}
            re = requests.post(self.phone_url, data=data, headers=self.hd).json()
            code = re['code']
            if code == 0:
                self.phone = re['data']['phone']
                sign, sign1, timestamp = self.sg(self.check_url)
                self.hd['sign'] = sign
                self.hd['timestamp'] = timestamp
                r = requests.post(self.check_url, data=data, headers=self.hd).json()
                coin_code = r['code']
                balance = r['data']['integral'] if coin_code == 0 else 'N/A'
                print(f"[{self.phone}] 登录成功！积分余额: {balance}")
                return self.phone
            else:
                msg = re["msg"]
                print(f"[账号{i + 1}]登录失败==> {msg}")
                return False
        except Exception as e:
            print(e)
            return False

    # 签到
    def sign(self):
        try:
            data = {'activityId': '600001', 'token': self.token}
            sign, sign1, timestamp = self.sg(self.sign_url)
            self.hd['sign'] = sign
            self.hd['timestamp'] = timestamp
            re = requests.post(self.sign_url, data=data, headers=self.hd).json()
            msg = re['msg']
            print(f"[{self.phone}] 签到==> {msg}")
        except Exception as e:
            print(e)

    # 浏览商品
    def shop(self):
        for t in range(5):
            try:
                b1 = string.ascii_lowercase + string.digits
                item_code = ''.join(random.choice(b1) for _ in range(6))
                data = {'itemCode': item_code, 'token': self.token}
                sign, sign1, timestamp = self.sg(self.shop_url)
                self.hd['sign'] = sign
                self.hd['timestamp'] = timestamp
                re = requests.post(self.shop_url, data=data, headers=self.hd).json()
                q = re["data"]
                if q is not None:
                    amount = re["data"]["rewardIntegral"]
                    print(f"[{self.phone}] 第{t + 1}次浏览商品成功,获得==> {amount}!")
                else:
                    print(f"[{self.phone}] 第{t + 1}次浏览商品失败==> {q}")
                    break
            except Exception as error:
                print(error)
            time.sleep(6)

    # 支付宝广告任务
    def zfbgg(self):
        for t in range(5):
            try:
                data = {'taskType': "9", 'token': self.token}
                sign, sign1, timestamp = self.sg(self.rcrw_url)
                self.hd['sign'] = sign1
                self.hd['timestamp'] = timestamp
                self.hd['channel'] = "alipay"
                response = requests.post(self.rcrw_url, data=data, headers=self.hd).json()
                msg = response["data"]
                if msg:
                    print(f"[{self.phone}] 第{t + 1}次支付宝广告==> {msg}")
                else:
                    print(f"[{self.phone}] 第{t + 1}次支付宝广告失败==> {msg}")
                    break
            except Exception as error:
                print(error)
            time.sleep(6)

    # 看视频赚积分
    def kspzjf(self):
        for t in range(5):
            try:
                data = {'taskType': "2", 'token': self.token}
                sign, sign1, timestamp = self.sg(self.rcrw_url)
                self.hd['sign'] = sign
                self.hd['timestamp'] = timestamp
                response = requests.post(self.rcrw_url, data=data, headers=self.hd).json()
                msg = response["data"]
                if msg:
                    print(f"[{self.phone}] 第{t + 1}次看视频赚积分==> {msg}")
                else:
                    print(f"[{self.phone}] 第{t + 1}次看视频赚积分失败==> {msg}")
                    break
            except Exception as error:
                print(error)
            time.sleep(6)

    # 看广告赚积分
    def kggzjf(self):
        for t in range(8):
            try:
                data = {'taskCode': '18893134-715b-4307-af1c-b5737c70f58d', 'token': self.token}
                sign, sign1, timestamp = self.sg(self.rcrw_url)
                self.hd['sign'] = sign
                self.hd['timestamp'] = timestamp
                res = requests.post(self.rcrw_url, data=data, headers=self.hd).json()
                msg = res['data']
                if msg:
                    print(f'[{self.phone}] 第{t + 1}次看广告赚积分==> {msg}')
                else:
                    print(f'[{self.phone}] 第{t + 1}次看广告赚积分失败==> {msg}')
                    break
            except Exception as e:
                print(e)
            time.sleep(6)

    # 隐藏任务
    def ycrw(self):
        for t in range(8):
            try:
                data = {'taskCode': '15eb1357-b2d9-442f-a19f-dbd9cdc996cb', 'token': self.token}
                sign, sign1, timestamp = self.sg(self.rcrw_url)
                self.hd['sign'] = sign
                self.hd['timestamp'] = timestamp
                re = requests.post(self.rcrw_url, data=data, headers=self.hd).json()
                msg = re['data']
                if msg:
                    print(f'[{self.phone}] 第{t + 1}次看广告赚积分==> {msg}')
                else:
                    print(f'[{self.phone}] 第{t + 1}次看广告赚积分失败==> {msg}')
                    break
            except Exception as e:
                print(e)
            time.sleep(6)

    # 遍历日常
    def rcrw(self):
        try:
            data = {'token': self.token}
            sign, sign1, timestamp = self.sg(self.listUrl)
            self.hd['sign'] = sign
            self.hd['timestamp'] = timestamp
            response = requests.post(self.listUrl, data=data, headers=self.hd).json()
            code = response['code']
            if code == 0:
                tasklist = []
                for item in response['data']['items']:
                    tasklist.append(item['taskCode'])
                for a1 in tasklist:
                    data = {'taskCode': a1, 'token': self.token}
                    sign, sign1, timestamp = self.sg(self.rcrw_url)
                    self.hd['sign'] = sign
                    self.hd['timestamp'] = timestamp
                    time.sleep(2)
                    response = requests.post(self.rcrw_url, data=data, headers=self.hd).json()
                    data1 = response["data"]
                    if data1:
                        print(f'[{self.phone}] 完成日常任务成功==> {data1}')
                    else:
                        print(f'[{self.phone}] 完成日常任务失败==> {data1}')
                    time.sleep(6)
            else:
                print("获取任务列表失败!")
        except Exception as e:
            print(e)

    # 打卡报名
    def dkbm(self):
        try:
            ti = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = {'startTime': ti, 'token': self.token}
            sign, sign1, timestamp = self.sg(self.bmcodeurl)
            self.hd['sign'] = sign
            self.hd['timestamp'] = timestamp
            r = requests.post(self.bmcodeurl, data=data, headers=self.hd).json()
            code = r['code']
            if code == 0:
                code1 = r['data']['taskCode']
                data = {'taskCode': code1, 'token': self.token}
                sign, sign1, timestamp = self.sg(self.dkbm_url)
                self.hd['sign'] = sign
                self.hd['timestamp'] = timestamp
                time.sleep(2)
                r1 = requests.post(self.dkbm_url, data=data, headers=self.hd).json()
                code2 = r1['code']
                data1 = r1["data"]
                msg = r1["msg"]
                if code2 == 0:
                    print(f"[{self.phone}] 打卡报名成功==> {data1}")
                else:
                    print(f"[{self.phone}] 打卡报名失败==> {msg}")
            else:
                print(f"获取code失败!{r}")
        except Exception as e:
            print(e)

    # 瓜分积分
    def gfjf(self):
        try:
            current_datetime = datetime.now()
            yesterday_datetime = current_datetime - timedelta(days=1)
            yesterday_now = yesterday_datetime.replace(hour=current_datetime.hour, minute=current_datetime.minute,
                                                       second=current_datetime.second,
                                                       microsecond=current_datetime.microsecond)
            k = yesterday_now.strftime("%Y-%m-%d %H:%M:%S")
            data = {"startTime": k, "token": self.token}
            sign, sign1, timestamp = self.sg(self.bmcodeurl)
            self.hd['sign'] = sign
            self.hd['timestamp'] = timestamp
            r = requests.post(self.bmcodeurl, headers=self.hd, data=data).json()
            if r['code'] == 0:
                code1 = r['data']['taskCode']
                data1 = {'taskCode': code1, 'token': self.token}
                sign, sign1, timestamp = self.sg(self.dkbm_url1)
                self.hd['sign'] = sign
                self.hd['timestamp'] = timestamp
                time.sleep(2)
                r1 = requests.post(self.dkbm_url1, headers=self.hd, data=data1).json()
                print(f"领取瓜分资格==> {r1['msg']}")
                return code1
            else:
                print(f"获取taskCode失败! {r}")
                return None
        except Exception as e:
            print(f"异常发生: {str(e)}")

    def gfjf1(self):
        try:
            aa = self.gfjf()
            data1 = {'taskCode': aa, 'token': self.token}
            sign, sign1, timestamp = self.sg(self.dkbm_url2)
            self.hd['sign'] = sign
            self.hd['timestamp'] = timestamp
            req = requests.post(self.dkbm_url2, headers=self.hd, data=data1).json()
            a1 = req["data"]
            if aa:
                print(f"[{self.phone}] 报名瓜分成功==> {a1}")
            else:
                print(f"[{self.phone}] 报名瓜分失败==> {req['msg']}")
        except Exception as e:
            print(f"异常发生: {str(e)}")

    # 今日积分
    def jrjf(self):
        try:
            data = {'token': self.token}
            sign, sign1, timestamp = self.sg(self.phone_url)
            self.hd['sign'] = sign
            self.hd['timestamp'] = timestamp
            r = requests.post(self.phone_url, data=data, headers=self.hd).json()
            if r['code'] == 0:
                phone = r['data']['phone']
                data = {
                    'page': (None, '1'),
                    'pageSize': (None, '100'),
                    'type': (None, '100'),
                    'receivedStatus': (None, '1'),
                    'token': (None, self.token),
                }
                hd = {
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; 23117RK66C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 AgentWeb/5.0.0 UCBrowser/11.6.4.950 com.qiekj.QEUser',
                    'Accept': 'application/json, text/plain, */*',
                    'channel': 'android_app',
                }
                re = requests.post(self.jrjf_url, headers=hd, files=data).json()
                current_date = datetime.now().strftime('%Y-%m-%d')
                for item in re['data']['items']:
                    received_date = item['receivedTime'][:10]
                    if received_date == current_date:
                        self.total_amount += item['amount']
                print(f"[{phone}]今日获得积分==> {self.total_amount}")
            else:
                print(f"[账号{i + 1}]登录失败==> {r['msg']}")
        except Exception as e:
            print(e)

    def start(self):
        a1 = self.name()
        if a1:
            now_time1 = datetime.now().hour
            if int(a) <= now_time1 <= int(b):
                print("-----开始执行签到-----")
                self.sign()
                time.sleep(6)
                print("-----开始执行看视频赚积分-----")
                self.kspzjf()
                time.sleep(6)
                print("-----开始执行看广告赚积分-----")
                self.kggzjf()
                time.sleep(6)
                print("-----开始执行浏览商品赚积分-----")
                self.shop()
                time.sleep(6)
                print("-----开始执行隐藏任务-----")
                self.ycrw()
                time.sleep(6)
                print("-----开始执行支付宝看视频赚积分-----")
                self.zfbgg()
                time.sleep(6)
                print("-----开始执行打卡报名-----")
                self.dkbm()
                time.sleep(6)
                print("-----开始执行领取瓜分资格-----")
                self.gfjf()
            else:
                print(f"当前时间非{int(a)}-{int(b)}，跳过今日任务")
            if int(c) <= now_time <= int(d):
                print("-----开始执行瓜分打卡积分-----")
                self.gfjf1()
            else:
                print(f"当前时间非{int(c)}-{int(d)}，跳过瓜分打卡积分")


if __name__ == '__main__':
    if 'PGSH_TOKEN' in os.environ:
        cookie = os.environ.get('PGSH_TOKEN')
    else:
        print("环境变量中不存在[PGSH_TOKEN],启用本地变量模式")
        cookie = ck
    if cookie == "":
        print("本地变量为空，请设置其中一个变量后再运行")
        exit(-1)
    cookies = cookie.split("&")
    print("QQ交流群：795406340")
    print(f"胖乖生活共获取到 {len(cookies)} 个账号")
    for i, ck in enumerate(cookies):
        print(f"======开始第{i + 1}个账号======")
        now_time = datetime.now().hour
        if int(a) <= now_time <= int(b):
            PGSH(ck).start()
        if int(c) <= now_time <= int(d):
            PGSH(ck).start()
        print("2s后进行下一个账号")
        time.sleep(2)
    time.sleep(2)
    print(f"======开始第查询所有号当日收益======")
    for i, ck in enumerate(cookies):
        PGSH(ck).jrjf()
        time.sleep(2)
