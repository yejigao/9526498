oo0o ='''
cron: 30 */30 8-22 * * *
new Env('f可乐阅读');
活动入口：http://90762702221442.evhjixw.cn/r?upuid=907627
使用方法：
1.入口,WX打开：http://89933102211423.aaxogdc.cn/r?upuid=899331
'''#line:7
'''
1.入口,WX打开http://90762702221442.evhjixw.cn/r?upuid=907627
若链接微信无法打开，请复制到浏览器复制新链接打开

User_Agent参数1.5f版本UA可以不用填
由于回调服务器失效，没有key的可以临时填xxxx。
key获取方法:http://175.24.153.42:8882/getkey
2.打开活动入口，抓包的任意接口cookie参数
3.青龙配置文件，添加本脚本环境变量
填写变量参数时为方便填写可以随意换行
单账户：export klydconfig=[{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'这个随便填','User_Agent':'xxxxx}']
多账户：export klydconfig=
[{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx','User_Agent':'xxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx','User_Agent':'xxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx','User_Agent':'xxxx'}]
参数说明：
name:备注名随意填写
cookie:打开活动入口，抓包的任意接口headers中的cookie参数
key：每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取
User-Agent:抓包任意接口在headers中看到
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
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','cookie': 'PHPSESSID=xxxx; udtauth3=a267Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'}
]
6.在本脚本最下方代码if __name__ == '__main__':下配置UA变量
User-Agent参数可以抓包任意接口在headers中看到
定时运行每半个小时一次
'''#line:59
import requests #line:60
import re #line:61
import random #line:62
import os #line:63
import threading #line:64
import json #line:65
import hashlib #line:66
import time #line:67
from urllib .parse import urlparse ,parse_qs #line:68
checkDict ={'onenotischeck':['第一篇文章','过检测'],}#line:71
push_num =[1 ,2 ]#line:72
def getmsg ():#line:73
    OOOOOO0OOOOO0O0O0 ='v1.5f'#line:74
    OOOOOOO000O000OO0 =''#line:75
    try :#line:76
        OOO00O0O00OO000O0 ='http://175.24.153.42:8881/getmsg'#line:77
        O00OO0OO0OOO0OO0O ={'type':'zhyd'}#line:78
        OOOOOOO000O000OO0 =requests .get (OOO00O0O00OO000O0 ,params =O00OO0OO0OOO0OO0O ,timeout =2 )#line:79
        OO0O000O0O0OO0OOO =OOOOOOO000O000OO0 .json ()#line:80
        O00O00OOOO0000O0O =OO0O000O0O0OO0OOO .get ('version')#line:81
        OO00O0OO0O0O0O0OO =OO0O000O0O0OO0OOO .get ('gdict')#line:82
        OOOO00OOO00OOOOOO =OO0O000O0O0OO0OOO .get ('gmmsg')#line:83
        print ('系统公告:',OOOO00OOO00OOOOOO )#line:84
        print (f'最新版本{O00O00OOOO0000O0O},当前版本{OOOOOO0OOOOO0O0O0}')#line:85
        print (f'系统的公众号字典{len(OO00O0OO0O0O0O0OO)}个:{OO00O0OO0O0O0O0OO}')#line:86
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:87
        print ('='*50 )#line:88
    except Exception as O0OOOO000OOOOO0O0 :#line:89
        print (O0OOOO000OOOOO0O0 )#line:90
        print ('公告服务器异常')#line:91
