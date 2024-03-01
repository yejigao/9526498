oo0o ='''
cron: 30 */30 8-22 * * *
new Env('f猫猫看看阅读');
活动入口：https://3r6q.714l63.shop/haobaobao/auth/d5f3876a22d5562d2a83ddf0629186d8
使用方法：
1.入口,WX打开：https://3r6q.714l63.shop/haobaobao/auth/d5f3876a22d5562d2a83ddf0629186d8
'''#line:7
'''
1.入口,WX打开https://3r6q.714l63.shop/haobaobao/auth/d5f3876a22d5562d2a83ddf0629186d8
若链接微信无法打开，请复制到浏览器复制新链接打开
2.打开活动入口，抓包的任意接口cookie参数中的bbus
3.青龙配置文件，添加本脚本环境变量
填写变量参数时为方便填写可以随意换行
单账户：export mmkkydconfig="[{'name':'备注名','bbus': 'eyJpdVlIjxxxx','key':'xxxxxxx','uids':'xxxxxxx'}]"
多账户：export mmkkydconfig="[
{'name':'备注名','bbus': 'eyJpdVlIjxxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','bbus': 'eyJpdVlIjxxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','bbus': 'eyJpdVlIjxxxx','key':'xxxxxxx','uids':'xxxxxxx'}
]"
参数说明：
name:备注名随意填写
cookie:打开活动入口，抓包的任意接口headers中的cookie参数
key：每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取
4.青龙环境变量菜单，添加本脚wxpusher环境变量(不需要重复添加)
建议使用方式二
方式一：青龙添加环境变量参数 ：
名称 ：push_config
参数 ：{"printf":0,"threadingf":1,"threadingt":3,"appToken":"xxxx"}
方式二：配置文件添加
export push_config="{'printf':0,'threadingf':1,'threadingt':3,'appToken':'xxxx'}"
参数说明：
printf:0是不打印调试日志，1是打印调试日志
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
threadingt:并行运行时每个账号的间隔时间默认3s
appToken 这个是填wxpusher的appToken,找不到自己百度

5.本地电脑python运行
在本脚本最下方代码if __name__ == '__main__':下填写
例如
loc_push_config={"printf":0,"threadingf":1,"threadingt":3,"appToken":"xxxx"}
loc_klydconfig=[
{'name':'备注名','bbus': 'eyJpdiI6IxxxbHVlIj','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','bbus': 'eyJpdiI6IjxxxsInZhbHVlIj','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','bbus': 'eyJpdxxxxIsInZhbHVlIj','key':'xxxxxxx','uids':'xxxxxxx'}
]
6.在本脚本最下方代码if __name__ == '__main__':下配置UA变量
User-Agent参数可以抓包任意接口在headers中看到
定时运行每半个小时一次
'''#line:53
import requests #line:54
import re #line:55
import random #line:56
import os #line:57
import threading #line:58
import json #line:59
import hashlib #line:60
import time #line:61
from urllib .parse import urlparse ,parse_qs #line:62
checkDict ={'onenotischeck':['第一篇文章','过检测'],}#line:65
push_num =[-1 ]#line:66
def getmsg ():#line:67
    O0000000O00OOOOO0 ='v1.6f'#line:68
    O0O0OOO0OO0000000 =''#line:69
    try :#line:70
        O00OO0000OOOO0000 ='http://175.24.153.42:8881/getmsg'#line:71
        O00O0O0000OOOO0OO ={'type':'zhyd'}#line:72
        O0O0OOO0OO0000000 =requests .get (O00OO0000OOOO0000 ,params =O00O0O0000OOOO0OO ,timeout =2 )#line:73
        O0OO00OOO0O00O00O =O0O0OOO0OO0000000 .json ()#line:74
        O000O00OOO00OOO0O =O0OO00OOO0O00O00O .get ('version')#line:75
        OO0O0O0O0OO0000OO =O0OO00OOO0O00O00O .get ('gdict')#line:76
        O00O000OOOO0OO000 =O0OO00OOO0O00O00O .get ('gmmsg')#line:77
        print ('系统公告:',O00O000OOOO0OO000 )#line:78
        print (f'最新版本{O000O00OOO00OOO0O},当前版本{O0000000O00OOOOO0}')#line:79
        print (f'系统的公众号字典{len(OO0O0O0O0OO0000OO)}个:{OO0O0O0O0OO0000OO}')#line:80
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:81
        print ('='*50 )#line:82
    except Exception as OO0OO0OOO0O0O000O :#line:83
        print (OO0OO0OOO0O0O000O )#line:84
        print ('公告服务器异常')#line:85
