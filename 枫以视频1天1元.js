/**
 * 枫以视频
 * 变量：fysp，多账号用# @ 换行分隔
 * 抓tv.palmestore.com域名/task_api/task/list/by_act_ids请求的参数
 * 只需要p1之后的参数，例如：p1=XXX&p16=XXXX&p2=XXX
 * 自动提现，如需修改提现金额修改101、102、103行参数
 * 提现时间修改62行
 */
const $ = new Env('枫以视频');

const { log } = require("console");
const crypto = require("crypto");
let fysp = process.env.fysp ? process.env.fysp : ""
let privateKey = '-----BEGIN PRIVATE KEY-----\n' +
    'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZo0B6v3MzB5EIQNXdKui3nQqZg39mGHFHk96/iRyEydN6AUJBHhS3UQ1H7obpJOdToo4SyRf9dANYjh30ZNnJ7tJ3Pe+iWBbCXgCTxQhcbjQHCKvC4EkbaooRZqaF9Ki+jHI/xEbKHzHMaW0FNoJhHHp7LV2UrLHvYYS7947OUpIMhv0npYim4ET1nKbrKdeggkszq/m2M9B349Pf3ao07XyPypjdUaJtOFtI8pJJk1qwJKeYQC2fAa3y8HzL6QRgXeG12ngw8Si5V3sKsAQLjFaGC5jBdlertCxbYlAtJBfIV0ZdUWjrhPh7c+TQodF+3xEwnjwLip45HoK8FRDtAgMBAAECggEAKM2ZpinEsFmH0HNPZVLJJLuVpChqNzr36gKILYLITQEF3AbmZAz+t0vD4KuQsZ9Qm3aLimwXSlZ41h528T4DMv/Kh76d8eLwCWrUUuAK7EFhEbyHb1bbff9geVi0ecLf7DGqrdffqb9ld7yASwzoLsrHD9b2h4xFI+s1loQYSwgJhR7lljt+/ESNylUVpKDuCnOsMcjBquEScBHo5m4PhZE+BtpiRdoU+6ig9OgrnQoMO8ioR0p4J5bjlLgt9dat/bn7SOk3iQD/dACG0GnZOZJUtJ97RkYjAi/convpl60oibm2XKV/WqGZYlvCO2PVdi28iyUcN+LM1ie23KfTBQKBgQDtsKc36mKpS5CD1kDdnth+ye1dLZZh9sJtCKEpVFoseOgpbG8mKhrxpeOaDlp8RV88plMclvIQEesJlaAd1nn5JfcXNhB676t+ERfexwRebDfzl91wmySAs8Af0wnX9oRnwyb28xz2kvGQ8H+102HeCQ4b+I6kONkQFQzhhIwaiwKBgQDqZyhy+tu2tmQb5zCd3PFN7vxMuvRJ+m6sWrBiUt0v3GHskLYz61CiMxO8l6QDfV3IHkKNBvTpUQUobNH4szTq7OVSaIbUJJI50JCO7mEAqab4gYrlS5BsGVVvgzrHL8uKdQajagqGzaYX2YUO28mRyQxNRTG2mLA/mAEbcsaJZwKBgHw1/Kyzx6tA2dyLcopeIDThwTEYSaYYFbJ0+ANpGVZ0OJ6tE8iV6E6vqikvpwmaFxLSuEwQdZ8APhtcHbh6BHO261Et557W8H+I3ziEODw/wV2C1y2pZYH8bUI0PsilArxWt14F3fTdBXAAvjx+on4trTngwmn/ay+EUJ7pbW3RAoGBANH5dKeDBlynCAhi0g8nw1Uvtvy5IGpAlvF4D7cUSaU9As9aVo0txz51CMIRCNBDdkX0rWMNj0iN1lP/Hxxs1AN6EHcAwX65/+8gYM5YxbZFQxgrWxPJ2+apzvmkkXuq2eb+q+Ko9CMLhzSoGuRTiD463fU9/al3H7Ln5F4FM8oTAoGAcxDGaSUJ9Y+j/k+O3464gzbQ0I6R8TcD+efDK0rm7oDKssRsYasMEUoh/+MgrPlCTsgcuIaiD7EzNHozYioEOb78iBqhzNQN3BYtNvYdKhFS7hmNVuWlIIvPGZtrkQYRZG45W5weydCdVX2ZejUuqBObiFjIyhHW8uqCUJsrp+U=' +
    '\n-----END PRIVATE KEY-----'