def push (OO0O000O0OOOOOO0O ,OOO0O000O00O00OOO ,OOOO000000O0O0O00 ,OOOO0O0000O0OOO00 ,O0O0OOO0OOOOO0OOO ,OO0O0O0O00OOOOOO0 ):#line:92
    OO00OO0OO0O0OO0O0 ='''
<body onload="window.location.href='LINK'">
<p>TEXT</p><br>
<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>
</body>
    '''#line:98
    OO0OOO0O0O00O00OO =OO00OO0OO0O0OO0O0 .replace ('TITTLE',OO0O000O0OOOOOO0O ).replace ('LINK',OOO0O000O00O00OOO ).replace ('TEXT',OOOO000000O0O0O00 ).replace ('TYPE',OOOO0O0000O0OOO00 ).replace ('KEY',OO0O0O0O00OOOOOO0 )#line:100
    O0OO0O0O0OO00000O ={"appToken":appToken ,"content":OO0OOO0O0O00O00OO ,"summary":OO0O000O0OOOOOO0O ,"contentType":2 ,"uids":[O0O0OOO0OOOOO0OOO ]}#line:107
    O0O000O000OO0OO0O ='http://wxpusher.zjiecode.com/api/send/message'#line:108
    try :#line:109
        OOO000OOOOOO0O0OO =requests .post (url =O0O000O000OO0OO0O ,json =O0OO0O0O0OO00000O ).text #line:110
        print ('推送结果：',OOO000OOOOOO0O0OO )#line:111
        return True #line:112
    except Exception as OO00O0OO0OOO0000O :#line:113
        print ('推送失败！')#line:114
        print ('推送结果：',OO00O0OO0OOO0000O )#line:115
        return False #line:116
def getinfo (OOOOOO00OO0O0O000 ):#line:117
    try :#line:118
        O00O0O00OO0OO0O0O =requests .get (OOOOOO00OO0O0O000 )#line:119
        O0000OO00O0O00000 =re .sub ('\s','',O00O0O00OO0OO0O0O .text )#line:121
        O00O0O0O00OO0O0O0 =re .findall ('varbiz="(.*?)"\|\|',O0000OO00O0O00000 )#line:122
        if O00O0O0O00OO0O0O0 !=[]:#line:123
            O00O0O0O00OO0O0O0 =O00O0O0O00OO0O0O0 [0 ]#line:124
        if O00O0O0O00OO0O0O0 ==''or O00O0O0O00OO0O0O0 ==[]:#line:125
            if '__biz'in OOOOOO00OO0O0O000 :#line:126
                O00O0O0O00OO0O0O0 =re .findall ('__biz=(.*?)&',OOOOOO00OO0O0O000 )#line:127
                if O00O0O0O00OO0O0O0 !=[]:#line:128
                    O00O0O0O00OO0O0O0 =O00O0O0O00OO0O0O0 [0 ]#line:129
        O0OO0OOOO0OOO00O0 =re .findall ('varnickname=htmlDecode\("(.*?)"\);',O0000OO00O0O00000 )#line:130
        if O0OO0OOOO0OOO00O0 !=[]:#line:131
            O0OO0OOOO0OOO00O0 =O0OO0OOOO0OOO00O0 [0 ]#line:132
        OOO000O0OOOOOO0OO =re .findall ('varuser_name="(.*?)";',O0000OO00O0O00000 )#line:133
        if OOO000O0OOOOOO0OO !=[]:#line:134
            OOO000O0OOOOOO0OO =OOO000O0OOOOOO0OO [0 ]#line:135
        OOOO0000O00OO00OO =re .findall ("varmsg_title='(.*?)'\.html\(",O0000OO00O0O00000 )#line:136
        if OOOO0000O00OO00OO !=[]:#line:137
            OOOO0000O00OO00OO =OOOO0000O00OO00OO [0 ]#line:138
        OOOOOO00O00OO0OO0 =re .findall ("varoriCreateTime='(.*?)';",O0000OO00O0O00000 )#line:139
        if OOOOOO00O00OO0OO0 !=[]:#line:140
            OOOOOO00O00OO0OO0 =OOOOOO00O00OO0OO0 [0 ]#line:141
        OO0OOOOO000OOO00O =re .findall ("varcreateTime='(.*?)';",O0000OO00O0O00000 )#line:142
        if OO0OOOOO000OOO00O !=[]:#line:143
            OO0OOOOO000OOO00O =OO0OOOOO000OOO00O [0 ]#line:144
        OOO0O0000OO0OOO0O =f'公众号唯一标识：{O00O0O0O00OO0O0O0}|文章:{OOOO0000O00OO00OO}|作者:{O0OO0OOOO0OOO00O0}|账号:{OOO000O0OOOOOO0OO}|文章时间戳:{OOOOOO00O00OO0OO0}|文章时间:{OO0OOOOO000OOO00O}'#line:145
        print (OOO0O0000OO0OOO0O )#line:146
        print ('')#line:147
        return O0OO0OOOO0OOO00O0 ,OOO000O0OOOOOO0OO ,OOOO0000O00OO00OO ,OOO0O0000OO0OOO0O ,O00O0O0O00OO0O0O0 ,OOOOOO00O00OO0OO0 ,OO0OOOOO000OOO00O #line:148
    except Exception as O0OO0O0O0O0OOOO0O :#line:149
        print (O0OO0O0O0O0OOOO0O )#line:150
        print ('异常')#line:151
        return False #line:152
