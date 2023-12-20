'''
cron: 50 59 9 * * 3
new Env('中国移动和包抢商品');
频道地址：https://t.me/ymxzpd
问题反馈请联系-->https://t.me/bwersgt

1.使用方法打开活动,拉起和包活动地址或者自行打开和包活动
https://ump.cmpay.com/info/version4/marketing/2023/Q2/memberGift5.html?jrnNo=ACT1057&rulerId=JKJE5470&rulerGiftId=QUNM0810&utm_source=QTQD&utm_medium=FX&utm_term=hbkhd&utm_content=DN5&utm_campaign=BYHYL&_channel_track_key=jPpaw0ki&shareUrl=AF9AF11681D0817EEE24C283C9B95272
2.抓包和包app
抓包任意接口cookie中的act_sid=act-xxxx-2d19-4c76-xxxx-xxxx
填到脚本136行左右
3.具体抢购商品请看脚本136行左右说明
'''
import threading
import time
import requests
import datetime
class hebao_hy_goods:
    "手机号获取和包ck"
    def __init__(self):
        self.headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; LIO-AN00 Build/LIO-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/24.0)',
            'Host': 'ump.cmpay.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'Cookie': ck
        }

    def prizeList(self):
        prizeTypedict={'1':'积分','2':'生活缴费券','3':'话费满返券','4':'加油券','5':'金融满返券','6':'积分'}
        print('月月领会员日')
        couponTicketList = 'https://ump.cmpay.com/activities/v1/members/couponTicketList'
        r = requests.get(couponTicketList, headers=self.headers)
        print(r.text)
        rj = r.json()
        msgCd = rj.get('msgCd')
        if msgCd == 'MKM00000':
            self.prizeList = rj.get('body').get('prizeList')
            for i in self.prizeList:
                prizeAmt = i.get('prizeAmt')
                prizeNo = i.get('prizeNo')
                prizeType = i.get('prizeType')
                useThreshold = i.get('useThreshold')
                residualRate = i.get('residualRate')
                try:
                    print(f'奖品{prizeAmt}{prizeTypedict[prizeType]},使用条件:{useThreshold},ID:{prizeNo},剩余{residualRate}%')
                except Exception as e:
                    print(e)
        else:
            print('异常')
            print(r.text)
            return False
        print('周三会员日')
        couponTicketList = 'https://ump.cmpay.com/activities/v1/members/integralTicketList'
        r = requests.get(couponTicketList, headers=self.headers)
        rj = r.json()
        msgCd = rj.get('msgCd')
        if msgCd == 'MKM00000':
            self.prizeList = rj.get('body').get('prizeList')
            for i in self.prizeList:
                prizeAmt = i.get('prizeAmt')
                prizeNo = i.get('prizeNo')
                prizeType = i.get('prizeType')
                useThreshold = i.get('useThreshold')
                residualRate = i.get('residualRate')
                print(f'奖品{prizeAmt}{prizeTypedict[prizeType]},使用条件:{useThreshold},ID:{prizeNo},剩余{residualRate}%')
        else:
            print('异常')
            print(r.text)
            return False

    def couponTicketReceive(self,p):
        u = 'https://ump.cmpay.com/activities/v1/members/couponTicketReceive'
        p = {"prizeNo": p, "opDfp": ""}
        r = requests.post(u, headers=self.headers, json=p).json()
        print('月月领会员日', r.get('gwa'))
    def integralTicketReceive(self):
        print(datetime.datetime.now())
        u = 'https://ump.cmpay.com/activities/v1/members/integralTicketReceive'
        p = {"prizeNo": p3, "opDfp": ""}
        r = requests.post(u, headers=self.headers, json=p).json()
        print('周三会员日',r.get('gwa'))
    def wait(self, sleepTime):
        nowTine = time.strftime('%H', time.localtime())
        nextTime = str(int(nowTine) + 1).zfill(2)
        print('脚本提前', sleepTime, f'活动开始时间{nextTime}:00:00')
        timeArray = time.strptime(time.strftime('%Y%m%d') + f'100000', "%Y%m%d%H%M%S")
        timeStamp = int(time.mktime(timeArray))
        while True:
            reduce_time = time.time() + sleepTime - timeStamp  # 差值秒
            if time.time() + sleepTime - timeStamp > 0:
                print(
                    f"当前时间{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))},提前结束{sleepTime}s")
                break
            else:
                if abs(reduce_time) > 2:  # 如果剩余时间大于2s，则睡眠剩余的一半时间
                    print(
                        f"当前时间{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))},睡眠{abs(reduce_time) / 2}s")
                    time.sleep(abs(reduce_time) / 2)
    def main(self):
        self.prizeList()
        print('-' * 50)
        for p in plist:
            self.couponTicketReceive(p)
            time.sleep(0.2)
        day=datetime.datetime.now().weekday()
        hour=datetime.datetime.now().hour
        print('-' * 50)
        if day==2 and hour>=9:
            self.wait(0.01)
            for i in range(5):
                t=threading.Thread(target=self.integralTicketReceive,args=())
                t.start()
                time.sleep(0.02)
        else:
            print('周三会员秒杀，周三9点后脚本才会进行')


if __name__ == '__main__':
    #https://www.cmpay.com/front-msa/memberCenter/
    '''
月月领会员日1
奖品100积分,使用条件:None,ID:QYHQ20231001,剩余22%
奖品2生活缴费券,使用条件:20-2,ID:QYHQ20231002,剩余93%
奖品2话费满返券,使用条件:20-2,ID:QYHQ20231003,剩余94%
奖品10加油券,使用条件:100-10,ID:QYHQ20231004,剩余90%
奖品2金融满返券,使用条件:20-2,ID:QYHQ20231005,剩余96%
奖品500积分,使用条件:1000-500,ID:QYHQ20231006,剩余100%
周三会员日
奖品10生活缴费券,使用条件:100-10,ID:JFMS20230004
奖品10话费满返券,使用条件:100-10,ID:JFMS20230005
奖品10金融满返券,使用条件:100-10,ID:JFMS20230006
奖品1000积分,使用条件:积分商城,ID:JFMS20230007
    '''
    ck='act_sid=864cb190-xxxx-xxxx-bc89-55cd336b6963'
    plist=['QYHQ20231006']#每月要抢的
    p3='JFMS20230007'#周三要抢的
    sa = hebao_hy_goods()
    sa.main()