/**
 * 微信小程序：战马能量星球
 * 抓包：get请求 https://zm.t7a.cn/api
 * header后面的safe的值
 * 例如safe=123456789
 * 变量格式 export zmnlxq = 'XXXXXX'
 */
 
const $ = Env('战马能量星球');
const notify = $.isNode() ? require('./sendNotify') : '';      // 这里是 node（青龙属于node环境）通知相关的
const Notify = 0; //0为关闭通知，1为打开通知,未添加
const debug = 0; //0为关闭调试，1为打开调试,默认为0
//////////////////////////////////////////////////////////////////
let zmnlxq = process.env.zmnlxq;
let zmnlxqArr = [];
let data = '';
let msg = '';
let Version = "0.0.1";
let VersionLatest = '';
let ok = ''


!(async () => {
 
	if (!(await Envs()))  	//多账号分割 判断变量是否为空  初步处理多账号
		return;
	else {
        //await getVersion();
        console.log(`\n============ 当前版本：${Version}  最新版本：${VersionLatest} ============`)
        console.log(`目前实现功能：日常签到`);

		console.log(`\n\n=========================================    \n脚本执行 - 北京时间(UTC+8)：${new Date(
			new Date().getTime() + new Date().getTimezoneOffset() * 60 * 1000 +
			8 * 60 * 60 * 1000).toLocaleString()} \n=========================================\n`);
 
		console.log(`\n=================== 共找到 ${zmnlxqArr.length} 个账号 ===================`)
         
		for (let index = 0; index < zmnlxqArr.length; index++) {
 
 
			let num = index + 1
zmnlxq = zmnlxqArr[index]
            console.log(`\n========= 开始【第 ${num} 个账号】=========\n`)
//			data = zmnlxqArr[index].split('&');    

			console.log('开始获取信息');
			await getuser();
			await $.wait(2 * 1000);
           
			if(ok == 1){
				console.log('开始签到');
                await $.wait(2 * 1000);
			    await checkin();

//封印中。。                    console.log('小程序分享');
//                      await $.wait(2 * 1000);
//  			        await getshare();

                	console.log('查询题库');
                    await $.wait(2 * 1000);
			        await gettiku();
			}


			await SendMsg(msg);    // 与发送通知有关系
		}
	}
 
})()
	.catch((e) => console.log(e))
	.finally(() => $.done())

/**
 * 获取信息
 * 
 */
async function getuser(timeout = 2 * 1000) {
	return new Promise((resolve) => {
		let url = {
			url: `https://zm.t7a.cn/api/getusercenter.php?safe=${zmnlxq}`,   
			headers: {          
				'Host' : 'zm.t7a.cn',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6242 MicroMessenger/8.0.20.2080(0x28001435) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx532ecb3bdaaf92f9'
			},
			// body: '',     
 
		} 
		$.get(url, async (error, response, data) => {    
			try {
				result = JSON.parse(data)
                if(result.status == 1){

                    ok = 1 ;

                    console.log(`用户：${result.nickname}` + `当前能量：${result.nowscore} `);
                    if(result.isgzhkl == 0){
                        console.log('公众号口令任务：未完成' + '\n' +'开始完成任务')
                        await gzhkl();
                    }
                    

                }else{
                    
                    console.log(`信息获取失败请检查` )

                }

			} catch (e) {
				console.log(e)
			} finally {
				resolve();
			}
		}, timeout)
	})
}

/**
 * 签到
 * 
 */
function checkin(timeout = 2 * 1000) {
	return new Promise((resolve) => {
		let url = {
			url: `https://zm.t7a.cn/api/checkin.php?safe=${zmnlxq}`,   
			headers: {          
				'Host' : 'zm.t7a.cn',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6242 MicroMessenger/8.0.20.2080(0x28001435) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx532ecb3bdaaf92f9'
			},
			// body: '',     
 
		} 
		$.get(url, async (error, response, data) => {    
			try {
				result = JSON.parse(data)

                if(result.status == 1){

                    console.log(result.msg)  
                                   
                }else{

                    console.log(result.msg) 

                }				
			} catch (e) {
				console.log(e)
			} finally {
				resolve();
			}
		}, timeout)
	})
}


/**
 * 小程序分享任务
 * 
 */
 function getshare(timeout = 2 * 1000) {
	return new Promise((resolve) => {
		let url = {
			url: `https://zm.t7a.cn/api/getshare.php?safe=${zmnlxq}`,   
			headers: {          
				'Host' : 'zm.t7a.cn',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6242 MicroMessenger/8.0.20.2080(0x28001435) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx532ecb3bdaaf92f9'
			},
			// body: '',     
 
		} 
		$.get(url, async (error, response, data) => {    
			try {
				result = JSON.parse(data)
                if(result.status == 1){
                    console.log(result.msg)
                }else{
					console.log(result.msg)

                }
				
			} catch (e) {
				console.log(e)
			} finally {
				resolve();
			}
		}, timeout)
	})
}