def push (OOOO00O0O0O0OO0O0 ,OO0O00O000OO00O0O ,O000O00OOO0OOOO00 ,OOO000O0000O0OOOO ,O0000O00O0O00000O ,O0OOOOOO000OO0OO0 ):#line:86
    O00OO000O0OO0O00O ='''
<body onload="window.location.href='LINK'">
<p>TEXT</p><br>
<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>
</body>
    '''#line:92
    OOOOOO0O0000O0OOO =O00OO000O0OO0O00O .replace ('TITTLE',OOOO00O0O0O0OO0O0 ).replace ('LINK',OO0O00O000OO00O0O ).replace ('TEXT',O000O00OOO0OOOO00 ).replace ('TYPE',OOO000O0000O0OOOO ).replace ('KEY',O0OOOOOO000OO0OO0 )#line:94
    OOOO0OOO0OO00OO00 ={"appToken":appToken ,"content":OOOOOO0O0000O0OOO ,"summary":OOOO00O0O0O0OO0O0 ,"contentType":2 ,"uids":[O0000O00O0O00000O ]}#line:101
    OO000O000OOOOO00O ='http://wxpusher.zjiecode.com/api/send/message'#line:102
    try :#line:103
        OOOO0000000000O00 =requests .post (url =OO000O000OOOOO00O ,json =OOOO0OOO0OO00OO00 ).text #line:104
        print ('推送结果：',OOOO0000000000O00 )#line:105
        return True #line:106
    except Exception as O0000O00OOO0O0OOO :#line:107
        print ('推送失败！')#line:108
        print ('推送结果：',O0000O00OOO0O0OOO )#line:109
        return False #line:110
