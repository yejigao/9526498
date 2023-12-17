/*
 作者：ZFeng1005
 日期：11-19
 微信小程序：康师傅味道馆
 功能：签到-任务-抽奖
 抓包：https://ksf.plscn.com 任意请求body的 encryptsessionid
 变量：wdgCookie='xxxx@xxxx '  多个账号用 @ 或者 换行 分割 
 定时一天两次，
 cron: 15 8,19 * * *
 */
const $ = new Env('康师傅味道馆')
const CryptoJS = require('crypto-js')
const notify = $.isNode() ? require('./sendNotify') : '';
let cookiesArr = [],
  message = "",
  cookie = ($.isNode() ? process.env.wdgCookie : $.getdata("wdgCookie")) || ``
  !(async () => {
    await requireConfig();
    await getActionDate();
    for (let i = 0; i < cookiesArr.length; i++) {
      if (cookiesArr[i]) {
        cookie = cookiesArr[i];
        msg = '';
        $.index = i + 1;
        $.nickName = '';
        $.mobile = '';
        $.memberId = '';
        $.canRead = true;
        $.canView = true;
        await takePostRequest('getinfo')
        console.log(`\n******开始【🐸康师傅味道馆账号${$.index}】${$.nickName}*********\n`);
        await main()
      }
    }
    if ($.isNode() && message) {
      await notify.sendNotify(`${$.name}`, `${message}`)
    }
  })()
  .catch((e) => $.logErr(e))
  .finally(() => $.done())

async function main() {
  if ($.memberId) {
    console.log(`【开始获取签到信息】`)
    await takePostRequest('getsigninfo')
    await $.wait(1500)
    console.log(`【开始浏览文章】`)
    for (i = 0; i < 3 && $.canRead; i++) await takePostRequest('sendreadbonus')
    await $.wait(1500)
    console.log(`【开始观看视频】`)
    for (i = 0; i < 3 && $.canView; i++) await takePostRequest('viewvideo')
    await $.wait(1500)
    console.log(`【微信步数兑换积分】`)
    await takePostRequest('getbywxstep')
    console.log(`【查询账号信息】`)
    await takePostRequest('getinfo')
    msg += `当前账号拥有积分：${$.bonus}`
    console.log(msg)
    await showMsg()
  } else console.log(`【获取账号信息失败，退出~】\n`)
}
async function takePostRequest(type) {
  let body = ``;
  let myRequest = ``;
  switch (type) {
    case 'getinfo': //账号信息
      body = `itemid=1189`;
      myRequest = await taskUrl(`vip/getinfo`, body);
      break;
    case 'getsigninfo': //签到信息
      body = `month=${new Date().getFullYear()}-${new Date().getMonth()+1}&pageid=733`;
      myRequest = await taskUrl(`bonus/getsigninfo`, body);
      break;
    case 'signin': //签到
      body = `pageid=733&signday=${actionDate}`;
      myRequest = await taskUrl(`bonus/signin`, body);
      break;
    case 'sendreadbonus': //浏览文章
      body = `gameid=73`;
      myRequest = await taskUrl(`bonus/sendreadbonus`, body);
      break;
    case 'viewvideo': //观看视频
      body = `event=viewvideo&type=ended&linkid=0&articleid=1311&itemid=1010`;
      myRequest = await taskUrl(`wxa/onitemevt`, body);
      break;
    case 'getbywxstep': //微信步数换积分
      body = `itemid=985`;
      myRequest = await taskUrl(`bonus/getbywxstep`, body);
      break;
    default:
      console.log(`错误${type}`);
  }
  return new Promise(async resolve => {
    $.post(myRequest, (err, resp, data) => {
      try {
        //console.log(data);
        dealReturn(type, data);
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve();
      }
    })
  })
}

async function dealReturn(type, data) {
  try {
    data = JSON.parse(data);
  } catch (e) {
    console.log(`返回异常：${data}`);
    return;
  }
  switch (type) {
    case 'getinfo':
      //console.log(JSON.stringify(data))
      if (data.errcode === 0) {
        $.memberId = data.result.vipcode
        $.nickName = data.result.vipname
        $.score = data.result.vipbonus
        $.bonus = data.result.vipbonus
      }
      break;
    case 'getsigninfo':
      if (data.errcode === 0) {
        console.log(`获取成功！`)
        console.log(`【开始每日签到】`)
        if (data.result.lastsigndate == actionDate) {
          console.log(`今日已签到！`)
        } else {
          await takePostRequest('signin')
        }
      }
      break;
    case 'signin':
      if (data.errcode === 0) {
        console.log(`签到成功！获得[${data.result.signsuccesstext.split('+')[1].split('<')[0]}]积分`)
      } else {
        console.log(data.errmsg)
      }
      break;
    case 'sendreadbonus':
      if (data.errcode === 0) {
        console.log(`浏览成功！获得[3]积分`)
        $.wait(1500)
      } else {
        $.canRead = false
        console.log(data.errmsg)
      }
      break;
    case 'viewvideo':
      if (data.errcode === 0) {
        console.log(`观看成功！获得[5]积分`)
      } else {
        $.canView = false
        console.log(data.errmsg)
      }
      break;
    case 'getbywxstep':
      if (data.errcode === 0) {
        console.log(`兑换成功！`)
      } else {
        $.canView = false
        console.log(data.errmsg)
      }
      break;
    default:
      console.log(`未判断的异常${type}`);
  }
}
/**
 * 
 * API
 */
