# -*- coding: utf-8 -*-
# 和包签到
# Author: kk
# date：2023/9/14 18:36
from random import randint
import time
import requests


class HBQD:
    """和包签到中心"""

    def __init__(self, ck):
        self.s = requests.session()
        self.cookie = ck
        self.s.cookies.update(self.cookie)
        self.s.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 hebao/9.14.58 NetType/wifi UnionPay/1.0 CMPAY'
        }

    def get_index(self):
        data = {"isClient": "0"}
        url = 'https://ump.cmpay.com/activities/v1/signAwardPoint/index'
        res = self.s.post(url, json=data).json()
        msg = res.get("msgInfo")
        if msg:
            print(msg)
            return False
        body = res.get('body')
        self.taskList = body.get('taskList')
        print([{i['taskName']:i['taskNo']} for i in self.taskList])
        return True

    def do_task(self):
        taskblacklist = ['TASK199504','TASK623379']   # 加入     
        for task in self.taskList:
            taskNo = task.get('taskNo')
            taskStatus = task.get('taskStatus')
            taskName = task.get('taskName')
            if taskStatus == '2':
                print(f'{taskName}：任务已完成')
            elif taskNo not in taskblacklist and taskStatus != '2':
                data = {'taskNo': taskNo,'opDfp':self.cookie['BSFIT_DEVICEID']}
                taskurl = 'https://ump.cmpay.com/activities/v1/signAwardPoint/finishTask'
                self.s.post(taskurl,json={**data,**{'checkSign':''}})
                t = randint(5, 10)
                time.sleep(t)
                url = 'https://ump.cmpay.com/activities/v1/signAwardPoint/awardFinishTask'
                res = self.s.post(url, json=data).json()
                # print(res)
                if not res.get('msgInfo'):
                    print(f'任务【{res.get("taskName")}】已完成')
                time.sleep(2)

    def run(self):
        if self.get_index():
            self.do_task()


if __name__ == '__main__':
    ck = {'act_sid': '',  'BSFIT_DEVICEID': ''} 
    # 进入和包签到页面之后再开启抓包，cookie里找这两项。每月一次，运行前需进入签到页面激活ck。
    hb = HBQD(ck)
    hb.run()
