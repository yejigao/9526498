#抓这个ecustomer.cntaiping.com域名下的x-ac-token-ticket
#备注名&x-ac-token-ticket 多账号换行

ck = """
      备注名&x-ac-token-ticket
	 """ 
     
import time
import os
import random
import requests
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


l = ['121', '120', '169', '66']

p = {
    '121': '10元E卡',
    '120': '5元E卡',
    '169': '2元E卡',
    '66': '1元E卡',
}


class TPT:
    def __init__(self):
        self.accounts_list = ck.strip().split('\n')
        self.num_of_accounts = len(self.accounts_list)
        print(f'NONE益达,共找到{self.num_of_accounts}个账号,开始运行\n')

    def run(self):
        with ThreadPoolExecutor() as executor:
            futures = []
            for i, account in enumerate(self.accounts_list, start=1):
                name, ck = account.split('&')
                future = executor.submit(self.process_account, i, name, ck)
                futures.append(future)

            for future in as_completed(futures):
                result = future.result()
                print(result)

    def process_account(self, i, name, ck):
        self.headers = {
            'Host': 'ecustomer.cntaiping.com',
            'Accept': 'application/json;charset=UTF-8',
            'x-ac-token-ticket': ck,
            'x-ac-channel-id': 'KHT',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': 'https://ecustomercdn.itaiping.com',
            'Content-Length': '39',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/77777;yuangongejia#ios#kehutong#CZBIOS',
            'Referer': 'https://ecustomercdn.itaiping.com/',
            'x-ac-mc-type': 'gateway.user',
            'Connection': 'keep-alive'
        }
        result = f"==============开始执行账号{i}==============\n"
        result += self.login(name, ck)
        result += f"==============运行结束==============\n"
        return result

    def login(self, name, ck):
        Surl = "https://ecustomer.cntaiping.com/campaignsms/couponAndsign"
        _S = {}
        result = f"==============每日签到==============\n"
        response = requests.post(Surl, headers=self.headers, json=_S)
        s = response.json()
        if s['success'] == True:
            message = s['data']['dailySignRsp']['message']
            integralSend = s['data']['dailySignRsp']['integralSend']
            self.integral = s['data']['dailySignRsp']['integral']
            result += f"签到-{message}[{integralSend}]-当前有{self.integral}金币\n"
        else:
            result += f"签到失败,{s['msg']}\n"
        for m in l:
            Qurl = "https://ecustomer.cntaiping.com/campaignsms/coin/exchange/receive"
            _Q = {
                'id': m,
                'appVersion':'3.4.8',
            }
            response = requests.post(Qurl, headers=self.headers, json=_Q)
            q = response.json()
            if q['success'] == True:
                couponId = q['data']['couponId']
                result += f"{name}:{p[m]}兑换成功-{b}\n"
            else:
                result += f"{name}:{p[m]}兑换失败,{q['msg']}\n"
        return result


tpt = TPT()
tpt.run()