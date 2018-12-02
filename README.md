# wechat_robot

wechat_robot

>一个简单的聊天回复的脚本,
>
@author: Roger @2017年04月30日20:38:05

### 功能:
1. 启动后,会根据你的配置,进行群聊和私聊的自动回复.

### 说明:
- python 2.7 坏境
- 依赖的python库
    - `requests`
    - `itchat`
    - `json`
    - `datetime`
    - `ConfigParser`
- 图灵api, [接口文档](https://www.kancloud.cn/turing/www-tuling123-com/718227)

```
http://www.tuling123.com/openapi/api
```

### 参数解释:

```
[options]
;图灵API的key
key=xxxxxxxxxxxxxxxxxxxxxx

;群聊配置, 用`;;`分隔
[group]
allow=true
white_list=group1;;group2
black_list=

;私聊配置, 用`;;`分隔
[single]
allow=true
white_list=name1;;name2;;name3
black_list=
```
