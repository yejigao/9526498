'''
new Env('天瑞地安');
BY:YourAhTzu
日期:1.31 15:15
抓authorization填入trda变量多号@
'''
import requests
import os
def info(authorization):
    print("开始获取用户")
    url = "https://crm.rabtv.cn/v2/index/userInfo"
    headers = {
        "Host": "crm.rabtv.cn",
        "authorization": authorization,
        "user-agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36;xsb_ruian;xsb_ruian;2.31.744;native_app;6.7.0",
        "accept": "*/*",
        "origin": "https://crm.rabtv.cn",
        "x-requested-with": "com.test.android.app.ruian",
        "referer": "https://crm.rabtv.cn/sign/index.html",
    }

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        total_sign_num_in_month = response_data["data"]["total_sign_num_in_month"]
        beauty_mobile = response_data["data"]["beauty_mobile"]
        print(f"用户:{beauty_mobile}已签到:{total_sign_num_in_month}天")
    else:
        print("获取用户信息失败")
def signin(authorization):
    print("开始执行签到")
    url = "https://crm.rabtv.cn/v2/index/signIn"
    headers = {
        "Host": "crm.rabtv.cn",
        "authorization": authorization,
        "user-agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36;xsb_ruian;xsb_ruian;2.31.744;native_app;6.7.0",
        "accept": "*/*",
        "origin": "https://crm.rabtv.cn",
        "x-requested-with": "com.test.android.app.ruian",
        "referer": "https://crm.rabtv.cn/sign/index.html",
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data["code"] == 1:
            score = data["data"]["score"]
            print(f"恭喜获得: {score} 积分")
        else:
            msg = data["msg"]
            print(f"签到失败: {msg}")
    else:
        print("签到请求失败")
if __name__ == "__main__":
    authorizations = os.environ.get('trda') 
    if not authorizations:
        print("获取账号失败，检查是否配置正确")
    else:
        tokens_list = authorizations.split('@')
        num = len(tokens_list)
        print(f"=====成功获取到{num}个账号=====")   
        for num, authorization in enumerate(tokens_list, start=1):
            print(f"=====开始执行第{num}个账号任务=====")
            info(authorization)
            signin(authorization)
            print("==============================")
