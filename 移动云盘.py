#下载链接https://caiyun.feixin.10086.cn:7071/portal/cloudItem/index.html?path=acceptInvite&id=qyntuolmW66KgfaJ1%2BV1roPEBadE05REBGDyinS9bRE%3D0001705658809595&phone=152****1801
# 功能：签到 每日任务 撸会员
# 抓包 Cookie：任意Authorization
# 变量格式：export ydypCk= authorization#手机号 多个账号用 @ 隔开
# Draw = 1 抽奖次数，每天首次免费， 每天可抽次数50，draw=1，只会抽奖一次
# num = 15 摇一摇，戳一戳次数
# 每日任务
# 先自行上传一个文件，抓/richlifeApp/devapp/IUploadAndDownload请求体中parentCatalogID的值，这是上传到哪个磁盘的id，不填默认根目录
# 进入笔记，找到任意请求头中含有NOTE_TOKEN，抓取NOTE_TOKEN和APP_AUTH值填入
# 定时：一天两三次
import os
import random
import time

import requests

cookies = os.getenv("ydypCk")
ua = 'com.ss.android.ugc.live/250301 (Linux; U; Android 10; zh_CN; MI 8; Build/QKQ1.190828.002; Cronet/TTNetVersion:8e43839d 2023-03-22 QuicVersion:6ea2111b 2023-03-16)'  
note_token = 'djF8dDF8OUVCNDlEMzAwMzI0NEI2N0Y1QUE3MzYzOTA4NDU1RUU4RkU5MkM4MEQ0NUM5MDkwMUMxOENBNThGQTgzQzRBRUJGM0QzRTQwRjI0MTBCODZFNjBDQjU3QUMyMTlDMDlE'
note_auth = 'Basic MTcyNjIxMjU2NDA6cXZGcVF0a0V8MXxSQ1N8MTY5NjM0MjM1NjI4M3xIRTJma1ZEdmVXMnQ4UWV3anpGMFNRWlEueWtpZTR5SkRscS5lc2lXZTg1ejgxeEJHeEVIV3Mxa3Q1RWJuWGY3aWtMZEtBX2gubXdILkU1TUtjUy5JR0FCUG1iU1BibjByUXIxaUIyNUsxNHJoWnNYTHk1WmlkVVpfMFVtb1UxMTFGWVN1NzJHbXJDMlNlMDFqclZncFVsOTVDOGpMQzF3S2Jldnd4bjZrX3Mt'
parent_catalogid = ''  # 上传文件的父文件夹id，不填默认根目录


