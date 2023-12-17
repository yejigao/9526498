"""
@仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。

微信阅读_至尊宝 V2.11

原作者 不知道是谁，群里下载的

Update by Huansheng

入口 微信打开：http://2621738.wburj4uaa9ned.gbl.wk47j64rz9hp.cloud/?p=2568134
网页在线取CK：http://ck-tools.freemyip.com/

变量名称：ydtoken     变量值：cookie@key
多账号用'===='隔开 例 账号1====账号2

定时，7点至23点，每3小时1次
cron：0 7-23/3 * * *

定制、偷撸、投稿 联系 QQ：1047827439

阅读文章抓出cookie（找不到搜索Cookie关键词） 

支持（环境变量）：
1. 企业微信推送 
wechatBussinessKey 企业微信webhook机器人后面的 key
2. wxpusher推送
wxpusherAppToken 填wxpusher的appToken
wxpusherTopicId  # 这个是wxpusher的topicId改成你自己的
具体使用方法请看文档地址：https://wxpusher.zjiecode.com/docs/#/

"""

import random
import hashlib
import json
import os
import time
import requests
import threading
from multiprocessing import Pool, freeze_support
from multiprocessing.pool import ThreadPool

lock = threading.Lock()

# 填wxpusher的appToken
wxpusherAppToken = os.getenv("wxpusherAppToken") or ""
wxpusherTopicId = os.getenv("wxpusherTopicId") or ""
# 如果采用企业微信的机器人推送就配置这个
wechatBussinessKey = os.getenv("wechatBussinessKey") or ""
# 获取 xwytoken 环境变量值
accounts = os.getenv("ydtoken")
theadNumber = 1  # 并发线程数(建议单线程，多线程容易黑微信号)
# 等待检测文章的延时区间，默认等待 15 - 20s 的随机时间，请在该时间内完成点击阅读 检测文章
delayMiniTime = 15
delayMaxTime = 20
# 限制只有自己的下级方可自动阅读过检测
onlyChildrenAutoRead = False
# 限制自动检测的账号起始坐标（在这个之前的账号不检测是否为下级），注意：在 conc 和 desi 的情况下会异常，请改为 0
disabledCheckAccountIndex = 0
# 我的邀请id，根据这个检查是否是自己的下级
myInviteId = "2568134"


def getParentId(cookie, accountIndex):
    print(f"\n=======💚开始查询 账号【{accountIndex}】上级信息💚=======")
    current_time = str(int(time.time()))
    # 计算 sign
    sign_str = f"key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}"
    sha256_hash = hashlib.sha256(sign_str.encode())
    sign = sha256_hash.hexdigest()
    url = "http://2568134.neavbkz.jweiyshi.r0ffky3twj.cloud/person/info"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
        "Cookie": cookie,
    }

    data = {"time": current_time, "sign": sign}
    response = {}
    try:
        result = requests.get(url, headers=headers, json=data)
        if result:
            response = result.json()
            if response["code"] == 0:
                parentId = response["data"]["pid"]
                return parentId
    except Exception as e:
        # 处理异常
        print(f"幻生逼逼叨:", " 账号【{i}】获取上级信息失败", e)
        return


