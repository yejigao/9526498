# 美美日历
#AppStore下载抓https://apimmrl.xiaoqiezia.cn下的authorization, device, model, brand, user_agent, osversion参数，用&符号连接，多账号用@隔开

import requests
import time
import random
from bs4 import BeautifulSoup
import re
import os
from datetime import datetime

cookies = os.getenv('mmrl_ck')
#cookies = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaW1tcmwueGlhb3FpZXppYS5jbi9lYXJuL21laW1laXJpbGkvdjEvdXNlci93eExvZ2luIiwiaWF0IjoxNzE4MjU1NDE0LCJleHAiOjI5Mjc4NTU0MTQsIm5iZiI6MTcxODI1NTQxNCwianRpIjoiVHg4VkI3R3pIdFhQTllJcCIsInN1YiI6Mzg4NjI0MCwicHJ2IjoiODY2NWFlOTc3NWNmMjZmNmI4ZTQ5NmY4NmZhNTM2ZDY4ZGQ3MTgxOCJ9.6U-kw4dxFPlI9csX8n-s1kmFQzhJULdSMz4tneZibUE&9AD441A0-18F2-4D18-B0D7-BDC7B04FDB54&CA8E0A5E-A637-4A7B-9EE7-54D594F08705&iPhone15,2&D73AP&DBCalendar/1.2.7 (com.whay.mmrl; build:17; iOS 17.4.1) Alamofire/5.8.0&17.4.1@Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaW1tcmwueGlhb3FpZXppYS5jbi9lYXJuL21laW1laXJpbGkvdjEvdXNlci93eExvZ2luIiwiaWF0IjoxNzE4Mjg5Nzg5LCJleHAiOjI5Mjc4ODk3ODksIm5iZiI6MTcxODI4OTc4OSwianRpIjoicGwxWlAyMVNKVnhsb1BJdyIsInN1YiI6Mzg4NjgxNCwicHJ2IjoiODY2NWFlOTc3NWNmMjZmNmI4ZTQ5NmY4NmZhNTM2ZDY4ZGQ3MTgxOCJ9.-M0EiKjSfccJO9WXhddUFtTQiLf4gIksMbXbgiGH4mU&4B9DAB7E-5DDB-4EE7-A17F-0B920E72C605&2315C53F-F099-4C71-B046-8A2C080CC937&iPad5,3&J81AP&DBCalendar/1.2.7 (com.whay.mmrl; build:17; iOS 15.7.7) Alamofire/5.8.0&15.7.7'


class InvalidURLException(Exception):
    pass