/**
 * 公众号口令只可完成一次
 * 
 */
function gzhkl(timeout = 2 * 1000) {
	return new Promise((resolve) => {
		let url = {
			url: `https://zm.t7a.cn/api/gzhkl.php?safe=${zmnlxq}&kl=%E6%9C%89%E8%83%BD%E9%87%8F%EF%BC%8C%E6%94%BE%E9%A9%AC%E6%9D%A5`,   
			headers: {          
				'Host' : 'zm.t7a.cn',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6242 MicroMessenger/8.0.20.2080(0x28001435) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx532ecb3bdaaf92f9'
			},
			// body: '',     
 
		} 
		$.get(url, async (error, response, data) => {    
			try {
				result = JSON.parse(data)
                if(result.status == 0){

                    console.log(result.msg) 

                }else{

                    console.log(result.msg)  

                }				
			} catch (e) {
				console.log(e)
			} finally {
				resolve();
			}
		}, timeout)
	})
}


/**
 * 查询题库
 * 
 */
async function gettiku(timeout = 2 * 1000) {
	return new Promise((resolve) => {
		let url = {
			url: `https://zm.t7a.cn/api/getquesbackstatus.php?safe=${zmnlxq}`,   
			headers: {          
				'Host' : 'zm.t7a.cn',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6242 MicroMessenger/8.0.20.2080(0x28001435) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx532ecb3bdaaf92f9'
			},
			// body: '',     
 
		} 
		$.get(url, async (error, response, data) => {    
			try {
				result = JSON.parse(data)
                if(result.status == 1){
                    console.log(result.msg)
                    
					console.log('刷新题目')

					await $.wait(2 * 1000);
			        await getques();

					console.log('开始去答题'+'\n'+'因为是自定义答题，不排除黑号风险'+'\n'+'后期有能力修改题目获取方式');

                    await $.wait(2 * 1000);
			        await ques1();

					await $.wait(2 * 1000);
			        await ques2();

					await $.wait(2 * 1000);
			        await ques3();

                }else{
                    console.log(result.msg)                 
                }



				
			} catch (e) {
				console.log(e)
			} finally {
				resolve();
			}
		}, timeout)
	})
}

/**
 * 刷新题目
 * 
 */
 function getques(timeout = 2 * 1000) {
	return new Promise((resolve) => {
		let url = {
			url: `https://zm.t7a.cn/api/getques.php?safe=${zmnlxq}`,   
			headers: {          
				'Host' : 'zm.t7a.cn',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6242 MicroMessenger/8.0.20.2080(0x28001435) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx532ecb3bdaaf92f9'
			},
			// body: '',     
 
		} 
		$.get(url, async (error, response, data) => {    
			try {
				result = JSON.parse(data)
                console.log(result.msg)
                			
			} catch (e) {
				console.log(e)
			} finally {
				resolve();
			}
		}, timeout)
	})
}



/**
 * 答题1
 * 
 */
 function ques1(timeout = 2 * 1000) {
	return new Promise((resolve) => {
		let url = {
			url: `https://zm.t7a.cn/api/subques.php?safe=${zmnlxq}&qid=126&val=C`,   
			headers: {          
				'Host' : 'zm.t7a.cn',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6242 MicroMessenger/8.0.20.2080(0x28001435) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx532ecb3bdaaf92f9'
			},
			// body: '',     
 
		} 
		$.get(url, async (error, response, data) => {    
			try {
				result = JSON.parse(data)
                if(result.status == 1){
                    console.log(result.msg)
                }else{
                    console.log(result.msg)
                }				
			} catch (e) {
				console.log(e)
			} finally {
				resolve();
			}
		}, timeout)
	})
}


/**
 * 答题2
 * 
 */
 function ques2(timeout = 2 * 1000) {
	return new Promise((resolve) => {
		let url = {
			url: `https://zm.t7a.cn/api/subques.php?safe=${zmnlxq}&qid=138&val=C`,   
			headers: {          
				'Host' : 'zm.t7a.cn',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6242 MicroMessenger/8.0.20.2080(0x28001435) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx532ecb3bdaaf92f9'
			},
			// body: '',     
 
		} 
		$.get(url, async (error, response, data) => {    
			try {
				result = JSON.parse(data)
                if(result.status == 1){
                    console.log(result.msg)
                }else{
					console.log(result.msg)

                }
				
			} catch (e) {
				console.log(e)
			} finally {
				resolve();
			}
		}, timeout)
	})
}