class WXYD :#line:153
    def __init__ (O000OOOOOO0000O00 ,O00O0000O00O00O0O ):#line:154
        O000OOOOOO0000O00 .name =O00O0000O00O00O0O ['name']#line:155
        O000OOOOOO0000O00 .key =O00O0000O00O00O0O ['key']#line:156
        O000OOOOOO0000O00 .uids =O00O0000O00O00O0O ['uids']#line:157
        O000OOOOOO0000O00 .count =0 #line:158
        O000OOOOOO0000O00 .User_Agent =O00O0000O00O00O0O .get ('User_Agent','xxxxxx')#line:159
        if 'Mozilla'not in O000OOOOOO0000O00 .User_Agent :#line:160
            print (O000OOOOOO0000O00 .name ,'UA填写有误使用默认UA,默认UA可能会运行异常')#line:161
            O000OOOOOO0000O00 .User_Agent ='Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.43(0x18002b29) NetType/WIFI Language/zh_CN'#line:162
        O000OOOOOO0000O00 .host =O000OOOOOO0000O00 .get_host ()#line:163
        O000OOOOOO0000O00 .headers ={'Accept':'application/json, text/plain, */*','User-Agent':O000OOOOOO0000O00 .User_Agent ,'Referer':f'{O000OOOOOO0000O00.host}/new?upuid=','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','Cookie':O00O0000O00O00O0O ['cookie'],}#line:171
    def printjson (OO0OO000O000OOOOO ,OOOOO0O000O0O00O0 ):#line:172
        if printf ==0 :#line:173
            return False #line:174
        print (OO0OO000O000OOOOO .name ,OOOOO0O000O0O00O0 )#line:175
    def setstatus (O0O00OO00OO0OOO00 ):#line:176
        try :#line:177
            OOOOO00OO0O00O00O ='http://175.24.153.42:8882/setstatus'#line:178
            O000OOO0OOOOO000O ={'key':O0O00OO00OO0OOO00 .key ,'type':'zhyd','val':'1','ven':oo0o }#line:179
            O00O0000O00OO00O0 =requests .get (OOOOO00OO0O00O00O ,params =O000OOO0OOOOO000O ,timeout =5 )#line:180
            print (O0O00OO00OO0OOO00 .name ,O00O0000O00OO00O0 .text )#line:181
            if '无效'in O00O0000O00OO00O0 .text :#line:182
                exit (0 )#line:183
        except Exception as O0OO00O0OOO000000 :#line:184
            print (O0O00OO00OO0OOO00 .name ,'设置状态异常')#line:185
            print (O0O00OO00OO0OOO00 .name ,O0OO00O0OOO000000 )#line:186
            return 99 #line:187
    def getstatus (O0O0O00O0O0O0O0O0 ):#line:189
        try :#line:190
            OO0O0O00OOO000OO0 ='http://175.24.153.42:8882/getstatus'#line:191
            OOO00OO0O0000OO0O ={'key':O0O0O00O0O0O0O0O0 .key ,'type':'zhyd'}#line:192
            O0OOO0000O0OOOO00 =requests .get (OO0O0O00OOO000OO0 ,params =OOO00OO0O0000OO0O ,timeout =3 )#line:193
            return O0OOO0000O0OOOO00 .text #line:194
        except Exception as O00O00O0OO0OOO0OO :#line:195
            print (O0O0O00O0O0O0O0O0 .name ,'查询状态异常',O00O00O0OO0OOO0OO )#line:196
            return False #line:197
    def get_host (OOOO0O00O00000000 ):#line:198
        OOOOO00OOO00O000O ='https://m.cdcd.plus/entry/new_ld'#line:199
        OOO0OOO0OO0O00OO0 ={'User-Agent':OOOO0O00O00000000 .User_Agent }#line:200
        O00O00O000OO0000O =requests .get (OOOOO00OOO00O000O ,headers =OOO0OOO0OO0O00OO0 ).json ()#line:201
        OO00OO0O0OO00OOOO =O00O00O000OO0000O .get ('jump')#line:202
        O0OO00OO00000O00O =urlparse (OO00OO0O0OO00OOOO ).netloc #line:203
        return f'http://{O0OO00OO00000O00O}'#line:204
    def tuijian (O000O0OOO0O00O0OO ):#line:205
        O00O0OOO00O0000OO =f'{O000O0OOO0O00O0OO.host}/tuijian'#line:206
        OOOOO000OOOO00O0O =requests .get (O00O0OOO00O0000OO ,headers =O000O0OOO0O00O0OO .headers )#line:207
        try :#line:208
            O0O0O0O0OO00O0OOO =OOOOO000OOOO00O0O .json ()#line:209
            if O0O0O0O0OO00O0OOO .get ('code')==0 :#line:210
                O00OO0OOOOO000OOO =O0O0O0O0OO00O0OOO ['data']['user']['username']#line:211
                OOOOO0O000OO00OOO =float (O0O0O0O0OO00O0OOO ['data']['user']['score'])/100 #line:212
                print (O000O0OOO0O00O0OO .name ,f'{O00OO0OOOOO000OOO}:当前剩余{OOOOO0O000OO00OOO}元')#line:213
                return True #line:214
            else :#line:215
                print (O000O0OOO0O00O0OO .name ,O0O0O0O0OO00O0OOO )#line:216
                print (O000O0OOO0O00O0OO .name ,'账号异常0,ck可能失效')#line:217
                return False #line:218
        except Exception as OOO0000OOO00OO00O :#line:219
            print (O000O0OOO0O00O0OO .name ,OOO0000OOO00OO00O )#line:220
            print (O000O0OOO0O00O0OO .name ,'账号异常1，ck可能失效')#line:221
            return False #line:222
    def get_read_url (OOOOOOOO0O000OO00 ):#line:223
        O00O00000OOOOO00O =f'{OOOOOOOO0O000OO00.host}/new/get_read_url'#line:224
        O000OO000OO00O0OO =requests .get (O00O00000OOOOO00O ,headers =OOOOOOOO0O000OO00 .headers )#line:225
        OO000O0OO0OO0OOOO =O000OO000OO00O0OO .json ()#line:226
        O0OO0OO00O000OOOO =OO000O0OO0OO0OOOO .get ('jump')#line:228
        OOOO0O0O00OOOO0O0 =parse_qs (urlparse (O0OO0OO00O000OOOO ).query )#line:229
        O0O0000O000O0OO00 =urlparse (O0OO0OO00O000OOOO ).netloc #line:230
        O0O00O00O0O0OO00O =OOOO0O0O00OOOO0O0 .get ('iu')[0 ]#line:231
        print (O0O00O00O0O0OO00O )#line:232
        O0OOO00O000OO00OO ={'Host':O0O0000O000O0OO00 ,'User-Agent':OOOOOOOO0O000OO00 .User_Agent ,'X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':O0OO0OO00O000OOOO ,'Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9',}#line:241
        print (O0OO0OO00O000OOOO )#line:242
        O000OO000OO00O0OO =requests .get (O0OO0OO00O000OOOO ,headers =O0OOO00O000OO00OO )#line:243
        O0OOO00O000OO00OO .update ({'Cookie':f'PHPSESSID={O000OO000OO00O0OO.cookies.get("PHPSESSID")}'})#line:244
        return O0O00O00O0O0OO00O ,O0O0000O000O0OO00 ,O0OOO00O000OO00OO #line:245
    def do_read (O00O00O0OOO0000O0 ):#line:247
        O0O000OO00O0OO0O0 =O00O00O0OOO0000O0 .get_read_url ()#line:248
        O00O00O0OOO0000O0 .jkey =''#line:249
        O00OOO0OOOO0OOO0O =0 #line:250
        while True :#line:251
            O00O00O0OOO0000O0 .tuijian ()#line:252
            O0O0000OO00OO00O0 =f'?for=&zs=&pageshow&r={round(random.uniform(0, 1), 17)}&iu={O0O000OO00O0OO0O0[0]}{O00O00O0OOO0000O0.jkey}'#line:253
            O0O000O00OOO0000O =f'http://{O0O000OO00O0OO0O0[1]}/tuijian/do_read{O0O0000OO00OO00O0}'#line:254
            O00O00O0OOO0000O0 .printjson (O0O000O00OOO0000O )#line:255
            O0OO0OO0O0OOO00O0 =requests .get (O0O000O00OOO0000O ,headers =O0O000OO00O0OO0O0 [2 ])#line:256
            print (O00O00O0OOO0000O0 .name ,'-'*50 )#line:257
            print (O0OO0OO0O0OOO00O0 .text )#line:258
            O00O00OOO0O0O0OO0 =O0OO0OO0O0OOO00O0 .json ()#line:259
            if O00O00OOO0O0O0OO0 .get ('msg'):#line:260
                print (O00O00O0OOO0000O0 .name ,'弹出msg',O00O00OOO0O0O0OO0 .get ('msg'))#line:261
            O0O0000O00OOOO0OO =O00O00OOO0O0O0OO0 .get ('url')#line:262
            O00O00O0OOO0000O0 .printjson (O0O0000O00OOOO0OO )#line:263
            if O0O0000O00OOOO0OO =='close':#line:264
                print (O00O00O0OOO0000O0 .name ,f'阅读结果：{O00O00OOO0O0O0OO0.get("success_msg")}')#line:265
                return True #line:266
            if 'weixin'in O0O0000O00OOOO0OO :#line:267
                O00OOO0OOOO0OOO0O +=1 #line:268
                print (O00O00O0OOO0000O0 .name ,f'上一篇阅读结果：{O00O00OOO0O0O0OO0.get("success_msg","开始阅读或者异常")}')#line:269
                OOOO00O000000O00O =O00O00OOO0O0O0OO0 .get ('jkey')#line:270
                O00O00O0OOO0000O0 .jkey =f'&jkey={OOOO00O000000O00O}'#line:271
                OO0OO0O0OOOOO0OOO =getinfo (O0O0000O00OOOO0OO )#line:272
                if O00OOO0OOOO0OOO0O in push_num :#line:273
                    O00OOO00OO00O0O00 =list (OO0OO0O0OOOOO0OOO )#line:274
                    O00OOO00OO00O0O00 [4 ]='oneischeck'#line:275
                    if O00O00O0OOO0000O0 .testCheck (O00OOO00OO00O0O00 ,O0O0000O00OOOO0OO )==False :#line:276
                        return False #line:277
                else :#line:278
                    if O00O00O0OOO0000O0 .testCheck (OO0OO0O0OOOOO0OOO ,O0O0000O00OOOO0OO )==False :#line:279
                        return False #line:280
                if O00O00O0OOO0000O0 .count >=5 :#line:282
                    print (O00O00O0OOO0000O0 .name ,'过检测超过4次中止阅读')#line:283
                    return False #line:284
                OO0000000O000O0OO =random .randint (6 ,9 )#line:285
                print (O00O00O0OOO0000O0 .name ,f'本次模拟读{OO0000000O000O0OO}秒')#line:286
                time .sleep (OO0000000O000O0OO )#line:287
            else :#line:288
                print (O00O00O0OOO0000O0 .name ,'未知结果')#line:289
                print (O00O00O0OOO0000O0 .name ,O00O00OOO0O0O0OO0 )#line:290
                break #line:291
    def testCheck (OO00O0OOO00OO0000 ,OO0000OOO0O0OO0OO ,OOO0OOOO0OOO00O0O ):#line:292
        if OO0000OOO0O0OO0OO [4 ]==[]:#line:293
            print (OO00O0OOO00OO0000 .name ,'这个链接没有获取到微信号id',OOO0OOOO0OOO00O0O )#line:294
            return True #line:295
        if (checkDict .get (OO0000OOO0O0OO0OO [4 ])!=None )or (int (time .time ())-int (OO0000OOO0O0OO0OO [5 ])>60 *60 *24 *30 ):#line:296
            OO00O0OOO00OO0000 .count +=1 #line:297
            if OO00O0OOO00OO0000 .setstatus ()==99 :#line:298
                print (OO00O0OOO00OO0000 .name ,'过检测服务器异常，使用无回调方案，请在50s内阅读检测文章')#line:299
                push (f'可乐阅读过检测:{OO00O0OOO00OO0000.name}',OOO0OOOO0OOO00O0O ,OO0000OOO0O0OO0OO [3 ],'zhyd',OO00O0OOO00OO0000 .uids ,OO00O0OOO00OO0000 .key )#line:300
                time .sleep (50 )#line:301
                return True #line:302
            for OO0O00OO0O0OOOOO0 in range (60 ):#line:303
                if OO0O00OO0O0OOOOO0 %30 ==0 :#line:304
                    OO0000OOOOOOOO00O =f'http://175.24.153.42:8882/lookwxarticle?key=KEY&type=TYPE&wxurl={OOO0OOOO0OOO00O0O}'#line:305
                    push (f'可乐阅读过检测:{OO00O0OOO00OO0000.name}',OO0000OOOOOOOO00O ,OO0000OOO0O0OO0OO [3 ],'zhyd',OO00O0OOO00OO0000 .uids ,OO00O0OOO00OO0000 .key )#line:306
                OOO00O000O000OOOO =OO00O0OOO00OO0000 .getstatus ()#line:307
                if OOO00O000O000OOOO =='0':#line:308
                    print (OO00O0OOO00OO0000 .name ,'过检测文章已经阅读')#line:309
                    return True #line:310
                elif OOO00O000O000OOOO =='1':#line:311
                    print (OO00O0OOO00OO0000 .name ,f'正在等待过检测文章阅读结果{OO0O00OO0O0OOOOO0}秒。。。')#line:312
                    time .sleep (1 )#line:313
                else :#line:314
                    print (OO00O0OOO00OO0000 .name ,OOO00O000O000OOOO )#line:315
                    print (OO00O0OOO00OO0000 .name ,'服务器异常')#line:316
                    return False #line:317
            print (OO00O0OOO00OO0000 .name ,'过检测超时中止脚本防止黑号')#line:318
            return False #line:319
        else :#line:320
            return True #line:321
    def withdrawal (OOOOOO0000O000OO0 ):#line:322
        OOO0O0O0O00OO0O00 =f'{OOOOOO0000O000OO0.host}/withdrawal'#line:323
        OO000OOOO0OO000OO =requests .get (OOO0O0O0O00OO0O00 ,headers =OOOOOO0000O000OO0 .headers )#line:324
        O00O000OOOOO0000O =OO000OOOO0OO000OO .json ()#line:325
        time .sleep (3 )#line:326
        if O00O000OOOOO0000O .get ('code')==0 :#line:327
            OOOOO00OOO0000O00 =int (float (O00O000OOOOO0000O ['data']['user']['score']))#line:328
            if OOOOO00OOO0000O00 >=2000 :#line:329
                OOOOO00OOO0000O00 =2000 #line:330
            OO0OO0O0OO00OO000 =OOOOOO0000O000OO0 .headers .copy ()#line:331
            OO0OO0O0OO00OO000 .update ({'Content-Type':'application/x-www-form-urlencoded'})#line:332
            OOO0O0O0O00OO0O00 =f'{OOOOOO0000O000OO0.host}/withdrawal/doWithdraw'#line:333
            OO0O00OO0O0O0O0O0 =f'amount={OOOOO00OOO0000O00}&type=wx'#line:334
            OO000OOOO0OO000OO =requests .post (OOO0O0O0O00OO0O00 ,headers =OO0OO0O0OO00OO000 ,data =OO0O00OO0O0O0O0O0 )#line:335
            print (OOOOOO0000O000OO0 .name ,'提现结果',OO000OOOO0OO000OO .text )#line:336
        else :#line:337
            print (OOOOOO0000O000OO0 .name ,O00O000OOOOO0000O )#line:338
    def run (OOO00OOOOO000O00O ):#line:339
        if hashlib .md5 (oo0o .encode ()).hexdigest ()!='e00d9b235da07e11c89608f0fc8c8e36':OOO00OOOOO000O00O .setstatus ()#line:340
        if OOO00OOOOO000O00O .tuijian ():#line:341
            OOO00OOOOO000O00O .do_read ()#line:342
            time .sleep (2 )#line:343
            OOO00OOOOO000O00O .withdrawal ()#line:344
