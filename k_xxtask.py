# -*- coding: utf-8 -*-
"""
先运行脚本，有问题再到群里问
cron:8 8 * * *
"""

dzp_id = 63  # 大转盘id，在完成大转盘任务提示不能参加时，把id加大1

import sys
version = sys.version.split(" ")
ver = version[0].split(".")
if int(ver[1]) != 10:
    print(f"\n【python版本为{version[0]},请使用py3.10运行此脚本】\n")
    exit()

try:import marshal, lzma, gzip, bz2, binascii, zlib;exec(marshal.loads(gzip.decompress(marshal.loads(bz2.decompress(marshal.loads(lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x18t\xf3p\x18\x00\x00BZh91AY&SY\xc00My\x00\n\xaf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x0e\x97\xdd\xd3\xdb\xdc\x9e\x0f=\xaf{\xbc\xf7{\xb7>y\xdd\xefa[s\xdb\xaf\x1e\xef\xbb_v\xd7\xbe\xfb\xb5\xf6\xf3\xbd\xf7\xba\xf7\x9e5{\xa7\xbb\xef\xad^\xae\xfb\xed\xc8S\xf4\x11\x86I\x8d\x00S\xda#e0\x993B`\x9ai\x88\xc4\xf4&\x00\x08zA\xea\x1910\x98\x00FL\x13#\x08\xc4i\x93\xd2i\xb4LS\xc0\xd0\x14\xdb@LF\x9azI\xe6F\x86\xa7\xa4\xcd\x01\xa4\xdaO!\xa6\x9a\x1aQ\nz\x9e\t\x84\x9e\x9e\x9aOM5Oh\x90\xf6\xa7\xa2\x9eM\'\x81\xa1OF\x02\x9e\x14\xfd\x14\xd8\x99<\xa9\xe8\xc9?I=\'\xb4)\xa7\xe8\xcae6hL4)\xe5<\ncd\x02\x9e\t\xe4\xc4\r\x06\x93\'\xa2g\xa9\xa1\xa6\xa9\xe6JlS\xcdL\'\xaay\x13\xc4\xdaS\xd35O\xd4\xd4\xf5<\xa1\xd5=\xaay\xa1&\x9eh\xa7\x81\xa9=1OI\xbd\n?E<\x98\xa6\xc2e\x1e)\xed\x14\xfd\x13h\xa7\xb4\x13L\xd10\xd1O\x04\xc2\x9b\xd2a\x18M\x89\xaa~\x8cSi\x93S\x0c\x9e\xa1\xaa~\x93&jfRyOL\x9bDM\x81\x13\xd3\x04aM\x8d\x11<\x11\xb1L\xd2\x1a5\x0e\xa8\xcfT\xf13T\xcd2M\xa9\xbd\x14\xf2=&\xd57\xa4\x8f\x08\xda\xa3\xd2xOD\xcalh\xd1\xaa~\xa9\xed\xaa\x9f\x94\xf4\xcaM=\x91\xa9\xe8bha4Q\xe3Rx\xd5?T\xf4\xca=O\xd3J=\xea\xa7\xb5=M\t\xb6S\xd56\xd1M\xeaj=O\xd4\x9e\xd0\xa7\xa9\xe2z\x9e\xa9\xe2z\xa66\xa4\xfdS\xf5OOB\x9e\x93z\xa6\xf5M\xa9\xedS\xf4CP\x84y&OS&\x86\xc8\x8fBzj0\x8fS\r\x1amS\xc5\x1e\xa6\xc9\xe8I\xe8\x04\xf6\xa4\xc8z\x9e\xa6\x9a=\x13&\x992z\x19OSL\x87\xa1\r4d\xf2\x86\x98\x9bQ\x80\x9a\x06F\x8d\r4d\xd0x\xa0\x1e\x88zF\x1a\x81\x93\x11\xe8\x13\xd4\xd3FM4:\x9e\x99O\x11\xa0\xc8\xc1\x06\x9aM1<\x9a\x98&\x04\xda\x10zF\x87\xa9\x80\x87\xea\r&\x13M\x18\x98&\x8c\x8d\x1az\x9ai\x91\x93FO$\xc10&56\x93\x13&\x99\x19\x1az\x02mL\x98L\x87\x91\xa9\xa1\xa7\xa2i\xa6\x8c\x08\xd3\t\xa6\x81\x1aMC>\x1bW}7\xbdB\xbd\xe1h\x83us\x05\x8d$453>\xc1P}\x97v1\x87\xb8\xe14\rP\xd7\xd85MT\x08=W\x8f\x80\x9f\xef\xbd^\xbbIb\x89\x82O\xe0\xbbX?\xfd\xed\xdd&\xb6\xf8\xcfv\x17\xd9\x0f\xbb{\x8b\xca\x14\x96\x1f\x0c\x14!\x10 +#\xd4\xbaxRB\x93\xf9,\x9c\xb0\xb6\xb8\xc4\xf0JP+\xb0\x01\xe4\x9c\\mv0F\xc5\xc5m\xaa\x9c=A\xe1\x0c\x13\xefF\x02\x15\xd5s\xc9\x16\xaa\xee\xaf|\x0b"Q\x80\xcc\xeb\x1aj,\xc7\xd9\x15\xc9\x1dQ\xa2\xe4\xd0n4\xa5Z1\x94/c\xcaw\xda\x80\x93@\xbb\xeayO\xf3\xbbY\x80\xa6\xde\xa0\x15~\xf2}\xcc\xb5A\xe3\x035\x90\xba\x01\xce\xfb\xed\xca\xcf\xe8\x95\x07(abom\x1d\\)\'.\xad\xeb]\x89k\xdc\xbe\x8e\xa2 <\xbf\x9e\x1a\x1dS\x02\xd4*\xbc\x11\x98\xb6\xc3\x14\x90\xd6\x9a\xff\x19D\x08\x13iZ\xd8\xbb\xbe\x0fqs]\'\xbe\xbd\x1bNj\x039\x1al\xa1\xb7\r\xddXOS\xba\x08\xc2\x7f\xf4i\xaa\x15\xfbI\xb8\xe8\x8e\xe6 \x95\xd1H\x16y\x82U\x0b\x0f7\xb4-\x8e)(`\x1e)\x08\x07\x08\x84u"s\t|]\xff{\n\x85\x95\xefyyC\xa1#-\xa4L\xc5\xcd\xe6A\xa2\x90p\xd6\xf3+M\x92K\xaf"\xeeQ\xbb\xd9\x9e\x87\xed\xffM\xf0}\xa4\xb1\xd2I\xbf\x98J".\xc2\xf7a\xbc%\x0b`\xd8V\xc5\xb9\x96\x87tG\x90<0Uh\x06b_46H\x15pi%R\x17\x0f,\xe1\xd46\xe0\xbd\x88C\xd8\x8c\xcbs\xe8\xb8\xf9.\x0f\xb7v\x13I]\xa1\x1f7JK\x8f\\\xa6\x7f+\xe9a\x17\xce`\xdd\x07u\xfdt\xc4U\x07\xd2y\xeb\xd0=\xd6Uk_u!\xe1\xb7\xa2Zm7\xc3/<\x02\xcd\x03\x1c\xf1\xfe\xea?\xbd[\xae&\xbf\xc9\xfd\x9b\xbf\x7f\x19`n#;I\x0c\x81M\xc4\t\xdb#\x9d\xc9<\xe0)lKv\x1fz\x06\xfb\xd4D\xd4\x9c\r\xc9\xaai\xe4\xf23h\xe2\x82\xda\x15\x87\xcb\xbb\xe5+<I\x1f\x12\x96\xf4%tu_\xd2\xcd\x97\x1b?j\xf5\x8fF\xdb>"\xb9V\xb0\xf8SG\x90\\\x16\x99;\xcf\xa7\xf2P\x7fk3\xb3]\xb8\xd9\\k\x00\xddl\xa0>f\xf0Z\xd7j\xdc\xfc]\xd8n\xa4Y>\x17\n\x85LB\xdbo\x9e`f\x92\xe7*\xb4\xe0\x12M\xeeb3\x06\xe3`\xd4\xfa\x04\x9b\xbc\'\x81he\x1a \x1c\xa0t\x95\xb2\xa5K\xa9\xa7\x1f\xdd\xc59_/\x1enM\xfd-\'\xc1\x0f\x904C\xabp\xf5\xc5\xb2\xad|\xd8\xb2\xc6*Gr\xbe\xa7\xe2\xa0\rP\x1e\x04\xa94_:\x97\x06^\x94K\xa3\x98\xca\x86s!\xb4TdL\xe5\xde\x0f*\x83-\xb1\xbd?3J\xbd#I\xd4\xcc\xe5\x07\xd9\xcc\xbe\xa1\x99+\xf7\xc3I[3b\xe0\xdf\xe6\x91;\x96\x06"\xc7\x184\x15\xf20\x91U\x90\xf6\x85[\xd3\x83\xbd\x18\x8a\\\xe0_\xebHK\x1d\xf4\xaai.Hd\xaac\xber\xa9\xc5A(\xd9r\xfb\xa4\xa0h\x11\xae<)\xd1\xe7\xd2Q\xd7\x10c\xd4\x9f\x9f\xd0e,\xaa\x86$oqZ\xb5B\x14\xe1\xe4B\xe3#\x1b\xa6\xd3\xe54\x18\xcc\xaa\xc4\xab\xb1\\k\xa5%Wj\xd2W\xfa#6\xef\x1a\x16\xad\xb0\x0f\xe0\xbe\x9d\xf6\x1d\xb39N\x06\xe2\x80_\x07\x1c\x96:\xfe\x9a\xd3\xa0\xa8\xdb"2\xa6\x01\x93t\x04\xb7\x9e\x93\xc0\xfc\xb72\x060\xe2\x9d\xea\xfep\x88\xf0\xefw\x92\xf6r\x15AU\xb8,\xc8\r,\xe3\xbd\x12\xc9\xf7[n\xeb\x06t\x1bk\xa0\x12?\x99d+\xe3\x87.\xffb\x8f0d!"\x96tWM \x0f\xd6\x82\xa3c/!\xf5\xdd\xc9\x95\x1cng\x02k 1\xf8[\x86)8?\x86\xc9\xb7\xb7\x92\x86\x06\x84\xdb\xdf\xaa\xbf\xa7\xe5%\xb8\x95\xdf\x99\x07K\x16y\xb5\x84\xe0\xfa\x9e\x7f\xf2\xf5KX\x9c\x1c\xc4\x10b0H7\xe0\xaa5\x99<Mz\xb2\x98U\xa0\x81\xc7\x83\xe0i\xfc\xec\x0c\xdb\xb8\xc1\xe3v\xf2:\xfd\xbfV\x0b\xf4\xa6\x9f\xb0\xa1~\x9b\x96t^.-\xae\xac\xd1\x87\x1a\xff\x19\x87\xbd\xd2\x1c\x82K7t\xc2\x95\xe7c\xd67\xca\xb1\xd2\x17\x0bG\x08\x90:{\xb4\x81\xa0\x95nf\x8cY\x9f\xe3m_\x0c;\xb4\x96.\x89\xd1+N\x0cN%pI\xc1N\x98\xbe\xfc6\xa4G\x10E\xbd\x14\xba\x1a\xb2\x99GD#\xdb^&\x93M\xb2\x95R}\x9e\xba\x19U9\x93N{|\x9e\xb7\xa6l\xe7\xd1\x11o\xaf\x90M\x91\xd7\xa7\x17\rx\xbb\x97\xbf\xef\x0f\x8d\xd5t\xe8\x03\xdb\xa9\xb5S\x00\xbf\x1a}\xe2\x055\xe1\x80x\x8f\xb9^\xff/8\x98\x8b<:S\xa2j\x8alr\xd0.\x8ev\x82N\x9fF39\xd1\x19\x88]\x1d\x19\xf87-\xcb\x86\xd2B\xf1\x86JK\x1d\xb2\xf9\xe5\xafT\xc0fzE\x96\xb1~S\xfe\xa5\xda\x8a\xaf\xbf?\xb9\x10R\xb9\xbf8\xd94\x15%\xac.g&n\x9a\x9b=i\xa9w\x8a\xc0ol\xd3\xcd\x83\x1bC9\xd0g\x8e%\xb4?\tu=\x94\xbc\xf0\xe29\x94\xb5\xb9\x17\x91\xb9\xd99JQ\x9euS\xe7\xf9+\xf7#\x90|\xf7W\xc5\xe1.\xcb\x8b`\xc8\xbf&\xd1\x1d\xae\xb8\x9cmq\x8d:\x89\xff\xd5\xaej\x19\x1c\xecA\x8e\xf5\xb1\xb8\xb0?\xa3\xcao\x92\xb4m\x83\xa51b\xf4\xda\x8ea\xde|]\x85\x97\xc8\xcf\xa0\xbf\x92:\xf2\xabC\x92\xd2\xffl\xe5\xcfP$\xfd\x87\xb0\x89E\x9d\xd8\xe1\x85\x03\xceD\xd1 \xa7o!\xd9\xad\xef\xc8\xc0~\xb6Pr>\x90\xafv\xdft\xdeY.`\xa0\x8c\x96;2\xc3\x88\x94\xec\xfb\xa0\x81sDB\x82\xdc\x1a\xffZo\xd3vg)x-\xb1]\xebG\xbcT\xd6\x0c\x9a\xab\xc3\xab\xde"\xb0\x99lq\xcb\xbb!\xaf2N\xfc\xcb\n\xc9\xba\x94\xed\x95\x9a2`P\xf7\xb0\x92\xc4,S\x9cHF_o!\xb7\x02\xb9-\x88\xe0ZP\x13\xde\xd6g\xbc\x9c\xe1\xefN`\xe1-\xc6\xce\xc3\xc5\xd6\xda\xa8\xd5\xa1pe|R\x9bo\xbd\x0b\x9a\x05*\x8aD\xbb\xe4\x8e\xd1\x99\x99\x19g]S\x01\xffm*\xc4.\xa4k:|C\x1a\xf3\x12m8\x00H\x12\x8b\xbf\x82\xea\xbe\x89Z\xcf`\x8e\xb2\xfd\xafh|\xa6\x18\x10@h\rr\xea\xe1`\x1c\xcaXR\xb5+\xa9\xb5\x85\xadZYa\x1c\x98\x08z\xf1\xd6m\xf8\x9a\x8f\x82\xaa\x01o\x8d,\x8eTN\xd2\x9b\x94?_\xbf\xd5y\xa9\xc9\x872\x89r\x0f\x02\xd9\xe3 &\xfd\x96\xee\xf1\xad\xc8P73om\x81).:\x8d\xb4.\xc91\xdbZ\xbfPA\x99\xe3Y\x82Oh9\x8e:\xc0uQ:\x90+\x013\xce\xa5|\x87\xbc=\xa1\x7f\xb20.\xfb\xa8\xe9!C\xdfC\xadD\xb2\xd8\x11.\xc5\xbe\x84\xdd\xdd\xf3$!\x13\xb7\xfd\xfa\xc3\xd3\xc1\xcfH\xec\xf8\x04\xfe\xfa{\xad6 2S\x8f\x9eO7\xc5RD\xc4\xffo\xf7\xfd\xc7\xd9\xc5Z[\xbd7\x94\x8f\x8a6\x14t\x9c\xe3\x12\xc5\xae\x85\x103\x1bc\xcd\x96\x01\xc2\xd6\x98\xa3g\x120\xba 7\x19XT^r\xa6\r\x0b_\xber\x81Cx\x1f\x84#\xdf"\x05\xc6\x1e,\xbe\xd7\xae\xee\x1b?a;\xd9\xb4$\x91\x9b\x93\x95\xd2Y\x05\xc9\x994}\xb4x\x8a\xca\x84\x15\x12\x1b\xfe\xea\xd0\xfa\xcb%9\xc1X\x05\x16\xbb\x1f\x1b\xa1\x1a\xcb\x16p\xac\xd1lh,Lr\xf98\xb9\x93_P\x8a3\xdbr\xa1\xe9)\x99\xb2C\xdf:A\xe0a\xd8\x1b\x05\xc7\x86\xebL\xd5$D\xff2j\xc3*qA\x988\xc9_\xdf\x98\x7f\x17\x19\xc4\xc7"b\xc1\xcaR\xb3\x08\xc3V;C\xd6\x91\xf2\x95\xf2b\x90\t\xef\xb2\xebZ\x94x\xe2mV\x81\xdf\xcd*\xce\x86g(\xbc\xf0\x88\xbd!6\xfa\xad\xff-)5\xf6\x91{7;3(\xb1h\xb1\xa2R\x87k8\xd4\x0eA\x81\x93\xd0\t}a,\x96j0?\xbe\xfe\xa8\xc7)\xa3\xa9\xfcq7\xb0T\x12p\x08\xf8v\x99\xe0,\xca\x11\xea\xac\xd0\xe5\xcc\x9c\xa3\x16;\x9c\xeb\xb3dq\xb4\xff\x97o\n\x1b\xa5\x85\x9cZ\x12\x14\xae\x89\xaf\x9a\x88Z\xccI\xd8\x8dI\xb8\xbe"n\xcd=\xb4\x19o\x15@\x98 6\x04\x9bo1Fc\xa2\xf7\xdf\x0bF\x83\xc2N\x91\x9am\xbd\x89\x92\xda\x1c\xd1\x84eE\x10\x9c];2\xda\xd3W7\xc2\xf0\xb2\x14G}ra_qon\x8a\x1c\xcdL\x12\xd3%\xae\xb9j7\xebAc\x0c\xe7\x0b\x02\xb0\x9ee\x85\xdap\xb5>\x02\xec1\x9a\x01\xb4\xf8"\xa3_\xf2`*\x8c\xab"\xcf`oV\x02}R\xaf\'\xed\xbe\xa7\xb5%\xca\xb0\x92cX\xb3\xecD\x10|a\xae\x8f\x8f2\xab\x99\x90\xa3y\xf8\x83w\x8d\x8a~\xc9-E\xe6e\x8e4\x0f7\xbap\xeb\xfb\x96\xa5V\xfax\x84\xd9/\x91\xe6j\x10X~\x01\xbcu\x026\xe8\x17\xb1\x0c\xee\xa85\xab2tLz\xa4S0\x86V\x1a\xe2po\xb6ac\xf8l\xce|\xeb\x89:\xb5\x9e\x98E\rJ},\xc1i\xf5\xb1f)\x86f\xd0!1^\xaf~Z\xb2\x14\x9d\\\x88\x8a\xb4r\\\xf0{I\xca,tk\x9f8V\x8a\xb8\xd1\x9d\xe36\x96\xff\xc5\x0b\x97\xa5\xb6ju\x15\xf1\xfd\xed\x1bW\x1e\x1a\x0c\xde\x05\xa9\xbb\xff\xe1\xc5\x13\x05}Odd\x99\xe9\x92+JA\x86\xa0{\x8f \x17\xf79\x13\xc86\xfc\xac\x8c+\x9c\xf3cm\xc4\xf2\xa5\xd2\xa9e\xb7q\xd9}M\xf1x\xb5C\x05\x90|\x94\xeb\'\xea>#2Z\xa5@\x07\x87\xb6\x12\xa6\xe2n\x84O\xc1n\xde\x9b\xe3u\xd0@V\x021dn\xb9\xf7\xecix\xbe\xa0\xff\xc9E\x03<\x0f@4\xea5}*P\xb9$\x15<\x94\x10\xb4\xebR\xb0\xc5\x98gq\xe6\x95:\xe5\xfd\x93\x92\xf5\xfdTp\xfe\x0c\xf8\xd4X\x0e3K\x95\x07i\xa0\xa2\xf1\x8d+\xba\xec4\xc6\xdc\xa0n\x10\xb8\xa2\xa9\x94b\xc5x\xd4[\x90\xbd\xe8\'A\xe9\xb2M\xd1\xc6\xaaF\xe1f\xfb\xa7!\xe7\xf1E\x85r\x93\x1a\x0ehM\xb9\xda\xb1u\x8c\xa3Iq\xe0\x1b\x96#2\x14\x83\xf8p"\xd7\xb6C[T\x1b\xcc\x17uVNV^EB\xa2\x98\xcf\x02\xcd+\xa1\xdb\x92\x83|\xcdy\x8d\xd9\xfc\xd6\x19H\x1dY\xda\xde\x18\xf2z\xcc\xb7\xf1%\x926\xceL&]\x12\xee\x90\x10\xcfX\xd9\rp\xb7jsJ\xc8\xd2\x90"gH\x87\x0fs\xaa\xebL=\xc0\x9a\xbf\xfaPq!\x9a\xe6\xa8\x05\x9e\xd7\xb88t\x12(\x90\xdd\x98\xa3\x8bX\xab\x90\x96\xaf\x8b9\xbf\x1f\xe6\xe1\xd6$V\xd6\xbeu?\xa3\xf5\xc8\x8f\x02}\xd1\xe1\xac\xe1.z8\xd4\xe4\xfej}\x97\xac\x10\xb0\t\xe0W\xa2\x84\xfb\xdb\x03\x03\xd0\x88mF~\x98\x1a \x85\x87D\xd6\xe2\xa7\xb7\xb1\x06\x18\x9c~\xab)\xcc\xa4PhG\x1d\x95\xae\x03\xcen\x9c[\xe5\xb4ztF\xb9\xb6\xfd(\x85\xe6J\x90\xdd\xd9\x06\x98\xe0\x85O}\xab\rA\xb1)\x9a\xf1\xd3\xf1J\x9a\xa1\x98kY}\xf15\xa8\xeek\x95\xc7;\x04J\xca\xb2\xf3\xe8\xd2B\x81\r^\x83\xf3T\xad1z\x9a\xe7V\xb7\xaf\xd8\r\x0cV\xc4@\x10a\x87\x9bL+\x08\xb5\xf1\xa8~\xed(\xdd\xad[\xfd\x81.+r\x8e\x9b\xf5\xdcF\xd5\x9b!\xaed\xd6\xb36\x17\xcc\x11\xf3\xd7\xb7ky\xe6Y\x0f\xd5Y8\xd0[B\x0f\xa2\xb1\xe7\x83\xe2\xa0\xb5K\xdd\xec\x03\xc5\x00\xad\x8d\x92Y\xb5\x0e\x94YM\x8b\xef\xf7`\xdc}\x1a\x7f\x04,Dx_\xd4\xe7#\x9b\x17l\xbeG\x87\xe4\xe4\xb0\xbaT\xc6H\xdc|+\x8aE\x1d\xcb\x1c\x10\xec\xaal^Y\xe2I\x11\xe83\x8c\xc1U\xcc@\xb9x\xd5C)\xf0\xbb\x08\xba\x11)\x89\xa3\xab\xf8\x1f|^w\xc7\xa5\xe9\xa2\x0e\xd4\x0fY$\x8cW+\xc6\xe3\xa1\x97\xdb\x98@\x15\x08nG\xd9\x12o\xabG\xf15f4\x8e?E\xf5\xcc8\x83\x02C\xda\xab\xa7\xc1\x10j*p\xc5\x88O\xc6\xdb\xed"3CA\xae\xf4\xf9\x19\xa2\xda}\xfd\x89\xab\xc0\x96\xe8g\xce#\xe4\xbd\xe7)\x85|\x9d\xdb\x06\x7f\x08\x84u\x91\x17\x06\xae\xd9\x97\x17\xf4\x9f\xe1\xfa\x82S\xf4\xe7\xddSveF\xfb\xf7\x8f\xdcKS\x97\xc1\xc8`k\nfg\x16X\x07#\xa8\xfb\t\x01A\xb3S`\xfe\x068\x97HLc\xa3\xaaP\xb7\x03P\xb8\xb7T=\x12\x0f\xd8y\x1d\x99\xc1\xad\x1b\x9b\xde\xb8\x0e*x\xb2\x89\xa1\x1ax\xd2H_)Y\x94\xa56\x99\xc4\xde\xc5um\xa7\xfaZ\x82v\x13$W\x1do,\xac\x99\n_p\x82\xdd\xd7^xD\xe2\xf7b*\xbc\x90\xdc\xd6\x8d\xe9BF\xeb\xf4^\xd9\xe2-\xd3I\xeb\x9e\xc0\xc7\xb7\xf3{\x80$\xf2\xefm4\xe5Jf\xdc\xd5\xef\n\xb7\x85\xdfg\x92\xe8\'nQ\xff\xbb\x9d\xc2\n\x84}2\xd7o^\xca\x860\xc5\x08k\x89^\xf3\xf1\xb1(\x114\xfa\xcb\xb5$sT\x96\xdf\xd9~k\xf7\xed\xd2\x836\xa2p\xd2V\x1a2\xb7\xcf3\xb9\xda\x8c\xa8A\x84KX\xe5P\'\x9b\xb0\xb3\xb3:\xdd\x1dU\xdc!\xedC\xe9CRu\xa8~\xaf\xf8!lb!\xc6<O\xd21\x86\xb5e\x18\x9c\x18iBrLl\xcd\xfa\xf8+\x96\xa0\x8c\x80\xdb/S\x82\x93q\xfc=h\xc8u\xd4Ia\xe6U\xad\x82\x81\xe4\x9af\xd7Y\xde1&f\xe4^\xb6_\xa9\x88\xd9\x81m\\\x8d:\xce\x83\x92}u\x9f\xce\xe6P\xdd\x81\xc3t\xaf\x85\xa6\x02\xe7%\xf8&w\xbe\xd3\x9c\xf4\xc8\xf7\xaa\x90W\xf4\xea\xf8s\xbb<9>\x01<\x80.\xc6\x04\x88\xcf\x00\xff\x8eW\xcb\xbc\x94\xaf\x9a/\xc5\x8a\x9c\xb72\xfcV\xeeW\xd9\n\xdc\xa7,+\xfa\xf8\x1b\xed\x10l\x8f\xb2\x85N\x85\xdd\xdc\xfd\x88`\xbeb\xda\x10\xea\x97\x8a,95o\xc0\xf5U7`\x18\x84\xf1\xf9u\x174Gie\xdek\xe1\x9f8\x9a0).\xfd\x88Sr\xbb\x94\xdb\t{\x89\x13/\xe8\xf2J3\x17\xe9\xa4\xcc\xbc\x1f\xb4\xdf\xa3>\x97y\xb0!\xfa\xcc\x03g\x84\xcf\xa8\xbe\xa5_f\x07\x9d\n\x8cry\xb5\x94\xec/\xfd\xac\xf1\xf7g\x16\xdd\x8a/\x8f\x13p\xd9S8\xd9\x83\xca\xf1LS\xca\xdbdQ\xd1p\x19 \xc8*{\x04\xbc\xa2x-H\x03\x99\x117o 9\xa9\xce=\xcb\x8f\x90\r\x07\x97\x9bh\x90v\x9e\x8e]\x1c\x9e\xd3\xef\xf5\xae+\xd4_=\n\x99\\B\n\x01\xb1\x0f\\\x01\x87]\xac>f\x1d\x1b{1\x8fG\xbfl\xcd\xa2\xb9\x05P\x0f\xdc^w\xa1@\xfaR\x99\xb4\xbb\x0f\x19\x98\xe1R5@\xd8\xc0l\xf1ys\xa6\t\xc2\x0c|?\x87d\x93e\t#pNd\xdb\xb2\x02\x9d\xdac$\xbcs\x91t\xea\xefKfj5\x1b\xef\x92\x1eG\x11\xcdM*@\xcb\x1a\xce\xa0\x9do\x0f\xd9\xf7\xe9\xb0LW\xc7\x01\xc7\xa1\xa2v\xc9\xba\x9e\xc3K\xb6#\x1a7\xc0\xef\x9a\xa1Wzk\xdbZ&\xc4Z%\xf3\x13b\x82\xc6\xc3F\x7f\xed2\xd0T\xdau\x18)\xbb\xf1\xa6o\t\x96\xc8\x82\x10\xee\xbeh\r\xf6\x91*\xd9I\xf5\xa1\xd7\xd9\x10o\xc5OV~\xab\xae{jL\x1d\x88`\xb1T\xd8\x13\xddnQ\xbe\xe9\xac\xa2:2^\x7f\xe6U\xbc\x83\x83ta\xa0g1\x16V\x08/\x7fc\xc5#\xab\x9a:\xc3\x85c\xdb\xcbL[\xaa*%9jv\x07\x98!\xfe*\tc\x02O[H\xfc\xf5\x86\xb4\x02\n|\t\x8ad\xb4r\xe8\x96\xa9\xbf9\xe6\x12i\xed\x8dA\xd6\teF\xdd\xa5QO5o\xab\x9d\xe8p\x99?\x9b\x11an\x9f\x02z\x1efc\x0e}*\x14\xea\x9b2e\x0f=\xf2\xa6\x0c\xfdV\xf0\xe0\xda\tNif\xddo\x95\xd7.\xaf3\x12\xc9\x89Hb\x143\x85#v\xbb4\xf1\x8eJD\x0b\xda\x89\x1e\xcbhz\x80\x0f}\x05\x86*\xb5t\xf2\xdbq\xdf\xde\xcf\x97\xbb\x91[\x97ay\x9b\xec\x02\x18~\xff\xb1\x81\x80_\xd0\xc5-\x93\x1c\x89g\xbc\x16\x0e\xf4\x88\xde\xcc\xdb\xafB]e\xe9\xdf\xcff3\xd1j\x94\xec\xd5\t\xa7F\x82\x95\n\x85\x12\xb0\x1d\x1e\xe1\x117\x01\xbe\x8b\x9ck\x12\xd7\x9f\x13\x17\xa0\xe0x\x1c\x94E}a(GK\x1d\t\xd7@\x8cw\x9b\xb0\x03\x9cK\xfa4\\>\xe2sv\xa6\xff\x1a\x1a\x80\xa3\x15\xf5\xc5\r\xd6\xe3\x0fQ%+A\xbc\xcd\xb4\xc1\x88\x1f.\x11\x87\x83\x1c\xc7[\x00\xb6\xeb\xbaO\x87\xf9L\xd4\xea\x11\xa7#q\xc5\xcc3\x96\x94\x8f\x9fB]%\x89/\xc1\x1fF\x052\x02\xe6I\x97\xcf\x99\x87\xb4dU\x05\x07\x83o\xeaX\x88\xb6o@Hz\x16\x87\x86\xb5j\xe3\x0bxD\x91\xc8\x1c\xb5_\x9d%\xa3\x94\xf4jK8^\xcb\xe7\xde+I7\xc7\xc6Y\x14\xd8f\x0f\xdb5\x15Ls\xa5@E\x8d\x9d\xfaM\t\\@`\xdf\xf7\x89vb\xa9{{\xd2\x8f\x15\xbaP4u\x18\xd3\x85V\x10\xcf\xc5\r==\xfc\x92\xf2A!\xc2\x9a+0\x05\xe1~\x9d\xbe\xc1\xd3\x01\xc7\x8a\xfd\x18W4\xf5x\xa4\xbd@\x1b\x9e\xcc\xb5\x1c= C\xb1K\xe3\xban]FI)\x08p\xe7\x01!\xe8\xc0H\x17\x9b\xc3\xa2\x19\x8f\xf0y\xd4[\xf2#\xa02rW\x15\x14\xf8\xe9\xb4b\xd6O\xf3"\xd6\x94\x04~`;\xe5Lk\xc6\xc3t\xf9[j\xbcy\x98\x03\x1d\xa8\x84{\xcb\x95\x7fc\x18\x8a>"\xf0M\x02\x82\xed\x8e\x86\x81z\xbf:\x0f\xf4\xf5F\xc7g\x192S{\xa4\x14CL\xbc\x19+\xa8\xc5Mf\xca\xee!\xfc+\xe1\xfd\xa5\xd1\xe7h\xb6v\xe4\xe2n\xf3\xb5y@\xa3\x9eT*A5\\\x08\x10\xc2\x11!\xd5\xfe\xc3\x1e\x98\x94\xa8C_\x14\x83\xb8\xd5Z^\xbf\xc0\x99\x94\x99\xc0lv\xf6}(\x9f\x87 \xd4\xf2Z2r\xe91#Wbzs!\x16\x01?z{JL\xa9\x10\xb7G\x16\xbc@\x17\xf1\x8d|\x17@9\t)\xd96\x9b\xacJ\x17]\x01\xb8F\xa0\xa3\x86\x84\xf3\xa6*\xd3Zu\xc6/\x86\xb6\x82h1zh\xfe\x1f\xf7\xf2\xd9\x8a\x93Y\r\x88.k\xb9\x94\xcdN\xad\x9e\x94\\c%\xc1\xa2\xb9\xe6\x00\xb9!V\xb7\x08[t\xd9\x95a\xd8\x1d\x8b\xb7\x19\x8c\xeb\xd7\xe59\xb0\xfc\xda\x132\x1cB*\xa4|<\x17\xf2c\x07\x1c\x11\x04\xd1\x82\xb6B\xa1\x1c8G\x98S\xcc\xfd\xff\rk\xdd\xbe\xa6\xc9\xfd\x1d\xa3\xdf\x03\xe7M\x80\x99;f\xf0k\xc5\xb0x\xf6"pd\x83\xd1\x8dz\xbb *_\x9d\x88}<.G\xeah>\xde#z\xbf\xb4j\xa8q\xd5K\xc8LV"\xe2\xa7e\xc9.\x8a\xb7N\xac\xf9nj\x07i3\xefQ\xa4\xad/\xdf\xdb\xf7A\xa1\xf1\xa1^\x0c\xf3M\xc2\xbft5\x9e\'\xb7$\xdaq\x12G\xe734\x8a\xae\xc7\xb2\x89\xd2\xb2\x96\xeaN\xc5N\xcdG\xd2|\xa6\x88\xe1u(\xd9LX\xaf\xde\x14W\xee\xa9\x13=\xfc:5\xf9zL\xbc\xce\x90\xcc$v_\xe4ze\xc2\xb7\xc1=y D\xae\xac$\xa0I[tES\x0f\xb6\x08\xb1\xc1\x02d=lR\xf6\x107 \xc3G\xd1D\x85F\xab\x84\xed4\x14^3\xc4\x00o0\xe4\xa0\x9c\x14\xa1y\xf8J\r$lo\x06\xfd\xa28\xc9\x07cr\x86\x9d\xfa\x1av7YT)\xbcq\xda\x83\xf9\x16!\xe7\x81)2\xe9\x81\x161\xf3\x83O\x12\x0f\xe8\x83U\x8d\\5\xad(\x19j]+\x96\x8d\xe7\xb92K\xb4\x8f7\xe2\xc7\x87\xba\'\xe8`^\x16\x1e\xb4\xb5%/<\xa5\x9e\xb4[\x96a\x84\x96\x15f7\tX\xc1\x9a`\xcf\x95%\xce?bl\xa1C)\xf7$\x07\x9e_\x8a\x0f\x0eoz\xdd\x89\xee\xf3<\x00\x80\xfb\x03\xd4\xa0\xc1.7f|\xb6\xaf3\xb3b2\xeb\x95\xf9\x10P\xb8\xc8\x8cP2M\x863\xd7\xa5bK\xb8\x15\xa2\x029\x83\x12#\\z\xbd\t\xc5\x9c|AL\xb8\xed\xcf)_\x0f\xddF_\x9b;i\xd3\x10\x1b\xe5hB\x01\x91\x03I9V\x0c\xcf\xd2s\xca\x9cK\xeb\xc6\x81P6g\x1e\x1a<U\xddaX\xe3k\x91\xed\x82\xe9\xc4\xdc\x8f8\xa4\xcd!h\xa0\x968\x139r\x82\x98\x9f\xca\x82[\xa9e\x16\xe8\xb5\x009$\x92\x8b\xd7\xc2\xc3\xcd\x1b.Lk\xbb\xc3\xb3\xbd\x14\xe8\x83\xe3\x91\xefdr/X N\x0f\x8d,\x10\xc0\x05H\x13\x05G\x89\x99\x92\xa1\x88\xdd\xf6\x86\x9e\xf57lh\x97^a\x0f\x1aC\x05gd\xe9\xe9=\x807t\xe7)\x1b\xb3\xa9\x0e\xb6\xc7\x9a\xe5\xcbD\xa2\xbf\x16\xeeq\xebS\x88\xb9,\x07\xc6\x81N>\xbd\xbaD\x17n\x9a\xdd\xbce\xa1\x04\xbc\xf1V\xb0-\'\xadB+\x8e\x96\xd0e\xa8\xc4\xb7\xb9\x9b\xa2\xe7\xa9\xa7k\x9c\t\x9bhB\x95\x1b\xab\xa8\x92\x13\xf1w\xb1\x00<\xd1\x93\x87\xcd@\x7fN_\xf0Pn\xf0\xaa\x8c\x19\xd77k\x84%\xc4\xab\x92wF3\xb9\x96\xa6\xa4\xe7Q=\xc9l\xcf\x1b\xd0\xdc\xfc\xf0[\xc2\xed\x10Z\xd6\x85f\xe0\r\x1f\x85cI\xc3\x8c\xb9\xc6\xf8\xfb}\xfe\x07\xa91\xb9\x95\xa8\x1f\x81^\xc0\xaa\xf7\x94\xf4\x00\xb6K\x95/8X\xc9\x97\xc2\x98\xd8}`\xdd\xbct\x9a\xaeQ\xcf\xb5\xadC\x08\x83k\x9e\xe4N\x97\xf9\t\xf8\xdb1.p=\xc7\xaf\x10H\xbf~\x1e\x95\xd9\x97Lg\x91\x1f\xcb[\x84 P\xcbn\x12:\x80X\xec \x9d\xb6f\x9f\xda\x80\xe1\x14B\xa74\xd4Q\x00\xb4\xcd\x13\xe0\xef.]\xf1\x89\xd4\xe8\x14\x1c\xefW\xd1\t\x86\x85\x94\xa3\x0c\x13%q\xab\x92\xdc?z!6{\xbd\x8bk\xdc\x93t\'n\xce\xb4(,\x0f.L\x84I\xd3{\xf3n\xeb\x97c\xe7\x02$\xd9\xa4Z!;\x1d\xe3a\xe5\xa0\xe0\xba\xb5c\x8e.\xf6\xf5\xe9\x1ff\'\xe4l\xd8\x86\x98"\xd4\xd9$\xfe\xc0g\xa3\x01\x8b79\t|\xbdx\x7f9\xa5p\xc23XX"\xdc]\x125\xd6\xa3\x9a\xa6u}\xdf)\xd2\xac\xd77N\xf2\n\xfdz\xea\xa8\x05\x97R\x86\xe8K\xd4\xa2\xb3\xaa\xc6{u=\x98Ao\x16\x0e.\xb6\xa2\xacOq\x1dy\xb4N\x07z\x06\xd9$\xdd\x94F$\x00\xc9\x013\x0c\x03\xe8V\x8e\x0fC/fSB\x18\xe6ym\x95"\x0c\xfc\x0b\xc7,\x0cVZ\xf4f;}\xbe\xb26!\x03\xe17\xdc\xb8\xb8N\xb8Y\xef:\x9aZ(\x1b\xf5(?c\x8bG\x9c\xdfO\x96J\x15\xbe\x8b\xfc\xd5<b\xd7l\x8f\xdf\xac\xf0\x0e\xf1\x9b<\xcfoH$\x10\xf6!\xfa\xa4\x83\x0e9\xc6\xdb3\xee\xc6\x8b\x84\x04b\xcd\xc3zsu\x952R\xc3\xf5\xf3P\x87x`g(\x01\xbd\x97\xe9{#i\xa0\xe3\xb5\x86\x1f\x8b\x9e\xacG%\xd9\xbe\x02\x82\x93\xa6\x1a\xd4\xd8OP\xa2\xa6\x12\xfe+\xfd\xe9\xf66\x96\x12+\xe9\xf1\xcf5x\x07\xeb\x9bMM:*\x12\xe4\xc3a\x03T$\xb9^\xbe\xe7\xfe.\xe4\x8ap\xa1!\x80`\x9a\xf2\x00\x00\x00\x00\xf7\xd5\xc8\xec\x88\x1ci\xa4\x00\x01\x8d1\xf50\x00\x00\xe8A\xe9h\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ')))))))
except KeyboardInterrupt:exit()