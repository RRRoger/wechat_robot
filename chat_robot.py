# -*- encoding: utf-8 -*-

import requests
import itchat #这是一个用于微信回复的库
import json
import datetime

now = lambda :datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

ALLOW_GROUP = True  # 允许群聊
ALLOW_SINGLE = True  # 允许私聊

# 收到群信息满足该群名称
# 在白名单且不在黑名单才可以自动回复

# 群聊白名单
GROUP_NAME_WHITE_LIST = [
    ]
# 群聊黑名单
GROUP_NAME_BLACK_LIST = [
    ]

SINGLE_NAME_WHITE_LIST = [
    u'山阳吕生君则',
]

SINGLE_NAME_BLACK_LIST = [
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

    if group_name in GROUP_NAME_WHITE_LIST and group_name not in GROUP_NAME_BLACK_LIST:

        print u'%s GROUP_msg from@ %s: [%s]' % (now(), group_name, msg['Text'])
        print u'%s GROUP_reply to@ %s: [%s]' % (now(), group_name, reply)

        if msg['isAt']:
            # isAt 这个key是检测你在群聊中是否被别人@
            # 如果是,那么就会@那个人
            return u'@%s : %s' % (msg['ActualNickName'], reply)
        else:
            return reply or defaultReply
    else:
        print u'%s GROUP_msg from@ %s: [%s]' % (now(), group_name, msg['Text'])

# 注册方法/私聊
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply_single(msg):
    if not ALLOW_SINGLE:
        return

    if msg['User']['NickName'] in SINGLE_NAME_WHITE_LIST and msg['User']['NickName'] not in SINGLE_NAME_BLACK_LIST:

        # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
        defaultReply = 'I received: ' + msg['Text']
        # 如果图灵Key出现问题，那么reply将会是None
        reply = get_response(msg['Text'])
        print u'%s SINGLE_msg from@ %s: [%s]' % (now(), msg['User']['NickName'], msg['Text'])
        print u'%s SINGLE_reply to@ %s: [%s]' % (now(), msg['User']['NickName'], reply)
        # a or b的意思是，如果a有内容，那么返回a，否则返回b
        return reply or defaultReply
    else:
        print '%s ignore msg from@ %s: [%s] ' % (now(), msg['User']['NickName'], msg['Text'])
        return
 
# 为了让修改程序不用多次扫码,使用热启动
# 在auto_login()里面提供一个True，即hotReload=True
# 即可保留登陆状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(hotReload=0)
itchat.run()
