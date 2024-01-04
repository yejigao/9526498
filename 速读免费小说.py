"""
代码请勿用于非法盈利，一切与本人无关，该代码仅用于学习交流，请阅览下载24小时内删除代码
new Env("速读免费小说")
app 速读免费小说
export speedreadcks='整条url#提现目标' # 抓https://welfare-dj.palmestore.com 整条url 请注意url参数p16=xxxx 如果带有空格请手动去除空格
如 export speedreadcks='整条url#15'
并发格式 sd_multi='true'
cron: 8 7,9-21 * * *
不恰钱也不对外开放了
"""
import asyncio
import platform
import sys
import os
import subprocess


def check_environment(file_name):
    v, o, a = sys.version_info, platform.system(), platform.machine()
    print(f"Python版本: {v.major}.{v.minor}.{v.micro}, 操作系统类型: {o}, 处理器架构: {a}")
    if (v.minor in [10]) and o == 'Linux' and a in ['x86_64', 'aarch64', 'armv8']:
        print("符合运行要求,arm8没试过不知道行不行,仓库加密的脚本均不支持青龙模块")
        check_so_file(file_name, v.minor, a)
    else:
        if not (v.minor in [10]):
            print("不符合要求: Python版本不是3.10")
            return
        if o != 'Linux':
            print("不符合要求: 操作系统类型不是Linux")
            return
        if a not in ['x86_64','aarch64']:
            print("不符合要求: 处理器架构不是x86_64 aarch64 armv8中的一种")
            return


def check_so_file(filename, py_v, cpu_info):
    if os.path.exists(filename):
        print(f"{filename} 存在")
        import speedread as sd
        asyncio.run(sd.main())
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
        if main_url != 'https://files.doudoudou.top/?f=/script/others':
            print(f"下载失败：{filename},更换备用url下载")
            download_so_file(filename,py_v,cpu_info,main_url='https://files.doudoudou.top/?f=/script/others')

if __name__ == '__main__':
    check_environment('speedread.so')