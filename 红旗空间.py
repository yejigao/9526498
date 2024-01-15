'''
红旗空间小程序
变量名：hqkjck，抓包Cookie中的JSESSIONID=XXX
定时：0 7 * * *
'''
import os,requests
ck=os.getenv('hqkjck')
resp=requests.get('https://hqpp-gw.faw.cn/gimc-hongqi-webapp/f/checkin/user-checkin',headers={'Cookie':ck}).json()
msg=resp['msg']
if msg=='success':
    print('签到成功！')
else:
    print(msg)