/**
 * 答题3
 * 
 */
 function ques3(timeout = 2 * 1000) {
	return new Promise((resolve) => {
		let url = {
			url: `https://zm.t7a.cn/api/subques.php?safe=${zmnlxq}&qid=119&val=A`,   
			headers: {          
				'Host' : 'zm.t7a.cn',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6242 MicroMessenger/8.0.20.2080(0x28001435) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx532ecb3bdaaf92f9'
			},
			// body: '',     
 
		} 
		$.get(url, async (error, response, data) => {    
			try {
				result = JSON.parse(data)
                if(result.status == 1){
                    console.log(result.msg)
                }else{
					console.log(result.msg)

                }
				
			} catch (e) {
				console.log(e)
			} finally {
				resolve();
			}
		}, timeout)
	})
}

/**
* 获取远程版本，鸟VPS不改post请求获取不了内容
*/
function getVersion(timeout = 3 * 1000) {
  return new Promise((resolve) => {
    let url = {
      url: `http://www.holyxie.com/script/zmnlxq/zmnlxq.js`,
    }
    $.post(url, async (err, resp, data) => {
      try {
       VersionLatest = data.match(/"\d.+"/)
      console.log(`最新版本号为：${VersionLatest}`);
      } catch (e) {
        $.logErr(e, resp);
      } finally {
        resolve()
      }
    }, timeout)
  })
}


//#region 固定代码 可以不管他
// ============================================变量检查============================================ \\
async function Envs() {
	if (zmnlxq) {
		if (zmnlxq.indexOf("@") != -1) {
			zmnlxq.split("@").forEach((item) => {
				zmnlxqArr.push(item);
			});
		} else {
			zmnlxqArr.push(zmnlxq);
		}
	} else {
		console.log(`\n 【${$.name}】：未填写变量 zmnlxq`)
		return;
	}
 
	return true;
}
 