const baseurl = 'https://tv.palmestore.com'
const debug = false

class User {
    constructor(param,usr,index) {
        this.param = param
        this.index = index
        this.nick = ''
        this.usr = usr
        this.bookid = 0
    }
}

    !(async () => {
        if(fysp){
            fysp = Envs()
            let userList = []
            log(`共${fysp.length}个账号`)
            for(let k = 0;k<fysp.length;k++){

                userList.push(new User(fysp[k],getValue(fysp[k],'usr'),k+1))
            }
            
            for(let user of userList){
                log(`开始第${user.index}个账号`)


                await adcfg(user)
                await withdrawTypelist(user)
                await userGold(user)
                await taskList(user)
            
                log('---------------')
            }

            // userList = userList.filter(user => user.bookid !== 0)
            // for(let i = 0;i<50;i++){
            //     for(let j = 0;j< userList.length;j++){
                   
            //     //   videoTimeReport(userList[j].bookid,userList[j])

            //     }
            //     // await $.wait(50000)
            // }
            
            if(new Date().getHours() === 11){
                for(let user of userList){
                    await withdraw(user)
                }
            }

        }else{
            log('未设置环境变量')
        }


        


    })()
    .catch((e) => $.logErr(e))
    .finally(() => $.done())

    function Envs() {
        let t = []
        if (fysp.indexOf('#') > -1){
            t = fysp.split('#')
        }else if (fysp.indexOf('@') > -1){
            t = fysp.split('@')
        }else if (fysp.indexOf('\n') > -1){
            t = fysp.split('\n')
        }else if (fysp.length > 0) {
            t.push(fysp)
        }
        return t.filter(item => !!item)
    
    
    }
/**金额 id 签到天数
 * 2元 281 7
 * 10 282 15
 * 20 283 20
 * 30 276 30
 */
async function withdraw(user){
    let amount = 20 //根据注释填写
    let subid = 283
    let day = 7
    if(user.rmb >= 1 && user.signinday >= day){
        if(user.alipay){
            await exec('alipay',amount,subid,user)
        }else if(user.wechat){
            await exec('wechat',amount,subid,user)
        }else{
            log('没有绑定提现账号')
        }
    }else{
        log(`${user.index} 余额不足`)
    }


    

}

async function userGold(user){

    let opt = buildURLObject('/tv_welfare/gold/user/gold_account','gold_type=3&'+user.param)
    
    let res = await get(opt)
    if(res.code === 0){
        log(`金币：${res.body.total_gold_num} 余额：${res.body.total_rmb} 累计提现：${res.body.total_withdraw}`)
        user.rmb = res.body.total_rmb
        log(`观看时长：${formatSeconds(res.body.watching_time.day)}`)
    }else{
        log(`获取金币错误，`,$.toStr(res))
    }

}

async function adcfg(user){
    let opt = buildURLObject('/ad/cfg',`app_id=10183&timestamp=${Date.now()}&apiver=2&app_name=%E6%9E%AB%E4%BB%A5%E8%A7%86%E9%A2%91&app_package=com.app.fengyiFree&app_platform=501611&app_ver=1.0.3.1&is_mobile=1&os_type=android&plugin_name=pluginwebdiff_ad&plugin_ver=30&sdkVersion=1010020&${user.param}`)
    opt.url = opt.url.replace('tv.palmestore.com','saad.ms.zhangyue.net')
    opt.headers['Host'] = 'saad.ms.zhangyue.net'
    let res = await get(opt)
    if(res.code === 0){
        log(`广告配置成功！`)
        for(let r of res.body.rules){
            switch(r.slotId){
                case 'SIGN_WINDOW_VIDEO':
                    user.sign_window_video = r.rule
                    getRandomADCfg(r.rule)
                    break
                case 'VIDEO_AGAIN':
                    user.video_again = r.rule
                    break
                case 'VIDEO_WELFARE_GOLD':
                    user.video_welfare_gold = r.rule
                    break
                case 'WELFARE_SCREEN':
                    user.welfare_screen = r.rule
                    break

            }
        }


        


    }else{
        log(`获取广告配置错误，`,$.toStr(res))
    }
}