def getinfo (OO0OO0OOOO00OO00O ):#line:111
    try :#line:112
        OO00000OOOOO00OO0 =requests .get (OO0OO0OOOO00OO00O )#line:113
        OOO0OOOOOOO000OO0 =re .sub ('\s','',OO00000OOOOO00OO0 .text )#line:115
        O0O0OO00000000OO0 =re .findall ('varbiz="(.*?)"\|\|',OOO0OOOOOOO000OO0 )#line:116
        if O0O0OO00000000OO0 !=[]:#line:117
            O0O0OO00000000OO0 =O0O0OO00000000OO0 [0 ]#line:118
        if O0O0OO00000000OO0 ==''or O0O0OO00000000OO0 ==[]:#line:119
            if '__biz'in OO0OO0OOOO00OO00O :#line:120
                O0O0OO00000000OO0 =re .findall ('__biz=(.*?)&',OO0OO0OOOO00OO00O )#line:121
                if O0O0OO00000000OO0 !=[]:#line:122
                    O0O0OO00000000OO0 =O0O0OO00000000OO0 [0 ]#line:123
        O0000O0OOO00O0O0O =re .findall ('varnickname=htmlDecode\("(.*?)"\);',OOO0OOOOOOO000OO0 )#line:124
        if O0000O0OOO00O0O0O !=[]:#line:125
            O0000O0OOO00O0O0O =O0000O0OOO00O0O0O [0 ]#line:126
        OOOO000O0OO00OOOO =re .findall ('varuser_name="(.*?)";',OOO0OOOOOOO000OO0 )#line:127
        if OOOO000O0OO00OOOO !=[]:#line:128
            OOOO000O0OO00OOOO =OOOO000O0OO00OOOO [0 ]#line:129
        OOO00O000OOOOO000 =re .findall ("varmsg_title='(.*?)'\.html\(",OOO0OOOOOOO000OO0 )#line:130
        if OOO00O000OOOOO000 !=[]:#line:131
            OOO00O000OOOOO000 =OOO00O000OOOOO000 [0 ]#line:132
        O0OO0O0O00O0O0OOO =re .findall ("varoriCreateTime='(.*?)';",OOO0OOOOOOO000OO0 )#line:133
        if O0OO0O0O00O0O0OOO !=[]:#line:134
            O0OO0O0O00O0O0OOO =O0OO0O0O00O0O0OOO [0 ]#line:135
        O0OO00O0O0OO0O000 =re .findall ("varcreateTime='(.*?)';",OOO0OOOOOOO000OO0 )#line:136
        if O0OO00O0O0OO0O000 !=[]:#line:137
            O0OO00O0O0OO0O000 =O0OO00O0O0OO0O000 [0 ]#line:138
        O0OOOOOOO00OO0O00 =f'公众号唯一标识：{O0O0OO00000000OO0}|文章:{OOO00O000OOOOO000}|作者:{O0000O0OOO00O0O0O}|账号:{OOOO000O0OO00OOOO}|文章时间戳:{O0OO0O0O00O0O0OOO}|文章时间:{O0OO00O0O0OO0O000}'#line:139
        print (O0OOOOOOO00OO0O00 )#line:140
        return O0000O0OOO00O0O0O ,OOOO000O0OO00OOOO ,OOO00O000OOOOO000 ,O0OOOOOOO00OO0O00 ,O0O0OO00000000OO0 ,O0OO0O0O00O0O0OOO ,O0OO00O0O0OO0O000 #line:141
    except Exception as OOOOOOOO0OOO0O0O0 :#line:142
        print (OOOOOOOO0OOO0O0O0 )#line:143
        print ('异常')#line:144
        return False #line:145
