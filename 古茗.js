/**
 * @title: 古茗抢购
 * @name: 偷撸项目组
 * @author: 6
 * @version: 1.0.0
 * @TS: 该版本为测试版，测试阶段
 * @description: 古茗抢购
 * @copyright: 2024 偷撸项目组保留所有权利。
 * @since: 2024-07-17
 * @env: ck变量：gmck token,多号&隔开
 * @cron: 55 11 * * *
 */

const axios = require('axios');
const dayjs = require('dayjs');

//==================自定义区域=================

let magnum = 1000; // 抢购上限次数
let bfsum = 1; // 并发请求数量
let site = 2000; // 请求超时时间，毫秒级
let tqyc = 0.2; // 提前延迟时间，单位：秒,默认加，要减则设置为负数
let qqjg = 0.02; // 循环请求间隔
let bfjg = 0.02; // 并发请求间隔
let qgid = '冷链鲜牛乳'; // 口令

//================变量区域====================

let log = console.log;
let token;
if (process.env.gmck) {
    token = process.env.gmck;
} else {
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJHT09ETUUuQ09NIiwiYXVkIjpbImFwcGxldCJdLCJpYXQiOjE3MjExNzgwOTksImp0aSI6IjE2MzYwMWJlLWQ3YmUtNGQwZS1hMThkLTNmNTgxZGQwNDg0ZSIsImVjcF9waG9uZSI6InB0UElsLzJYQ2RWNmU4T1VLVzUweHc9PSIsImNyZWF0ZV90aW1lc3RhbXAiOjE3MjExNzgwOTEwMDAsImxvZ2luVHlwZSI6IjQxIiwib3Blbl9pZCI6Im9NekF3NVVoQW84Q3NJVzdLUTg5cGtESmdXVlUiLCJuaWNrbmFtZSI6IueIseiKneWjq-iMieiOieeahOWkp-iMl-aYnyIsInVzZXJJZCI6IjIwMDAwMDAwMDAxMjY0NTAxMjIiLCJ2ZXJzaW9uIjoiMS4wIiwiZXhwIjoxNzIyMTk2ODk5fQ.fy35gUEShdZV_PogRXb5b4IZpgaQDhAVQrOsojiLAc_scvA30yabgGTQBsroxBx7z_fZJw8q2mWpumVDKpNM-nI5L0Pvd4zn_ZOZyHS45-DCvT218-HKeWbkENInV6lX5APHZM0fZrYq-7wp7ZYlqQFyOKBMYjox3iyvMCDH2OjexfRWWmUrlpyWuFKZxvpDqsfFgAeBJb1fs5hzGJ-YJLhpEhs9q5BXyoBvKl1qCI3BRBB7Eq1Aic83o9GfdOnvuwPVXkDKMxLb6cp85_IhESoerkfoemr8dKDOVOyjYuqX4PDL4pl5Q-A0306bo0O0vW4pxw5Z5g1z9PZpf42uvQ';
    if (token === '') {
        log("检测到环境变量、本地ck都为空");
        return;
    }
}
let cks = token.split("&");

//===============代码块=======================

function getCurrentTime() {
    return dayjs().format('HH:mm:ss.SSS');
}

function p(p) {
    if (p.length === 11) {
        return p.slice(0, 3) + '****' + p.slice(7);
    } else {
        return p;
    }
}

class QG {
    constructor(ck2) {
        this.token = ck2.split("#")[0];
        this.qg_hour = 11;
        this.qg_minute = 59;
        this.qg_second = 59;
        this.hd = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 14; 23117RK66C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220133 MMWEBSDK/20240404 MMWEBID/7136 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 miniProgram/wx1736dcbd36f4c055",
            'Content-Type': "application/json",
            't-token': "iWPHA1721142011CvgbrbnLup5",
            'Authorization': "Bearer " + this.token,
            'Cache-Control': "max-age=0",
            'X-Requested-With': "com.tencent.mm",
            'Referer': "https://h5.gumingnc.com/",
            'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        };
    }