def main_task(accountData, accountIndex):
    global wechatBussinessKey, wxpusherAppToken, wxpusherTopicId
    # 按@符号分割当前账号的不同参数
    values = accountData.split("@")
    if len(values) == 2:
        cookie, wechatBussinessKey = values[0], values[1]
    else:
        cookie = values[0]
    findParentId = 0
    autoSkipRead = True
    # 如果当前坐标大于等于检测的坐标，说明需要检测
    if disabledCheckAccountIndex <= accountIndex:
        findParentId = getParentId(cookie, accountIndex)
        print(
            f"\n账号【{accountIndex}】找到的上级ID：{findParentId} 与 我的邀请ID：{myInviteId} 不符，将禁止推送到自动阅读！"
        )
        if findParentId:
            if findParentId == myInviteId:
                autoSkipRead = True
            else:
                autoSkipRead = False
        else:
            autoSkipRead = False
    else:
        print(f"\n账号【{accountIndex}】不在设置的检测账号内，无需检测父级")
    # 输出当前正在执行的账号
    print(f"\n=======💚开始执行 账号【{accountIndex}】阅读任务💚=======")
    current_time = str(int(time.time()))

    # 计算 sign
    sign_str = f"key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}"
    sha256_hash = hashlib.sha256(sign_str.encode())
    sign = sha256_hash.hexdigest()
    url = "http://2568134.neavbkz.jweiyshi.r0ffky3twj.cloud/share"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
        "Cookie": cookie,
    }

    data = {"time": current_time, "sign": sign}
    response = {}
    try:
        result = requests.get(url, headers=headers, json=data)
        if result:
            print()
        else:
            result = requests.get(url, headers=headers, json=data)
        if result:
            response = result.json()
            share_link = response["data"]["share_link"][0]
            myUserId = share_link.split("=")[1].split("&")[0]
            # 如果当前用户是自己，肯定跳过啦
            if myUserId == findParentId:
                autoSkipRead = True
            url = "http://2568134.neavbkz.jweiyshi.r0ffky3twj.cloud/read/info"
            result = requests.get(url, headers=headers, json=data)
            if result:
                response = result.json()
            else:
                result = requests.get(url, headers=headers, json=data)
                response = result.json()
            if result.json()["code"] == 0:
                print(
                    f" 账号【{accountIndex}】获取到了任务信息，可以执行阅读啦，今日已赚：",
                    result.json()["data"]["gold"],
                )
            else:
                print(
                    f" 账号【{accountIndex}】获取任务信息出错：",
                    result.json()["message"],
                )
        else:
            print(f" 账号【{accountIndex}】未获取到share信息：", result.text)
            return
        if response["code"] == 0:
            remain = response["data"]["remain"]
            read = response["data"]["read"]
            print(
                f" 账号【{accountIndex}】ID:{myUserId}-----钢镚余额:{remain}\n今日阅读量::{read}\n推广链接:{share_link}"
            )
        else:
            print(f" 账号【{accountIndex}】获取用户信息失败：", response["message"])
    except Exception as e:
        # 处理异常
        print(f"幻生逼逼叨:", " 账号【{i}】不对啊，获取不到信息，不做了！请检查你的Cookies啊", e)
        return
    # 如果关闭了限制检查，则前面的判断无效，全部推翻
    if onlyChildrenAutoRead == False:
        autoSkipRead = True
    print(f"============📖开始执行 账号【{accountIndex}】阅读文章📖============")
    for readIndex in range(30):
        isCheckedPost = False
        biz_list = [
            "MzkyMzI5NjgxMA==",
            "MzkzMzI5NjQ3MA==",
            "Mzg5NTU4MzEyNQ==",
            "Mzg3NzY5Nzg0NQ==",
            "MzU5OTgxNjg1Mg==",
            "Mzg4OTY5Njg4Mw==",
            "MzI1ODcwNTgzNA==",
            "Mzg2NDY5NzU0Mw==",
            "MzA4OTI3ODY4Mg=",
            "MzAwNTIzNjYzNA==",
            "Mzg4NjY5NzE4NQ==",
            "MzkwODI5NzQ4MQ==",
            "MzkzMzI5Njc0Nw==",
            "Mzg5NDg5MDY3Ng==",
            "MzA3MjMwMTYwOA==",
            "MzkyNTM5OTc3OQ==",
            "MjM5OTQ0NzI3Ng==",
            "MzkwOTU3MDI1OA==",
            "MzAwOTc2NDExMA==",
            "MzA3OTI4MDMxMA==",
            "MzkxNzI2ODcwMQ==",
            "MzA3MDMxNzMzOA==",
            "Mzg3NjAwODMwMg==",
            "MzI3NDE2ODk1Nw==",
            "MzIyMDMyNTMwMw==",
            "MzIzMjY2NTMwNQ==",
            "MzkxNzMwMjY5Mg==",
            "MzA5Njg3MDk2Ng==",
            "MzA5MzM1OTY2OQ==",
            "MzA4NTQwNjc3OQ==",
            "MjM5NTY5OTU0MQ==",
            "MzU1NTc4OTg2Mw==",
            "MzkwMzI0NjQ4Mw==",
            "MzI3OTA2NDk0Nw==",
            "MjM5MDU4ODgwMw==",
            "Mzg4NzUyMjQxMw==",
        ]
        # 计算 sign
        sign_str = (
            f"key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}"
        )
        sha256_hash = hashlib.sha256(sign_str.encode())
        sign = sha256_hash.hexdigest()
        url = "http://2568134.9o.10r8cvn6b1.cloud/read/task"

        try:
            response = requests.get(url, headers=headers, json=data, timeout=7).json()
        except requests.Timeout:
            print(f" 账号【{accountIndex}】❗第{readIndex+1}次阅读请求超时，尝试重新发送请求...")
            response = requests.get(url, headers=headers, json=data, timeout=7).json()
        if response["code"] == 1:
            print(f" 账号【{accountIndex}】第{readIndex+1}次阅读结果：", response["message"])
            break
        else:
            try:
                # print("返回：", response["data"])
                postUrl = response["data"]["link"]
                if postUrl:
                    try:
                        mid = postUrl.split("&mid=")[1].split("&")[0]
                        biz = postUrl.split("__biz=")[1].split("&")[0]
                        isCheckedPost = True
                    except Exception as e:
                        url = response["data"]["link"]
                        isCheckedPost = False
                        try:
                            result = requests.get(
                                url, headers=headers, timeout=7, allow_redirects=False
                            )
                        except requests.Timeout:
                            result = requests.get(
                                url, headers=headers, timeout=7, allow_redirects=False
                            )
                        if result.status_code == 302:
                            postUrl = result.headers.get("Location")
                            try:
                                mid = postUrl.split("&mid=")[1].split("&")[0]
                                biz = postUrl.split("__biz=")[1].split("&")[0]
                            except Exception as e:
                                print(
                                    f" 账号【{accountIndex}】第{readIndex+1}次阅读失败：提不到文章参数，请联系作者帮忙更新"
                                )
                                continue
                            if (mid == None) or (biz == None):
                                print(
                                    f" 账号【{accountIndex}】第{readIndex+1}次阅读失败：提不到文章参数，请联系作者帮忙更新"
                                )
                                continue
                        else:
                            # 处理异常
                            print(
                                f" 账号【{accountIndex}】第{readIndex+1}次阅读失败：提不到文章参数，请联系作者帮忙更新"
                            )
                            continue

                    print(f" 账号【{accountIndex}】第{readIndex+1}次获取文章成功---{mid} 来源[{biz}]")

                    if (biz in biz_list) or isCheckedPost:
                        print(
                            f" 账号【{accountIndex}】第{readIndex+1}次阅读文章 >>> 发现目标[{biz}] 疑似检测文章！！！"
                        )
                        link = response["data"]["link"]
                        url = "http://wxpusher.zjiecode.com/api/send/message"
                        if wechatBussinessKey:
                            url = (
                                "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="
                                + wechatBussinessKey
                            )

                        messages = [
                            f"出现检测文章！！！\n<a style='padding:10px;color:red;font-size:20px;' href='{link}'>点击我打开待检测文章</a>\n请尽快点击链接完成阅读",
                        ]

                        for message in messages:
                            data = {
                                "appToken": wxpusherAppToken,
                                "content": message,
                                "summary": "钢镚阅读",
                                "contentType": 2,
                                "topicIds": [wxpusherTopicId or "11686"],
                                "contentType": 2,
                                "url": link,
                            }
                            if wechatBussinessKey:
                                data = {"msgtype": "text", "text": {"content": message}}
                            headers = {"Content-Type": "application/json"}
                            randomWaitTime = random.randint(delayMiniTime, delayMaxTime)
                            with lock:
                                if autoSkipRead == False:
                                    print(
                                        f" 账号【{accountIndex}】不属于{myInviteId}的下级，抱歉，不执行自动阅读推送--{randomWaitTime}s后继续运行"
                                    )
                                    time.sleep(randomWaitTime)
                                    url = (
                                        "http://2568134.9o.10r8cvn6b1.cloud/read/finish"
                                    )
                                    headers = {
                                        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
                                        "Cookie": cookie,
                                    }
                                    data = {"time": current_time, "sign": sign}
                                    try:
                                        response = requests.get(
                                            url, headers=headers, data=data, timeout=7
                                        ).json()
                                    except requests.Timeout:
                                        print(
                                            f" 账号【{accountIndex}】❗第{readIndex+1}次阅读请求超时，尝试重新发送请求..."
                                        )
                                        response = requests.get(
                                            url, headers=headers, data=data, timeout=7
                                        ).json()
                                    if response["code"] == 0:
                                        gain = response["data"]["gain"]
                                        print(
                                            f" 账号【{accountIndex}】第{readIndex+1}次阅读检测文章成功---获得钢镚[{gain}]，返回值：",
                                            response,
                                        )
                                        print(f"--------------------------------")
                                    else:
                                        print(
                                            f" 账号【{accountIndex}】第{readIndex+1}次阅读❗过检测失败，请尝试重新运行"
                                        )
                                        break
                                else:
                                    response = requests.post(
                                        url, headers=headers, data=json.dumps(data)
                                    )
                                    print(
                                        f" 账号【{accountIndex}】已将第{readIndex+1}篇文章推送至微信请在{randomWaitTime}s内点击链接完成阅读--{randomWaitTime}s后继续运行"
                                    )
                                    time.sleep(randomWaitTime)
                                    url = (
                                        "http://2568134.9o.10r8cvn6b1.cloud/read/finish"
                                    )
                                    headers = {
                                        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
                                        "Cookie": cookie,
                                    }
                                    data = {"time": current_time, "sign": sign}
                                    try:
                                        response = requests.get(
                                            url, headers=headers, data=data, timeout=7
                                        ).json()
                                    except requests.Timeout:
                                        print(
                                            f" 账号【{accountIndex}】❗第{readIndex+1}次阅读请求超时，尝试重新发送请求..."
                                        )
                                        response = requests.get(
                                            url, headers=headers, data=data, timeout=7
                                        ).json()
                                    if response["code"] == 0:
                                        gain = response["data"]["gain"]
                                        print(
                                            f" 账号【{accountIndex}】第{readIndex+1}次阅读检测文章成功---获得钢镚[{gain}]，返回值：",
                                            response,
                                        )
                                        print(f"--------------------------------")
                                    else:
                                        print(
                                            f" 账号【{accountIndex}】第{readIndex+1}次阅读❗过检测失败，请尝试重新运行"
                                        )
                                        break
                    else:
                        sleep = random.randint(15, 20)
                        print(f" 账号【{accountIndex}】第{readIndex+1}次模拟阅读{sleep}秒")
                        time.sleep(sleep)
                        url = "http://2568134.9o.10r8cvn6b1.cloud/read/finish"
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
                            "Cookie": cookie,
                        }
                        data = {"time": current_time, "sign": sign}
                        try:
                            response = requests.get(
                                url, headers=headers, data=data, timeout=7
                            ).json()
                        except requests.Timeout:
                            print(
                                f" 账号【{accountIndex}】第{readIndex+1}次完成阅读❗请求超时，尝试重新发送请求..."
                            )
                            response = requests.get(
                                url, headers=headers, data=data, timeout=7
                            ).json()
                        if response["code"] == 0:
                            gain = response["data"]["gain"]
                            print(
                                f" 账号【{accountIndex}】第{readIndex+1}次阅读文章成功---获得钢镚[{gain}]，返回值：",
                                response,
                            )
                            print(f"--------------------------------")
                        else:
                            print(
                                f" 账号【{accountIndex}】❗第{readIndex+1}次阅读文章失败{response}"
                            )
                            break
                else:
                    print(f" 账号【{accountIndex}】第{readIndex+1}次获取文章失败", response["data"])
            except KeyError:
                print(f" 账号【{accountIndex}】❗获取文章失败,错误未知：", response)
                break
    print(f"============💰 账号【{accountIndex}】开始微信提现💰============")
    url = "http://2568134.84.8agakd6cqn.cloud/withdraw/wechat"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
            "Cookie": cookie,
        },
        json={"time": current_time, "sign": sign},
    ).json()
    if response["code"] == 0:
        print(f" 账号【{accountIndex}】微信提现结果：", response["message"])
    elif response["code"] == 1:
        print(f" 账号【{accountIndex}】微信提现结果：", response["message"])
    else:
        print(f" 账号【{accountIndex}】❗微信提现错误未知：{response}")


if __name__ == "__main__":
    freeze_support()
    # 检查 xwytoken 是否存在
    if accounts is None:
        print(
            "❗没有检测到ydtoken，请检查是否填写正确 \n活动入口，微信打开：http://2621738.wburj4uaa9ned.gbl.wk47j64rz9hp.cloud/?p=2568134 \n定制、偷撸、投稿 联系 QQ：1047827439"
        )
    else:
        # 获取环境变量的值，并按指定字符串分割成多个账号的参数组合
        accounts_list = os.environ.get("ydtoken").split("====")

        # 输出有几个账号
        num_of_accounts = len(accounts_list)
        print(
            f"幻生提示：获取到 {num_of_accounts} 个账号 \n活动入口，微信打开：http://2621738.wburj4uaa9ned.gbl.wk47j64rz9hp.cloud/?p=2568134 \n定制、偷撸、投稿 联系 QQ：1047827439"
        )

        # 遍历所有账号
        with Pool(processes=num_of_accounts) as pool:
            thread_pool = ThreadPool(theadNumber)
            thread_pool.starmap(
                main_task,
                [(account, i) for i, account in enumerate(accounts_list, start=1)],
            )
        # for i, account in enumerate(accounts_list, start=1):
