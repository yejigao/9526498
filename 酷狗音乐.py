# Author: lindaye
# Update:2023-11-11
# 酷狗音乐
# 添加账号说明(青龙/本地)二选一
#   青龙: 青龙变量kgtoken 值{"userid":"xxx","ck":"http://acsing.kugou.com/sing7/listenguide/json/v3/的整个链接"} 一行一个(回车分割)
#   本地: 脚本内置ck方法ck_token = [{"userid":"xxx","ck":"http://acsing.kugou.com/sing7/listenguide/json/v3/"},{"userid":"xxx","ck":"http://acsing.kugou.com/sing7/listenguide/json/v3/"}]
# 软件版本
version = "0.0.1"
name = "酷狗音乐"
linxi_token = "kgtoken"
linxi_tips = '{"userid":"xxx(后面这个链接请求头里面的KG-FAKE)","ck":"http://acsing.kugou.com/sing7/listenguide/json/v3/的整个链接"}'

import os
import re
import time
import json
import hashlib
import requests
from multiprocessing import Pool
from urllib.parse import urlparse,parse_qs,quote

# 提现限制(元)
Limit = 0
# 变量类型(本地/青龙)
Btype = "青龙"
# 域名(无法使用时请更换)
domain = 'https://gateway.kugou.com/'
# 保持连接,重复利用
ss = requests.session()
# 全局基础请求头
headers = {
    "kg-thash": "3d6790c",
    "accept-encoding": "gzip, deflate",
    "user-agent": "Android10-AndroidPhone-11109-47-0-MusicalNoteProtocol-wifi",
    "kg-rc": "1",
    "kg-rf": "0080d6f1",
    'Content-Type':'application/json; charset=UTF-8'
}

def kugousign(taskid,ck):
    # 生成Unix时间戳
    timestamp = str(round(time.time()))
    # 生成签名
    if taskid:
        sign_str = 'OIlwieks28dk2k092lksi2UIkpappid=1005clienttime='+ timestamp +'clientver=11109dfid='+ ck['dfid'] +'from=clientmid='+ ck['mid'] +'token='+ ck['token'] +'userid='+ ck['userid'] +'uuid='+ ck['uuid'] +'{"taskid":'+ taskid +',"user_label":{"val6":3456,"val5":0,"val4":0,"val3":0,"val2":128,"val1":4224}}OIlwieks28dk2k092lksi2UIkp'
    else:
        sign_str = 'OIlwieks28dk2k092lksi2UIkpappid=1005clienttime='+ timestamp +'clientver=11109dfid='+ ck['dfid'] +'from=clientmid='+ ck['mid'] +'token='+ ck['token'] +'userid='+ ck['userid'] +'uuid='+ ck['uuid'] +'OIlwieks28dk2k092lksi2UIkp'
    m = hashlib.md5()
    m.update(sign_str.encode('utf-8'))
    sign = m.hexdigest()
    return timestamp,sign


def user_info(i,ck):
    headers['kg-fake'] = ck['userid']
    timestamp,kgsign = kugousign(None,ck)
    result = ss.get(domain+"/mstc/musicsymbol/v1/user/info?dfid="+ ck['dfid'] +'&signature='+ kgsign +'&appid=1005&mid='+ ck['mid'] +'&clientver=11109&from=client&clienttime='+ timestamp +'&uuid='+ ck['uuid'] +'&userid='+ ck['userid'] +'&token='+ ck['token'], headers=headers).json()
    if result['errcode'] == 0:
        print(f"账号【{i+1}】✅ 用户:{result['data']['base']['nickname']} 余额:{result['data']['account']['balance_coins']}")
    else:
        print(f"账号【{i+1}】❌ 获取用户信息失败!")


def do_read(i,ck):
    headers['kg-fake'] = ck['userid']
    task_list =['1','6','9','9','9','9','9','9','9','9','9','9','9','9','9','11','21','22','23','29','31','34','35','36','37','38','39','43','45','46','1101','1105','1107','2206','2213']
    for task_id in task_list:
        timestamp,kgsign = kugousign(task_id,ck)
        body = '{"taskid":'+ task_id +',"user_label":{"val6":3456,"val5":0,"val4":0,"val3":0,"val2":128,"val1":4224}}'
        result = ss.post(domain+"mstc/musicsymbol/v1/task/submit?dfid="+ ck['dfid'] +'&signature='+ kgsign +'&appid=1005&mid='+ ck['mid'] +'&clientver=11109&from=client&clienttime='+ timestamp +'&uuid='+ ck['uuid'] +'&userid='+ ck['userid'] +'&token='+ ck['token'], headers=headers, data=body).json()
        if result['errcode'] == 0:
            print(f"账号【{i+1}】✅ 任务[{task_id}]成功 获得{str(result['data']['awards']['coins'])}狗狗币")
        else:
            print(f"账号【{i+1}】❌ 任务[{task_id}]失败 {result['error']}")
        time.sleep(5)


def handle_exception(e,i):
    print(f"账号【{i+1}】🆘 程序出现异常:", e)
    data = {
        "name": "林夕",
        "project": name,
        "status": "程序出现异常",
        "content": f"异常:{e}",
        "url":"http://linxi.tk"
    }
    result = ss.post("https://linxi-send.run.goorm.app/",json=data).json()
    print(f"账号【{i+1}】🆘 微信消息上报: {result['msg']}")

def process_wrapper(func, args):
    try:
        func(*args)
    except Exception as e:
        handle_exception(e,args[0])


if __name__ == "__main__":
    print(f"""欢迎使用
""")
    if Btype == "青龙":
        if os.getenv(linxi_token) == None:
            print(f'⛔ 青龙变量异常: 请添加{linxi_token}变量示例:{linxi_tips} 确保一行一个')
            exit()
        # 变量CK列表
        #ck_token = [json.loads(line) for line in os.getenv(linxi_token).splitlines()]
        ck_token = [json.loads(li) if "&" in line else json.loads(line) for line in os.getenv(linxi_token).splitlines() for li in re.findall(r'{.*?}', line)]
    else:
        # 本地CK列表
        ck_token = [
            # 这里填写本地变量
        ]
        if ck_token == []:
            print(f'⛔ 本地变量异常: 请添加本地ck_token示例:{linxi_tips}')
            exit()
    desired_keys = ["uuid", "dfid", "token", "userid", "mid", "clientver", "kgfb"]
    new_ck_token = []
    for item in ck_token:
        url_parts = urlparse(item['ck'])
        parameters = parse_qs(url_parts.query)
        result = {key: parameters.get(key, [None])[0] for key in desired_keys}
        result["userid"]=item['userid']
        new_ck_token.append(result)
    # 创建进程池
    with Pool() as pool:
        print("=================👻获取账号信息👻================")
        pool.starmap(process_wrapper, [(user_info, (i, ck)) for i, ck in enumerate(new_ck_token)])
        print("=================💫开始执行任务💫================")
        pool.starmap(process_wrapper, [(do_read, (i, ck)) for i, ck in enumerate(new_ck_token)])
        print("=================🐣获取账号信息🐣================")
        pool.starmap(process_wrapper, [(user_info, (i, ck)) for i, ck in enumerate(new_ck_token)])


        # 关闭进程池
        pool.close()
        # 等待所有子进程执行完毕
        pool.join()

        # 关闭连接
        ss.close
        # 输出结果
        print(f"================[{name}V{version}]===============")