    async login() {
        const url = "https://newton.gumingnc.com/newton-buyer/newton/buyer/member/v2/myInfo?brandId=1";
        const axiosConfig = {
            headers: this.hd,
            timeout: Number(site),
        };
        try {
            const r = await axios.get(url, axiosConfig);
            if (r.data.code === 0) {
                const name = r.data.data.mobile;
                this.name = p(name);
                return true;
            } else {
                log(`登录失败`);
                return false;
            }
        } catch (e) {
            log(`[${name}]--[${getCurrentTime()}]--${e}`);
            return false;
        }
    }

    async get_id() {
        const url = "https://h5.gumingnc.com/newton-buyer/newton/buyer/ump/milk/tea/activity/index";
        const payload = {
            channelCode: 20,
            brandId: 1
        };
        const axiosConfig = {
            headers: this.hd
        };

        try {
            const response = await axios.post(url, payload, axiosConfig);

            if (response.data.code === 0) {
                const allActivities = response.data.data.allActivity;
                this.id = null;
                allActivities.forEach(activity => {
                    if ('consumptionInventoryId' in activity) {
                        this.id = activity.consumptionInventoryId;
                        log(`[${this.name}]--[${getCurrentTime()}]--获取ID成功`);
                        return this.id;
                    }
                });
                if (this.id !== null) {
                    return this.id;
                } else {
                    console.log(`未找到id`);
                    return null;
                }
            } else {
                console.error(`获取 ID 失败: ${response.data}`);
                return null;
            }
        } catch (error) {
            console.error('获取 ID 出现错误:', error);
            return null;
        }
    }

    async post_qg() {
        const url = "https://h5.gumingnc.com/newton-buyer/newton/buyer/ump/milk/tea/activity/fcfs";
        const payload = {
            channelCode: 20,
            activityId: 13,
            brandId: 1,
            keyWordAnswer: qgid,
            consumptionInventoryId: this.id
        };
        const axiosConfig = {
            headers: this.hd,
            timeout: Number(site),
        };
        let count = 0;
        this.shouldStop = false;
        while (count < Number(magnum) && !this.shouldStop) {
            const promises = [];
            for (let i = 0; i < Number(bfsum); i++) {
                promises.push(
                    (async () => {
                        try {
                            const r = await axios.post(url, payload, axiosConfig);
                            if (r.data.code === 0) {
                                if (typeof r.data === 'string' && (r.data.includes('成功') || r.data.includes('恭喜'))) {
                                    log(`[${this.name}]--[${getCurrentTime()}]--抢兑成功`);
                                    this.shouldStop = true;
                                }
                            } else {
                                if ('msg' in r.data) {
                                    log(`[${this.name}]--[${getCurrentTime()}]--${r.data.msg}`);
                                } else {
                                    log(`[${this.name}]--[${getCurrentTime()}]--${JSON.stringify(r.data)}`);
                                }
                            }
                        } catch (e) {
                            log(`[${this.name}]--[${getCurrentTime()}]--${e}`);
                        }
                    })()
                );
                await new Promise(resolve => setTimeout(resolve, Number(bfjg)));
            }
            await Promise.all(promises);
            count++;
            if (!this.shouldStop) {
                await new Promise(resolve => setTimeout(resolve, Number(qqjg) * 1000));
            }
        }
        log(`[${this.name}]--[${getCurrentTime()}]--停止请求`);
    }


    async start() {
        const now = dayjs();
        const target_time = now.set('hour', this.qg_hour).set('minute', this.qg_minute).set('second', this.qg_second);
        if (now.isAfter(target_time)) {
            log("抢购时间已过，你来晚了!");
            return;
        }
        let time_to_wait = target_time.diff(now, 'seconds');
        log(`等待 ${time_to_wait} 秒后发起请求`);
        await new Promise(resolve => setTimeout(resolve, (time_to_wait - Number(tqyc)) * 1000));
        await this.post_qg()
    }

    async main() {
        try {
            if (await this.login()) {
                if (await this.get_id()) {
                    await this.start();
                } else {
                }
            } else {
            }
        } catch (error) {
        }
    }
}

(async () => {
    const promises = cks.map(async (ck) => {
        const qg = new QG(ck);
        await qg.main();
    });
    await Promise.all(promises);
})();


