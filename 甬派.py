/**
 *  https://ypapp.cnnb.com.cn/yongpai-user/api/duiba/autologin  链接下的userId
 */

const yongpai = ""//格式为userId#deviceId支付宝账号#姓名 多账户&
//手动点赞文章后https://ypapp.cnnb.com.cn/yongpai-ugc/api/praise/save_news?deviceId=的值 就是deviceId
//deviceId 一般是16位  必须真机抓 瞎写的的点赞不成功
const axios = require("axios").default;
var lodash = require('lodash');
const $ = new Env("甬派");
const Notify = 0;
let envSplitor = "&"
window = {}
function getUuid() {
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
        const r = (Math.random() * 16) | 0;
        const v = c === "x" ? r : (r & 0x3) | 0x8;
        return v.toString(16);
    });
}
async function get_id() {
    let url = `https://ypapp.cnnb.com.cn/yongpai-news/api/v2/news/list?channelId=0&currentPage=1&timestamp=${new Date().getTime()}`;
    let res = await $.get(url);
    let newsId = (res.data.content.find(c => c.title.includes("大转盘"))).newsId
    url = `https://ypapp.cnnb.com.cn/yongpai-news/api/news/detail?newsId=${newsId}&userId=${$.userId}`;
    res = await $.get(url);
    $.id = /hdtool\/index\?id=(\d.*)&/.exec(res.data.body)[1]
}
async function get_autologin() {
    let url = `https://ypapp.cnnb.com.cn/yongpai-user/api/duiba/autologin?dbredirect=https%3A//92722.activity-12.m.duiba.com.cn/hdtool/index?id%3D${$.id}%26dbnewopen&userId=${$.userId}`;
    $.autologin = (await $.get(url)).data;
}
async function get_token() {
    try {
        await axios.get($.autologin, { "maxRedirects": 0 })
    } catch (error) {
        $.wdata = error.response.headers["set-cookie"].filter(c => c.includes("wdata")).join(";")
    }

    let url = `https://92722.activity-12.m.duiba.com.cn/hdtool/index?id=${$.id}&dbnewopen&from=login&spm=92722.1.1.1`;
    let headers = {
        'authority': '92722.activity-12.m.duiba.com.cn',
        'accept': 'application/json',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': $.wdata,
        'origin': 'https://92722.activity-12.m.duiba.com.cn',
        'pragma': 'no-cache',
        'referer': `https://92722.activity-12.m.duiba.com.cn/hdtool/index?id=${$.id}&dbnewopen&from=login&spm=92722.1.1.1`,
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    let res = await $.get(url, headers);
    let code = /<script\b[^>]*>\s*var([\s\S]*?)<\/script>/.exec(res)[1];
    //console.log(code)
    eval(code)
    global.key = /var\s+key\s+=\s+'([^']+)';/.exec(getDuibaToken.toString())[1];
    //console.log(key)
    url = 'https://92722.activity-12.m.duiba.com.cn/hdtool/ctoken/getTokenNew';
    let data = `timestamp=${new Date().getTime()}&activityId=${$.id}&activityType=hdtool&consumerId=4066466507`;
    res = eval((await $.post(url, data, headers)).token);
    //console.log(window[key]);
}
async function doTask() {
    let device_id = getUuid().toUpperCase()
    let url = `https://ypapp.cnnb.com.cn/yongpai-news/api/v2/news/list?channelId=0&currentPage=1&timestamp=${new Date().getTime()}`;
    let res = await $.get(url);
    for (const item of res.data.content) {
        let newsId = item.newsId;
        url = `https://ypapp.cnnb.com.cn/yongpai-news/api/news/detail?newsId=${newsId}&userId=${$.userId}`;
        res = await $.get(url);
        res.message == 'OK' ? $.addMsg(`阅读：[${item.title}]:✅`) : $.addMsg(`阅读：[${item.title}]:❌`)
        await $.wait(2);
        let likeHeaders = {
            "appversion": `10.1.4`,
        }
        url = `https://ypapp.cnnb.com.cn/yongpai-ugc/api/praise/save_news?deviceId=${$.deviceId}&newsId=${newsId}&userId=${$.userId}`
        res = await $.get(url, likeHeaders);
        //console.log(res)
        res.message == 'OK' ? $.addMsg(`点赞：[${item.title}]:✅`) : $.addMsg(`点赞：[${item.title}]:❌`)
        await $.wait(2);
        url = `https://ypapp.cnnb.com.cn/yongpai-ugc/api/forward/news?newsId=${newsId}&source=4&userId=${$.userId}`
        res = await $.get(url);
        res.message == 'OK' ? $.addMsg(`分享：[${item.title}]:✅`) : $.addMsg(`分享：[${item.title}]:❌`)
        await $.wait(2);
    }
    debugger
}
async function doJoin() {
    let url = `https://92722.activity-12.m.duiba.com.cn/hdtool/doJoin?dpm=92722.3.1.0&activityId=${$.id}&_=${new Date().getTime()}`;
    let data = `actId=${$.id}&oaId=${$.id}&activityType=hdtool&consumerId=4066466507&token=${window[key]}`
    let headers = {
        'authority': '92722.activity-12.m.duiba.com.cn',
        'accept': 'application/json',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': $.wdata,
        'origin': 'https://92722.activity-12.m.duiba.com.cn',
        'pragma': 'no-cache',
        'referer': `https://92722.activity-12.m.duiba.com.cn/hdtool/index?id=${$.id}&dbnewopen&from=login&spm=92722.1.1.1`,
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    let res = await $.post(url, data, headers);
    $.addMsg(JSON.stringify(res))
}
async function doTakePrize() {
    let url = `https://92722.activity-12.m.duiba.com.cn/crecord/getrecord?page=1&_=${new Date().getTime()}`;
    let headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        "Content-Type": "application/x-www-form-urlencoded",
        //'Content-Length': '0',
        'Cookie': $.wdata,
        'Origin': 'https://92722.activity-12.m.duiba.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://92722.activity-12.m.duiba.com.cn/activity/takePrizeNew?recordId=7074365348&dpm=92722.26.0.1&dcm=101.53.217692856808979.0&dbnewopen',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"'
    }
    let res = await $.get(url, headers);
    let recordIds = res.records.filter(c => !c.quantity).map(c => (JSON.parse(c.emdJson).info));
    for (const recordId of recordIds) {
        url = `https://92722.activity-12.m.duiba.com.cn/activity/takePrizeNew?recordId=${recordId}&dpm=92722.26.0.1&dcm=101.53.217692856808979.0&dbnewopen`;
        res = await $.get(url, headers);
        let code = /<script\b[^>]*>\s*var([\s\S]*?)<\/script>/.exec(res)[1];
        eval(code)
        global.key = /var\s+key\s+=\s+'([^']+)';/.exec(getDuibaToken.toString())[1];
        url = 'https://92722.activity-12.m.duiba.com.cn/ctoken/getToken.do';
        res = eval((await $.post(url, '', headers)).token);
        url = 'https://92722.activity-12.m.duiba.com.cn/activity/doTakePrize';
        let data = `alipay=${encodeURIComponent($.account)}&realname=${encodeURIComponent($.realName)}&recordId=${recordId}&token=${window[key]}`
        res = await $.post(url, data, headers)
        console.log(JSON.stringify(res));
    }
}
(async () => {
    let arr = $.checkEnv("yp");
    if (!arr) return await $.SendMsg("未填写token"), $.done();;
    $._ = lodash.range(0, arr.length);
    for (let index = 0; index < arr.length; index++) {
        $.addMsg(`账号${index + 1}:`);
        console.log(arr)
        $.userId = arr[index].split("#")[0];
        $.deviceId = arr[index].split("#")[1]
        $.account = arr[index].split("#")[2];
        $.realName = arr[index].split("#")[3];
        console.log($.userId, $.account)
        await doTask();
        //await get_id()
        $.id = 255562754277781
        await get_autologin();
        await get_token()
        await doJoin()
        await $.wait(10)
        await doTakePrize()
    }
    await $.SendMsg($._msg);
    $.done();
})();