// ============================================发送消息============================================ \\
async function SendMsg(message) {
	if (!message)
		return;
 
	if (Notify > 0) {
		if ($.isNode()) {
			var notify = require('./sendNotify');
			await notify.sendNotify($.name, message);
		} else {
			$.msg(message);
		}
	} else {
		console.log(message);
	}
	
}
// prettier-ignore   固定代码  不用管他
function Env(t, e) { "undefined" != typeof process && JSON.stringify(process.env).indexOf("GITHUB") > -1 && process.exit(0); class s { constructor(t) { this.env = t } send(t, e = "GET") { t = "string" == typeof t ? { url: t } : t; let s = this.get; return "POST" === e && (s = this.post), new Promise((e, i) => { s.call(this, t, (t, s, r) => { t ? i(t) : e(s) }) }) } get(t) { return this.send.call(this.env, t) } post(t) { return this.send.call(this.env, t, "POST") } } return new class { constructor(t, e) { this.name = t, this.http = new s(this), this.data = null, this.dataFile = "box.dat", this.logs = [], this.isMute = !1, this.isNeedRewrite = !1, this.logSeparator = "\n", this.startTime = (new Date).getTime(), Object.assign(this, e), this.log("", `🔔${this.name}, 开始!`) } isNode() { return "undefined" != typeof module && !!module.exports } isQuanX() { return "undefined" != typeof $task } isSurge() { return "undefined" != typeof $httpClient && "undefined" == typeof $loon } isLoon() { return "undefined" != typeof $loon } toObj(t, e = null) { try { return JSON.parse(t) } catch { return e } } toStr(t, e = null) { try { return JSON.stringify(t) } catch { return e } } getjson(t, e) { let s = e; const i = this.getdata(t); if (i) try { s = JSON.parse(this.getdata(t)) } catch { } return s } setjson(t, e) { try { return this.setdata(JSON.stringify(t), e) } catch { return !1 } } getScript(t) { return new Promise(e => { this.get({ url: t }, (t, s, i) => e(i)) }) } runScript(t, e) { return new Promise(s => { let i = this.getdata("@chavy_boxjs_userCfgs.httpapi"); i = i ? i.replace(/\n/g, "").trim() : i; let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout"); r = r ? 1 * r : 20, r = e && e.timeout ? e.timeout : r; const [o, h] = i.split("@"), n = { url: `http://${h}/v1/scripting/evaluate`, body: { script_text: t, mock_type: "cron", timeout: r }, headers: { "X-Key": o, Accept: "*/*" } }; this.post(n, (t, e, i) => s(i)) }).catch(t => this.logErr(t)) } loaddata() { if (!this.isNode()) return {}; { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e); if (!s && !i) return {}; { const i = s ? t : e; try { return JSON.parse(this.fs.readFileSync(i)) } catch (t) { return {} } } } } writedata() { if (this.isNode()) { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e), r = JSON.stringify(this.data); s ? this.fs.writeFileSync(t, r) : i ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r) } } lodash_get(t, e, s) { const i = e.replace(/\[(\d+)\]/g, ".$1").split("."); let r = t; for (const t of i) if (r = Object(r)[t], void 0 === r) return s; return r } lodash_set(t, e, s) { return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), e.slice(0, -1).reduce((t, s, i) => Object(t[s]) === t[s] ? t[s] : t[s] = Math.abs(e[i + 1]) >> 0 == +e[i + 1] ? [] : {}, t)[e[e.length - 1]] = s, t) } getdata(t) { let e = this.getval(t); if (/^@/.test(t)) { const [, s, i] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : ""; if (r) try { const t = JSON.parse(r); e = t ? this.lodash_get(t, i, "") : e } catch (t) { e = "" } } return e } setdata(t, e) { let s = !1; if (/^@/.test(e)) { const [, i, r] = /^@(.*?)\.(.*?)$/.exec(e), o = this.getval(i), h = i ? "null" === o ? null : o || "{}" : "{}"; try { const e = JSON.parse(h); this.lodash_set(e, r, t), s = this.setval(JSON.stringify(e), i) } catch (e) { const o = {}; this.lodash_set(o, r, t), s = this.setval(JSON.stringify(o), i) } } else s = this.setval(t, e); return s } getval(t) { return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? (this.data = this.loaddata(), this.data[t]) : this.data && this.data[t] || null } setval(t, e) { return this.isSurge() || this.isLoon() ? $persistentStore.write(t, e) : this.isQuanX() ? $prefs.setValueForKey(t, e) : this.isNode() ? (this.data = this.loaddata(), this.data[e] = t, this.writedata(), !0) : this.data && this.data[e] || null } initGotEnv(t) { this.got = this.got ? this.got : require("got"), this.cktough = this.cktough ? this.cktough : require("tough-cookie"), this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar, t && (t.headers = t.headers ? t.headers : {}, void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar)) } get(t, e = (() => { })) { t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? (this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.get(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) })) : this.isQuanX() ? (this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t))) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, e) => { try { if (t.headers["set-cookie"]) { const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString(); s && this.ckjar.setCookieSync(s, null), e.cookieJar = this.ckjar } } catch (t) { this.logErr(t) } }).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) })) } post(t, e = (() => { })) { if (t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), t.headers && delete t.headers["Content-Length"], this.isSurge() || this.isLoon()) this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.post(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) }); else if (this.isQuanX()) t.method = "POST", this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t)); else if (this.isNode()) { this.initGotEnv(t); const { url: s, ...i } = t; this.got.post(s, i).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) }) } } time(t, e = null) { const s = e ? new Date(e) : new Date; let i = { "M+": s.getMonth() + 1, "d+": s.getDate(), "H+": s.getHours(), "m+": s.getMinutes(), "s+": s.getSeconds(), "q+": Math.floor((s.getMonth() + 3) / 3), S: s.getMilliseconds() }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, (s.getFullYear() + "").substr(4 - RegExp.$1.length))); for (let e in i) new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? i[e] : ("00" + i[e]).substr(("" + i[e]).length))); return t } msg(e = t, s = "", i = "", r) { const o = t => { if (!t) return t; if ("string" == typeof t) return this.isLoon() ? t : this.isQuanX() ? { "open-url": t } : this.isSurge() ? { url: t } : void 0; if ("object" == typeof t) { if (this.isLoon()) { let e = t.openUrl || t.url || t["open-url"], s = t.mediaUrl || t["media-url"]; return { openUrl: e, mediaUrl: s } } if (this.isQuanX()) { let e = t["open-url"] || t.url || t.openUrl, s = t["media-url"] || t.mediaUrl; return { "open-url": e, "media-url": s } } if (this.isSurge()) { let e = t.url || t.openUrl || t["open-url"]; return { url: e } } } }; if (this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(e, s, i, o(r)) : this.isQuanX() && $notify(e, s, i, o(r))), !this.isMuteLog) { let t = ["", "==============📣系统通知📣=============="]; t.push(e), s && t.push(s), i && t.push(i), console.log(t.join("\n")), this.logs = this.logs.concat(t) } } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, e) { const s = !this.isSurge() && !this.isQuanX() && !this.isLoon(); s ? this.log("", `❗️${this.name}, 错误!`, t.stack) : this.log("", `❗️${this.name}, 错误!`, t) } wait(t) { return new Promise(e => setTimeout(e, t)) } done(t = {}) { const e = (new Date).getTime(), s = (e - this.startTime) / 1e3; this.log("", `🔔${this.name}, 结束! 🕛 ${s} 秒`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t) } }(t, e) }