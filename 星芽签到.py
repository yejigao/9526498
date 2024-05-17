import requestsimport
import jsondef 
handler(event, context):   
    url1 = "https://app.whjzjx.cn/v1/account/login" #登录激活今日签到机会  
   cookie = "eyJhbxxxxx"   
    headers = {        "Content-Type":"application/json;charset=UTF-8",        "Accept": "application/json, text/plain, */*",        "User-Agent": "Mozilla/5.0 (Linux; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.186 Mobile Safari/537.36",       
     "Cookie": cookie,    }  
       response1 = requests.post(url=url1, data='{}', headers=headers) #{"code":"200","message":"成功","data":{"useChance":0,"chance":1}}   
        res1 = (response1.json()).get("message")    returnMes= f"-->>当前状态: {res1}"    #发送微信消息  
          token = 'xxxxx' 
          #在pushpush网站中可以找到  
            title= f"签到结果{res1} " #改成你要的标题内容    
            content =res1 #改成你要的正文内容  
              url = 'http://www.pushplus.plus/send'   
               data = {        "token":token,        "title":title,        "content":content    }   
                body=json.dumps(data).encode(encoding='utf-8')    headers = {'Content-Type':'application/json'}   
                 requests.post(url,data=body,headers=headers) 
                        return res1