def getEnv (O000O0O0OO0000O00 ):#line:345
    OOOO0O00OOOOOOOO0 =os .getenv (O000O0O0OO0000O00 )#line:346
    if OOOO0O00OOOOOOOO0 ==None :#line:347
        print (f'{O000O0O0OO0000O00}青龙变量里没有获取到，使用本地参数')#line:348
        return False #line:349
    try :#line:350
        OOOO0O00OOOOOOOO0 =json .loads (OOOO0O00OOOOOOOO0 .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:351
        return OOOO0O00OOOOOOOO0 #line:352
    except Exception as O00OOO0OOOOOO0000 :#line:353
        print ('错误:',O00OOO0OOOOOO0000 )#line:354
        print ('你填写的变量是:',OOOO0O00OOOOOOOO0 )#line:355
        print ('请检查变量参数是否填写正确')#line:356
        print (f'{O000O0O0OO0000O00}使用本地参数')#line:357
if __name__ =='__main__':#line:358
    loc_push_config = {"printf": 0, "threadingf": 0, "appToken": "AT_9KCY75iQ8vL4qFkqkbHOrJxgwpxyu6JC"}
    loc_klydconfig = [
        {'name': '备注名1','cookie': 'PHPSESSID=984abblg4d47safdus6h058f2r; udtauth3=eaadRFN5fYhOJSP670thpBTlvRor3x2VfQAgUlS%2BRCRIHA9xcS6ctOt3OrkkoUE4bI0ir7PxcKZyw4VZbOozmOIaqRKPFPMlwDyUutr4qqB8guxycYXaJHrokWHBnJ5VTT3Z2cdrRPGfY45ykTkAxNEJudiuhTNlYaveV6wUH10','key': '4e9b969fd348c5e8a0cce5f451f2a78a', 'uids': 'UID_qiTw3K1TOPPsyO85poTwGbrpZOvH'},
        # {'name':'zh','cookie':'PHPSESSID=dp1xxxxxc; udtauth3=adxxxx','key':'xxxxx','uids':'xxxx','User_Agent':'xxxxx'},
    ]
    # --------------------------------------------------------
    push_config = getEnv('push_config')
    if push_config == False: push_config = loc_push_config
    print(push_config)
    klydconfig = getEnv('klydconfig')
    if klydconfig == False: klydconfig = loc_klydconfig
    print(klydconfig)
    printf = push_config.get('printf', 0)  # 打印调试日志0不打印，1打印，若运行异常请打开调试
    appToken = push_config['appToken']  # 这个是填wxpusher的appToken
    threadingf = push_config.get('threadingf', 1)
    getmsg()
    if threadingf == 1:
        tl = []
        for cg in klydconfig:
            print('*' * 50)
            print(f'开始执行{cg["name"]}')
            api = WXYD(cg)
            t = threading.Thread(target=api.run, args=())
            tl.append(t)
            t.start()
            threadingt = push_config.get('threadingt', 3)
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
