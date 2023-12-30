# 中青快应用 邀请code https://user.youth.cn/h5/fastAppWeb/invite/invite_ground_2.html?share_uid=1038191728&channel=c8000&nickname=%E5%91%A8%E6%A0%91%E4%BA%BA%E9%B2%81%E8%BF%85&avatar=http%3A%2F%2Fres.youth.cn%2Favatar_202203_28_28n_6241677754c3f1038191728m.jpg&v=1697879197
# author @wangquanfugui233
# cron 一天一次 一次3毛，自动提现 微信支付宝都可以
# python3.10.X 64位可以运行，别的没适配
# 抓userinfo? 只要问号后面的参数就行 
# 变量    自动提现： 1是微信 0是支付宝，不填不行,多账户就@分开 
# export zqurl='url?后面的参数#1是微信#true（是当够10元就提10不填就不提，打开可能导致黑号）'
# export zqurl='zzzzzz#1@cccccccccc#0'
# 如果想提高一点收益可以 export zq_open='true' 可不填
# github上的so为旧版
# new Env("中青快应用")
# cron: 1 12 * * *


import asyncio
import platform
import sys
import os
import subprocess


def check_environment(file_name):
    v, o, a = sys.version_info, platform.system(), platform.machine()
    print(f"Python版本: {v.major}.{v.minor}.{v.micro}, 操作系统类型: {o}, 处理器架构: {a}")
    if (v.minor in [10]) and o == 'Linux' and a in ['x86_64', 'aarch64', 'armv8']:
        print("符合运行要求,arm8没试过不知道行不行")
        check_so_file(file_name, v.minor, a)
    else:
        if not (v.minor in [10]):
            print("不符合要求: Python版本不是3.10")
        if o != 'Linux':
            print("不符合要求: 操作系统类型不是Linux")
        if a != 'x86_64':
            print("不符合要求: 处理器架构不是x86_64 aarch64 armv8")


def check_so_file(filename, py_v, cpu_info):
    if os.path.exists(filename):
        print(f"{filename} 存在")
        import aiozqfast as zq
        asyncio.run(zq.main())
    else:
        print(f"不存在{filename}文件,准备下载文件")
        url = 'https://files.doudoudou.top/?f=/script/others'
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
    # print(github_url)
    # 您的命令，使用 -# 参数显示下载进度
    command = ['curl', '-#', '-o', filename, url]
    # 执行命令并处理输出
    result = run_command(command)
    if result == 0:
        print(f"下载完成：{filename},调用check_so_file funtion")
        check_so_file(filename,py_v,cpu_info)
    else:
        if main_url != 'https://files.doudoudou.fun/?f=/script/others':
            print(f"下载失败：{filename},更换备用url下载")
            download_so_file(filename,py_v,cpu_info,main_url='https://files.doudoudou.fun/?f=/script/others')

if __name__ == '__main__':
    check_environment('aiozqfast.so')