function getRandomADCfg(arr,flag = 'reward'){
    //收集数组中对象的strategies属性，strategies是一个数组,并过滤mixAdType属性是reward的对象
    if (flag === ''){
        let strategies =  arr.map(item => item.strategies).flat()
        let randomStrategy = strategies[Math.floor(Math.random() * strategies.length)]
        return randomStrategy   
    }
    let strategies = arr.map(item => item.strategies).flat().filter(item => item.mixAdType !== flag)
    //随机一个strategies
    let randomStrategy = strategies[Math.floor(Math.random() * strategies.length)]
    return randomStrategy
}


async function taskList(user){
    let opt = buildURLObject('/task_api/task/list/by_act_ids','act_ids=act_a0a1f9d9,act_e80ba223&'+user.param)
    let res = await get(opt)
    if(res.code === 0){
        let tasks = res.body['act_a0a1f9d9']['task_list']
        for(let task of tasks){
            log(`${task.title}广告  ${task.rewarded_count}/${task.reward_limit_count}`)
        }
        tasks = res.body['act_e80ba223']['task_list']
        for (let task of tasks) {
            if(task.id === 'task_7ba48625'){ //新人2元见面礼
                log(`${task.title} ${task.reward_status === 'rewarded'?'已完成':'未完成'}`)

            }else if(task.id === 'task_357d80d1'){ //新人
                log(task.title)
                let ts = Date.now()
                for(let sub of task['sub_task_list']){
                    if(sub.reward_status === 'un_reward' && (ts > sub.start_time && ts < sub.end_time)){
                        await draw_gift('新人奖励',`act_id=act_e80ba223&task_id=task_357d80d1&sub_task_id=${sub.id}&${user.param}`)
                        break
                    }
                }
            }else if(task.id === 'task_a2cdf5f5'){ //签到
                user.signinday = task.continuous_drew_num
                let ts = Date.now()
                for(let sub of task['sub_task_list']){
                    if(ts > sub.start_time && ts < sub.end_time){
                        if(sub.reward_status === 'un_reward' ){
                            await draw_gift('签到',`act_id=act_e80ba223&task_id=task_a2cdf5f5&sub_task_id=${sub.id}&${user.param}`)
                            let ecpm = (crypto.randomInt(50,60))*100
                            let sid = getRandomADCfg(user.video_welfare_gold).id
                            await draw_gift('签到广告',`${user.param}&act_id=act_a0a1f9d9&task_id=task_0688f0ce&sid=${sid}&ecpm=${ecpm}`)
    
                            break
                        }else{
                            log(`今日已签到，连续签到${task.continuous_drew_num}`)
                            user.signinday = task.continuous_drew_num
                            break
                        }
                        
                    }
                }
            }else if(task.id === 'task_d8ad3326'){ //宝箱
                if (task.reward_limit_count != task.rewarded_count){
                    await draw_gift('宝箱',`act_id=act_e80ba223&task_id=task_d8ad3326&sub_task_id=&${user.param}`)
                    let ecpm = (crypto.randomInt(50,60))*100
                    let sid = getRandomADCfg(user.video_welfare_gold).id
                    await draw_gift('宝箱广告',`${user.param}&act_id=act_a0a1f9d9&task_id=task_a27a7a25&sid=${sid}&ecpm=${ecpm}`)
    
                }
            }else if(task.id === 'task_ee85283c'){ //三餐
                
                
            }else if(task.id === 'task_acab7244' || task.id === 'task_8aef8790'){ // 看热播剧赚金币
                let l = task.sub_task_list
                for (let sub of l){
                    if(sub.status === 'un_finished'){
                        log(`观看视频 ${sub.tv_series.name}`)
                        user.bookid = sub.tv_series.id
                        break
                    }else if(sub.reward_status === ''){

                    }
                }
                
            }else if(task.id === 'task_122addf6'){ // 看剧赚金币
                let l = task.sub_task_list
                for(let sub of l){
                    if(sub.status === 'finished'&& sub.reward_status === 'un_reward'){
                        await draw_gift(task.title,`act_id=act_e80ba223&task_id=task_122addf6&sub_task_id=${sub.id}&${user.param}`)
                    }
                }
            }else if(task.id === 'task_fb1296a1' ){
                //看视频赚金币
                if(task.reward_limit_count != task.rewarded_count){
                    let subl = task.sub_task_list
                    for(let s of subl){
                        if (s.reward_status === 'un_reward'){
                            let ecpm = (crypto.randomInt(15,30))*100
                            let sid = getRandomADCfg(user.video_welfare_gold).id
                            await draw_gift('看视频赚金币',`${user.param}&act_id=act_e80ba223&task_id=task_fb1296a1&sub_task_id=${s.id}&sid=${sid}&ecpm=${ecpm}`)
                            break
                        }
                        
                    }
                }
                
            }else if(task.id === 'task_5e779d39' ){
                if( task.reward_limit_count != task.rewarded_count){
                    let ecpm = (crypto.randomInt(50,60))*100
                    let sid = getRandomADCfg(user.video_welfare_gold,'rewardToInsert').id
                    await draw_gift('看图文赚金币',`${user.param}&act_id=act_e80ba223&task_id=${task.id}&sid=${sid}&ecpm=${ecpm}`)
                    sid = getRandomADCfg(user.video_welfare_gold,'rewardToInsert').id
                    await draw_gift('看图文赚金币全局广告',`${user.param}&act_id=act_e80ba223&task_id=${task.id}&sid=${sid}&ecpm=${ecpm}`)
                    await $.wait(20000)
                    sid = getRandomADCfg(user.video_welfare_gold,'rewardToInsert').id
                    await draw_gift('看图文赚金币全局广告',`${user.param}&act_id=act_e80ba223&task_id=${task.id}&sid=${sid}&ecpm=${ecpm}`)
                    await $.wait(20000)
                    sid = getRandomADCfg(user.video_welfare_gold,'rewardToInsert').id
                    await draw_gift('看图文赚金币全局广告',`${user.param}&act_id=act_e80ba223&task_id=${task.id}&sid=${sid}&ecpm=${ecpm}`)
    
                }
                
            }else if (task.id === 'task_78b51c0d' ){
                if(task.reward_limit_count != task.rewarded_count){
                    let ecpm = (crypto.randomInt(50,60))*100
                    let sid = getRandomADCfg(user.welfare_screen,'').id
                    await draw_gift('点击秒赚金币',`${user.param}&act_id=act_e80ba223&task_id=${task.id}&sid=${sid}&ecpm=${ecpm}`)
                    sid = getRandomADCfg(user.welfare_screen).id
                    await draw_gift('点击秒赚金币全局广告',`${user.param}&act_id=act_a0a1f9d9&task_id=task_a27a7a25&sid=${sid}&ecpm=${ecpm}`)
                    await $.wait(20000)
                    sid = getRandomADCfg(user.welfare_screen).id
                    await draw_gift('点击秒赚金币全局广告',`${user.param}&act_id=act_a0a1f9d9&task_id=task_a27a7a25&sid=${sid}&ecpm=${ecpm}`)
                    await $.wait(20000)
                    sid = getRandomADCfg(user.welfare_screen).id
                    await draw_gift('点击秒赚金币全局广告',`${user.param}&act_id=act_a0a1f9d9&task_id=task_a27a7a25&sid=${sid}&ecpm=${ecpm}`)
    
                }
                
            }else{
                log(`${task.title} 未实现，请手动完成！`)
            }
        }

        
        
    }else if(res.code === 1301015){
        await taskList(user)
    }else{
        log('任务列表获取失败，',$.toStr(res))
    }
}


