'''
定时59 23,7,11,15,19 * * * 
'''
import requests
import re
import concurrent.futures
import os
from datetime import datetime, timedelta
import time
def login(q):
    url = "http://ar.i.kuwo.cn/US_NEW/kuwo/login_kw"
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; POCO F2 Pro Build/UQ1A.240105.004)",
        "Accept": "*/*",
        "Host": "ar.i.kuwo.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }
    params = {
        "f": "ar",
        "q": q
    }

    response = requests.get(url, headers=headers, params=params)

    username = re.search(r'uname3=([^;]+)', response.headers['Set-Cookie']).group(1)
    loginSid = re.search(r'websid=([^;]+)', response.headers['Set-Cookie']).group(1)
    loginUid = re.search(r'userid=([^;]+)', response.headers['Set-Cookie']).group(1)
    account = re.search(r'userid=([^;]+)', response.headers['Set-Cookie']).group(1)
    return username, loginSid, loginUid, account


def coin(loginUid, loginSid, devId, appUid):
    headers = {
        #'User-Agent': "Mozilla/5.0 (Linux; Android 13; MEIZU 20 Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36/ kuwopage",
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip, deflate",
        'Origin': "https://h5app.kuwo.cn",
        'X-Requested-With': "cn.kuwo.player",
        'Sec-Fetch-Site': "same-site",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        #'Referer': "https://h5app.kuwo.cn/apps/earning-sign/bill.html?random=1714466331159&kwflag=2655868582_1714466296959",
        'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    params2 = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'devId': devId,
        'appUid': appUid,
        'apiVer': "3",
        'source': "kwplayer_ar_10.8.0.1_meizu.apk",
        'function': "1",
        'terminal': "1",
        'version': "10.8.0.1",
        'scoreInfo': "",
        # 't': "0.1941318175506508"
    }
    url2 = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newUserSignList"
    response = requests.get(url2, params=params2, headers=headers).json()
    allcoin = response['data']['remainScore']
    return allcoin


def tx(loginUid, loginSid, appUid, phone):
    print('正在等待...')
    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/getWithdraw"
    params = {
        "quotaId": "30002",
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        "source": "kwplayer_ar_10.7.6.2_qq.apk",
        "version": "1",
        "phone": phone
    }
    headers = {
        "Host": "integralapi.kuwo.cn",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?1",
        # "User-Agent": "Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage",
        "sec-ch-ua-platform": '"Android"',
        "Origin": "https://h5app.kuwo.cn",
        "X-Requested-With": "cn.kuwo.player",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        #"Referer": "https://h5app.kuwo.cn/apps/earning-sign/cash_out.html?transparentTitleView=1&defBack=black&endBgColor=white&random=1711186177362&kwflag=2642624794_1711186175255",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.."
                           "9,en-US;q=0.8,en;q=0.7"
    }
    #time.sleep(seconds_until_1830)
    while True:
        hour = datetime.now().hour

        if hour == 0 or hour == 8 or hour == 12 or hour == 16 or hour == 20:
            break
    if phone is None:
        return



    response = requests.get(url, params=params, headers=headers).json()
    text = response['data']['text']
    print(f"提现2元>>>>>{text}")


kwyy = os.getenv('kwyy')
kwyys = kwyy.split('&')

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for i, kw in enumerate(kwyys):
        print(i)
        try:
            kws = kw.split('#')
            if len(kws) == 3:
                continue
            appUid = kws[0]
            devId = kws[1]
            q = kws[2]
            phone = kws[3]
            if '==' not in phone:
                continue
            username, loginSid, loginUid, account = login(q)
            allcoin = coin(loginUid, loginSid, devId, appUid)
            if int(allcoin) >= 20000:
                    executor.submit(tx, loginUid, loginSid, appUid, phone)
                    # tx(loginUid, loginSid, appUid, phone)
        except Exception:
            continue
