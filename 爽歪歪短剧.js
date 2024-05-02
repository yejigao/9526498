/**
 * @Time: 2024/4/27 下午2:40
 * @Author: 魂焱
 * @File: 爽歪歪短剧.js
 * @Software: WebStorm
 * @Description: 变量名 syyCookie 抓admin.yunhuikunpeng.com请求的authorization 多号用&分割
 * 不知道咋玩的 写了新手任务，签到，观看激励视频,夏日激爽视频
 * 链接 https://admin.yunhuikunpeng.com/appDownload/?promotionCode=96LNB8
 * 有条件的最好可以填写一下我的推广码 96LNB8  我的-->邀请人ID-->去绑定
 * 脚本运行时如果当前账号未绑定上级，则会自动绑定为我
 */

const $ = new ENV("爽歪歪短剧", ["syyCookie"]);
const {v4: uuidv4} = require('uuid');
const cookieArr = $.syyCookie.split("&");


class SYY {
    constructor(ck, index) {
        this.authorization = ck;
        this.index = ++index;
        this.pubk = `-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoXlZ9Bk+wLScOoyeIgxLSIq10Kiw3pVx2H7YgJLRF3PhRTM9eIwBL2hjPwO6oi9OFMU59/+zw3qq6s5OJ0R9TpwUAs6xPpCsMFniZ2GNl8bsLwznHDFNaz/YrgPC+kZ4bRsFzMeik3nI+/JxMz9/Upilm9me4+mMg7wsjk+SyEIGQXuMaGd8moC8PGYMIKNvZ3lzB2B4INJfu5NFrbE8gCPhGi/HOXL6Wx07dhLgWWttiTe4O8FI9FqehfXYLQqjuw50IDNJtAPoEziR/GVZ8INK2NWEwrQUNBkuS8L1TWwlo4VfYfwiJyvKHM4f/UMmFrHqpXdPGqHt7vnjEQ0iPQIDAQAB
-----END PUBLIC KEY-----`;
    }

