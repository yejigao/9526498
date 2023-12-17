/**
 * cron 45 18 * * *  sleepTreasure.js
 * @author:https://github.com/smallfawn/QLScriptPublic
 * 变量名:sleepTreasure
 * 变量值:https://mapi.shuijiaobao.cn   headers ua   去掉最后两个参数  多账户@
 * //错误示范
   //a|10|2.0.5|ql_sleep|f8899fasasasasa4d7unknown|1080|2154|0|8085828|1700222660000|asdfffffffffffffffffffffffffas|3f5722f0cb8313435a4413231afde7ec|Xiaomi
   //正确示范
   //a|10|2.0.5|ql_sleep|f8899fasasasasa4d7unknown|1080|2154|0|8888888|1700222660000|asdfffffffffffffffffffffffffas
 * scriptVersionNow = "0.0.1";
 */

   const $ = new Env("睡觉宝");
   const notify = $.isNode() ? require('./sendNotify') : '';
   let ckName = "sleepTreasure";
   let envSplitor = ["@", "\n"]; //多账号分隔符
   let strSplitor = "&"; //多变量分隔符
   let userIdx = 0;
   let userList = [];
   
   class UserInfo {
       constructor(str) {
           this.index = ++userIdx;
           this.ua = str.split(strSplitor)[0]; //单账号多变量分隔符
           this.ckStatus = true;
           this.userId = null
           this.accessToken = null;
           this.seeAdNum = ""
           this.collectNum = ""
           this.collectId = ""
           this.collectGold_number = ""
       }
       async main() {
           await this.login()
           await $.wait(3000)
           await this.user();
           if (this.ckStatus) {
               if (this._isEatTime()) {
                   await this.eat();
               }
               if (this._isSleepTime()) {
                   await this.sleep()
               }
               if (this.collectNum !== "" && this.collectNum !== 0) {
                   await this.collect(this.collectGold_number, this.collectId)
               }
               await this.newList()
               if (this.seeAdNum !== "") {
                   for (let i = 0; i < this.seeAdNum; i++) {
                       await this.seeAd()
                       await $.wait(60000)
                   }
               }
           }
       }
       async login() {
           //
           const ck = this.ua
           this.id = ck.split('|')[8].split('|')[0]
           let times = Math.round(new Date().getTime() / 1000).toString();
           let signid2 = this._getSign(`${this.id}4BmeNjXs6vLWpT8A${times}000`)
           let uanow = ck.replace(/\d{13}/g, `${times}000`) //匹配10或13位
           let uanow1 = uanow.replace(/\w{32}/, `${signid2}`)
           console.log(uanow1)
           //let equipment = ck.split('|')[4].split('|')[0]
           let options = {
               fn: "登录",
               method: "post",
               url: `https://mapi.shuijiaobao.cn/login/code`,
               headers: {
                   "Content-Type": "application/x-www-form-urlencoded",
                   "ua": uanow1
               },
               body: `channel=sl_ali&pName=ql_sleep&versionName=2.0.5&userId=${this.id}`,
           }
           let { body: result } = await httpRequest(options)
           result = JSON.parse(result)
           this.accessToken = result.data.userInfo.accessToken
           times = Math.round(new Date().getTime() / 1000).toString();
           signid2 = this._getSign(`${this.id}4BmeNjXs6vLWpT8A${times}000`)
           uanow = uanow1.replace(/\d{13}/g, `${times}000`)
           this.ua = uanow.replace(/\w{32}/, `${signid2}`) + "|" + this.accessToken + "|xiaomi"
       }
       async user() {
           try {
               //睡觉
               let options = {
                   fn: `信息查询`,
                   method: `post`,
                   url: `https://mapi.shuijiaobao.cn/home/user`,
                   headers: {
                       "Host": "mapi.shuijiaobao.cn",
                       "ua": this.ua,
                       "Content-Type": "application/x-www-form-urlencoded",
                       "Content-Length": 0,
                       "accept-encoding": "gzip",
                       "user-agent": "okhttp/3.10.0"
                   },
                   body: ``
               }
               console.log(options)
               let { body: result } = await httpRequest(options);;
               result = JSON.parse(result)
               if (result.ok == "1") {
                   if (result.data.bubble_list == "") {
                       this.collectNum = 0
                   } else {
                       this.collectNum = (result.data.bubble_list).length
                       this.collectId = result.data.bubble_list[0].id
                       this.collectGold_number = result.data.bubble_list[0].gold_number
                   }
                   console.log(`${options.fn}成功 id=${result.data.userInfo.id} accessToken=${result.data.userInfo.accessToken} 当前有${this.collectNum}个需要待收集的金币`);
                   this.userId = result.data.userInfo.id
                   this.accessToken = result.data.userInfo.accessToken
                   this.ckStatus = true
               } else {
                   console.log(`${options.fn}失败`);
                   console.log(JSON.stringify(result));
                   this.ckStatus = false
               }
           } catch (e) {
               console.log(e);
           }
       }
       async sleep() {
           try {
               //睡觉
               let options = {
                   fn: `睡觉`,
                   method: `post`,
                   url: `https://mapi.shuijiaobao.cn/sleep/createOrderSleep`,
                   headers: {
                       "Host": "mapi.shuijiaobao.cn",
                       "ua": this.ua,
                       "Content-Type": "application/x-www-form-urlencoded",
                       "Content-Length": 0,
                       "accept-encoding": "gzip",
                       "user-agent": "okhttp/3.10.0"
                   },
                   body: ``
               }
               let { body: result } = await httpRequest(options);
               result = JSON.parse(result)
               //console.log(options);
               console.log(result);
           } catch (e) {
               console.log(e);
           }
       }
       _isEatTime() {
           var currentTime = new Date().getHours();
           if (currentTime >= 5 && currentTime < 9) {
               console.log("当前时间在5-9早");
               return true
           }
           else if (currentTime >= 11 && currentTime < 14) {
               console.log("当前时间在11-14午");
               return true
           }
           else if (currentTime >= 17 && currentTime < 20) {
               console.log("当前时间在17-20晚");
               return true
           }
           else if (currentTime >= 21 || currentTime < 5) {
               console.log("当前时间在21-24夜宵");
               return true
           }
           else {
               console.log("当前时间不在吃饭的时段内");
               return false
           }
       }
       _isSleepTime() {
           var now = new Date();
           var hour = now.getHours();
           if (hour >= 20 || hour < 2) {
               console.log("当前时间在晚上20点到凌晨2点之间");
               return true
           } else if (hour >= 12 && hour < 14) {
               console.log("当前时间在12点到14点之间");
               return true
           } else {
               console.log("当前时间不在睡觉时间");
               return false
           }
       }
       //开饭时间 5-9早  11-14午  17-20晚  21-24夜宵
       async eat() {
           try {
               let options = {
                   fn: `吃饭`,
                   url: `https://mapi.shuijiaobao.cn/sleep/dinnerCreate`,
                   method: `post`,
                   headers: {
                       "Host": "mapi.shuijiaobao.cn",
                       "ua": this.ua,
                       "Content-Type": "application/x-www-form-urlencoded",
                       "Content-Length": 0,
                       "accept-encoding": "gzip",
                       "user-agent": "okhttp/3.10.0"
                   },
                   body: ``
               }
               let { body: result } = await httpRequest(options);
               result = JSON.parse(result)
               //result = JSON.parse(result)
               //console.log(options);
               //console.log(result);
           } catch (e) {
               console.log(e);
           }
       }
       //收集金币
       //id和number在user返回的result.data.bubble_list[0].id 和 gold_number
       async collect(number, id) {
           try {
               let options = {
                   fn: "收集金币",
                   url: `https://mapi.shuijiaobao.cn/sleep/collectSleepGold`,
                   method: `post`,
                   headers: {
                       "Host": "mapi.shuijiaobao.cn",
                       "ua": this.ua,
                       "Content-Type": "application/x-www-form-urlencoded",
                       //"Content-Length": 0,
                       "accept-encoding": "gzip",
                       "user-agent": "okhttp/3.10.0"
                   },
                   body: `number=${number}&id=${id}`
               }
               let { body: result } = await httpRequest(options);
               result = JSON.parse(result)
               //console.log(options);
               console.log(result);
               if (result.ok == "1") {
                   console.log(`${options.fn}成功  获得${result.data.money}🎉`);
               } else {
                   console.log(`${options.fn}失败`);
                   console.log(JSON.stringify(result));
               }
           } catch (e) {
               console.log(e);
           }
       }
       _getSign(str) {
           const crypto = require('crypto');
           return crypto.createHash("md5").update(str).digest("hex")
       }
       //看广告
       async seeAd() {
           try {
               let timeStamp = new Date().getTime() / 1000;
               let sign = this._getSign(`${this.userId}49lfdkislkcsiT8A${timeStamp}${this.accessToken}`)
               let options = {
                   fn: `看广告`,
                   method: `post`,
                   url: `https://mapi.shuijiaobao.cn/task/dayReward`,
                   headers: {
                       "Host": "mapi.shuijiaobao.cn",
                       "ua": this.ua,
                       "Content-Type": "application/x-www-form-urlencoded",
                       //"Content-Length": 0,
                       "accept-encoding": "gzip",
                       "user-agent": "okhttp/3.10.0"
                   },
                   body: `timeStamp=${timeStamp}&sign=${sign}&type=155`
               }
               let { body: result } = await httpRequest(options);
               result = JSON.parse(result)
   
               //console.log(options);
               //console.log(result);
               if (result.ok == "1") {
                   console.log(`${options.fn}成功 获得${result.data.user_info.add_gold_coin}金币 当前金币${result.data.user_info.gold_coin}`);
   
               } else {
                   console.log(`${options.fn}失败`);
                   console.log(JSON.stringify(result));
               }
           } catch (e) {
               console.log(e);
           }
       }
       async newList() {
           try {
               let options = {
                   fn: `任务列表`,
                   method: `post`,
                   url: `https://mapi.shuijiaobao.cn/task/newList`,
                   headers: {
                       "Host": "mapi.shuijiaobao.cn",
                       "ua": this.ua,
                       "Content-Type": "application/x-www-form-urlencoded",
                       //"Content-Length": 0,
                       "accept-encoding": "gzip",
                       "user-agent": "okhttp/3.10.0"
                   },
                   body: ``
               }
               let { body: result } = await httpRequest(options);
               result = JSON.parse(result)
               //console.log(options);
               //console.log(result);
               if (result.ok == "1") {
                   console.log(`${options.fn}成功 任务看广告剩余次数${Number(result.data.day_list[3].totalNum) - Number(result.data.day_list[3].curNum)}`);
                   this.seeAdNum = Number(result.data.day_list[3].totalNum) - Number(result.data.day_list[3].curNum)
               } else {
                   console.log(`${options.fn}失败`);
                   console.log(JSON.stringify(result));
               }
           } catch (e) {
               console.log(e);
           }
       }
   }
   
   async function start() {
       let taskall = [];
       for (let user of userList) {
           if (user.ckStatus) {
               taskall.push(await user.main());
           }
       }
       await Promise.all(taskall);
   }
   
   !(async () => {
       if (!(await checkEnv())) return;
       if (userList.length > 0) {
           await start();
       }
   })()
       .catch((e) => console.log(e))
       .finally(() => $.done());
   
   //********************************************************
   /**
    * 变量检查与处理
    * @returns
    */
   async function checkEnv() {
       let userCookie = ($.isNode() ? process.env[ckName] : $.getdata(ckName)) || "";
       if (userCookie) {
           let e = envSplitor[0];
           for (let o of envSplitor)
               if (userCookie.indexOf(o) > -1) {
                   e = o;
                   break;
               }
           for (let n of userCookie.split(e)) n && userList.push(new UserInfo(n));
       } else {
           console.log("未找到CK");
           return;
       }
       return console.log(`共找到${userList.length}个账号`), true; //true == !0
   }
   
   /////////////////////////////////////////////////////////////////////////////////////
   function httpRequest(options) {
       if (!options["method"]) {
           return console.log(`请求方法不存在`);
       }
       if (!options["fn"]) {
           console.log(`函数名不存在`);
       }
   
       return new Promise((resolve) => {
           $[options.method](options, (err, resp, data) => {
               try {
                   if (err) {
                       $.logErr(err);
                   } else {
                       try {
                           resp = JSON.parse(resp);
                       } catch (error) { }
                   }
               } catch (e) {
                   $.logErr(e, resp);
               } finally {
                   resolve(resp);
               }
           });
       });
   }
   // prettier-ignore
   function Env(t, s) { return new (class { constructor(t, s) { (this.name = t), (this.data = null), (this.dataFile = "box.dat"), (this.logs = []), (this.logSeparator = "\n"), (this.startTime = new Date().getTime()), Object.assign(this, s), this.log("", `\ud83d\udd14${this.name},\u5f00\u59cb!`) } isNode() { return "undefined" != typeof module && !!module.exports } isQuanX() { return "undefined" != typeof $task } isSurge() { return "undefined" != typeof $httpClient && "undefined" == typeof $loon } isLoon() { return "undefined" != typeof $loon } getScript(t) { return new Promise((s) => { this.get({ url: t }, (t, e, i) => s(i)) }) } runScript(t, s) { return new Promise((e) => { let i = this.getdata("@chavy_boxjs_userCfgs.httpapi"); i = i ? i.replace(/\n/g, "").trim() : i; let o = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout"); (o = o ? 1 * o : 20), (o = s && s.timeout ? s.timeout : o); const [h, a] = i.split("@"), r = { url: `http://${a}/v1/scripting/evaluate`, body: { script_text: t, mock_type: "cron", timeout: o }, headers: { "X-Key": h, Accept: "*/*" }, }; this.post(r, (t, s, i) => e(i)) }).catch((t) => this.logErr(t)) } loaddata() { if (!this.isNode()) return {}; { (this.fs = this.fs ? this.fs : require("fs")), (this.path = this.path ? this.path : require("path")); const t = this.path.resolve(this.dataFile), s = this.path.resolve(process.cwd(), this.dataFile), e = this.fs.existsSync(t), i = !e && this.fs.existsSync(s); if (!e && !i) return {}; { const i = e ? t : s; try { return JSON.parse(this.fs.readFileSync(i)) } catch (t) { return {} } } } } writedata() { if (this.isNode()) { (this.fs = this.fs ? this.fs : require("fs")), (this.path = this.path ? this.path : require("path")); const t = this.path.resolve(this.dataFile), s = this.path.resolve(process.cwd(), this.dataFile), e = this.fs.existsSync(t), i = !e && this.fs.existsSync(s), o = JSON.stringify(this.data); e ? this.fs.writeFileSync(t, o) : i ? this.fs.writeFileSync(s, o) : this.fs.writeFileSync(t, o) } } lodash_get(t, s, e) { const i = s.replace(/\[(\d+)\]/g, ".$1").split("."); let o = t; for (const t of i) if (((o = Object(o)[t]), void 0 === o)) return e; return o } lodash_set(t, s, e) { return Object(t) !== t ? t : (Array.isArray(s) || (s = s.toString().match(/[^.[\]]+/g) || []), (s.slice(0, -1).reduce((t, e, i) => Object(t[e]) === t[e] ? t[e] : (t[e] = Math.abs(s[i + 1]) >> 0 == +s[i + 1] ? [] : {}), t)[s[s.length - 1]] = e), t) } getdata(t) { let s = this.getval(t); if (/^@/.test(t)) { const [, e, i] = /^@(.*?)\.(.*?)$/.exec(t), o = e ? this.getval(e) : ""; if (o) try { const t = JSON.parse(o); s = t ? this.lodash_get(t, i, "") : s } catch (t) { s = "" } } return s } setdata(t, s) { let e = !1; if (/^@/.test(s)) { const [, i, o] = /^@(.*?)\.(.*?)$/.exec(s), h = this.getval(i), a = i ? ("null" === h ? null : h || "{}") : "{}"; try { const s = JSON.parse(a); this.lodash_set(s, o, t), (e = this.setval(JSON.stringify(s), i)) } catch (s) { const h = {}; this.lodash_set(h, o, t), (e = this.setval(JSON.stringify(h), i)) } } else e = this.setval(t, s); return e } getval(t) { return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? ((this.data = this.loaddata()), this.data[t]) : (this.data && this.data[t]) || null } setval(t, s) { return this.isSurge() || this.isLoon() ? $persistentStore.write(t, s) : this.isQuanX() ? $prefs.setValueForKey(t, s) : this.isNode() ? ((this.data = this.loaddata()), (this.data[s] = t), this.writedata(), !0) : (this.data && this.data[s]) || null } initGotEnv(t) { (this.got = this.got ? this.got : require("got")), (this.cktough = this.cktough ? this.cktough : require("tough-cookie")), (this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar()), t && ((t.headers = t.headers ? t.headers : {}), void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar)) } get(t, s = () => { }) { t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? $httpClient.get(t, (t, e, i) => { !t && e && ((e.body = i), (e.statusCode = e.status)), s(t, e, i) }) : this.isQuanX() ? $task.fetch(t).then((t) => { const { statusCode: e, statusCode: i, headers: o, body: h } = t; s(null, { status: e, statusCode: i, headers: o, body: h }, h) }, (t) => s(t)) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, s) => { try { const e = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString(); this.ckjar.setCookieSync(e, null), (s.cookieJar = this.ckjar) } catch (t) { this.logErr(t) } }).then((t) => { const { statusCode: e, statusCode: i, headers: o, body: h, } = t; s(null, { status: e, statusCode: i, headers: o, body: h }, h) }, (t) => s(t))) } post(t, s = () => { }) { if ((t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), delete t.headers["Content-Length"], this.isSurge() || this.isLoon())) $httpClient.post(t, (t, e, i) => { !t && e && ((e.body = i), (e.statusCode = e.status)), s(t, e, i) }); else if (this.isQuanX()) (t.method = "POST"), $task.fetch(t).then((t) => { const { statusCode: e, statusCode: i, headers: o, body: h } = t; s(null, { status: e, statusCode: i, headers: o, body: h }, h) }, (t) => s(t)); else if (this.isNode()) { this.initGotEnv(t); const { url: e, ...i } = t; this.got.post(e, i).then((t) => { const { statusCode: e, statusCode: i, headers: o, body: h } = t; s(null, { status: e, statusCode: i, headers: o, body: h }, h) }, (t) => s(t)) } } time(t) { let s = { "M+": new Date().getMonth() + 1, "d+": new Date().getDate(), "H+": new Date().getHours(), "m+": new Date().getMinutes(), "s+": new Date().getSeconds(), "q+": Math.floor((new Date().getMonth() + 3) / 3), S: new Date().getMilliseconds(), }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, (new Date().getFullYear() + "").substr(4 - RegExp.$1.length))); for (let e in s) new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? s[e] : ("00" + s[e]).substr(("" + s[e]).length))); return t } msg(s = t, e = "", i = "", o) { const h = (t) => !t || (!this.isLoon() && this.isSurge()) ? t : "string" == typeof t ? this.isLoon() ? t : this.isQuanX() ? { "open-url": t } : void 0 : "object" == typeof t && (t["open-url"] || t["media-url"]) ? this.isLoon() ? t["open-url"] : this.isQuanX() ? t : void 0 : void 0; this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(s, e, i, h(o)) : this.isQuanX() && $notify(s, e, i, h(o))), this.logs.push("", "==============\ud83d\udce3\u7cfb\u7edf\u901a\u77e5\ud83d\udce3=============="), this.logs.push(s), e && this.logs.push(e), i && this.logs.push(i) } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, s) { const e = !this.isSurge() && !this.isQuanX() && !this.isLoon(); e ? this.log("", `\u2757\ufe0f${this.name},\u9519\u8bef!`, t.stack) : this.log("", `\u2757\ufe0f${this.name},\u9519\u8bef!`, t) } wait(t) { return new Promise((s) => setTimeout(s, t)) } done(t = {}) { const s = new Date().getTime(), e = (s - this.startTime) / 1e3; this.log("", `\ud83d\udd14${this.name},\u7ed3\u675f!\ud83d\udd5b ${e}\u79d2`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t) } })(t, s) }
   