async function draw_gift(taskname,body){
    let opt = buildURLObject('/task_api/task/draw_gift','',body)
    let res = await post(opt)
    if(res.code === 0){
        log(`${taskname} 领取成功，获得${res.body.gift_info[0].amount}金币`)
    }else{
        log(`${taskname} 领取失败，`,$.toStr(res))
    }
}


async function withdrawTypelist(user){
    let opt = buildURLObject('/tv_welfare/gold/withdraw/type_list',`gold_type=3&${user.param}`)
    let res = await get(opt)
    if(res.code === 0){
        let list = res.body.list
        log(`${list[0].title} ${list[0].bind_info.is_bind?'已绑定':'未绑定'} ${list[0].bind_info.nick}`)
        log(`${list[1].title} ${list[1].bind_info.is_bind?'已绑定':'未绑定'} ${list[1].bind_info.nick}`)
        user.alipay = list[0].bind_info.is_bind
        user.wechat = list[1].bind_info.is_bind

        //每日提现
    }else{
        log('获取提现账号信息失败，',$.toStr(res))
    }
}

async function exec (type,amount ,subid,user){
    let opt = buildURLObject('/tv_welfare/gold/withdraw/exec','',`type=${type}&amount=${amount}&sub_id=${subid}&gold_type=3&${user.param}`)
    let res = await post(opt)
    if(res.code === 0){
        log(`账号 ${user.index} 提现成功！`)
    }else{
        log(`账号 ${user.index} 提现失败，`,$.toStr(res))
    }
}

