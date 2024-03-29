/**
 * cron 10 10 * * *
 * Show:得物 心愿森林  &  得物 心愿海洋 入口都在 APP下方=>我=> 下方=>
 * 更新上上签版本
 * 变量名:dewuCookies
 * 变量值:抓app.dewu.com   请求头Headers中的x-auth-token  去掉Bearer  # 连接SK # 连接cookie中dutoken得值 可以直接搜dutoken
 * 例如ejxxxxx...#90xxxx...#d41d8cd9|16...2233|17...|4sasasasa...
 * 一共三个值 不要看错了 分别是x-auth-token得值 # SK得值 # dutoken得值
 * 多账号& 或换行 或新建同名变量
 * scriptVersionNow = "0.0.6";
 * new Env("得物")
 * 把UA换成自己的UA  把UA换成自己的UA   把UA换成自己的UA   否则会触发风控
 * 依赖 crypto-js & jsencrypt 版本最新即可
 * UA变量名 dewuUA  必须填自己的 否则会风控 请求头Headers中的User-Agent 必填
 * 助力码变量名 dewuHelpCode 分享链接中的几个表情 例如 😻💥💬😻🌹🌼😿
 * 这里我只推荐在青龙配置文件里面写UA变量
 * export dewuUA=""
 * export dewuHelpCode=""
 * 下面是变量名 不是变量 别再瞎改了
 */
//UA变量名   UA注意看是下面的格式的UA 不是很短的那个
let UAName = "dewuUA";
//助力码变量名
let helpCodeName = "dewuHelpCode"
//cookie变量名
let ckName = "dewuCookies";
//UA默认值
let UAdefult = "Mozilla/5.0 (Linux; Android 11; MI 8 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36/duapp/5.39.1(android;10)";
//助力码默认值
let helpCodeDefult = "";