function Env(name) {
    return new (class {
        constructor(name) {
            this.name = name;
            console.log(`\ud83d\udd14${this.name},\u5f00\u59cb!`);
            Object.defineProperty(this, "random", {
                get() {
                    let i = lodash.random(0, this._.length - 1);
                    let n = this._[i];
                    this._.splice(i, 1);
                    return n;
                }
            })
        }
        async get(url, headers) {
            try {
                return (await axios.get(url, { headers })).data;
            } catch (err) {
                console.log(`error:${err.message}`);
                return this.get(url, headers);
            }
        }
        async post(url, data, headers) {
            try {
                return (await axios.post(url, data, { headers: headers })).data;
            } catch (err) {
                console.log(`error:${err.message}`);
                return this.post(url, data, headers);
            }
        }
        async SendMsg(message) {
            if (!message) return;
            if (Notify > 0) {
                var notify = require("./sendNotify");
                await notify.sendNotify(this.name, message);
            }
        }
        addMsg(msg) {
            if (!this._msg) this._msg = "";
            console.log(msg);
            this._msg += msg + "\n";
        }
        wait(delay) {
            return new Promise((res) => {
                setTimeout(res, delay * 1000);
            });
        }
        checkEnv() {
            //let userCookie = ($.isNode() ? process.env[ckName] : $.getdata(ckName)) || "";
            let userCookie = yongpai;
            let userList = []
            if (userCookie) {
                let e = envSplitor[0];
                for (let o of envSplitor)
                    if (userCookie.indexOf(o) > -1) {
                        e = o;
                        break;
                    }
                for (let n of userCookie.split(e)) userList.push(n);
                return userList
            } else {
                console.log("未找到CK");
                return;
            }
        }
        done() {
            console.log(`\ud83d\udd14${this.name},\u7ed3\u675f!`);
        }
    })(name);
}