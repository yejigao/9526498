# 酷狗音乐
# author @wangquanfugui233
# cron */30 8-18 * * *
# 抓酷狗gateway的url的带有dfid=&appid=&token=&mid=&clientver=&from=client&clienttime=&userid&uuid=有这几个就行，不要求排序，脚本自动的,
# 抓提现的openid,去提现页面,点一下提现至微信就能抓到的了，nickname 也一样,ture=2提现2块 ture=5就提现5块，依次类推
# 变量 export kgyycks='url?后面的参数，不要url?只要参数#openid#nickname#ture=2'

"""
# new Env("酷狗音乐")
# cron: */30 8-18 * * *
通用代码
只需要修改  asyncio.run(common.main("qimao"))  "qimao"代表七猫脚本 "ydcd"代表 有道词典，现有hkread ,speedread,fyys,shengdu,kgyy,qimao
5.13开放一天
代码请勿用于非法盈利，一切与本人无关，该代码仅用于学习交流，请阅览下载24小时内删除代码
"""
SCRIPT_NAME = "kgyy"   # 脚本名称 记得修改这里


import asyncio
import platform
import sys
import os
import subprocess



def check_environment(file_name):
    v, o, a = sys.version_info, platform.system(), platform.machine()
    print(f"Python版本: {v.major}.{v.minor}.{v.micro}, 操作系统类型: {o}, 处理器架构: {a}")
    if (v.minor in [9,10,11,12]) and o == 'Linux' and a in ['x86_64', 'aarch64', 'armv8', 'armv7l']:
        print("符合运行要求,ARMv7,ARMv8请自行尝试")
        check_so_file(file_name, v.minor, a)
    else:
        if not (v.minor in [9,10,11,12]):
            print("不符合要求: Python版本不是3.9 3.10 3.11 3.12中的一种")
            return
        if o != 'Linux':
            print("不符合要求: 操作系统类型不是Linux")
            return
        if a not in ['x86_64','aarch64', 'armv8', 'armv7l']:
            print("不符合要求: 处理器架构不是x86_64 aarch64 armv8 armv7中的一种")
            return


def check_so_file(filename, py_v, cpu_info):
    if os.path.exists(filename):
        print(f"{filename} 存在")
        import common
        asyncio.run(common.main(SCRIPT_NAME))
    else:
        print(f"不存在{filename}文件,准备下载文件")
        url = 'https://files.doudoudou.top/?f=/script/others'
        # 固定 url = 'https://raw.githubusercontent.com/wyourname/wool/master/others'
        download_so_file(filename, py_v, cpu_info,main_url=url)

def run_command(command):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, 
        text=True  
    )
    for line in process.stdout:
        line = line.strip()
        if "%" in line:
            print(line)
    process.wait()
    return process.returncode


def download_so_file(filename, py_v, cpu_info, main_url):
    file_base_name = os.path.splitext(filename)[0]
    if cpu_info in ['aarch64', 'armv8']:
        url = main_url + f'/{file_base_name}_3{py_v}_aarch64.so'
    if cpu_info == 'x86_64':
        url = main_url + f'/{file_base_name}_3{py_v}_{cpu_info}.so'
    if 'armv7' in cpu_info:
        url = main_url + f'/{file_base_name}_3{py_v}_armv7.so'
    # print(github_url)
    # 您的命令，使用 -# 参数显示下载进度
    command = ['curl', '-#', '-o', filename, url]
    # 执行命令并处理输出
    result = run_command(command)
    if result == 0:
        print(f"下载完成：{filename},调用check_so_file funtion")
        check_so_file(filename,py_v,cpu_info)
    else:
        print(f"下载失败,请让检查一下他们家网络,或者自行修改为GitHub下载的 url:https://raw.githubusercontent.com/wyourname/wool/master/others")

if __name__ == '__main__':
    check_environment('common.so')