# wechat_robot
wechat_robot

@author: Roger @2017年04月30日20:38:05

简介:
    一个简单的聊天回复的脚本,
    原本是从网上copy的,
    后来根据自己的需要有了很大的改动,
    其中, 图灵的key是来自网络,请不要用于商业用途
    其他解释权归本人所有,😂谢谢!!

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