class YP:
    token = None
    jwtToken = None
    notebook_id = None
    draw = 1
    num = 25
    timestamp = str(int(round(time.time() * 1000)))
    cookies = {'sensor7s_stay_time': timestamp}

    def __init__(self, cookie):
        self.Authorization = cookie.split('#')[0]
        self.account = cookie.split('#')[1]
        self.jwtHeaders = {
            'User-Agent': ua,
            'Accept': '*/*',
            'Host': 'caiyun.fheixin.10086.cn:7071',
        }

    def run(self):
        self.sso()
        self.jwt()
        self.signin_status()
        self.click()
        print(f'\n---每日任务---')
        self.get_tasklist()
        print(f'\n---公众号任务---')
        self.wxsign()
        self.shake()
        self.surplus_num()
        self.receive()

    def send_request(self, url, headers, data=None, method='GET', cookies=None):
        with requests.Session() as session:
            session.headers.update(headers)
            if cookies is not None:
                session.cookies.update(cookies)

            try:
                if method == 'GET':
                    response = session.get(url, timeout = 10)
                elif method == 'POST':
                    response = session.post(url, json = data, timeout = 10)
                else:
                    raise ValueError('Invalid HTTP method.')

                response.raise_for_status()
                return response.json()

            except requests.Timeout as e:
                print("请求超时:", str(e))

            except requests.RequestException as e:
                print("请求错误:", str(e))

            except Exception as e:
                print("其他错误:", str(e))

    # 随机延迟默认1-1.5s
    def sleep(self, min_delay=1, max_delay=1.5):
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)

    # 刷新令牌
    def sso(self):
        url = 'https://orches.yun.139.com/orchestration/auth-rebuild/token/v1.0/querySpecToken'
        headers = {
            'Authorization': self.Authorization,
            'User-Agent': ua,
            'Contentg-Type': 'application/json',
            'Accept': '*/*',
            'Host': 'orches.yun.139.com'
        }
        data = {"account": self.account, "toSourceId": "001005"}
        return_data = self.send_request(url, headers = headers, data = data, method = 'POST')
        self.sleep()
        if 'success' in return_data:
            if return_data['success']:
                self.token = return_data['data']['token']
            else:
                print(return_data['message'])
        else:
            print("出现未知错误")

    # 获取jwttoken
    def jwt(self):
        url = f"https://caiyun.feixin.10086.cn:7071/portal/auth/tyrzLogin.action?ssoToken={self.token}"
        return_data = self.send_request(url = url, headers = self.jwtHeaders, method = 'POST')
        self.sleep()
        if return_data['code'] != 0:
            return print(return_data['msg'])
        self.jwtToken = return_data['result']['token']
        self.jwtHeaders['jwtToken'] = self.jwtToken
        self.cookies['jwtToken'] = self.jwtToken

    # 签到查询
    def signin_status(self):
        url = 'https://caiyun.feixin.10086.cn/market/signin/page/info?client=app'
        return_data = self.send_request(url, headers = self.jwtHeaders, cookies = self.cookies)
        self.sleep()
        if return_data['msg'] == 'success':
            today_sign_in = return_data['result'].get('todaySignIn', False)

            if today_sign_in:
                return print('已经签到了')
            else:
                print('未签到，去签到')
                config_url = 'https://caiyun.feixin.10086.cn/market/manager/commonMarketconfig/getByMarketRuleName?marketName=sign_in_3'
                config_data = self.send_request(config_url, headers = self.jwtHeaders, cookies = self.cookies)

                if config_data['msg'] == 'success':
                    print('签到成功')
                else:
                    print(config_data['msg'])
        else:
            print(return_data['msg'])

    # 戳一下
    def click(self):
        url = "https://caiyun.feixin.10086.cn/market/signin/task/click?key=task&id=319"
        for _ in range(self.num):
            return_data = self.send_request(url, headers = self.jwtHeaders, cookies = self.cookies)
            self.sleep()
            if 'result' in return_data:
                print(f'{return_data["result"]}')
            elif return_data.get('msg') == 'success':
                print('未获得')

    # 任务列表
    def get_tasklist(self):
        url = 'https://caiyun.feixin.10086.cn/market/signin/task/taskList?marketname=sign_in_3'
        return_data = self.send_request(url, headers = self.jwtHeaders, cookies = self.cookies)
        self.sleep()
        task_list = return_data.get('result', {}).get('day', [])

        for value in task_list:
            task_id = value.get('id')
            if task_id == 404:
                continue
            task_name = value.get('name')
            task_status = value.get('button', {}).get('out', {}).get('text')

            if task_status == '已完成':
                print(f'已完成: {task_name}')
                continue
            print(f'去完成: {task_name}')
            self.day_task(task_id)

    def day_task(self, task_id):
        url = f'https://caiyun.feixin.10086.cn/market/signin/task/click?key=task&id={task_id}'
        return_data = self.send_request(url, headers = self.jwtHeaders, cookies = self.cookies)
        self.sleep()
        if return_data['msg'] != 'success':
            return print(return_data['msg'])
        if task_id == 106:
            print('开始上传文件，默认0kb')
            self.updata_file()
        elif task_id == 107:
            print('获取默认笔记id')
            note_url = 'http://mnote.caiyun.feixin.10086.cn/noteServer/api/syncNotebookV3.do'
            headers = {
                'X-Tingyun-Id': 'p35OnrDoP8k;c=2;r=1122634489;u=43ee994e8c3a6057970124db00b2442c::8B3D3F05462B6E4C',
                'Charset': 'UTF-8',
                'Connection': 'Keep-Alive',
                'User-Agent': 'mobile',
                'APbP_CP': 'android',
                'CP_VERSION': '3.2.0',
                'x-huawei-channelsrc': '10001400',
                'APP_NUMBER': self.account,
                'APP_AUTH': note_auth,
                'NOTE_TOKEN': note_token,
                'Host': 'mnote.caiyun.feixin.10086.cn',
                'Content-Type': 'application/json; charset=UTF-8',
                'Accept': '*/*'
            }
            payload = {
                "addNotebooks": [],
                "delNotebooks": [],
                "notebookRefs": [],
                "updateNotebooks": []
            }
            return_data = self.send_request(url = note_url, headers = headers, data = payload,
                                            method = 'POST')
            if return_data is None:
                return print('出错了')
            self.notebook_id = return_data['notebooks'][0]['notebookId']
            print('开始创建笔记')
            self.create_note(headers)

    def updata_file(self):
        url = 'http://ose.caiyun.feixin.10086.cn/richlifeApp/devapp/IUploadAndDownload'
        headers = {
            'x-huawei-uploadSrc': '1',
            'x-ClientOprType': '11',
            'Connection': 'keep-alive',
            'x-NetType': '6',
            'x-DeviceInfo': '6|127.0.0.1|1|10.0.1|Xiaomi|M2012K10C|CB63218727431865A48E691BFFDB49A1|02-00-00-00-00-00|android 11|1080X2272|zh||||032|',
            'x-huawei-channelSrc': '10000023',
            'x-MM-Source': '032',
            'x-SvcType': '1',
            'APP_NUMBER': self.account,
            'Authorization': self.Authorization,
            'X-Tingyun-Id': 'p35OnrDoP8k;c=2;r=1955442920;u=43ee994e8c3a6057970124db00b2442c::8B3D3F05462B6E4C',
            'Host': 'ose.caiyun.feixin.10086.cn',
            'User-Agent': 'okhttp/3.11.0',
            'Content-Type': 'application/xml; charset=UTF-8',
            'Accept': '*/*'
        }
        payload = '''
                            <pcUploadFileRequest>
                                <ownerMSISDN>{phone}</ownerMSISDN>
                                <fileCount>1</fileCount>
                                <totalSize>1</totalSize>
                                <uploadContentList length="1">
                                    <uploadContentInfo>
                                        <comlexFlag>0</comlexFlag>
                                        <contentDesc><![CDATA[]]></contentDesc>
                                        <contentName><![CDATA[000000.txt]]></contentName>
                                        <contentSize>1</contentSize>
                                        <contentTAGList></contentTAGList>
                                        <digest>C4CA4238A0B923820DCC509A6F75849B</digest>
                                        <exif/>
                                        <fileEtag>0</fileEtag>
                                        <fileVersion>0</fileVersion>
                                        <updateContentID></updateContentID>
                                    </uploadContentInfo>
                                </uploadContentList>
                                <newCatalogName></newCatalogName>
                                <parentCatalogID>{parent_catalogid}</parentCatalogID>
                                <operation>0</operation>
                                <path></patbh>
                                <manualRename>2</manualRename>
                                <autoCreatePath length="0"/>
                                <tagID></tagID>
                                <tagType></tagType>
                            </pcUploadFileRequest>
                        '''.format(phone = self.account, parent_catalogid = parent_catalogid)

        response = requests.post(url = url, headers = headers, data = payload)
        if response is None:
            return
        if response.status_code != 200:
            return print('上传失败')
        print('上传成功，快去领取奖励啦')

    def create_note(self, headers):
        note_id = self.get_note_id(32)  # 获取随机笔记id
        createtime = str(int(round(time.time() * 1000)))
        time.sleep(3)
        updatetime = str(int(round(time.time() * 1000)))
        note_url = 'http://mnote.caiyun.feixin.10086.cn/noteServer/api/createNote.do'
        payload = {
            "archived": 0,
            "attachmentdir": note_id,
            "attachmentdirid": "",
            "attachments": [],
            "audioInfo": {
                "audioDuration": 0,
                "audioSize": 0,
                "audioStatus": 0
            },
            "contentid": "",
            "contents": [{
                "contentid": 0,
                "data": "<font size=\"3\">000000</font>",
                "noteId": note_id,
                "sortOrder": 0,
                "type": "RICHTEXT"
            }],
            "cp": "",
            "createtime": createtime,
            "description": "android",
            "expands": {
                "noteType": 0
            },
            "latlng": "",
            "location": "",
            "novteid": note_id,
            "notestatus": 0,
            "remindtime": "",
            "remindtype": 1,
            "revision": "1",
            "sharecount": "0",
            "sharestatus": "0",
            "system": "mobile",
            "tags": [{
                "id": self.notebook_id,
                "orderIndex": "0",
                "text": "默认笔记本"
            }],
            "title": "00000",
            "topmost": "0",
            "updatetime": updatetime,
            "userphone": self.account,
            "versi on": "1.00",
            "visitTime": ""
        }
        return_data = requests.post(note_url, headers = headers, json = payload)
        if return_data.status_code == 200:
            print('创建笔记成功,快去领取奖励啦')
        else:
            print('创建失败')

    def get_note_id(self, length):
        characters = '19f3a063d67e4694ca63a4227ec9a94a19088404f9a28084e3e486b928039a299bf756ebc77aa4f6bfa250308ec6a8be8b63b5271a00350d136d117b8a72f39c5bd15cdfd350cba4271dc797f15412d9f269e666aea5039f5049d00739b320bb9e858504ca6c1426941ec82f22679b3f4b9d140b27c6e91286381cceadb2788529fc6125d74c96e0c820b308a587f941ffd7c9cc35b4a80d33e41ed739d893b61716bd66e77464fa1c6ab9d1422409ae7615b09660acc8e1eacc6cca7069b7979ec326003fe025831704c9df1211d3ed2b3bd97d49887200ce23baaa70be048f9ef875317c81ed2b72234b31fb20dd11e95a00f32480d03ffdbd226cb88f0746233a1f27766dba55e7b8dd59d2fc788eaa897a01db3f3593332574d0a66a0bf3e5bd4baaf46baf0d98a2cb6206c0386ffcce7c3aef88e3fda7429cc2abf91250ae8a269a9a160c04f34192c7dcc25fff37d4a8bbdc0fa0eb10864b11d40d0ec55bba0b41441873f3e11831357ab44b96cab3b69bcbf43da1096c7fc830a63b91713425cb5613130d1f5ebcfd74f71f9febaee7c895271de4e49954ffc6748b825fba0de16e38034c0fccd3e83d064045c9cb27d6a61a23faf07021740f5f273afae38721edd08905ee8eca4ca0d72cda4a076c443087cd14a04e14d53cb581efc276b6f7cfe747841536d0d3fea1b9aba07868286fdd768b1d524fa54c576835ac4e7eac9922868e08ef3f78376ca64c4c40c08cb225462ad9abe5e96e355c1fc3477527d8ed265353b1120dc26f16af52f518790555747f876e29ba6768d00cfc531ededbf41a101cfaae3b31dff54922b09b33385e54a1c8c630b2c5a1225a5efad9c4fa4895d6dd43a95b31e64a47873cb28632bca322b75ae7da5c697a74cce6b1bd7de60506342c166bbaf87c3cad8335a25e205116497e9ded94c6e902964645ca4fed889d067497ef56ccb1606ac12fdec94b0e406a01b1aaf42948df326d7f219ed1a5ae297b233bb0112c764c756267cbe1b0bcbc0b25a38bc9aa2936bd16b4cd4ff0a7e4cd1039110a962dbb2b73b89ce56e3097bbeedb90c257c258731e581d97819923ac983d639c6576c2186d65cdb11b3359054df4b546810a7f71decb22649d295cad7030e458562b610b4147676adbb143431e54dbbae5bc67c290fc70911fc1c5f82b1f681c237515716f373c2d6faf503d125bca96fe1fe237d85b17705afd58187b28b6d07174e25d82e2d79a6c3fe1c99de203fbef4baf7a2702d7c752f0b40aff134fc50ee2ec496c33e3c99ab1ce6951be6b8a551a5224f41cd6171b480b086d0dc57da5c30b41a43db262d59b96bd6e8dd8521d4e45c7ec97d84216c2ec36f7b6fb31214b57def5d36767d9060d647cc4914d81ffc16bd4e6eee2285e1bed67360f8304346dbc7eec219e07bccd54b24f297d2d1950c00f84b76681f6bc57dca03a2abeed01db651fb69cad74ca02e8cc16f8b4b1cca7f4925475237190a850e9b2e656824f3dff796868a185d18813d1d05d46421d1c55ce6aadf846e866f42cb0ac9c2e56f2c0564998d1afa60b91f1855874643b309fe982ff540f2ac2178b7fea52bc854f788dea089141275f4734be5314356b254f583195ee447c6b4ddaa371ce55e918fe1e56342fa175784043b4c83e38adf5acb8f36ed6f50c41f5e4dbe6fccf393a21b3cb5575ce13d813da689011f9bbd62704b73eea51d9195e84e9353596e2180c59fc56d776f5f7230ec5cd68d8d491f848f2eb910b3926cf70f6efc4b82622c43146c5ec7fa31de49a6117e9c1f5dba64dc0bffe0ec73d19b7ac17d061bd3de75a2384489bbc9c7c51469423790414726c2aee7af8d5908445ce31792d133f09bc2ed3ec9875a2dae9f382614b32c6e840d3dc4cbb009186f9ed6d756d66da71023eab8fd5daf42f51a99a4155a170ead43f925cf33562c9d0e21fcc7a3d18e096387e3cd915c1d696daead197fb9902f6fb27ef3f1f5bdcb0adc995429dcd94a83862f96545383ec6fe0353f3e964e12d332626c680a8fa02afd9d9c43f4cd04b3e348e031be02946ef783aa0847b71dac5a360f4fd3fb484ee72cedfba63d7e9713949f0b4f1e9e11e5966f849f48b1fcb34879a9c00c63224095a17c7e177ab2274ea524de88e80b40464d63bcedf92f74356fa2504b3018a6c68300ebcc74ea3b1300c140cea0fd0bcf338eeef3e75701812e3ba7c4776961f37622d993e039991660d6ef95d3d7eedcb0bda15d302b30a35c31d060562cd92944fa973c8b5cf2fa008b52c1cbd86970cae9476446f3e41871de8d9f6112db94b05e5dc7ea0a942a9daf145ac8e487d3d5cba7cea145680efc64794d43dd15c5062b81e1cda7bf278b9bc4e1b8955846e6bc4b6a61c28f831f81b2270289e5a8a677c3141ddc9868129060c0c3b5ef507fbd46c004f6de346332ef7f05c0094215eae1217ee7c13c8dca6d174cfb49c716dd42903bb4b02d823b5f1ff93c3f88768251b56cc8b12650b441e6f998a1719cd17ade7980fb1558b5a5592bn0fc378ae21302d241991c0576870e3a037bfed4c5f356daf0a00f9527fe9d8e5209d0d22ab0a194c36a4f1d9bfa6dbf727c23c8b7a59a2fdbf379b9085a1b675bbae2c58b47391e89db727ef29c5c9cd7339c9c8a6db77d448fb62890d454201ee5a7f70935ce01e1ddba5053acf00dfb1d5dd7cfc35c501d69054c04734cdae8800c128b31bf0e414d4c9a7d4a2a6f9a451d0db885ccd3e8a3fd5d25e6a09e79b49b5936971f43cf8fbbb586676a888efe85826bcbe163f453e84d097154137f7b7fdf1a68ae0cd77fec6012e836f3efc1c8577e6fff8c569f62eef8fc616ffa1c81de765c011a0a5ad0e8ca41312f20232dee8f4ad178389734fc1324aa3d6844e5d632841dc09ac1d979154a0c374ba5f57c9123cc72096392102ce584afbd9272c1d4d2ca4213fcd9d1f22279995cebe9f757955fa5702fd4d92409e0fee1d02ca8bed860b464b03eae83fe260f2f094f731b3cfa2f82e7a1994bb74882231eba39c0a6c3a9b00ed4c52018835bd509ace44bf5a197b0bb74387a10987d7b07d1de99d5ad5cf8359794797799802a3114529beb44834b0193e4e709d1981547a2a29099d5ef748b6acaff5db578810c98fa53a108aee950c7997e62e1344cec608597aeb082f3bca7884a9ecfcabd1beb3f8e01a781e088e4fba02ce89944f45a272139827f8e4dfee8202dd4dc21f48c9e28949a3cb1bf0f32880b855efce328874542a1cfd487c3be42a182e302e8e8c394f407226cc9595c1512c976ae432d49dfcd8dc140ef94e03414a967f96655fd13a060a5da0c6fe36ba82dc8493716e1f22558e93c5bbd15cb8b35ff306b756bf858ff4a91f0e347a07d75cd039b38abf9c65d3730d0f5a8b7fe6864e5c3c50bc62f1797dce078c9f042b14bd5516791679c399348d9925842f5c580a2878e69af52e1dc16ea80ea3ffd1865416aaceb23bd07173b2e7cdafc7e423b85f0cac6e1e0490be44'
        note_id = ''.join(random.choice(characters) for _ in range(length))
        return note_id

    # 公众号签到
    def wxsign(self):
        url = 'https://caiyun.feixin.10086.cn/market/playoffic/followSignInfo?isWx=true'
        return_data = self.send_request(url, headers = self.jwtHeaders, cookies = self.cookies)
        self.sleep()
        if return_data['msg'] != 'success':
            return print(return_data['msg'])
        if not return_data['result'].get('todaySignIn'):
            return print('签到失败')
        return print('签到成功')

    # 摇一摇
    def shake(self):
        url = "https://caiyun.feixin.10086.cn:7071/market/shake-server/shake/shakeIt?flag=1"
        for _ in range(self.num):
            return_data = self.send_request(url = url, cookies = self.cookies, headers = self.jwtHeaders,
                                            method = 'POST')
            self.sleep()
            shake_prize_config = return_data["result"].get("shakePrizeconfig")
            if shake_prize_config is not None:
                print("⭕摇一摇成功，获得：" + str(shake_prize_config["name"]))
            elif shake_prize_config is None:
                print("未摇中")
            else:
                print("出错了")

    # 查询剩余抽奖次数
    def surplus_num(self):
        draw_info_url = 'https://caiyun.feixin.10086.cn/market/playoffic/drawInfo'
        draw_url = "https://caiyun.feixin.10086.cn/market/playoffic/draw"

        draw_info_data = self.send_request(draw_info_url, headers = self.jwtHeaders)
        self.sleep()
        if draw_info_data.get('msg') == 'success':
            num1 = draw_info_data['result'].get('surplusNumber', 0)
            print(f'---剩余抽奖次数{num1}---')
            if num1 > 50 - self.draw:
                for _ in range(self.draw):
                    draw_data = self.send_request(url = draw_url, headers = self.jwtHeaders)
                    self.sleep()
                    if draw_data.get("code") == 0:
                        prize_name = draw_data["result"].get("prizeName", "")
                        print("⭕ 抽奖成功，获得：" + prize_name)
                    else:
                        print("❌ 抽奖失败")
            else:
                pass
        else:
            print(draw_inifo_data.get('msg'))

    # 领取云朵
    def receive(self):
        url = "https://caiyun.feixin.10086.cn/market/signin/page/receive"
        return_data = self.send_request(url, headers = self.jwtHeaders, cookies = self.cookies)
        if return_data['msg'] == 'success':
            receive_amount = return_data["result"].get("receive", "")
            total_amount = return_data["result"].get("total", "")
            print(f'当前待领取:{receive_amount}云朵')
            print(f'当前云朵数量:{total_amount}云朵')
        else:
            print(return_data['msg'])


if __name__ == "__main__":
    cookies = cookies.split('@')
    ydypqd = f"移动硬盘共获取到{len(cookies)}个账号"
    print(ydypqd)
    for i, cookie in enumerate(cookies, start = 1):
        print(f"\n======== ▷ 第 {i} 个账号 ◁ ========")
        YP(cookie).run()
        # print("\n随机等待5-10s进行下一个账号")
        # time.sleep(random.randint(5, 10))
