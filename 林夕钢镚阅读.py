# Author: lindaye
# Update:2023-09-26
# 钢镚(充值购买)阅读
# 活动入口：http://2522481.yu.z136.7jegzdyrs1ly6.cloud/?p=2522481
# 添加账号说明(青龙/本地)二选一
#   青龙: 青龙变量gbtoken 值{"ck":"gfsessionid的值","ts":"Wxpusher的UID"} 一行一个(回车分割)
#   本地: 脚本内置ck方法ck_token = [{"ck":"gfsessionid的值","ts":"Wxpusher的UID"},{"ck":"gfsessionid的值","ts":"Wxpusher的UID"}]
# 脚本使用说明:
#   1.(必须操作)扫码关注wxpusher获取UID: https://wxpusher.zjiecode.com/demo/
#   2.在1打开的网页中点击发送文本消息,查看是否收到,收到可继续
#   3.将1打开的网页中的UID或者以及操作过1的账号UID复制备用
#   4.根据提示说明填写账号变量
# 回调服务器开放说明:
#   1.仅针对授权用户开放,需配合授权软件使用
#   2.青龙变量设置LID变量名,值为授权软件的LID
# 软件版本
version = "1.2.1 11-06"
name = "充值购买(钢镚)"
linxi_token = "gbtoken"
linxi_tips = '{"ck":"gfsessionid的值","ts":"Wxpusher的UID"}'
import requests
from multiprocessing import Pool
import re
import time
import hashlib
import random
import os
import json
from urllib.parse import quote
# 阅读等待时间
tsleep = 40
# 变量类型(本地/青龙)
Btype = "青龙"
# 提现限制(元)
Limit = 0.3
# 授权设备ID(软件版本>=1.3.3)[非授权用户不填即可]
imei = os.getenv('LID')
# 充值购买(钢镚)域名(无法使用时请更换)
domain = 'http://2496831.rrn.eqk7p066.4jvg40m4108yr.cloud'
# 保持连接,重复利用
ss = requests.session()

# 检测文章列表(如有未收录可自行添加)
check_list = [
    'MzkyMzI5NjgxMA==','MzkzMzI5NjQ3MA==','Mzg5NTU4MzEyNQ==','Mzg3NzY5Nzg0NQ==','MzU5OTgxNjg1Mg==',
    'Mzg4OTY5Njg4Mw==','MzI1ODcwNTgzNA==','Mzg2NDY5NzU0Mw==','MzA3MjMwMTYwOA==','MzkyNTM5OTc3OQ==',
    'MjM5OTQ0NzI3Ng==','MzkwOTU3MDI1OA==','MzAwOTc2NDExMA==','MzA3OTI4MDMxMA==','MzkxNzI2ODcwMQ==',
    'MzA3MDMxNzMzOA==','Mzg3NjAwODMwMg==','MzI3NDE2ODk1Nw==','MzIyMDMyNTMwMw==','MzIzMjY2NTMwNQ==',
    'MzkxNzMwMjY5Mg==','MzA5Njg3MDk2Ng==','MzA5MzM1OTY2OQ==','Mzg4NjY5NzE4NQ==','MzA4NTQwNjc3OQ==',
    'MjM5NTY5OTU0MQ==','MzU1NTc4OTg2Mw==','MzkwMzI0NjQ4Mw==','MzI3OTA2NDk0Nw==','MjM5MDU4ODgwMw==',
    'MzkwODI5NzQ4MQ==','MzkzMzI5Njc0Nw==','Mzg4NzUyMjQxMw==','Mzg5NDg5MDY3Ng=='
]
# 计算sign
def get_sign():
    current_time = str(int(time.time()))
    # 计算 sign
    sign_str = f"key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}"
    sha256_hash = hashlib.sha256(sign_str.encode())
    sign = sha256_hash.hexdigest()
    data = f'time={current_time}&sign={sign}'
    return data


# 获取个人信息模块
def user_info(i,ck):
    time.sleep(i*1)
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Redmi K30 Pro Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/3850 MicroMessenger/8.0.41.2441(0x28002951) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
        "Cookie":f"gfsessionid={ck['ck']};"
    }
    try:
        result = ss.get(domain+"/share", headers=headers, data=get_sign()).json()
        share_link = result["data"]["share_link"][0]
        userid = share_link.split("=")[1].split("&")[0]
    except:
        print(f"账号【{i+1}】请检查你的CK({ck['ck']})是否正确!")
        return False
    result = ss.get(domain+"/read/info", headers=headers, data=get_sign()).json()
    if result["code"] == 0:
        remain = result["data"]["remain"]
        read = result["data"]["read"]
        print(f"账号【{i+1}】UID:{userid} 余额:{remain} 今日:{read}篇")
    else:
        print(f'账号【{i+1}】用户信息获取失败:{result["message"]}')