    randomTime(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    get header() {
        return {
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; 22081212C Build/UKQ1.230917.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.14 Mobile Safari/537.36',
            'authorization': this.authorization,
            'clientid': '428a8310cd442757ae699df5d894f051',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
    }

    async main() {
        const info = await this.userInfo();
        if (!info) {
            return void 0;
        }
        await this.userWallet();
        if (this.parentId == 0) {
            await this.bindPromotion();
        }
        // await this.userActivate()
        if (this.activateFlag === "N") {
            $.log(`账号[${this.index}]【${this.nickName}】 去做新手任务`)
            await this.userActivate()
            await $.wait(1000)
        }
        $.log(`账号[${this.index}]【${this.nickName}】 获取任务状态`)
        const taskStatus = await this.taskState();
        if (!taskStatus) {
            return void 0;
        }
        let count = taskStatus.count;
        let vipCount = taskStatus.vipCount;
        const maxDate = taskStatus.maxDate;
        let completed = taskStatus.completed;
        let vipCompleted = taskStatus.vipCompleted;
        const maxNum = taskStatus.maxNum;

        $.log(`账号[${this.index}]【${this.nickName}】 已签到${maxNum}天`)
        if (!this.isToday(maxDate)) {
            $.log(`账号[${this.index}]【${this.nickName}】 去签到`)
            await this.signIn();
            await $.wait(2000)
        }
        if (count > completed) {
            $.log(`账号[${this.index}]【${this.nickName}】 去做观看激励视频任务`)
            for (; ;) {
                const result = await this.taskComplate();
                count = result.count;
                completed = result.completed;
                if (count <= completed) {
                    break;
                }
                const randomTime = this.randomTime(60000, 65000);
                $.log(`账号[${this.index}]【${this.nickName}】 等待${randomTime} ms`)
                await $.wait(randomTime);
            }
        } else {
            $.log(`账号[${this.index}]【${this.nickName}】 观看激励视频任务已完成`)
        }

        if (vipCount > vipCompleted) {
            $.log(`账号[${this.index}]【${this.nickName}】 去做夏日激爽视频任务`)
            for (; ;) {
                const result = await this.taskComplateVip();
                vipCount = result.count;
                vipCompleted = result.completed;
                if (vipCount <= vipCompleted) {
                    break;
                }
                const randomTime = this.randomTime(60000, 65000);
                $.log(`账号[${this.index}]【${this.nickName}】 等待${randomTime} ms`)
                await $.wait(randomTime);
            }
        } else {
            $.log(`账号[${this.index}]【${this.nickName}】 夏日激爽视频任务已完成`)
        }

    }

    isToday(inputDateString) {
        const inputDate = new Date(Date.parse(inputDateString));
        const today = new Date();

        return (
            inputDate.getFullYear() === today.getFullYear() &&
            inputDate.getMonth() === today.getMonth() &&
            inputDate.getDate() === today.getDate()
        );
    }

    async userInfo() {
        const options = {
            'method': 'GET',
            'url': 'https://admin.yunhuikunpeng.com/prod-api/appUser/userInfo',
            'headers': this.header
        };
        const res = await $.request(options);
        if (res.code === 200) {
            this.userId = res.data.userId;
            this.openId = res.data.openId;
            this.nickName = res.data.nickName;
            this.parentId = res.data.parentId;
            this.activateFlag = res.data.activateFlag;
            this.membershipEffectiveFlag = res.data.membershipEffectiveFlag;
            return true;
        } else {
            $.log(`获取用户信息失败: ${res.msg}`);
            return false;
        }
    }

    async userWallet() {
        const options = {
            'method': 'GET',
            'url': 'https://admin.yunhuikunpeng.com/prod-api/appUser/userWallet',
            'headers': this.header
        };
        const res = await $.request(options);
        if (res.code === 200) {
            this.reward = res.data.reward;
            this.contribute = res.data.contribute;
            this.contributeGrade = res.data.contributeGrade;
            this.nextLowerLevel = res.data.nextLowerLevel;
            this.balance = res.data.balance;
            this.dividendOne = res.data.dividendOne;
            this.dividendTwo = res.data.dividendTwo;
            $.log(`账号[${this.index}]【${this.nickName}】 贡献币余额：${this.contribute / 100} 距下一等级还差${this.nextLowerLevel / 100} 现金余额：${this.balance / 100}`)
            return true;
        } else {
            $.log(`获取用户信息失败: ${res.msg}`);
            return false;
        }
    }

    async taskState() {
        const options = {
            'method': 'GET',
            'url': 'https://admin.yunhuikunpeng.com/prod-api/appUser/queryTaskState',
            'headers': this.header
        };
        const res = await $.request(options);
        if (res.code === 200) {
            return res.data;
        } else {
            $.log(`获取任务信息失败: ${res.msg}`);
            return false;
        }
    }

    async signIn() {
        const {body, encryptKey} = this.postEncrypt
        const options = {
            'method': 'POST',
            'url': 'https://admin.yunhuikunpeng.com/prod-api/appUser/userSignInMD5',
            'headers': this.header,
            body: body
        };
        options.headers["content-type"] = "text/plain;charset=utf-8";
        options.headers["encrypt-key"] = encryptKey;
        // console.log(options)
        const res = await $.request(options);
        // console.log(res)
        if (res.code === 200) {
            $.log(`账号[${this.index}]【${this.nickName}】 签到成功`)
            return res.data;
        } else {
            $.log(`签到失败: ${res.msg}`);
            return false;
        }
    }

    async userActivate() {
        // let RSAUtils = Java.use("com.smart.shortvideo.util.RSAUtils");
        // RSAUtils["encryptDataByPublicKey"].implementation = function (bArr, publicKey) {
        //     console.log(`RSAUtils.encryptDataByPublicKey is called: bArr=${bArr}, publicKey=${publicKey}`);
        //     let result = this["encryptDataByPublicKey"](bArr, publicKey);
        //     console.log(`RSAUtils.encryptDataByPublicKey result=${result}`);
        //     return result;
        // };
        // let RSAUtils = Java.use("com.smart.shortvideo.util.RSAUtils");
        // RSAUtils["processData"].implementation = function (bArr, key, i) {
        //     console.log(`RSAUtils.processData is called: bArr=${bArr}, key=${key}, i=${i}`);
        //     let result = this["processData"](bArr, key, i);
        //     console.log(`RSAUtils.processData result=${result}`);
        //     return result;
        // };
        const {body, encryptKey} = this.postEncrypt
        const options = {
            'method': 'POST',
            'url': 'https://admin.yunhuikunpeng.com/prod-api/appUser/userActivateMD5',
            'headers': this.header,
            'body': body
        };
        options.headers["content-type"] = "text/plain;charset=utf-8";
        options.headers["encrypt-key"] = encryptKey;
        // console.log(options)
        const res = await $.request(options);
        // console.log(res)
        if (res.code === 200) {
            $.log(`账号[${this.index}]【${this.nickName}】 做新手任务成功`)
            return true;
        } else {
            $.log(`做新手任务失败: ${res.msg}`);
            return false;
        }
    }

    async taskComplate() {
        const {body, encryptKey} = this.postEncrypt
        const options = {
            'method': 'POST',
            'url': 'https://admin.yunhuikunpeng.com/prod-api/appUser/taskCompletedMD5',
            'headers': this.header,
            'body': body
        };
        options.headers["content-type"] = "text/plain;charset=utf-8";
        options.headers["encrypt-key"] = encryptKey;
        const res = await $.request(options);
        if (res.code === 200) {
            $.log(`账号[${this.index}]【${this.nickName}】 做任务观看激励视频成功`)
            return res.data;
        } else {
            $.log(`做任务观看激励视频失败: ${res.msg}`);
            return false;
        }
    }

    async taskComplateVip() {
        const {body, encryptKey} = this.postEncrypt
        const options = {
            'method': 'POST',
            'url': 'https://admin.yunhuikunpeng.com/prod-api/appUser/taskCompletedVipMD5',
            'headers': this.header,
            'body': body
        };
        options.headers["content-type"] = "text/plain;charset=utf-8";
        options.headers["encrypt-key"] = encryptKey;
        const res = await $.request(options);
        // console.log(res)
        if (res.code === 200) {
            $.log(`账号[${this.index}]【${this.nickName}】 做任务夏日激爽视频成功`)
            return res.data;
        } else {
            $.log(`做任务夏日激爽视频失败: ${res.msg}`);
            return false;
        }
    }

    async bindPromotion() {
        const options = {
            'method': 'POST',
            'url': 'https://admin.yunhuikunpeng.com/prod-api/appUser/bindPromotion',
            'headers': this.header,
            form: {
                'promotionCode': '96LNB8'
            }
        };
        try {
            await $.request(options);
        } catch (e) {

        }
    }

    get postEncrypt() {
        const bodyMd5 = $.md5(this.userId + this.openId)
        const key = uuidv4().replaceAll("-", "");
        const body = $.aesECBEncrypt(bodyMd5, key);
        const encryptKey = $.rsaPublicEncrypt(Buffer.from(key, "utf8").toString("base64"), this.pubk)
        // console.log(key)
        return {
            body,
            encryptKey
        }
    }
};

(async () => {
    const syy = [];
    for (const index in cookieArr) {
        syy.push(new SYY(cookieArr[index], index));
    }

    for (const syyElement of syy) {
        try {
            await syyElement.main();
        } catch (e) {
            console.log(e)
        }
    }
})();

function ENV(name, envNames) {
    const request = require("request");
    const cryptoJS = require("crypto-js");
    return new class {
        constructor(name, envNames = []) {
            this.name = name;
            this.envNames = envNames;
            this.startTime = Date.now();
            this.logs = [];
            if (this.envNames.length > 0) {
                for (const envName of envNames) {
                    this[envName] = process.env[envName];
                }
            }
            this.log(`🔔${this.name},开始！`)
        }

        log(...args) {
            args.length > 0 && (this.logs = [...this.logs, ...args])
            console.log(...args)
        }

        md5(str) {
            return cryptoJS.MD5(str).toString()
        }

        sha256(str) {
            return cryptoJS.SHA256(str).toString()
        }

        aesCBCEncrypt(data, key, iv) {
            const n = cryptoJS.enc.Hex.parse(key);
            const r = cryptoJS.enc.Hex.parse(iv);
            const o = cryptoJS.AES.encrypt(data, n, {
                iv: r,
                mode: cryptoJS.mode.CBC,
                padding: cryptoJS.pad.Pkcs7
            });
            return cryptoJS.enc.Base64.stringify(o.ciphertext);
        }

        aesCBCDecrypt(data, key, iv) {
            const n = cryptoJS.enc.Hex.parse(key);
            const r = cryptoJS.enc.Hex.parse(iv);
            const o = cryptoJS.AES.decrypt(data, n, {
                iv: r,
                mode: cryptoJS.mode.CBC,
                padding: cryptoJS.pad.Pkcs7
            });
            return o.toString(cryptoJS.enc.Utf8);
        }

        aesECBEncrypt(data, key) {
            const n = cryptoJS.enc.Utf8.parse(key);
            const o = cryptoJS.AES.encrypt(data, n, {
                mode: cryptoJS.mode.ECB,
                padding: cryptoJS.pad.Pkcs7
            });
            return cryptoJS.enc.Base64.stringify(o.ciphertext);
        }

        aesECBDecrypt(data, key) {
            const n = cryptoJS.enc.Utf8.parse(key);
            const o = cryptoJS.AES.decrypt(data, n, {
                mode: cryptoJS.mode.ECB,
                padding: cryptoJS.pad.Pkcs7
            });
            return o.toString(cryptoJS.enc.Utf8);
        }

        rsaPublicEncrypt(data, publicKey) {
            const jsencrypt = require("node-jsencrypt")
            const encrypt = new jsencrypt();
            encrypt.setKey(publicKey);
            return encrypt.encrypt(data);
        }

        request(options) {
            options.gzip = true;
            return new Promise((resolve, reject) => {
                request(options, (error, response, body) => {
                    if (error) {
                        resolve(error)
                    }
                    try {
                        const objBody = JSON.parse(body);
                        resolve(objBody);
                    } catch (e) {
                        resolve(body)
                    }
                })
            })
        }

        wait(time) {
            return new Promise((resolve) => setTimeout(resolve, time));
        }

    }(name, envNames)
}