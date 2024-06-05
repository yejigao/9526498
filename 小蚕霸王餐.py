#   --------------------------------注释区--------------------------------
#   入口https://s21.ax1x.com/2024/05/22/pkMb0gA.png
#   变量:yuanshen_xcplus 多号： @分割
#   找https://gwh.xiaocantech.com/rpc接口
#   抓该接口请求头 x-vayne 和 x-teemo 和 x-sivir的值
#   格式： x-vayne#x-teemo#x-sivir
bug = False #是否卡平台bug刷取20次机会 True开启 False关闭
#   --------------------------------一般不动区-------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#佛曰:  
#        写字楼里写字间，写字间里程序员；  
#        程序人员写程序，又拿程序换酒钱。  
#        酒醒只在网上坐，酒醉还来网下眠；  
#        酒醉酒醒日复日，网上网下年复年。  
#        但愿老死电脑间，不愿鞠躬老板前；  
#        奔驰宝马贵者趣，公交自行程序员。  
#        别人笑我忒疯癫，我笑自己命太贱；  
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))