# 阅读文章模块
def do_read(i,ck):
    global check_list
    time.sleep(i*5)
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Redmi K30 Pro Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/3850 MicroMessenger/8.0.41.2441(0x28002951) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
        "Cookie":f"gfsessionid={ck['ck']};"
    }
    while True:
        response = ss.get(domain+"/read/task", headers=headers, data=get_sign())
        try:
            response = response.json()
        except json.decoder.JSONDecodeError:
            print(f"账号【{i+1}】请检查你的CK({ck['ck']})是否正确!")
            return False
        if response["code"] == 1:
            if "秒" in response['message']:
                print(f"账号【{i+1}】即将开始:{response['message']}")
                time.sleep(5)
            elif response['message'] == "记录失效":
                print(f"账号【{i+1}】阅读异常,重新获取:{response['message']}")
            else:
                print(f"账号【{i+1}】{response['message']}")
                break
        else:
            try:
                s = random.randint(10,12)
                # 检测是否是检测文章
                if 'weixin' in response["data"]["link"]:
                    biz = re.findall("biz=(.*?)&",response["data"]["link"])[0]
                else:
                    l_result = ss.get(response["data"]["link"],headers=headers).text
                    try:
                        link = re.findall('_g.msg_link = "(.*?)"',l_result)[0]
                        # 获取biz
                        biz = re.findall("biz=(.*?)&amp;",link)[0]
                    except:
                        print(f"账号【{i+1}】BIZ获取失败喽:{response['data']['link']}")
                        break
                print(f"账号【{i+1}】获取文章成功-{biz}-模拟{s}秒")
                if biz in check_list:
                    print(f"账号【{i+1}】阅读检测文章-已推送微信,请40s内完成验证!")
                    # 过检测
                    check = check_status(ck['ts'],response["data"]["link"],i)
                    if check == True:
                        print(f"账号【{i+1}】检测文章-过检测成功啦!")
                        response = ss.post(domain+"/read/finish", headers=headers, data=get_sign()).json()
                        print(f'账号【{i+1}】阅读文章成功-获得钢镚[{response["data"]["gain"]}]-已读{response["data"]["read"]}篇')
                    else:
                        print(f"账号【{i+1}】检测文章-过检测失败啦!")
                        break
                else:
                    time.sleep(s)
                    response = ss.post(domain+"/read/finish", headers=headers, data=get_sign()).json()
                    # print(response)
                    if response["code"] == 0:
                        if response["data"]["check"] is False:
                            print(f'账号【{i+1}】阅读文章成功-获得钢镚[{response["data"]["gain"]}]-已读{response["data"]["read"]}篇')
                        else:
                            print(f"账号【{i+1}】获取到未收录检测: {biz} 将自动停止脚本")
                            check_list.append(biz)
                            break
                    else:
                        if response['message'] == "记录无效":
                            print(f"账号【{i+1}】记录无效,重新阅读")
                        else:
                            print(f"账号【{i+1}】{response}")
                            break
            except Exception as e:
                if response['code'] == 801:
                    print(f"账号【{i+1}】今日任务已完成: {response['message']}")
                    break
                else:
                    print(f"账号【{i+1}】获取文章失败,错误未知({e}) 结果:{response}")
                    break

# 提现模块
def get_money(i,ck):
    time.sleep(i*1)
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Redmi K30 Pro Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/3850 MicroMessenger/8.0.41.2441(0x28002951) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
        "Cookie":f"gfsessionid={ck['ck']};"
    }
    response = ss.get(domain+"/read/info", headers=headers, data=get_sign())
    try:
        response = response.json()
    except json.decoder.JSONDecodeError:
        print(f"账号【{i+1}】请检查你的CK({ck['ck']})是否正确!")
        return False
    if response["code"] == 0:
        remain = response["data"]["remain"]
    else:
        print(f'账号【{i+1}】获取用户信息失败: {response["message"]}')
    if remain >= Limit*10000:
        response = ss.get(domain+"/withdraw/wechat", headers=headers, data=get_sign()).json()
        if response["code"] == 0:
            print(f'账号【{i+1}】开始提现:{response["message"]}')
        elif response["code"] == 1:
            print(f'账号【{i+1}】开始提现:{response["message"]}')
        else:
            print(f'账号【{i+1}】未知错误:{response}')
    else:
        print(f'账号【{i+1}】当前余额为{remain} 未到达{Limit}元提现限制!')

