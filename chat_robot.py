# -*- encoding: utf-8 -*-
import requests
import itchat #这是一个用于微信回复的库
import json 

"""
  @autho: Roger @2017年04月30日20:38:05

  一个简单的聊天回复的脚本,
  原本是从网上copy的,
  后来根据自己的需要有了很大的改动,
  其中, 图灵的key是来自网络,请不要用于商业用途
  其他解释权归本人所有,谢谢!!

  功能:
    1.启动后,会根据你的配置,进行群聊和私聊的自动回复.
  
  用法:
    python 2.7 坏境
    依赖的python库目前有 requests, itchat, json 这些库

  常量的用途:
    GROUP_NAME_LIST : 允许自动回复的群的集合
    ALLOW_GROUP : 允许回复群聊,并会根据 GROUP_NAME_LIST 进行配置
    ALLOW_SINGLE : 允许回复私聊,目前只支持开关,回复指定人即将更新
    ...
"""

ALLOW_GROUP = True  # 允许群聊
ALLOW_SINGLE = True  # 允许私聊
GROUP_NAME_LIST = [
    u'大家五一快乐！',
    u'(1)(2)(3)(4)(5)(6)',
    u'伐木累',

    ]

# 这个key可以直接拿来用
# 网上直接down的,慎用
KEY = '8edce3ce905a4c1dbb965e6b35c3834d' 
 
# 向api发送请求
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
      'key'  : KEY,
      'info'  : msg,
      'userid' : 'pth-robot',
   }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
 
# 注册方法/群聊
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def tuling_reply_group(msg):
    if not ALLOW_GROUP:
        return 
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None

    # 群里的show name
    display_name = msg['User']['Self']['DisplayName']

    reply = get_response(msg['Text'].replace(u'@%s' % display_name, ''))
    # reply = get_response(msg['Text'])

    # 群名称
    group_name = msg['User']['NickName']

    print u'群聊_msg from@ %s : [%s]' % (group_name, msg['Text'])
    print u'群聊reply to@ %s : [%s]' % (group_name, reply)

    if group_name in GROUP_NAME_LIST:
        if msg['isAt']:
            # isAt 这个key是检测你在群聊中是否被别人@
            # 如果是,那么就会@那个人
            return u'@%s\u2005I : %s' % (msg['ActualNickName'], reply)
        else:
            return reply or defaultReply
    else:
        print u'私聊_msg from@ %s : [%s]' % (group_name, msg['Text'])

# 注册方法/私聊
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply_single(msg):
    if not ALLOW_SINGLE:
        return
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    print u'私聊msg from@ %s : [%s]' % (msg['User']['NickName'], msg['Text'])
    print u'私聊reply to@ %s : [%s]' % (msg['User']['NickName'], reply)
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    return reply or defaultReply
 
# 为了让修改程序不用多次扫码,使用热启动
# 在auto_login()里面提供一个True，即hotReload=True
# 即可保留登陆状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(hotReload=True)
itchat.run()