class User:

    def __init__(self, authorization, idfa, device, model, brand, user_agent, osversion):
        self.url = "https://apimmrl.xiaoqiezia.cn"
        self.Authorization = authorization
        self.idfa = idfa
        self.device = device
        self.model = model
        self.brand = brand
        self.user_agent = user_agent
        self.osversion = osversion
        self.header = {
            "Host": "apimmrl.xiaoqiezia.cn",
            "version": "17",
            "Authorization": f'{self.Authorization}',
            "idfa": f'{self.idfa}',
            "Accept": "*/*",
            "release": "1.2.7",
            "brand": f'{self.brand}',
            "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
            "Accept-Language": "zh-Hans-CN;q=1.0, en-CN;q=0.9",
            "store": "appstore",
            "platform": "2",
            "User-Agent": f'{self.user_agent}',
            "Connection": "keep-alive",
            "device": f'{self.device}',
            "model": f'{self.model}',
            "osversion": f'{self.osversion}'
        }
        ##气泡红包90分钟一秒10次上限好像

    def bubble(self):
        print(f'=========等待几秒钟开始执行气泡红包=========')
        time.sleep(random.randint(5, 10))
        for i in range(5):
            r1 = requests.get(f'{self.url}/earn/meimeirili/v1/system/actionBubble', headers=self.header).json()
            r2 = requests.get(f'{self.url}/earn/meimeirili/v1/system/actionBubble2', headers=self.header).json()
            if r1['result']['status'] == 0:
                print('明天再领，今天已达上限。')
                break
            else:
                if r1['result']['interval'] == 0 and r2['result']['interval'] == 0:
                    r = requests.post(f'{self.url}/earn/meimeirili/v1/system/actionBubble', headers=self.header).json()
                    if r['code'] == 0:
                        print(f"获得{r['result']['coin']}金币/获得{r['result']['coupon']}提现券")
                    elif r['code'] == 40302:
                        print('气泡红包时间未到')
                    elif r['code'] == 40301:
                        print('气泡红包已达上限')
                        break
                    else:
                        print(r['message'])
                else:
                    print('时间未到')
                    break
                sleep_time = random.randint(91, 120)
                print(f"等待{sleep_time}秒,执行下一次气泡红包。")
                time.sleep(sleep_time)

    def big_coin(self):
        print(f'=========等待几秒钟开始执行幸运红包=========')
        time.sleep(random.randint(5, 10))
        for i in range(4):
            r1 = requests.get(f'{self.url}/earn/meimeirili/v1/rewardCoinBig', headers=self.header).json()
            if r1['result']['status'] == 0:
                print('明天再领，今天已达上限。')
                break
            else:
                if r1['result']['interval'] == 0:
                    r = requests.post(f'{self.url}/earn/meimeirili/v1/rewardCoinBig', headers=self.header).json()
                    if r['code'] == 0:
                        print(f"获得{r['result']['coin']}金币")
                    elif r['code'] == 40302:
                        print('幸运红包已达上限')
                    elif r['code'] == 40301:
                        print('您操作太快了')
                    else:
                        print(r['message'])
                else:
                    print('时间未到。请等会儿再来')
                    break
                sleep_time = random.randint(91, 120)
                print(f"等待{sleep_time}秒，执行下一次幸运红包。")
                time.sleep(sleep_time)

    def rain(self):
        print(f'=========执行红包雨=========')
        r1 = requests.get(f"{self.url}/earn/meimeirili/v1/system/actionRain", headers=self.header).json()
        if r1['result']['red_e_count'] == 0:
            print('今日红包雨已达上限')
        elif r1['result']['red_e_time'] > 0:
            print('红包雨时间未到')
        elif r1['result']['red_e_count'] != 0 and r1['result']['red_e_time'] == 0:
            print('现在开始执行红包雨')
            r = requests.post(f"{self.url}/earn/meimeirili/v1/system/actionRain?", headers=self.header).json()
            if r['code'] == 0:
                print(f"获得{r['result']['coin']}金币/获得{r['result']['coupon']}提现券")
            elif r['code'] == 40302:
                print('红包雨时间未到')
            elif r["code"] == 40301:
                print(f"红包雨出错，{r['message']}")
            else:
                print(r['message'])
        else:
            print('未知错误')

    def barrier(self):
        print(f'=========等待几秒钟开始闯关=========')
        time.sleep(random.randint(40, 50))
        r1 = requests.get(f'{self.url}/earn/meimeirili/v1/system/rewardBarrierIndex', headers=self.header).json()
        barrier_position = r1['result']['barrier']
        task_num = 0
        task_start = 0
        for i in range(len(barrier_position)):
            if barrier_position[i]['state'] == 0:
                task_num = 7 - i
                task_start = i
                break
        for j in range(task_num):
            task_start = task_start + 1
            r = requests.post(f'{self.url}/earn/meimeirili/v1/system/rewardBarrierIndex?no={task_start}',
                              headers=self.header).json()
            if r['code'] == 0:
                print(
                    f"第{task_start}次闯关获得{r['result']['coin']}金币/获得{r['result']['coupon']}提现券/获得iPhone14碎片{r['result']['fragment']}")
                sleep_time = random.randint(35, 50)
                print(f"等待{sleep_time}秒执行下一次闯关")
                time.sleep(sleep_time)
            elif r['code'] == 40301:
                print(f"闯关出错，{r['message']}")
                break
            else:
                print(f"闯关出错{r['message']}")
                break

    def watchAD(self, task_num):
        print(f"🎉️=========看广告视频任务：{task_num}次=========")
        for i in range(task_num):
            r = requests.post(f"{self.url}/earn/meimeirili/v1/system/zhuanVideo?", headers=self.header).json()
            if r['result']['ticket'] is not None:
                ticket = r['result']['ticket']
                url = f'{self.url}/earn/meimeirili/v1/system/actionCompleted?channel=2&class=10000&ecpm=8074.00&platformname=2541&ticket=' + ticket + '&tid=38862401718287872&transid=F4FDD39D-B6A4-48E0-9225-F2834875DC56&type=9'
                res = requests.get(url, headers=self.header).json()
                if res['code'] == 0:
                    print(f"第{i + 1}次看广告获得{res['result']['reward']}金币/获得{res['result']['coupon']}提现券")
                    sleep_time = random.randint(35, 50)
                    print(f"等待{sleep_time}秒")
                    time.sleep(sleep_time)
                else:
                    print(res['message'])
                    break
            else:
                print(r['message'])
                break

    def watchVideo(self, task_num):
        print(f'=========刷视频{task_num}次=========')
        for i in range(task_num):
            r = requests.get(f"{self.url}/earn/meimeirili/v1/system/videoCoin?short=0&", headers=self.header).json()
            if r['result']['ticket'] is not None:
                ticket = r['result']['ticket']
                url = f"{self.url}/earn/meimeirili/v1/system/videoCoin?ticket=" + ticket + "&short=0&"
                res = requests.get(url, headers=self.header).json()
                if res['code'] == 0:
                    print(f"第{i + 1}次刷视频获得{res['result']['reward']}金币")
                    sleep_time = random.randint(35, 50)
                    print(f"等待{sleep_time}秒")
                    time.sleep(sleep_time)
                else:
                    print(res['message'])
                    break
            else:
                print(r['message'])
                break

    def watchNews(self, task_num):
        print(f'=========刷资讯{task_num}次=========')
        for i in range(task_num):
            r0 = requests.get(f"{self.url}/earn/meimeirili/v1/system/newsCoin?v=1", headers=self.header).json()
            r = requests.get(f"{self.url}/earn/meimeirili/v1/system/newsCoin", headers=self.header).json()
            if r['result']['ticket'] is not None:
                ticket = r['result']['ticket']
                r2 = requests.get(f"{self.url}/earn/meimeirili/v1/system/newsCost", headers=self.header).json()
                url = f"{self.url}/earn/meimeirili/v1/system/newsCoin?ticket=" + ticket
                res = requests.get(url, headers=self.header).json()
                if res['code'] == 0:
                    print(
                        f"今日已看资讯{res['result']['today_news_total']}次,第{i + 1}次刷资讯获得{res['result']['reward']}金币")
                    r3 = requests.get(f"{self.url}/earn/meimeirili/v1/system/newsCost?end=1",
                                      headers=self.header).json()
                    sleep_time = random.randint(15, 30)
                    print(f"等待{sleep_time}秒")
                    time.sleep(sleep_time)
                else:
                    print(res['success'])
                    break
            else:
                print("出错啦！")
                break

    def videoDown(self, task_num):
        print(f'=========执行大额奖励任务{task_num}次=========')
        for i in range(task_num):
            r0 = requests.get(f"{self.url}/earn/meimeirili/v1/system/videoDownIndex?id=6", headers=self.header).json()
            r6 = requests.get(f"{self.url}/earn/meimeirili/v1/system/actionLoad?channel=2&class=10000&minor=2&rid=&type=11", headers=self.header).json()
            r7 = requests.get(f"{self.url}/earn/meimeirili/v1/system/actionShowed??channel=2&class=10000&ecpm=7000.00&platformname=pangle&tid={r6['result']['tid']}&type=11", headers=self.header).json()
            r8 = requests.get(
                f"{self.url}/earn/meimeirili/v1/system/actionClicked?channel=2&class=10000&ecpm=7000.00&platformname=pangle&tid={r6['result']['tid']}&type=11",
                headers=self.header).json()

            time.sleep(random.randint(8, 10))
            r = requests.get(f"{self.url}/earn/meimeirili/v1/system/videoDownClick?id=6", headers=self.header).json()
            if r['result']['ticket'] is not None:
                sleep_time = random.randint(120, 150)
                print(f"等待{sleep_time}秒再返回领取奖励")
                time.sleep(sleep_time)
                ticket = r['result']['ticket']
                url = f"{self.url}/earn/meimeirili/v1/system/videoDownIndex?id=6&ticket=" + ticket
                res = requests.post(url, headers=self.header).json()
                if res['success']:
                    print(
                        f"大额任务奖励获得金币{res['result']['coin']}/获得提现券{res['result']['coupon']}")
                    sleep_time = random.randint(15, 30)
                    print(f"等待{sleep_time}秒")
                    time.sleep(sleep_time)
                else:
                    print(f"领取失败了，{res['success']}")
                    break
            else:
                print("出错啦！")
                break

    def receive(self, id):
        print(f'=========领取任务奖励=========')
        r = requests.post(f'{self.url}/earn/meimeirili/v1/system/zhuanDone?id={id}', headers=self.header,
                          data={"id": id}).json()
        if not r['success']:
            print(f"任务奖励领取失败，原因{r['message']}")
        else:
            print(f"任务奖励{r['result']['message']},获得金币{r['result']['coin']}/获得提现券{r['result']['coupon']}")

    def info(self):
        r = requests.get(f'{self.url}/earn/meimeirili/v1/user/profile?debug=0', headers=self.header).json()
        if not r['success']:
            print(f'🔛出错了，请检查')
        else:
            print(
                f"🆗账号:{r['result']['nickname']}-当前余额{r['result']['balance']}元-提现券{r['result']['ticket']}张\n今日已赚{r['result']['today_point']}金币-再凑{200 - r['result']['fragment']}碎片召唤iPhone14")

    def signin(self):
        r = requests.post(f'{self.url}/earn/meimeirili/v1/system/rewardSign', headers=self.header).json()
        if not r['success']:
            print(f"🔛出错了，{r['message']}")
        else:
            print(f"签到成功，获得金币{r['result']['coin']}/获得提现券{r['result']['coupon']}")

    def exchange(self):
        r = requests.get(f'{self.url}/earn/meimeirili/v1/system/exchangeLogs?page=1&per_page=25',
                         headers=self.header).json()
        if r['result']:
            date = r['result']['data']['data'][0]['time']
            now = datetime.now()
            time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            if now.year == time.year and now.month == time.month and now.day == time.day:
                print("当天已提过现")
            else:
                self.cashExchange()
        else:
            print("暂无提现记录")
            self.cashExchange()

    def cashExchange(self):
        r1 = requests.get(f'{self.url}/earn/meimeirili/v1/user/profile?debug=0', headers=self.header).json()
        ticket = int(r1['result']['ticket'])
        cash = int(r1['result']['balance'].split('.')[0])
        if ticket > 4000 and cash >= 5:
            print("准备提现5元")
            r2 = requests.post(f"{self.url}/earn/meimeirili/v1/system/cashExchange?amount=5&gate=wechat",
                               headers=self.header).json()
            print(r2['message'])
        elif ticket > 1000 and cash >= 1:
            print("准备提现1元")
            r2 = requests.post(f"{self.url}/earn/meimeirili/v1/system/cashExchange?amount=1&gate=wechat",
                               headers=self.header).json()
            print(r2['success'])
        else:
            print("条件不足，未提现")

    def lottery(self, task_num):
        print(f'=========抽奖{task_num}次=========')
        for i in range(task_num):
            r = requests.get(f"{self.url}/earn/meimeirili/v1/system/lotteryIndex", headers=self.header).json()
            if r['result']['ticket'] is not None:
                ticket = r['result']['ticket']
                url = f"{self.url}/earn/meimeirili/v1/system/lotteryIndex?ticket=" + ticket
                res = requests.post(url, headers=self.header).json()
                if res['success']:
                    print("抽奖成功，奖品未知")
                    sleep_time = random.randint(15, 30)
                    print(f"等待{sleep_time}秒")
                    time.sleep(sleep_time)
                else:
                    print(res['success'])
                    break
            else:
                print("出错啦！")
                break

    def run(self):
        self.info()
        time.sleep(2)
        self.rain()

        r1 = requests.get(f'{self.url}/earn/meimeirili/v1/system/rewardBarrierIndex', headers=self.header).json()
        barrier_num = r1['result']['current_barrier']
        if barrier_num < 7:
            print(f'今日已执行闯关任务{barrier_num}次，即将继续闯关。')
            self.barrier()
        else:
            print(f'闯关任务已完成，请明天再来。')

        r2 = requests.get(f'{self.url}/earn/meimeirili/v1/system/actionBubble', headers=self.header).json()
        if r2['result']['status'] == 0:
            print('气泡红包，今天已达上限。')
        else:
            self.bubble()

        r3 = requests.get(f'{self.url}/earn/meimeirili/v1/system/rewardCoinBig', headers=self.header).json()
        if r3['result']['status'] == 0:
            print('幸运红包，今天已达上限。')
        else:
            print('幸运红包，暂没找到。')
            # self.big_coin()

        r = requests.post(f"{self.url}/earn/meimeirili/v1/system/zhuanIndex?", headers=self.header).json()
        task_list = r['result']['items']
        for item in task_list:
            if item["id"] == 10:  # 判断签到
                if item["st"] == 1:
                    print(f'今日已签到，明天再签吧。')
                elif item["st"] == 0:
                    self.signin()
            if item["id"] == 9:  # 判断看广告视频任务
                if item["st"] == 1:
                    task_num = int(item['title'][-3:-1]) - int(
                        BeautifulSoup(item['title'], 'html.parser').find('font').get_text())
                    if task_num > round(int(item['title'][-3:-1]) / 2, 0):
                        task_num = random.randint(round(int(item['title'][-3:-1]) / 2, 0) - 2,
                                                  round(int(item['title'][-3:-1]) / 2, 0))
                    self.watchAD(task_num)
                elif item["st"] == 0:
                    print("请领取看广告视频奖励")
                    self.receive(id=9)
                elif item["st"] == 2:
                    print(f'今日看广告视频任务已完成。')
            if item["id"] == 8:  # 判断看资讯任务
                if item["st"] == 0:
                    task_num = int(item['rate'].split('$')[1]) - int(item['rate'].split('$')[0])
                    if task_num > round(int(item['rate'].split('$')[1]) / 2, 0):
                        task_num = random.randint(round(int(item['rate'].split('$')[1]), 0) - 2,
                                                  round(int(item['rate'].split('$')[1]), 0))
                    self.watchNews(task_num)
                elif item["st"] == 1:
                    print("请领取看广告视频奖励")
                    self.receive(id=8)
                elif item["st"] == 2:
                    print(f'看广告视频任务已完成。')
            if item["id"] == 4:  # 判断抽奖任务
                if item["st"] == 0:
                    task_num = int(item['rate'].split('$')[1]) - int(item['rate'].split('$')[0])
                    if task_num > round(int(item['rate'].split('$')[1]) / 2, 0):
                        task_num = random.randint(round(int(item['rate'].split('$')[1]), 0) - 2,
                                                  round(int(item['rate'].split('$')[1]), 0))
                    print(f'执行抽奖任务{task_num}次')
                    self.lottery(task_num)
                elif item["st"] == 1:
                    print("请领取抽奖任务奖励")
                    self.receive(id=4)
                elif item["st"] == 2:
                    print(f'看广告视频任务已完成。')
            if item['id'] == 38:  # 判断刷短剧领金币10次
                if item['st'] == 0:
                    task_num = int(item['rate'].split('$')[1]) - int(item['rate'].split('$')[0])
                    print(f'执行刷短剧领金币任务{task_num}次')
                    # self.watchVideo(task_num)
                elif item['st'] == 2:
                    print(f'刷短剧领金币任务已完成。')
            if item['id'] == 39:  # 判断刷短剧领金币20次
                if item['st'] == 0:
                    task_num = int(item['rate'].split('$')[1]) - int(item['rate'].split('$')[0])
                    print(f'执行刷短剧领金币任务{task_num}次')
                elif item['st'] == 2:
                    print(f'刷短剧领金币任务已完成。')
            if item['id'] == 40:  # 判断刷短剧领金币30次
                if item['st'] == 0:
                    task_num = int(item['rate'].split('$')[1]) - int(item['rate'].split('$')[0])
                    print(f'执行刷短剧领金币任务{task_num}次')
                elif item['st'] == 2:
                    print(f'刷短剧领金币任务已完成。')
            if item["id"] == 7:  # 刷视频领金币
                if item["st"] == 0:
                    task_num = int(item['rate'].split('$')[1]) - int(item['rate'].split('$')[0])
                    if task_num > round(int(item['rate'].split('$')[1]) / 2, 0):
                        task_num = random.randint(round(int(item['rate'].split('$')[1]), 0) - 2,
                                                  round(int(item['rate'].split('$')[1]), 0))
                    self.watchVideo(task_num)
                elif item["st"] == 1:
                    self.receive(id=7)
                elif item["st"] == 2:
                    print(f'刷视频，赚金币任务已完成。')
            if item["id"] == 6:  # 大额奖励任务
                if item["st"] == 0:
                    task_num = int(item['title'][-2:-1]) - int(
                        BeautifulSoup(item['title'], 'html.parser').find('font').get_text())
                    if task_num > 0:
                        self.videoDown(task_num=1)
                elif item["st"] == 2:
                    print(f'大额奖励任务已完成。')
                elif item["st"] == 1:
                    print(f'大额奖励任务还没有完成的哟。')

        self.rain()
        self.watchVideo(random.randint(4, 10))
        self.exchange()


if __name__ == "__main__":
    user_cookie = cookies.split('@')
    print(f"美美日历获取到{len(user_cookie)}个账号")
    i = 1
    try:
        for cookie_item in user_cookie:
            authorization, idfa, device, model, brand, user_agent, osversion = cookie_item.split('&')
            print(f"=========开始第{i}个账号=========")
            User(authorization, idfa, device, model, brand, user_agent, osversion).run()
            i += 1
    except InvalidURLException as e:
        print(str(e))
