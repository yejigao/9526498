"""
💰 钢蹦阅读_V2.65    ♻230924

🔔 帮助他人增加阅读量，自己也有奖金拿，每天最低1—2元，邀约还可以赚更多，本脚本自动推送检测文章到微信，需要用户手动阅读过检测，过检测后脚本自动完成阅读任务，每天180篇，每篇100金币，3000金币可提现，提现秒到账，10000金币=1元。不需要下载app，在微信打开下方链接即可进入到活动页。

🔔 为了您能持久获得收益，请仔细阅读以下说明

👉 活动入口 微信打开： http://w.6mcyrj8t2qnq.cloud/?p=2819634    备用链接：https://tinyurl.com/mmp6xsxm   建议将链接添加至微信收藏，或添加到悬浮窗，方便进入查看和阅读检测文章

@进入后点击永久入口，保存二维码，当链接失效时扫码获取最新链接！

@建议一个微信号只运行一个阅读任务，否则会被列入风险用户，导致阅读无效，得不偿失！

@运行脚本前建议手动阅读5篇左右再使用脚本，不然100%黑！！！

@本脚本仅供学习交流，请在下载后的24小时内完全删除 请勿用于商业用途或非法目的，否则后果自负。

提示：
建议使用“pushplus推送加”接收检测文章，微信公众号关注“pushplus推送加”，点击pushplus进入到官网首页注册并激活消息，注册后获取您token口令填写到下方(key=" ")。当然您也可以使用企业微信接收消息。
每天前两篇检测文章不过，有黑号的风险，导致阅读无效，如不能及时接收检测文章，或不能及时阅读检测文章，建议手动运行脚本，运行前去微信手动阅读三篇文章，每篇阅读6秒以上。
每天180个任务不建议跑满，细水长流，如出现阅读更新中，你的账号可能风险，建议24小时后再操作，平时在订阅号多读文章，多点赞评论，可以减小黑号的几率。
为了阅读账号安全，调试过程严谨反复运行脚本，可间隔2小时进行第二次调试，调试运行前应检查好各参数配置。

参数：
阅读文章时用抓包工具抓出cookie（搜索gfsessionid关键词），获取参数cookie
变量名称：ydtoken     变量值：gfsessionid=o-0fIv9cGv3xxxxxxx; zzbb_info=%7B%22xxxxxxx
多账号用'&'隔开 例 账号1&账号2

定时:
自动定时规则cron： 0 7-23/2 * * *   (每天7-23点每3小时一次)，期间注意接收微信通知，阅读检测文章，(key参数必填)
手动定时规则cron： 0                (不自动运行)，每次手动运行脚本前务必手动阅读3篇文章，每篇阅读6秒以上
"""

max_concurrency = 3  # 并发线程数(建议3线程)，多账号并发
money_Withdrawal = 1  # 提现开关 1开启 0关闭，自动提现
key = ""  # (自动运行必填) key参数为pushplus的token口令，或企业微信webhook机器人后面的 key，用于推送接收检测文章

import hashlib
import json
import os
import random
import threading
import time
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

import requests

lock = threading.Lock()