async function getVideoList(param){
    let opt = buildURLObject('/bookstore/frequency_list',`key=channel_40c4002f&${param}`)
    let res = await get(opt)
    if(res.code === 0){
        let list = res.body.list
        let r1 = random(1,list.length)
        let r2 = random(0,list[r1].tv_shows.length)
        let video = list[r1].tv_shows[r2]

    }else{
        log(`获取视频列表失败，`,$.toStr(res))

    }
}

async function videoTimeReport(id,user){
    let sec = random(50,60)
    let date = $.time('yyyy-MM-dd')
    let info = `[{"book_id":"${id}","date":"${date}","res_type":"watch","second":${sec}}]`
    let opt = buildURLObject('/reading/duration/report','',`app_id=zy3d1ef1&date_info=${info}&${user.param}&user_name=${user.usr}`)
    let res = await post(opt)
    if(res.code === 0){
        log(`账号 ${user.index} 视频时长上传成功！`)
    }else{
        log(`账号 ${user.index} 视频时长上传失败，`,$.toStr(res))
    }
}

function formatSeconds(value) {
    let theTime = parseInt(value);// 秒
    let theTime1 = 0;// 分
    let theTime2 = 0;// 小时
    if(theTime > 60) {
        theTime1 = parseInt(theTime/60);
        theTime = parseInt(theTime%60);
        if(theTime1 > 60) {
            theTime2 = parseInt(theTime1/60);
            theTime1 = parseInt(theTime1%60);
        }
    }
    let result = ""+parseInt(theTime)+"秒";
    if(theTime1 > 0) {
        result = ""+parseInt(theTime1)+"分"+result;
    }
    if(theTime2 > 0) {
        result = ""+parseInt(theTime2)+"小时"+result;
    }
    return result;
}

function sortQueryParams(urlString) {
    const url = new URLSearchParams(urlString);
    const sortedParams = [...url.entries()].sort((a, b) => a[0].localeCompare(b[0]));

    const sortedSearchParams = new URLSearchParams();
    sortedParams.forEach(param => {
        sortedSearchParams.append(param[0], param[1]);
    });

    return decodeURIComponent(sortedSearchParams.toString());
}



function createSign(data) {
    const sign = crypto.createSign('RSA-SHA256');
    sign.update(data);
    sign.end();
    return sign.sign(privateKey).toString('base64');

}

function random(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}






function buildURLObject(path,param,body=''){
    let url = baseurl + path
    if(param){
        url  = url + '?' + param
    }
    let ts = Date.now()
    let signstr = `${body}&${sortQueryParams(param)}&${path}&${ts}`
    let sign = createSign(signstr)
    let host = (url.split('//')[1]).split('/')[0]
    let urlObject = {
        url: url,
        headers: {
            'Host': host,
            "user-agent":'Mozilla/5.0 (Linux; Android 10; PBEM00 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 zyApp/sudu zyVersion/2.0.0 zyChannel/331104',
            // "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Encoding":"gzip, deflate",
            "X-SIG-Sign":sign,
            "X-SIG-Timestamp":ts,
            'X-AppId': 'zy3d1ef1',
            'X-SIG-Alg':'RSA-SHA256'
        },
    }
    if(body) urlObject.body = body
    
    return urlObject;
}
function getValue(str,key,split='&') {
    let reg = new RegExp(`${key}=([^${split}]*)`)
    let res = reg.exec(str)
    return res[1]
}



