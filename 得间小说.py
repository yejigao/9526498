#       得间小说签到专用
#       因无法破解sign，只能做到这样，等着大佬出新的版本吧。
#       变量：djxs
#       格式：备注#https://dj.palmestore.com/zycl/api/（开宝箱完整连接）
#       多账号请换行，备注自己设置任何东西。
#
#
#
#




import datetime
import json, os
import requests, time

#13位时间戳
def shijianchuo13():
    current_milli_time = str(round(time.time() * 1000))
    return current_milli_time




#GET方式发送
def get(urlcanshu):
    url ="https://dj.palmestore.com/zycl/api/glod/getConfig?"+urlcanshu+shijianchuo13()
    data =''
    headers ={
        'Host':'channel.cheryfs.cn',
        'Connection':'keep-alive',
        'wxappid':apid ,
        'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; 21091116C Build/N2G47H)',
        'tenantId':'619669306447261696',
        'activityId':'621950054462152705',
        'requestUrl':'https://channel.cheryfs.cn/archer/act/619669306447261696/619669369294712832/activity/pointsmall-detail/621950054462152705/48uISpgfyfD9eull?pageId=page1607309582231&num=1&cardId=754492665391370240&anchorId=&anchorAnimateType=',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-us,en',
        'accountId':acid,
        'Referer':'https://channel.cheryfs.cn/archer/act/619669306447261696/619669369294712832/activity/pointsmall-detail/621950054462152705/48uISpgfyfD9eull?pageId=page1607309582231&num=1&cardId=754492665391370240&anchorId=&anchorAnimateType=',
        'assemblyName':'%E7%A7%AF%E5%88%86%E5%95%86%E5%9F%8E%E5%85%91%E6%8D%A22'
    }
    res=requests.request ("GET",url ,headers =headers ,data =data)
    print("=========================")
    print(url)
    print("返回结果："+res)
    print("返回内容："+res.text())
    print("=========================")
    return res


#签到
def qiandao(urlcanshu):


    url ="https://dj.palmestore.com/zycl/api/glod/getConfig?"+urlcanshu+str(shijianchuo13())
    data =''
    headers ={
        'Host':'dj.palmestore.com',
        'Connection':'keep-alive',
        'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; 21091116C Build/N2G47H)',
        'Accept-Encoding':'gzip'
    }
    res=requests.request ("GET",url ,headers =headers ,data =data)
    print("=========================")
    print("URL:")
    print(url)
    print("返回结果：")
    print(res.status_code)
    print("返回内容：")
    print(json.loads(res.text))
    print("=========================")



    url ="https://dj.palmestore.com/zycl/gold/indexRefreshV5?"+urlcanshu+str(shijianchuo13())
    data =''
    headers ={
        'Host':'dj.palmestore.com',
        'Connection':'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.2; 21091116C Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 zyApp/dejian zyVersion/5.1.1.2 zyChannel/135313',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Dest':'empty',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    res=requests.request ("GET",url ,headers =headers ,data =data)
    print("=========================")
    print("URL:")
    print(url)
    print("返回结果：")
    print(res.status_code)
    print("返回内容：")
    print(json.loads (res.text))
    print("=========================")


    url ="https://dj.palmestore.com/zycl/gold/dailyWelfareV5?"+urlcanshu+str(shijianchuo13())
    data =''
    headers ={
        'Host':'dj.palmestore.com',
        'Connection':'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.2; 21091116C Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 zyApp/dejian zyVersion/5.1.1.2 zyChannel/135313',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Dest':'empty',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    res=requests.request ("GET",url ,headers =headers ,data =data)
    print("=========================")
    print("URL:")
    print(url)
    print("返回结果：")
    print(res.status_code)
    print("返回内容：")
    print(json.loads (res.text))
    print("=========================")


    url ="https://dj.palmestore.com/zycl/gold/indexRefreshV5?"+urlcanshu+str(shijianchuo13())
    data =''
    headers ={
        'Host':'dj.palmestore.com',
        'Connection':'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.2; 21091116C Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 zyApp/dejian zyVersion/5.1.1.2 zyChannel/135313',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Dest':'empty',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    res=requests.request ("GET",url ,headers =headers ,data =data)
    print("=========================")
    print("URL:")
    print(url)
    print("返回结果：")
    print(res.status_code)
    print("返回内容：")
    print(json.loads (res.text))
    print("=========================")

    return res



cshck =os.getenv ("djxs")
account_list=cshck.split ("\n")
for account in account_list:
    accountck =account.split ("#")
    print("=========================")
    print("备注："+accountck[0])
    print("CK："+accountck[1])
    print("=========================")
    urlcanshu=accountck[1].split ("?")
    print("=========================")
    print("URL参数："+urlcanshu[1])
    print("=========================")


    #签到
    print("得间小说签到开始")
    qiandao(urlcanshu[1])
    print("得间小说签到开始")



