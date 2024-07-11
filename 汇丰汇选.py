import math
import time

import execjs
import requests
import os

# 汇丰汇选 1.0
# 只有签到功能
# https://m.prod.app.hsbcfts.com.cn/wechat/pwcs/wechat/pinnacle/pinfmp/wechat/phoneAuth 这个链接下的refreshToken 一个月
# 环境变量 hfhx 获取 auth-Token 填入


print('汇丰汇选 1.0\n微信小程序: 汇丰汇选\n只有签到功能\nhttps://m.prod.app.hsbcfts.com.cn/wechat/pwcs/wechat/pinnacle/pinfmp/wechat/phoneAuth 这个链接下的refreshToken 一个月\n环境变量 hfhx 获取 auth-Token 填入')

ex_timeMills = math.floor(time.time()*1000)
hfhx_js="""
function n(n, r) {
    var t = (65535 & n) + (65535 & r);
    return (n >> 16) + (r >> 16) + (t >> 16) << 16 | 65535 & t
}
function r(r, t, e, u, o, c) {
    return n((f = n(n(t, r), n(u, c))) << (i = o) | f >>> 32 - i, e);
    var f, i
}
function t(n, t, e, u, o, c, f) {
    return r(t & e | ~t & u, n, t, o, c, f)
}
function e(n, t, e, u, o, c, f) {
    return r(t & u | e & ~u, n, t, o, c, f)
}
function u(n, t, e, u, o, c, f) {
    return r(t ^ e ^ u, n, t, o, c, f)
}
function o(n, t, e, u, o, c, f) {
    return r(e ^ (t | ~u), n, t, o, c, f)
}
function r(r, t, e, u, o, c) {
    return n((f = n(n(t, r), n(u, c))) << (i = o) | f >>> 32 - i, e);
    var f, i
}

function t(n, t, e, u, o, c, f) {
    return r(t & e | ~t & u, n, t, o, c, f)
}

function c(r, c) {
    r[c >> 5] |= 128 << c % 32,
    r[14 + (c + 64 >>> 9 << 4)] = c;
    var f, i, a, h, l, d = 1732584193, g = -271733879, v = -1732584194, s = 271733878;
    for (f = 0; f < r.length; f += 16)
        i = d,
        a = g,
        h = v,
        l = s,
        d = t(d, g, v, s, r[f], 7, -680876936),
        s = t(s, d, g, v, r[f + 1], 12, -389564586),
        v = t(v, s, d, g, r[f + 2], 17, 606105819),
        g = t(g, v, s, d, r[f + 3], 22, -1044525330),
        d = t(d, g, v, s, r[f + 4], 7, -176418897),
        s = t(s, d, g, v, r[f + 5], 12, 1200080426),
        v = t(v, s, d, g, r[f + 6], 17, -1473231341),
        g = t(g, v, s, d, r[f + 7], 22, -45705983),
        d = t(d, g, v, s, r[f + 8], 7, 1770035416),
        s = t(s, d, g, v, r[f + 9], 12, -1958414417),
        v = t(v, s, d, g, r[f + 10], 17, -42063),
        g = t(g, v, s, d, r[f + 11], 22, -1990404162),
        d = t(d, g, v, s, r[f + 12], 7, 1804603682),
        s = t(s, d, g, v, r[f + 13], 12, -40341101),
        v = t(v, s, d, g, r[f + 14], 17, -1502002290),
        d = e(d, g = t(g, v, s, d, r[f + 15], 22, 1236535329), v, s, r[f + 1], 5, -165796510),
        s = e(s, d, g, v, r[f + 6], 9, -1069501632),
        v = e(v, s, d, g, r[f + 11], 14, 643717713),
        g = e(g, v, s, d, r[f], 20, -373897302),
        d = e(d, g, v, s, r[f + 5], 5, -701558691),
        s = e(s, d, g, v, r[f + 10], 9, 38016083),
        v = e(v, s, d, g, r[f + 15], 14, -660478335),
        g = e(g, v, s, d, r[f + 4], 20, -405537848),
        d = e(d, g, v, s, r[f + 9], 5, 568446438),
        s = e(s, d, g, v, r[f + 14], 9, -1019803690),
        v = e(v, s, d, g, r[f + 3], 14, -187363961),
        g = e(g, v, s, d, r[f + 8], 20, 1163531501),
        d = e(d, g, v, s, r[f + 13], 5, -1444681467),
        s = e(s, d, g, v, r[f + 2], 9, -51403784),
        v = e(v, s, d, g, r[f + 7], 14, 1735328473),
        d = u(d, g = e(g, v, s, d, r[f + 12], 20, -1926607734), v, s, r[f + 5], 4, -378558),
        s = u(s, d, g, v, r[f + 8], 11, -2022574463),
        v = u(v, s, d, g, r[f + 11], 16, 1839030562),
        g = u(g, v, s, d, r[f + 14], 23, -35309556),
        d = u(d, g, v, s, r[f + 1], 4, -1530992060),
        s = u(s, d, g, v, r[f + 4], 11, 1272893353),
        v = u(v, s, d, g, r[f + 7], 16, -155497632),
        g = u(g, v, s, d, r[f + 10], 23, -1094730640),
        d = u(d, g, v, s, r[f + 13], 4, 681279174),
        s = u(s, d, g, v, r[f], 11, -358537222),
        v = u(v, s, d, g, r[f + 3], 16, -722521979),
        g = u(g, v, s, d, r[f + 6], 23, 76029189),
        d = u(d, g, v, s, r[f + 9], 4, -640364487),
        s = u(s, d, g, v, r[f + 12], 11, -421815835),
        v = u(v, s, d, g, r[f + 15], 16, 530742520),
        d = o(d, g = u(g, v, s, d, r[f + 2], 23, -995338651), v, s, r[f], 6, -198630844),
        s = o(s, d, g, v, r[f + 7], 10, 1126891415),
        v = o(v, s, d, g, r[f + 14], 15, -1416354905),
        g = o(g, v, s, d, r[f + 5], 21, -57434055),
        d = o(d, g, v, s, r[f + 12], 6, 1700485571),
        s = o(s, d, g, v, r[f + 3], 10, -1894986606),
        v = o(v, s, d, g, r[f + 10], 15, -1051523),
        g = o(g, v, s, d, r[f + 1], 21, -2054922799),
        d = o(d, g, v, s, r[f + 8], 6, 1873313359),
        s = o(s, d, g, v, r[f + 15], 10, -30611744),
        v = o(v, s, d, g, r[f + 6], 15, -1560198380),
        g = o(g, v, s, d, r[f + 13], 21, 1309151649),
        d = o(d, g, v, s, r[f + 4], 6, -145523070),
        s = o(s, d, g, v, r[f + 11], 10, -1120210379),
        v = o(v, s, d, g, r[f + 2], 15, 718787259),
        g = o(g, v, s, d, r[f + 9], 21, -343485551),
        d = n(d, i),
        g = n(g, a),
        v = n(v, h),
        s = n(s, l);
    return [d, g, v, s]
}
function i(n) {
    var r, t = [];
    for (t[(n.length >> 2) - 1] = void 0,
        r = 0; r < t.length; r += 1)
        t[r] = 0;
    for (r = 0; r < 8 * n.length; r += 8)
        t[r >> 5] |= (255 & n.charCodeAt(r / 8)) << r % 32;
    console.log(t);
    return t
}
function h(n) {
    return unescape(encodeURIComponent(n))
}
function f(n) {
    var r, t = "";
    for (r = 0; r < 32 * n.length; r += 8)
        t += String.fromCharCode(n[r >> 5] >>> r % 32 & 255);
    return t
}
function d(n, r) {
    return function(n, r) {
        var t, e, u = i(n), o = [], a = [];
        for (o[15] = a[15] = void 0,
        u.length > 16 && (u = c(u, 8 * n.length)),
        t = 0; t < 16; t += 1)
            o[t] = 909522486 ^ u[t],
            a[t] = 1549556828 ^ u[t];
        return e = c(o.concat(i(r)), 512 + 8 * r.length),
        f(c(a.concat(e), 640))
    }(h(n), h(r))
}


function a(n) {
    var r, t, e = "";
    for (t = 0; t < n.length; t += 1)
        r = n.charCodeAt(t),
            e += "0123456789abcdef".charAt(r >>> 4 & 15) + "0123456789abcdef".charAt(15 & r);
    return e
}

function get_token(sign1,sign2){
    var data = d(sign1,sign2)
    
    return a(data)
}
"""

def get_token(sign1,sign2):
    ctx = execjs.compile(hfhx_js)
    data = ctx.call('get_token', sign1,sign2)
    return data
token = get_token('wechat-sign','wechat-sign'+str(ex_timeMills))

def sign(au):
    headers = {
        'Host': 'm.prod.app.hsbcfts.com.cn',
        'xweb_xhr': '1',
        'XHSBCE2ETrustToken': token,
        'calltiming': str(ex_timeMills),
        'platform': 'pinf',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090926) XWEB/8555',
        'auth-Token': au,
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wxe13c5e6eb2f24313/66/page-frame.html',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    json_data = {}
    response = requests.post(
        'https://m.prod.app.hsbcfts.com.cn/wechat/pwcs/wechat/pinnacle/pinfmp/usertask/signIn',
        headers=headers,
        json=json_data,
    )
    print(response.text)

if __name__ == '__main__':
    Aus = os.environ["hfhx"].split("#")
    for i in Aus:
        sign(i)