function taskUrl(type, body) {
  rawSign = `${body}&encryptsessionid=${cookie}&qr=0&timestamp=${Date.now()}&versionid=1.1.0`
  opt = {
    url: `https://ksf.plscn.com/brandwxa/api/${type}`,
    body: `${rawSign}`,
    headers: {
      'Host': 'ksf.plscn.com',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
      'content-type': 'application/x-www-form-urlencoded',
      'x-account-key': 'd3hiNmQ5M2Q3YWY5M2YzMWRh',
      'x-account-sign': sign(rawSign),
      'Referer': 'https://servicewechat.com/wxb6d93d7af93f31da/81/page-frame.html',
      'Accept-Encoding': 'gzip, deflate, br'
    }
  }
  return opt
}
/**
 * 
 * sign计算
 */
function sign(e) {
  e = e.split('&')
  var n = [];
  for (var t in e) n.push(e[t].split('=')[1]);
  var o = "wxb6d93d7af93f31dawa_smartgo",
    i = n.sort(),
    r = "";
  for (var t in i) r += "" + n[t];
  return r += o, CryptoJS.MD5(r).toString();
}
/**
 * 
 * 消息推送
 */
function showMsg() {
  message += `===== ${$.nickName} =====\n`;
  message += `${msg}\n\n`
  //console.log(message)
}
/**
 * 时间获取
 */
function getActionDate() {
  actionDate = `${new Date().getFullYear()}-${new Date().getMonth()+1}-`
  if (new Date().getDate() < 10) {
    actionDate += `0${new Date().getDate()}`
  } else {
    actionDate += `${new Date().getDate()}`
  }
  //console.log(actionDate)
}
/**
 * 
 * cookie处理
 */