# 微信推送模块
def check_status(key,link,index):
    if imei != None:
        if ss.get("https://linxi-send.run.goorm.io").status_code ==200:
            callback = "https://linxi-send.run.goorm.io"
        else:
            callback = "https://auth.linxi.tk"
        result = ss.post(callback+"/create_task",json={"imei":imei}).json()
        uuid = result['uuid']
        msg = result['msg']
        # print(f"账号【{str(index+1)}】避免并发,本次延迟{index*2}秒,上传服务器[{result['msg']}]")
        # time.sleep(index*2)
        result = ss.get(f'https://wxpusher.zjiecode.com/demo/send/custom/{key}?content=检测文章-{name}%0A请在{tsleep}秒内完成验证!%0A%3Cbody+onload%3D%22window.location.href%3D%27{quote(link)}%27%22%3E').json()
        print(f"账号【{str(index+1)}】微信消息推送[{msg}]: {result['msg']},等待40s完成验证!")
        for i in range(10):
            result = ss.get(callback+f"/select_task/{imei}/{uuid}").json()
            if result['code'] == 200:
                print(f"账号【{str(index+1)}】服务器回调结果:{result['msg']}")
                result = ss.get(callback+f"/delete_task/{imei}/{uuid}").json()
                print(f"账号【{str(index+1)}】查询本次uuid结果:{result['msg']}")
                return True
            time.sleep(4)
        result = ss.get(callback+f"/delete_task/{imei}/{uuid}").json()
        print(f"账号【{str(index+1)}】清除本次uuid结果:{result['msg']}")
        return False
    else:
        # print(f"账号【{str(index+1)}】避免并发同一时间多个推送,本次推送延迟{index*2}秒")
        # time.sleep(index*2)
        result = ss.get(f'https://wxpusher.zjiecode.com/demo/send/custom/{key}?content=检测文章-{name}%0A请在{tsleep}秒内完成验证!%0A%3Cbody+onload%3D%22window.location.href%3D%27{quote(link)}%27%22%3E').json()
        print(f"账号【{str(index+1)}】微信消息推送: {result['msg']},等待40s完成验证!")
        #print(f"手动微信阅读链接: {link}")
        time.sleep(30)
        return True


if __name__ == "__main__":
    print(f"""██╗     ██╗███╗   ██╗██╗  ██╗██╗       ██████╗ ██████╗ ██╗   ██╗██████╗ 
██║     ██║████╗  ██║╚██╗██╔╝██║      ██╔════╝ ██╔══██╗╚██╗ ██╔╝██╔══██╗
██║     ██║██╔██╗ ██║ ╚███╔╝ ██║█████╗██║  ███╗██████╔╝ ╚████╔╝ ██║  ██║
██║     ██║██║╚██╗██║ ██╔██╗ ██║╚════╝██║   ██║██╔══██╗  ╚██╔╝  ██║  ██║
███████╗██║██║ ╚████║██╔╝ ██╗██║      ╚██████╔╝██████╔╝   ██║   ██████╔╝
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝       ╚═════╝ ╚═════╝    ╚═╝   ╚═════╝ 
    项目:{name}           BY-林夕          Verion: {version}(并发)
    Github仓库地址: https://github.com/linxi-520/LinxiPush
""")
    if Btype == "青龙":
        if os.getenv(linxi_token) == None:
            print(f'青龙变量异常: 请添加{linxi_token}变量示例:{linxi_tips} 确保一行一个')
            exit()
        # 变量CK列表
        ck_token = [json.loads(line) for line in os.getenv(linxi_token).splitlines()]
    else:
        # 本地CK列表
        ck_token = [
            # 这里填写本地变量
        ]
        if ck_token == []:
            print(f'本地变量异常: 请添加本地ck_token示例:{linxi_tips}')
    print("==================回调服务器状态=================")
    if imei:
        print(f"[回调服务器]:已启用-[授权ID:{imei}]")
    else:
        print(f"[回调服务器]:未启用-[变量ID:{imei}]")
    # 创建进程池
    with Pool() as pool:
        # 并发执行函数
        print("==================获取账号信息=================")
        pool.starmap(user_info, list(enumerate(ck_token)))
        print("==================开始阅读文章=================")
        pool.starmap(do_read, list(enumerate(ck_token)))
        print("==================开始账号提现=================")
        pool.starmap(get_money, list(enumerate(ck_token)))
        print("==================开始账号提现=================")

        # 关闭进程池
        pool.close()
        # 等待所有子进程执行完毕
        pool.join()

        # 关闭连接
        ss.close
        # 输出结果
        print(f"================[{name}V{version}]===============")
