"""
变量名 fxshCK     &隔开多个号，格式：备注#token#did
微信注册地址：https://m.fenxianglife3.com/h5-official/appPages/general/ttl-withdraw/index.html?unionId=oqICk1KNcEE0x8ngbKauBN5uuS9g#/share
注册好后下载app
"""

import hashlib
import os
import random
import time
import requests

ck = '' ## 本地ck，&隔开


def random_string(length):
    characters = "1234567890abcdef"
    return ''.join(random.choices(characters, k=length))


def random_num(length):
    characters = "1234567890"
    return ''.join(random.choices(characters, k=length))


class FXSH:
    def __init__(self, ck):
        self.name = ck.split('#')[0]
        self.token = ck.split('#')[1]
        self.did = ck.split('#')[2]
        self.body = None
        self.finger = random_string(32)
        self.noncestr = None
        self.oaid = random_string(16)
        self.timestamp = None
        self.sign = None
        self.traceid = None
        self.rwname = None
        self.rwid = None
        self.headers = {
            'Host': "fenxiang-lottery-api.fenxianglife.com",
            'User-Agent': "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 AgentWeb/5.0.0  UCBrowser/11.6.4.950",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/json",
            'timestamp': '',
            'traceid': '',
            'finger': f'{self.finger}',
            'did': f'{self.did}',
            'oaid': f'{self.oaid}',
            'noncestr': '',
            'platform': "h5",
            'token': f'{self.token}',
            'sign': '',
            'version': "1.0.0",
            'origin': "https://m.fenxianglife.com",
            'x-requested-with': "com.n_add.android",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }

    def get_headers(self):
        self.timestamp = f'{int(time.time() * 1000)}'
        self.headers['timestamp'] = self.timestamp
        self.noncestr = f'{random.randint(1, 9)}{random_num(7)}'
        self.headers['noncestr'] = self.noncestr
        self.traceid = f'{random_string(32)}'
        self.headers['traceid'] = self.traceid

        s = f'{self.body}did={self.did}&finger={self.finger}&noncestr={self.noncestr}&oaid={self.oaid}&platform=h5&timestamp={self.timestamp}&token={self.token}&traceid={self.traceid}&version=1.0.0粉象好牛逼a8c19d8267527ea4c7d2f011acf7766f'
        md5 = hashlib.md5()
        md5.update(s.encode('utf-8'))
        encrypted_str = md5.hexdigest()
        self.headers['sign'] = f'{encrypted_str}'

        return self.headers

    def reward(self):
        try:
            self.body = ''
            headers = self.get_headers()
            r = requests.post(
                "https://fenxiang-lottery-api.fenxianglife.com/fenxiang-lottery/user/sign/reward",
                json={},
                headers=headers
            )
            success = r.json().get('success', None)
            message = r.json().get('message', None)
            if success:
                codes = r.json()['data']['codes']
                print(f'{self.name}-签到成功!奖码:{codes}')
            else:
                print(f'{self.name}-{message}')

        except Exception as e:
            print(f'{self.name}-签到异常: {e}')
            return False

    def get_rwinfo(self):
        try:
            self.body = 'plateform=android&version=5.4.2'
            headers = self.get_headers()
            r = requests.post(
                "https://fenxiang-lottery-api.fenxianglife.com/fenxiang-lottery/home/data/V2",
                json={
                    "plateform": "android",
                    "version": "5.4.2"
                },
                headers=headers
            )
            success = r.json().get('success', None)
            message = r.json().get('message', None)
            if success:
                jms_list = []
                jms = r.json()['data']['openLotteryModule']['now']['rewardCodes']
                for jm in jms:
                    jms_list.append(jm['code'])
                print(f'{self.name}-奖码({len(jms_list)}个):{jms_list}')
                rws = r.json()['data']['taskModule']['taskResult']
                for rw in rws:
                    # print(rw)
                    # print()
                    self.rwname = rw['title']
                    self.rwid = rw['id']
                    if self.rwid in [21, 48, 10]:
                        print(f'去完成: {self.rwname}-{self.rwid}')
                        self.finish()
                        time.sleep(5)

            else:
                print(f'{self.name}-{message}')

        except Exception as e:
            print(f'{self.name}-签到异常: {e}')
            return False

    def finish(self):
        try:
            self.body = f'taskId={self.rwid}'
            headers = self.get_headers()
            r = requests.post(
                "https://fenxiang-lottery-api.fenxianglife.com/fenxiang-lottery/lotteryCode/task/finish",
                json={
                    "taskId": self.rwid
                },
                headers=headers
            )
            print(r.json())
            success = r.json().get('success', None)
            message = r.json().get('message', None)
            if success:
                print(f'{self.name}-{self.rwname}-完成成功!')
            else:
                print(f'{self.name}-{self.rwname}-{message}')

        except Exception as e:
            print(f'{self.name}-{self.rwname}: {e}')
            return False

    def main(self):
        self.reward()
        self.get_rwinfo()

        # self.finish()


if __name__ == '__main__':
    if 'fxshCK' in os.environ:
        cookie = os.environ.get('fxshCK')
    else:
        print("环境变量中不存在[fxshCK],启用本地变量模式")
        cookie = ck
    if cookie == "":
        print("本地变量为空，请设置其中一个变量后再运行")
        exit(-1)
    cookies = cookie.split("&")
    print(f"粉象生活共获取到 {len(cookies)} 个账号")
    for i, ck in enumerate(cookies):
        print(f"======开始第{i + 1}个账号======")
        FXSH(ck).main()
        time.sleep(2)
