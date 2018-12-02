# -*- encoding: utf-8 -*-

import requests
import itchat #这是一个用于微信回复的库
import json
import datetime
import ConfigParser

now = lambda :datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
CONF_PATH = "./robot.conf"


def get_conf(option, path):
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    conf = dict(cf.items(option))

    def _split(key):
        DELIMETER = ';;'
        r = conf.get(key)
        if not r:
            return []
        else:
            return r.split(DELIMETER)

    return {
        'allow': str(conf.get('allow')).lower() == 'true',
        'white_list': _split('white_list'),
        'black_list': _split('black_list'),
    }

def get_api_key(path):
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    conf = dict(cf.items("options"))
    return conf['key']

# 向api发送请求
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
      'key'  : get_api_key(CONF_PATH), # 图灵api key自行申请
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
    conf = get_conf('group', CONF_PATH)
    if not conf['allow']:
        return 

    # 群名称
    group_name = msg['User']['NickName']
    txt = msg['Text']

    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + txt
    # 如果图灵Key出现问题，那么reply将会是None

    # 群里的show name
    display_name = msg['User']['Self']['DisplayName']

    reply = get_response(msg['Text'].replace(u'@%s' % display_name, ''))
    # reply = get_response(msg['Text'])

    if group_name in conf['white_list'] and group_name not in conf['black_list']:

        print u'%s GROUP_msg from@ %s: [%s]' % (now(), group_name, txt)
        print u'%s GROUP_reply to@ %s: [%s]' % (now(), group_name, reply)

        if msg['isAt']:
            # isAt 这个key是检测你在群聊中是否被别人@
            # 如果是,那么就会@那个人
            return u'@%s : %s' % (msg['ActualNickName'], reply)
        else:
            return reply or defaultReply
    else:
        print u'%s GROUP_msg from@ %s: [%s]' % (now(), group_name, txt)

# 注册方法/私聊
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply_single(msg):
    conf = get_conf('single', CONF_PATH)

    if not conf['allow']:
        return

    nickname = msg['User']['NickName']
    txt = msg['Text']

    if nickname in conf['white_list'] and nickname not in conf['black_list']:

        # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
        defaultReply = 'I received: ' + txt
        # 如果图灵Key出现问题，那么reply将会是None
        reply = get_response(msg['Text'])
        print u'%s SINGLE_msg from@ %s: [%s]' % (now(), nickname, txt)
        print u'%s SINGLE_reply to@ %s: [%s]' % (now(), nickname, reply)
        # a or b的意思是，如果a有内容，那么返回a，否则返回b
        return reply or defaultReply
    else:
        print '%s ignore msg from@ %s: [%s] ' % (now(), nickname, txt)
        return
 
# 为了让修改程序不用多次扫码,使用热启动
# 在auto_login()里面提供一个True，即hotReload=True
# 即可保留登陆状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(hotReload=0)
itchat.run()