function getTimestamp() {
    let ts = new Date().getTime()
    return ts
}
async function post(opt) {
    return new Promise((resolve, reject) => {
        $.post(opt,async(err,resp,data) => {
            try {
                if (err){
                    console.log('post请求错误')
                    console.log($.toStr(err))
                }else {
                    if (debug){
                        console.log(data)}
                    httpResult = $.toObj(data)
                    resolve(httpResult)
                }
            }catch (e) {
                console.log(e)
            }finally{
                resolve()
            }
        })
    })
}

async function get(opt) {
    return new Promise((resolve, reject) => {
        $.get(opt,async(err,resp,data) => {
            try {
                if (err){
                    console.log('get请求错误')
                    console.log($.toStr(err))
                }else {
                    if (debug){
                        console.log(data)}
                    httpResult = $.toObj(data)
                    resolve(httpResult)
                }
            }catch (e) {
                console.log(e)
            }finally{
                resolve()
            }
        })
    })
}




function Env(t, e) { class s { constructor(t) { this.env = t } send(t, e = "GET") { t = "string" == typeof t ? { url: t } : t; let s = this.get; return "POST" === e && (s = this.post), new Promise((e, i) => { s.call(this, t, (t, s, r) => { t ? i(t) : e(s) }) }) } get(t) { return this.send.call(this.env, t) } post(t) { return this.send.call(this.env, t, "POST") } } return new class { constructor(t, e) { this.name = t, this.http = new s(this), this.data = null, this.dataFile = "box.dat", this.logs = [], this.isMute = !1, this.isNeedRewrite = !1, this.logSeparator = "\n", this.startTime = (new Date).getTime(), Object.assign(this, e), this.log("", `\ud83d\udd14${this.name}, \u5f00\u59cb!`) } isNode() { return "undefined" != typeof module && !!module.exports } isQuanX() { return "undefined" != typeof $task } isSurge() { return "undefined" != typeof $httpClient && "undefined" == typeof $loon } isLoon() { return "undefined" != typeof $loon } toObj(t, e = null) { try { return JSON.parse(t) } catch { return e } } toStr(t, e = null) { try { return JSON.stringify(t) } catch { return e } } getjson(t, e) { let s = e; const i = this.getdata(t); if (i) try { s = JSON.parse(this.getdata(t)) } catch { } return s } setjson(t, e) { try { return this.setdata(JSON.stringify(t), e) } catch { return !1 } } getScript(t) { return new Promise(e => { this.get({ url: t }, (t, s, i) => e(i)) }) } runScript(t, e) { return new Promise(s => { let i = this.getdata("@chavy_boxjs_userCfgs.httpapi"); i = i ? i.replace(/\n/g, "").trim() : i; let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout"); r = r ? 1 * r : 20, r = e && e.timeout ? e.timeout : r; const [o, h] = i.split("@"), a = { url: `http://${h}/v1/scripting/evaluate`, body: { script_text: t, mock_type: "cron", timeout: r }, headers: { "X-Key": o, Accept: "*/*" } }; this.post(a, (t, e, i) => s(i)) }).catch(t => this.logErr(t)) } loaddata() { if (!this.isNode()) return {}; { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e); if (!s && !i) return {}; { const i = s ? t : e; try { return JSON.parse(this.fs.readFileSync(i)) } catch (t) { return {} } } } } writedata() { if (this.isNode()) { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e), r = JSON.stringify(this.data); s ? this.fs.writeFileSync(t, r) : i ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r) } } lodash_get(t, e, s) { const i = e.replace(/\[(\d+)\]/g, ".$1").split("."); let r = t; for (const t of i) if (r = Object(r)[t], void 0 === r) return s; return r } lodash_set(t, e, s) { return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), e.slice(0, -1).reduce((t, s, i) => Object(t[s]) === t[s] ? t[s] : t[s] = Math.abs(e[i + 1]) >> 0 == +e[i + 1] ? [] : {}, t)[e[e.length - 1]] = s, t) } getdata(t) { let e = this.getval(t); if (/^@/.test(t)) { const [, s, i] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : ""; if (r) try { const t = JSON.parse(r); e = t ? this.lodash_get(t, i, "") : e } catch (t) { e = "" } } return e } setdata(t, e) { let s = !1; if (/^@/.test(e)) { const [, i, r] = /^@(.*?)\.(.*?)$/.exec(e), o = this.getval(i), h = i ? "null" === o ? null : o || "{}" : "{}"; try { const e = JSON.parse(h); this.lodash_set(e, r, t), s = this.setval(JSON.stringify(e), i) } catch (e) { const o = {}; this.lodash_set(o, r, t), s = this.setval(JSON.stringify(o), i) } } else s = this.setval(t, e); return s } getval(t) { return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? (this.data = this.loaddata(), this.data[t]) : this.data && this.data[t] || null } setval(t, e) { return this.isSurge() || this.isLoon() ? $persistentStore.write(t, e) : this.isQuanX() ? $prefs.setValueForKey(t, e) : this.isNode() ? (this.data = this.loaddata(), this.data[e] = t, this.writedata(), !0) : this.data && this.data[e] || null } initGotEnv(t) { this.got = this.got ? this.got : require("got"), this.cktough = this.cktough ? this.cktough : require("tough-cookie"), this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar, t && (t.headers = t.headers ? t.headers : {}, void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar)) } get(t, e = (() => { })) { t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? (this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.get(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) })) : this.isQuanX() ? (this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t))) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, e) => { try { if (t.headers["set-cookie"]) { const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString(); this.ckjar.setCookieSync(s, null), e.cookieJar = this.ckjar } } catch (t) { this.logErr(t) } }).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) })) } post(t, e = (() => { })) { if (t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), t.headers && delete t.headers["Content-Length"], this.isSurge() || this.isLoon()) this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.post(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) }); else if (this.isQuanX()) t.method = "POST", this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t)); else if (this.isNode()) { this.initGotEnv(t); const { url: s, ...i } = t; this.got.post(s, i).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) }) } } time(t) { let e = { "M+": (new Date).getMonth() + 1, "d+": (new Date).getDate(), "H+": (new Date).getHours(), "m+": (new Date).getMinutes(), "s+": (new Date).getSeconds(), "q+": Math.floor(((new Date).getMonth() + 3) / 3), S: (new Date).getMilliseconds() }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, ((new Date).getFullYear() + "").substr(4 - RegExp.$1.length))); for (let s in e) new RegExp("(" + s + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? e[s] : ("00" + e[s]).substr(("" + e[s]).length))); return t } msg(e = t, s = "", i = "", r) { const o = t => { if (!t) return t; if ("string" == typeof t) return this.isLoon() ? t : this.isQuanX() ? { "open-url": t } : this.isSurge() ? { url: t } : void 0; if ("object" == typeof t) { if (this.isLoon()) { let e = t.openUrl || t.url || t["open-url"], s = t.mediaUrl || t["media-url"]; return { openUrl: e, mediaUrl: s } } if (this.isQuanX()) { let e = t["open-url"] || t.url || t.openUrl, s = t["media-url"] || t.mediaUrl; return { "open-url": e, "media-url": s } } if (this.isSurge()) { let e = t.url || t.openUrl || t["open-url"]; return { url: e } } } }; this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(e, s, i, o(r)) : this.isQuanX() && $notify(e, s, i, o(r))); let h = ["", "==============\ud83d\udce3\u7cfb\u7edf\u901a\u77e5\ud83d\udce3=============="]; h.push(e), s && h.push(s), i && h.push(i), console.log(h.join("\n")), this.logs = this.logs.concat(h) } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, e) { const s = !this.isSurge() && !this.isQuanX() && !this.isLoon(); s ? this.log("", `\u2757\ufe0f${this.name}, \u9519\u8bef!`, t.stack) : this.log("", `\u2757\ufe0f${this.name}, \u9519\u8bef!`, t) } wait(t) { return new Promise(e => setTimeout(e, t)) } done(t = {}) { const e = (new Date).getTime(), s = (e - this.startTime) / 1e3; this.log("", `\ud83d\udd14${this.name}, \u7ed3\u675f! \ud83d\udd5b ${s} \u79d2`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t) } }(t, e) }