def process_account(account, i):
    values = account.split('@')
    cookie = values[0]

    print(f"\n=======💚开始执行账号{i}💚=======")
    current_time = str(int(time.time()))

    sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
    sha256_hash = hashlib.sha256(sign_str.encode())
    sign = sha256_hash.hexdigest()
    url = "http://2819634.neavbkz.jweiyshi.r0ffky3twj.cloud/share"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4475.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
        "Cookie": cookie
    }

    data = {
        "time": current_time,
        "sign": sign
    }

    with lock:
        response = requests.get(url, headers=headers, json=data).json()
        share_link = response['data']['share_link'][0]
        p_value = share_link.split('=')[1].split('&')[0]

        url = "http://w.6mcyrj8t2qnq.cloud/?p=2819634"

        try:
            response = requests.get(url, headers=headers, json=data, timeout=7).json()
        except requests.Timeout:
            print("❗请求超时，尝试重新发送请求...")
            response = requests.get(url, headers=headers, json=data, timeout=7).json()
        except Exception as e:
            print('❗设置状态异常')
            print(e)

        if response['code'] == 0:
            remain = response['data']['remain']
            read = response['data']['read']
            print(f"👤ID:{p_value}-----💰钢镚余额:{remain}\n📖今日阅读量::{read}")
        else:
            print(response['message'])

    print("============💚开始执行阅读文章💚============")

    for j in range(30):
        biz_list = ['MzkyMzI5NjgxMA==', 'MzkzMzI5NjQ3MA==', 'Mzg5NTU4MzEyNQ==', 'Mzg3NzY5Nzg0NQ==',
                    'MzU5OTgxNjg1Mg==', 'Mzg4OTY5Njg4Mw==', 'MzI1ODcwNTgzNA==', 'Mzg2NDY5NzU0Mw==']
        # 计算 sign
        sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
        sha256_hash = hashlib.sha256(sign_str.encode())
        sign = sha256_hash.hexdigest()
        url = "http://28199634.9o.10r8cvn6b1.cloud/read/task"

        try:
            response = requests.get(url, headers=headers, json=data, timeout=7).json()
        except requests.Timeout:
            print("❗请求超时，尝试重新发送请求...")
            response = requests.get(url, headers=headers, json=data, timeout=7).json()
        except Exception as e:
            print(e)
            print("❗状态异常，尝试重新发送请求...")
            response = requests.get(url, headers=headers, json=data, timeout=7).json()
        if response['code'] == 1:
            print(response['message'])
            break
        else:
            try:
                mid = response['data']['link'].split('&mid=')[1].split('&')[0]
                biz = response['data']['link'].split('__biz=')[1].split('&')[0]

                print(f"[{p_value}]获取文章成功---{mid} 来源[{biz}]")

                if biz in biz_list:
                    print(f"发现目标[{biz}] 疑似检测文章！！！")
                    link = response['data']['link']
                    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key

                    messages = [
                        f"出现检测文章！！！\n{link}\n请在60s内点击链接完成阅读",
                    ]

                    for message in messages:
                        data = {
                            "msgtype": "text",
                            "text": {
                                "content": message
                            }
                        }
                        headers = {'Content-Type': 'application/json'}
                        response = requests.post(url, headers=headers, data=json.dumps(data))
                        url = 'http://www.pushplus.plus/send'
                        data = {
                            "token": key,
                            "title": "出现检测文章！请在60s内完成阅读",
                            "content": f'<a href="\n{link}\n"target="_blank">点击阅读6s以上 \n{link}\n',
                            "template": "html"
                        }
                        response = requests.post(url, data=data).json()
                        print("已将该文章推送至微信请在60s内点击链接完成阅读--60s后继续运行")
                        time.sleep(60)
                        url = "http://2819634.9o.10r8cvn6b1.cloud/read/finish"
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4475.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
                            "Cookie": cookie
                        }
                        data = {
                            "time": current_time,
                            "sign": sign
                        }
                        try:
                            response = requests.get(url, headers=headers, data=data, timeout=7).json()
                        except requests.Timeout:
                            print("❗请求超时，尝试重新发送请求...")
                            response = requests.get(url, headers=headers, data=data, timeout=7).json()
                        except Exception as e:
                            print('❗设置状态异常')
                            print(e)
                        if response['code'] == 0:
                            gain = response['data']['gain']
                            print(f"第{j + 1}次阅读检测文章成功---获得钢镚[{gain}]")
                            print(f"--------------------------------")
                        else:
                            print(f"❗过检测失败，请尝试重新运行")
                            break
                else:
                    sleep = random.randint(8, 15)
                    print(f"本次模拟阅读{sleep}秒")
                    time.sleep(sleep)
                    url = "http://2819634.9o.10r8cvn6b1.cloud/read/finish"
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4475.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
                        "Cookie": cookie
                    }
                    data = {
                        "time": current_time,
                        "sign": sign
                    }
                    try:
                        response = requests.get(url, headers=headers, data=data, timeout=7).json()
                    except requests.Timeout:
                        print("❗请求超时，尝试重新发送请求...")
                        response = requests.get(url, headers=headers, data=data, timeout=7).json()
                    except Exception as e:
                        print('❗设置状态异常')
                        print(e)
                    if response['code'] == 0:
                        gain = response['data']['gain']
                        print(f"第{j + 1}次阅读文章成功---获得钢镚[{gain}]")
                        print(f"--------------------------------")
                    else:
                        print(f"❗阅读文章失败{response}")
            except KeyError:
                print(f"❗获取文章失败,错误未知{response}")
                break
    if money_Withdrawal == 1:
        print(f"============💰开始微信提现💰============")
        url = "http://w.6mcyrj8t2qnq.cloud/?p=2819634"
        response = requests.get(url, headers=headers, json=data).json()
        if response['code'] == 0:
            print(response['message'])
        elif response['code'] == 1:
            print(response['message'])
        else:
            print(f"❗错误未知{response}")
    elif money_Withdrawal == 0:
        print(f"{'-' * 30}\n不执行提现")


if __name__ == "__main__":
    accounts = os.getenv('ydtoken')
    response = requests.get('https://gitee.com/gngkj/wxyd/raw/master/label.txt').text
    print(response)
    if accounts is None:
        print('请检查变量ydtoken，是否填写正确')
    else:
        accounts_list = os.environ.get('ydtoken').split('&')
        num_of_accounts = len(accounts_list)
        print(f"获取到 {num_of_accounts} 个账号")
        with Pool(processes=num_of_accounts) as pool:
            thread_pool = ThreadPool(max_concurrency)
            thread_pool.starmap(process_account, [(account, i) for i, account in enumerate(accounts_list, start=1)])