function requireConfig() {
  if (cookie) {
    if (cookie.indexOf("@") != -1) {
      cookie.split("@").forEach((item) => {
        cookiesArr.push(item);
      });
    } else if (cookie.indexOf("\n") != -1) {
      cookie.split("\n").forEach((item) => {
        cookiesArr.push(item);
      });
    } else {
      cookiesArr.push(cookie);
    }
    console.log(`\n=============================================    \n脚本执行 - 北京时间(UTC+8)：${new Date(new Date().getTime() +new Date().getTimezoneOffset() * 60 * 1000 + 8 * 60 * 60 * 1000).toLocaleString()} \n=============================================\n`)
    console.log(`\n=========共有${cookiesArr.length}个${$.name}账号Cookie=========\n`);
  } else {
    console.log(`\n【缺少wdgCookies环境变量或者Cookies为空！】`)
    return;
  }
}
// prettier-ignore
function Env(t, e) { class s { constructor(t) { this.env = t } send(t, e = "GET") { t = "string" == typeof t ? { url: t } : t; let s = this.get; return "POST" === e && (s = this.post), new Promise((e, i) => { s.call(this, t, (t, s, r) => { t ? i(t) : e(s) }) }) } get(t) { return this.send.call(this.env, t) } post(t) { return this.send.call(this.env, t, "POST") } } return new class { constructor(t, e) { this.name = t, this.http = new s(this), this.data = null, this.dataFile = "box.dat", this.logs = [], this.isMute = !1, this.isNeedRewrite = !1, this.logSeparator = "\n", this.startTime = (new Date).getTime(), Object.assign(this, e), this.log("", `🔔${this.name}, 开始!`) } isNode() { return "undefined" != typeof module && !!module.exports } isQuanX() { return "undefined" != typeof $task } isSurge() { return "undefined" != typeof $httpClient && "undefined" == typeof $loon } isLoon() { return "undefined" != typeof $loon } toObj(t, e = null) { try { return JSON.parse(t) } catch { return e } } toStr(t, e = null) { try { return JSON.stringify(t) } catch { return e } } getjson(t, e) { let s = e; const i = this.getdata(t); if (i) try { s = JSON.parse(this.getdata(t)) } catch { } return s } setjson(t, e) { try { return this.setdata(JSON.stringify(t), e) } catch { return !1 } } getScript(t) { return new Promise(e => { this.get({ url: t }, (t, s, i) => e(i)) }) } runScript(t, e) { return new Promise(s => { let i = this.getdata("@chavy_boxjs_userCfgs.httpapi"); i = i ? i.replace(/\n/g, "").trim() : i; let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout"); r = r ? 1 * r : 20, r = e && e.timeout ? e.timeout : r; const [o, h] = i.split("@"), n = { url: `http://${h}/v1/scripting/evaluate`, body: { script_text: t, mock_type: "cron", timeout: r }, headers: { "X-Key": o, Accept: "*/*" } }; this.post(n, (t, e, i) => s(i)) }).catch(t => this.logErr(t)) } loaddata() { if (!this.isNode()) return {}; { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e); if (!s && !i) return {}; { const i = s ? t : e; try { return JSON.parse(this.fs.readFileSync(i)) } catch (t) { return {} } } } } writedata() { if (this.isNode()) { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e), r = JSON.stringify(this.data); s ? this.fs.writeFileSync(t, r) : i ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r) } } lodash_get(t, e, s) { const i = e.replace(/\[(\d+)\]/g, ".$1").split("."); let r = t; for (const t of i) if (r = Object(r)[t], void 0 === r) return s; return r } lodash_set(t, e, s) { return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), e.slice(0, -1).reduce((t, s, i) => Object(t[s]) === t[s] ? t[s] : t[s] = Math.abs(e[i + 1]) >> 0 == +e[i + 1] ? [] : {}, t)[e[e.length - 1]] = s, t) } getdata(t) { let e = this.getval(t); if (/^@/.test(t)) { const [, s, i] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : ""; if (r) try { const t = JSON.parse(r); e = t ? this.lodash_get(t, i, "") : e } catch (t) { e = "" } } return e } setdata(t, e) { let s = !1; if (/^@/.test(e)) { const [, i, r] = /^@(.*?)\.(.*?)$/.exec(e), o = this.getval(i), h = i ? "null" === o ? null : o || "{}" : "{}"; try { const e = JSON.parse(h); this.lodash_set(e, r, t), s = this.setval(JSON.stringify(e), i) } catch (e) { const o = {}; this.lodash_set(o, r, t), s = this.setval(JSON.stringify(o), i) } } else s = this.setval(t, e); return s } getval(t) { return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? (this.data = this.loaddata(), this.data[t]) : this.data && this.data[t] || null } setval(t, e) { return this.isSurge() || this.isLoon() ? $persistentStore.write(t, e) : this.isQuanX() ? $prefs.setValueForKey(t, e) : this.isNode() ? (this.data = this.loaddata(), this.data[e] = t, this.writedata(), !0) : this.data && this.data[e] || null } initGotEnv(t) { this.got = this.got ? this.got : require("got"), this.cktough = this.cktough ? this.cktough : require("tough-cookie"), this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar, t && (t.headers = t.headers ? t.headers : {}, void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar)) } get(t, e = (() => { })) { t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? (this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.get(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) })) : this.isQuanX() ? (this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t))) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, e) => { try { if (t.headers["set-cookie"]) { const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString(); s && this.ckjar.setCookieSync(s, null), e.cookieJar = this.ckjar } } catch (t) { this.logErr(t) } }).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) })) } post(t, e = (() => { })) { if (t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), t.headers && delete t.headers["Content-Length"], this.isSurge() || this.isLoon()) this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.post(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) }); else if (this.isQuanX()) t.method = "POST", this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t)); else if (this.isNode()) { this.initGotEnv(t); const { url: s, ...i } = t; this.got.post(s, i).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) }) } } time(t, e = null) { const s = e ? new Date(e) : new Date; let i = { "M+": s.getMonth() + 1, "d+": s.getDate(), "H+": s.getHours(), "m+": s.getMinutes(), "s+": s.getSeconds(), "q+": Math.floor((s.getMonth() + 3) / 3), S: s.getMilliseconds() }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, (s.getFullYear() + "").substr(4 - RegExp.$1.length))); for (let e in i) new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? i[e] : ("00" + i[e]).substr(("" + i[e]).length))); return t } msg(e = t, s = "", i = "", r) { const o = t => { if (!t) return t; if ("string" == typeof t) return this.isLoon() ? t : this.isQuanX() ? { "open-url": t } : this.isSurge() ? { url: t } : void 0; if ("object" == typeof t) { if (this.isLoon()) { let e = t.openUrl || t.url || t["open-url"], s = t.mediaUrl || t["media-url"]; return { openUrl: e, mediaUrl: s } } if (this.isQuanX()) { let e = t["open-url"] || t.url || t.openUrl, s = t["media-url"] || t.mediaUrl; return { "open-url": e, "media-url": s } } if (this.isSurge()) { let e = t.url || t.openUrl || t["open-url"]; return { url: e } } } }; if (this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(e, s, i, o(r)) : this.isQuanX() && $notify(e, s, i, o(r))), !this.isMuteLog) { let t = ["", "==============📣系统通知📣=============="]; t.push(e), s && t.push(s), i && t.push(i), console.log(t.join("\n")), this.logs = this.logs.concat(t) } } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, e) { const s = !this.isSurge() && !this.isQuanX() && !this.isLoon(); s ? this.log("", `❗️${this.name}, 错误!`, t.stack) : this.log("", `❗️${this.name}, 错误!`, t) } wait(t) { return new Promise(e => setTimeout(e, t)) } done(t = {}) { const e = (new Date).getTime(), s = (e - this.startTime) / 1e3; this.log("", `🔔${this.name}, 结束! 🕛 ${s} 秒`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t) } }(t, e) }