class WXYD :#line:146
    def __init__ (OO0OO0O00O00000OO ,OOO00000O0OO0O00O ):#line:147
        OO0OO0O00O00000OO .bbus =OOO00000O0OO0O00O ['bbus']#line:148
        OO0OO0O00O00000OO .name =OOO00000O0OO0O00O ['name']#line:149
        OO0OO0O00O00000OO .key =OOO00000O0OO0O00O ['key']#line:150
        OO0OO0O00O00000OO .uids =OOO00000O0OO0O00O ['uids']#line:151
        OO0OO0O00O00000OO .count =0 #line:152
        OO0OO0O00O00000OO .User_Agent ='/5.0 (Linux; Android 13; 22011211C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110017 MMWEBSDK/20231002 MMWEBID/2575 MicroMessenger/8.0.43.2480(0x28002BE1) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64'#line:153
        OO0OO0O00O00000OO .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':OO0OO0O00O00000OO .User_Agent ,'X-Requested-With':'XMLHttpRequest','Referer':'http://1709274738.lingyunche.xyz/haobaobao/home','Cookie':f'ejectCode=1; bbus={OO0OO0O00O00000OO.bbus}',}#line:160
    def printjson (O0000OO0OOOO000O0 ,OO0O0O0O00OO0000O ):#line:161
        if printf ==0 :#line:162
            return False #line:163
        print (O0000OO0OOOO000O0 .name ,OO0O0O0O00OO0000O )#line:164
    def setstatus (O0O0OO000OO00O00O ):#line:165
        try :#line:166
            OOOOO0OO000000OOO ='http://175.24.153.42:8882/setstatus'#line:167
            OOOOOO000OO0OO0OO ={'key':O0O0OO000OO00O00O .key ,'type':'rrb','val':'1','ven':oo0o }#line:168
            O0OOO000OO00O00OO =requests .get (OOOOO0OO000000OOO ,params =OOOOOO000OO0OO0OO ,timeout =5 )#line:169
            print (O0O0OO000OO00O00O .name ,O0OOO000OO00O00OO .text )#line:170
            if '无效'in O0OOO000OO00O00OO .text :#line:171
                exit (0 )#line:172
        except Exception as O000OOO0O0OO00OOO :#line:173
            print (O0O0OO000OO00O00O .name ,'设置状态异常')#line:174
            print (O0O0OO000OO00O00O .name ,O000OOO0O0OO00OOO )#line:175
            return 99 #line:176
    def getstatus (OO00O0O0OO0000O0O ):#line:178
        try :#line:179
            OOOOO0OO00OO00O0O ='http://175.24.153.42:8882/getstatus'#line:180
            OOO00OO00O000O0O0 ={'key':OO00O0O0OO0000O0O .key ,'type':'rrb'}#line:181
            OOO00000OO000000O =requests .get (OOOOO0OO00OO00O0O ,params =OOO00OO00O000O0O0 ,timeout =3 )#line:182
            return OOO00000OO000000O .text #line:183
        except Exception as OO00OOOOOO000OO00 :#line:184
            print (OO00O0O0OO0000O0O .name ,'查询状态异常',OO00OOOOOO000OO00 )#line:185
            return False #line:186
    def user (O00000O0OOOO00000 ):#line:187
        O00O0OO00O0OOO0O0 ='http://1709274738.lingyunche.xyz/haobaobao/user'#line:188
        try :#line:189
            O00O00O0OOOOOO000 =requests .get (O00O0OO00O0OOO0O0 ,headers =O00000O0OOOO00000 .headers )#line:190
            if 'userid'in O00O00O0OOOOOO000 .text :#line:191
                O0O0O0OO0O000000O =O00O00O0OOOOOO000 .json ()#line:192
                print (f'UID:{O0O0O0OO0O000000O["data"]["userid"]}',end =':')#line:193
                OO0O000000OO00000 ='http://1709274738.lingyunche.xyz/haobaobao/workinfo'#line:194
                O0O0O0OO0O000000O =requests .get (OO0O000000OO00000 ,headers =O00000O0OOOO00000 .headers ).json ()#line:195
                OOO00O0OO00O00OOO =O0O0O0OO0O000000O ['data']['dayreads']#line:196
                O0O0O0OOOO0O0O0OO =O0O0O0OO0O000000O ['data']['remain_gold']#line:197
                print (f'今日已读{OOO00O0OO00O00OOO}篇文章，剩余金币{O0O0O0OOOO0O0O0OO}')#line:198
                return True #line:199
        except :#line:200
            print ('网站网络异常，请手动查看网站活动是否还能打开')#line:201
            return False #line:202
    def wtmpdomain (OO0OO000OO0OOOO00 ):#line:203
        OOOO000O0O000OO00 =f'http://1709274738.lingyunche.xyz/haobaobao/wtmpdomain'#line:204
        OOOO00O0O0O0O00O0 =requests .post (OOOO000O0O000OO00 ,headers =OO0OO000OO0OOOO00 .headers )#line:205
        O0O00O0O00OOOO00O =OOOO00O0O0O0O00O0 .json ()#line:206
        if O0O00O0O00OOOO00O .get ('errcode')!=0 :#line:207
            return False #line:208
        OO0OO000O0O0O00OO =O0O00O0O00OOOO00O .get ('data')['domain']#line:209
        OOO0O00O0O00O000O =parse_qs (urlparse (OO0OO000O0O0O00OO ).query )#line:210
        O00O0O0OOOOO0OOOO =urlparse (OO0OO000O0O0O00OO ).netloc #line:211
        print (O00O0O0OOOOO0OOOO )#line:212
        O00OOOO0O0000O0O0 =OOO0O00O0O00O000O .get ('uk')[0 ]#line:213
        print (O00OOOO0O0000O0O0 )#line:214
        O000000OOOO0O0OOO ={'Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/8555 Flue','Origin':f'https://{O00O0O0OOOOO0OOOO}',}#line:219
        print (OO0OO000O0O0O00OO )#line:220
        OOOO00O0O0O0O00O0 =requests .get (OO0OO000O0O0O00OO ,headers =O000000OOOO0O0OOO )#line:221
        O000000OOOO0O0OOO .update ({'Cookie':f'PHPSESSID={OOOO00O0O0O0O00O0.cookies.get("PHPSESSID")}'})#line:222
        return O00OOOO0O0000O0O0 ,O000000OOOO0O0OOO ,O00O0O0OOOOO0OOOO #line:223
    def getread2 (OOOO0O00O000O000O ):#line:225
        OOOOO0OO0O0000O00 =OOOO0O00O000O000O .wtmpdomain ()#line:226
        O00OOO000O000O00O =0 #line:227
        while True :#line:228
            '"maos1709279562-1256911967.cos.ap-beijing.myqcloud.com1709280758000Lj*?Q3#pOviW"'#line:229
            OO00OOOOOO0O0O000 =int (time .time ())#line:230
            O00O000O0OO0OO0O0 =hashlib .md5 (f"{OOOOO0OO0O0000O00[2]}{OO00OOOOOO0O0O000}000Lj*?Q3#pOviW".encode ()).hexdigest ()#line:231
            OOOOOOO0O00O000O0 =f'https://nsr.zsf2023e458.cloud/haobaobao/getread2?time={OO00OOOOOO0O0O000}000&mysign={O00O000O0OO0OO0O0}&v=3.0&uk={OOOOO0OO0O0000O00[0]}'#line:232
            OOO00OOOOO0OOOO00 =requests .get (OOOOOOO0O00O000O0 ,headers =OOOOO0OO0O0000O00 [1 ])#line:234
            print (OOOO0O00O000O000O .name ,'-'*50 )#line:235
            O000O00O0OOO0OO00 =OOO00OOOOO0OOOO00 .json ()#line:236
            if O000O00O0OOO0OO00 .get ('errcode')!=0 :#line:237
                print (OOO00OOOOO0OOOO00 .text )#line:238
                return False #line:239
            O00OO00OOOO00O0OO =O000O00O0OOO0OO00 .get ('data')['link']#line:240
            OOOO0O00O000O000O .printjson (O00OO00OOOO00O0OO )#line:241
            if O00OO00OOOO00O0OO =='close':#line:242
                print (OOOO0O00O000O000O .name ,f'阅读结果：{O000O00O0OOO0OO00.get("success_msg")}')#line:243
                return True #line:244
            if 'weixin'in O00OO00OOOO00O0OO :#line:245
                OO000OO000OOO00O0 =getinfo (O00OO00OOOO00O0OO )#line:246
                if OOOO0O00O000O000O .testCheck (OO000OO000OOO00O0 ,O00OO00OOOO00O0OO )==False :#line:247
                    return False #line:248
                O0O00OOO0OO00O000 =random .randint (6 ,9 )#line:249
                print (OOOO0O00O000O000O .name ,f'本次模拟读{O0O00OOO0OO00O000}秒')#line:250
                time .sleep (O0O00OOO0OO00O000 )#line:251
                OOOO0000OOO0000O0 =int (time .time ())-OO00OOOOOO0O0O000 #line:252
                OOOO0O00O000O000O .addgolds2 (OOOO0000OOO0000O0 ,O00O000O0OO0OO0O0 ,OOOOO0OO0O0000O00 [0 ],OOOOO0OO0O0000O00 [1 ])#line:253
                time .sleep (1 )#line:254
            else :#line:255
                print (OOOO0O00O000O000O .name ,'未知结果')#line:256
                print (OOOO0O00O000O000O .name ,O000O00O0OOO0OO00 )#line:257
                break #line:258
    def addgolds2 (O0O0O0OOO0OO0OO0O ,O0OO0000O000O0OO0 ,O0O00OOO0O0OO0OOO ,OOO00O00OOOOO00OO ,O0O0O00OO0OOOO000 ):#line:259
        OOO000OOOOO00O0OO =f'https://nsr.zsf2023e458.cloud/haobaobao/addgolds2?time={O0OO0000O000O0OO0}&psign={O0O00OOO0O0OO0OOO}&uk={OOO00O00OOOOO00OO}'#line:260
        O00OO0OO0OO0000O0 =requests .get (OOO000OOOOO00O0OO ,headers =O0O0O00OO0OOOO000 )#line:261
        print (O00OO0OO0OO0000O0 .text )#line:262
        OO0OOO0OOO0O00O0O =O00OO0OO0OO0000O0 .json ()#line:263
        O000O0000O0OOOOOO =OO0OOO0OOO0O00O0O .get ('data')#line:264
        print (f'阅读成功获得{O000O0000O0OOOOOO["gold"]}金币，当天阅读{O000O0000O0OOOOOO["day_read"]}，剩余金币{O000O0000O0OOOOOO["last_gold"]}')#line:265
    def testCheck (O0OO00OO00O000O0O ,OOO00O00O00000O00 ,OO0OO0O0OO0O0OOOO ):#line:266
        if OOO00O00O00000O00 [4 ]==[]:#line:267
            print (O0OO00OO00O000O0O .name ,'这个链接没有获取到微信号id',OO0OO0O0OO0O0OOOO )#line:268
            return True #line:269
        if (checkDict .get (OOO00O00O00000O00 [4 ])!=None )or (int (time .time ())-int (OOO00O00O00000O00 [5 ])>60 *60 *24 *14 ):#line:270
            for O00000O00OO0O0O00 in range (60 ):#line:277
                if O00000O00OO0O0O00 %30 ==0 :#line:278
                    OO000O0OOOOOO0O0O =f'http://175.24.153.42:8882/lookwxarticle?key=KEY&type=TYPE&wxurl={OO0OO0O0OO0O0OOOO}'#line:279
                    push (f'猫猫看看阅读过检测:{O0OO00OO00O000O0O.name}',OO000O0OOOOOO0O0O ,OOO00O00O00000O00 [3 ],'rrb',O0OO00OO00O000O0O .uids ,O0OO00OO00O000O0O .key )#line:280
                O0OOO0OOO0000000O =O0OO00OO00O000O0O .getstatus ()#line:281
                if O0OOO0OOO0000000O =='0':#line:282
                    print (O0OO00OO00O000O0O .name ,'过检测文章已经阅读')#line:283
                    return True #line:284
                elif O0OOO0OOO0000000O =='1':#line:285
                    print (O0OO00OO00O000O0O .name ,f'正在等待过检测文章阅读结果{O00000O00OO0O0O00}秒。。。')#line:286
                    time .sleep (1 )#line:287
                else :#line:288
                    print (O0OO00OO00O000O0O .name ,O0OOO0OOO0000000O )#line:289
                    print (O0OO00OO00O000O0O .name ,'服务器异常')#line:290
                    return False #line:291
            print (O0OO00OO00O000O0O .name ,'过检测超时中止脚本防止黑号')#line:292
            return False #line:293
        else :#line:294
            return True #line:295
    def withdrawal (O0O0OOO0O0OOO0O00 ):#line:296
        O000O0O0O0000OOOO =f'{O0O0OOO0O0OOO0O00.host}/withdrawal'#line:297
        OO0O000O0O00O00OO =requests .get (O000O0O0O0000OOOO ,headers =O0O0OOO0O0OOO0O00 .headers )#line:298
        O00O0O0OOO0000O0O =OO0O000O0O00O00OO .json ()#line:299
        time .sleep (3 )#line:300
        if O00O0O0OOO0000O0O .get ('code')==0 :#line:301
            OO0O00OO00OO00O00 =int (float (O00O0O0OOO0000O0O ['data']['user']['score']))#line:302
            if OO0O00OO00OO00O00 >=2000 :#line:303
                OO0O00OO00OO00O00 =2000 #line:304
            O000OOO000000000O =O0O0OOO0O0OOO0O00 .headers .copy ()#line:305
            O000OOO000000000O .update ({'Content-Type':'application/x-www-form-urlencoded'})#line:306
            O000O0O0O0000OOOO =f'{O0O0OOO0O0OOO0O00.host}/withdrawal/doWithdraw'#line:307
            O0O000O00O000O000 =f'amount={OO0O00OO00OO00O00}&type=wx'#line:308
            OO0O000O0O00O00OO =requests .post (O000O0O0O0000OOOO ,headers =O000OOO000000000O ,data =O0O000O00O000O000 )#line:309
            print (O0O0OOO0O0OOO0O00 .name ,'提现结果',OO0O000O0O00O00OO .text )#line:310
        else :#line:311
            print (O0O0OOO0O0OOO0O00 .name ,O00O0O0OOO0000O0O )#line:312
    def run (OO00OO000O00O0000 ):#line:313
        if hashlib .md5 (oo0o .encode ()).hexdigest ()!='2d1954caac2dec8c9757516f1cc3e9a7':OO00OO000O00O0000 .setstatus ()#line:314
        if OO00OO000O00O0000 .user ():#line:315
            OO00OO000O00O0000 .getread2 ()#line:316
