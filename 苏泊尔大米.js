/*
 作者：ZFeng1005
 日期：10-19
 小程序：苏泊尔会员中心
 入口：苏泊尔会员中心小程序->首页->种大米
 功能：完成任务
 抓包：https://growrice.supor.com/rice/backend/public/index.php/api/login/auto-login? 链接中的 token=xxxxxxxxxx
 变量：sbrCookie='eyJ0xxxxxx@xxxxxxxx'  多个账号用 @ 或者 换行 分割
 tg频道：https://t.me/newtab0
 定时每天三次
 cron: 14 0,8,19 * * *
 */
const $ = new Env('苏泊尔')
const notify = $.isNode() ? require('./sendNotify') : '';
let cookiesArr = [],
  message = "",
  cookie = ($.isNode() ? process.env.sbrCookie : $.getdata("sbrCookie")) || ``
  !(async () => {
    await requireConfig();
    for (let i = 0; i < cookiesArr.length; i++) {
      if (cookiesArr[i]) {
        cookie = cookiesArr[i];
        msg = "";
        $.index = i + 1;
        $.canSteal = true;
        $.phpsessid = '';
        $.nickName = '';
        $.drawNum = '';
        $.taskList = {};
        $.friendList = {};
        await login()
        console.log(`\n******开始【👻苏泊尔账号${$.index}】 *********\n`);
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
  console.log(`【获取用户信息】`)
  await getUserInfo()
  await $.wait(1000)

  console.log(`\n【获取签到信息】`)
  await signInfo()
  await $.wait(1000)

  console.log(`\n【获取任务列表】`)
  await task()
  await $.wait(1000)

  for (i = 0; i < $.taskList.length; i++) {
    if ($.taskList[i].id === 8 && $.taskList[i].list[0]['is_finish'] === false) {
      console.log(`「浏览菜谱」`)
      await doTask($.taskList[i].id, $.taskList[i].list[0].id)
    } else if ($.taskList[i].id === 8 && $.taskList[i].list[0]['is_finish'] === true) {
      console.log(`「浏览菜谱」已完成`)
    } else if ($.taskList[i].id === 6 && $.taskList[i]['is_finish'] === false) {
      console.log(`「偷大米」`)
      await getid()
      await $.wait(1000)

      for (j = 0; j < $.friendList.length && $.canSteal; j++) {
        console.log(`去偷取：${$.friendList[j].id} 的大米`)
        await getRice($.friendList[j].id)
        await $.wait(1000)
      }
    } else if ($.taskList[i].id === 6 && $.taskList[i]['is_finish'] === true) {
      console.log(`「偷大米」已完成`)
    }
  }

  console.log(`\n【获取可收取大米列表】`)
  await index()
  if ($.taskList.length) {
    for (i = 0; i < $.taskList.length; i++) {
      console.log(`去收取：${$.taskList[i].name}`)
      await collect(`${$.taskList[i].id}`)
      await $.wait(1500)
    }
  } else console.log(`已收取完成！`)

  console.log(`\n【获取抽奖信息】`)
  await prize()
  await $.wait(1000)

  if ($.drawNum) {
    console.log(`共有：${$.drawNum} 次机会`)
    for (i = 0; i < $.drawNum; i++) {
      await draw()
      await $.wait(1000)
    }
  } else console.log(`暂无抽奖次数~`)

  console.log(`\n【获取账号情况】`)
  await index()
  console.log(`当前账号总数：${$.total}大米`)
  msg += `当前账号总数：${$.total}大米\n\n`
  await $.wait(1000)

  await showMsg()
  await $.wait(1000)
}
/**
 * 
 * 登录
 */
async function login() {
  let body = `?token=${cookie}`
  return new Promise(resolve => {
    $.get(taskUrl('login/auto-login', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (resp) {
            //resp = JSON.parse(resp);
            //console.log(JSON.stringify(resp));
            if (resp.status === 302 && resp['headers']['set-cookie']) {
              $.phpsessid = resp['headers']['set-cookie'][0].split(';')[0]
              //console.log($.phpsessid)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, data)
      } finally {
        resolve(resp);
      }
    })
  })
}
/**
 * 
 * 获取用户信息
 */
async function getUserInfo() {
  let body = ``
  return new Promise(resolve => {
    $.get(taskUrl('users/get-user-info', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              $.nickName = data.data.nickname
              console.log(`用户名：${$.nickName}`)
            } else {
              console.log(data.msg)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 获取签到信息
 */
async function signInfo() {
  let body = ``
  return new Promise(resolve => {
    $.get(taskUrl('signIn/sign-list', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              if (data.data['is_sign'] === false) {
                console.log(`今天未签到，去签到喽!`);
                await sign()
              } else {
                console.log(`今日已签到，明天再来吧！`)
              }
            } else {
              console.log(data.msg)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 签到
 */
async function sign() {
  let body = ``
  return new Promise(resolve => {
    $.post(taskUrl('signIn/sign', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              console.log(`签到成功！获得：${data.data['get_rice_num']}大米`);
            } else {
              console.log(data.msg)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 获取任务列表
 */
async function task() {
  let body = ``
  return new Promise(resolve => {
    $.get(taskUrl('task/index', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              $.taskList = data.data
              //console.log(JSON.stringify($.taskList))
            } else {
              console.log(data.msg)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 完成任务
 */
async function doTask(id, otherid) {
  let body = `&id=${id}&other_id=${otherid}`
  return new Promise(resolve => {
    $.post(taskPostUrl('task/link-task', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              console.log(`完成成功`)
            } else {
              console.log(data.msg)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 偷米
 */
async function getid() {
  let body = ``
  return new Promise(resolve => {
    $.get(taskUrl('users/same-city-list', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              $.friendList = data.data
            } else {
              console.log(data.msg)
              $.canSteal = false
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 偷米
 */
async function getRice(id) {
  let body = `&friend_id=${id}`
  return new Promise(resolve => {
    $.post(taskPostUrl('users/get-rice', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              console.log(`成功！总计:${data.data['sign_rice_num']}大米`)
            } else {
              console.log(data.msg)
              $.canSteal = false
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 获取可收取大米列表
 */
async function index() {
  let body = ``
  return new Promise(resolve => {
    $.get(taskUrl('index/index', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            console.log(JSON.stringify(data));
            if (data.code === 1) {
              $.taskList = data.data['rice_list']
              $.total = data.data['sign_rice_num']
              //console.log(JSON.stringify($.taskList))
            } else {
              console.log(data.msg)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 收米
 */
async function collect(id) {
  let body = `&id=${id}`
  return new Promise(resolve => {
    $.post(taskPostUrl('index/collect-rice', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              console.log(`成功！总计:${data.data['sign_rice_num']}大米`)
            } else {
              console.log(data.msg)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 获取抽奖信息
 */
async function prize() {
  let body = ``
  return new Promise(resolve => {
    $.get(taskUrl('prize/index', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              $.drawNum = data.data['draw_num_1']
              //console.log(JSON.stringify($.friendList))
            } else {
              console.log(data.msg)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * 抽奖
 */
async function draw() {
  let body = `cate=1`
  return new Promise(resolve => {
    $.post(taskPostUrl('prize/draw', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            //console.log(JSON.stringify(data));
            if (data.code === 1) {
              console.log(`抽奖成功！获得:${JSON.stringify(data.data)}`)
              msg += `抽奖成功！获得:${JSON.stringify(data.data)}\n`
            } else {
              console.log(data.msg)
            }
          } else {
            console.log("没有返回数据")
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}
/**
 * 
 * API
 */
function taskUrl(type, body) {
  return {
    url: `https://growrice.supor.com/rice/backend/public/index.php/api/${type}${body}`,
    headers: {
      "Host": "growrice.supor.com",
      "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "Accept-Encoding": "deflate, br",
      "Accept-Language": "en-us,en",
      "cookie": ($.phpsessid ? $.phpsessid : "PHPSESSID=o3lq8hkgmacf4rvsqkcn2te1ua")
    },
    "followRedirect": false,
    "allow_redirects": false,
  }
}

function taskPostUrl(type, body) {
  return {
    url: `https://growrice.supor.com/rice/backend/public/index.php/api/${type}`,
    headers: {
      "Host": "growrice.supor.com",
      "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "Accept-Encoding": "deflate, br",
      "Accept-Language": "en-us,en",
      "cookie": ($.phpsessid ? $.phpsessid : "PHPSESSID=o3lq8hkgmacf4rvsqkcn2te1ua")
    },
    "followRedirect": false,
    "allow_redirects": false,
    body: body
  }
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
    console.log(`\n【缺少sbrCookie环境变量或者sbrCookie为空！】`)
    return;
  }
}
/**
 * 
 * 消息推送
 */
async function showMsg() {
  message += `====== ${$.nickName} ======\n`;
  message += msg
  //console.log(message)
}
// prettier-ignore
function Env(t,e){class s{constructor(t){this.env=t}send(t,e="GET"){t="string"==typeof t?{url:t}:t;let s=this.get;return"POST"===e&&(s=this.post),new Promise((e,i)=>{s.call(this,t,(t,s,r)=>{t?i(t):e(s)})})}get(t){return this.send.call(this.env,t)}post(t){return this.send.call(this.env,t,"POST")}}return new class{constructor(t,e){this.name=t,this.http=new s(this),this.data=null,this.dataFile="box.dat",this.logs=[],this.isMute=!1,this.isNeedRewrite=!1,this.logSeparator="\n",this.startTime=(new Date).getTime(),Object.assign(this,e),this.log("",`🔔${this.name}, 开始!`)}isNode(){return"undefined"!=typeof module&&!!module.exports}isQuanX(){return"undefined"!=typeof $task}isSurge(){return"undefined"!=typeof $httpClient&&"undefined"==typeof $loon}isLoon(){return"undefined"!=typeof $loon}toObj(t,e=null){try{return JSON.parse(t)}catch{return e}}toStr(t,e=null){try{return JSON.stringify(t)}catch{return e}}getjson(t,e){let s=e;const i=this.getdata(t);if(i)try{s=JSON.parse(this.getdata(t))}catch{}return s}setjson(t,e){try{return this.setdata(JSON.stringify(t),e)}catch{return!1}}getScript(t){return new Promise(e=>{this.get({url:t},(t,s,i)=>e(i))})}runScript(t,e){return new Promise(s=>{let i=this.getdata("@chavy_boxjs_userCfgs.httpapi");i=i?i.replace(/\n/g,"").trim():i;let r=this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout");r=r?1*r:20,r=e&&e.timeout?e.timeout:r;const[o,h]=i.split("@"),n={url:`http://${h}/v1/scripting/evaluate`,body:{script_text:t,mock_type:"cron",timeout:r},headers:{"X-Key":o,Accept:"*/*"}};this.post(n,(t,e,i)=>s(i))}).catch(t=>this.logErr(t))}loaddata(){if(!this.isNode())return{};{this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e);if(!s&&!i)return{};{const i=s?t:e;try{return JSON.parse(this.fs.readFileSync(i))}catch(t){return{}}}}}writedata(){if(this.isNode()){this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e),r=JSON.stringify(this.data);s?this.fs.writeFileSync(t,r):i?this.fs.writeFileSync(e,r):this.fs.writeFileSync(t,r)}}lodash_get(t,e,s){const i=e.replace(/\[(\d+)\]/g,".$1").split(".");let r=t;for(const t of i)if(r=Object(r)[t],void 0===r)return s;return r}lodash_set(t,e,s){return Object(t)!==t?t:(Array.isArray(e)||(e=e.toString().match(/[^.[\]]+/g)||[]),e.slice(0,-1).reduce((t,s,i)=>Object(t[s])===t[s]?t[s]:t[s]=Math.abs(e[i+1])>>0==+e[i+1]?[]:{},t)[e[e.length-1]]=s,t)}getdata(t){let e=this.getval(t);if(/^@/.test(t)){const[,s,i]=/^@(.*?)\.(.*?)$/.exec(t),r=s?this.getval(s):"";if(r)try{const t=JSON.parse(r);e=t?this.lodash_get(t,i,""):e}catch(t){e=""}}return e}setdata(t,e){let s=!1;if(/^@/.test(e)){const[,i,r]=/^@(.*?)\.(.*?)$/.exec(e),o=this.getval(i),h=i?"null"===o?null:o||"{}":"{}";try{const e=JSON.parse(h);this.lodash_set(e,r,t),s=this.setval(JSON.stringify(e),i)}catch(e){const o={};this.lodash_set(o,r,t),s=this.setval(JSON.stringify(o),i)}}else s=this.setval(t,e);return s}getval(t){return this.isSurge()||this.isLoon()?$persistentStore.read(t):this.isQuanX()?$prefs.valueForKey(t):this.isNode()?(this.data=this.loaddata(),this.data[t]):this.data&&this.data[t]||null}setval(t,e){return this.isSurge()||this.isLoon()?$persistentStore.write(t,e):this.isQuanX()?$prefs.setValueForKey(t,e):this.isNode()?(this.data=this.loaddata(),this.data[e]=t,this.writedata(),!0):this.data&&this.data[e]||null}initGotEnv(t){this.got=this.got?this.got:require("got"),this.cktough=this.cktough?this.cktough:require("tough-cookie"),this.ckjar=this.ckjar?this.ckjar:new this.cktough.CookieJar,t&&(t.headers=t.headers?t.headers:{},void 0===t.headers.Cookie&&void 0===t.cookieJar&&(t.cookieJar=this.ckjar))}get(t,e=(()=>{})){t.headers&&(delete t.headers["Content-Type"],delete t.headers["Content-Length"]),this.isSurge()||this.isLoon()?(this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.get(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)})):this.isQuanX()?(this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t))):this.isNode()&&(this.initGotEnv(t),this.got(t).on("redirect",(t,e)=>{try{if(t.headers["set-cookie"]){const s=t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString();s&&this.ckjar.setCookieSync(s,null),e.cookieJar=this.ckjar}}catch(t){this.logErr(t)}}).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)}))}post(t,e=(()=>{})){if(t.body&&t.headers&&!t.headers["Content-Type"]&&(t.headers["Content-Type"]="application/x-www-form-urlencoded"),t.headers&&delete t.headers["Content-Length"],this.isSurge()||this.isLoon())this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.post(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)});else if(this.isQuanX())t.method="POST",this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t));else if(this.isNode()){this.initGotEnv(t);const{url:s,...i}=t;this.got.post(s,i).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)})}}time(t,e=null){const s=e?new Date(e):new Date;let i={"M+":s.getMonth()+1,"d+":s.getDate(),"H+":s.getHours(),"m+":s.getMinutes(),"s+":s.getSeconds(),"q+":Math.floor((s.getMonth()+3)/3),S:s.getMilliseconds()};/(y+)/.test(t)&&(t=t.replace(RegExp.$1,(s.getFullYear()+"").substr(4-RegExp.$1.length)));for(let e in i)new RegExp("("+e+")").test(t)&&(t=t.replace(RegExp.$1,1==RegExp.$1.length?i[e]:("00"+i[e]).substr((""+i[e]).length)));return t}msg(e=t,s="",i="",r){const o=t=>{if(!t)return t;if("string"==typeof t)return this.isLoon()?t:this.isQuanX()?{"open-url":t}:this.isSurge()?{url:t}:void 0;if("object"==typeof t){if(this.isLoon()){let e=t.openUrl||t.url||t["open-url"],s=t.mediaUrl||t["media-url"];return{openUrl:e,mediaUrl:s}}if(this.isQuanX()){let e=t["open-url"]||t.url||t.openUrl,s=t["media-url"]||t.mediaUrl;return{"open-url":e,"media-url":s}}if(this.isSurge()){let e=t.url||t.openUrl||t["open-url"];return{url:e}}}};if(this.isMute||(this.isSurge()||this.isLoon()?$notification.post(e,s,i,o(r)):this.isQuanX()&&$notify(e,s,i,o(r))),!this.isMuteLog){let t=["","==============📣系统通知📣=============="];t.push(e),s&&t.push(s),i&&t.push(i),console.log(t.join("\n")),this.logs=this.logs.concat(t)}}log(...t){t.length>0&&(this.logs=[...this.logs,...t]),console.log(t.join(this.logSeparator))}logErr(t,e){const s=!this.isSurge()&&!this.isQuanX()&&!this.isLoon();s?this.log("",`❗️${this.name}, 错误!`,t.stack):this.log("",`❗️${this.name}, 错误!`,t)}wait(t){return new Promise(e=>setTimeout(e,t))}done(t={}){const e=(new Date).getTime(),s=(e-this.startTime)/1e3;this.log("",`🔔${this.name}, 结束! 🕛 ${s} 秒`),this.log(),(this.isSurge()||this.isQuanX()||this.isLoon())&&$done(t)}}(t,e)}