def getEnv (OO0000O0000O0OOOO ):#line:317
    O0O0OO000O0000OO0 =os .getenv (OO0000O0000O0OOOO )#line:318
    if O0O0OO000O0000OO0 ==None :#line:319
        print (f'{OO0000O0000O0OOOO}青龙变量里没有获取到，使用本地参数')#line:320
        return False #line:321
    try :#line:322
        O0O0OO000O0000OO0 =json .loads (O0O0OO000O0000OO0 .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:323
        return O0O0OO000O0000OO0 #line:324
    except Exception as OOO0O0O0O0O00OO0O :#line:325
        print ('错误:',OOO0O0O0O0O00OO0O )#line:326
        print ('你填写的变量是:',O0O0OO000O0000OO0 )#line:327
        print ('请检查变量参数是否填写正确')#line:328
        print (f'{OO0000O0000O0OOOO}使用本地参数')#line:329
if __name__ =='__main__':#line:330
    loc_push_config = {"printf": 1, "threadingf": 0, "appToken": "xxxx"}
    loc_klydconfig  = [
        {'name':'zh','bbus':'PN','key':'8a0b79f','uids':'UID_xxx'},
        #{'name': '备注名', 'cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx'}
    ]
    #--------------------------------------------------------
    push_config = getEnv('push_config')
    if push_config == False: push_config = loc_push_config
    print(push_config)
    klydconfig = getEnv('mmkkydconfig')
    if klydconfig==False:klydconfig=loc_klydconfig
    print(klydconfig)
    printf = push_config.get('printf',0)  # 打印调试日志0不打印，1打印，若运行异常请打开调试
    appToken = push_config['appToken']  # 这个是填wxpusher的appToken
    threadingf = push_config.get('threadingf',1)
    getmsg()
    if threadingf == 1:
        tl=[]
        for cg in klydconfig:
            print('*' * 50)
            print(f'开始执行{cg["name"]}')
            api = WXYD(cg)
            t = threading.Thread(target=api.run, args=())
            tl.append(t)
            t.start()
            threadingt=push_config.get('threadingt',3)
            time.sleep(threadingt)
        for t in tl:
            t.join()
    elif threadingf == 0:
        for cg in klydconfig:
            print('*' * 50)
            print(f'开始执行{cg["name"]}')
            api = WXYD(cg)
            api.run()
            print(f'{cg["name"]}执行完毕')
            time.sleep(3)
    else:
        print('请确定推送变量中threadingf参数是否正确')
    print('全部账号执行完成')
    time.sleep(15)