# wechat_robot

wechat_robot

>一个简单的聊天回复的脚本,
>
@author: Roger @2017年04月30日20:38:05

### 功能:
1. 启动后,会根据你的配置,进行群聊和私聊的自动回复.

### 用法:
- python 2.7 坏境
- 依赖的python库目前有 `requests`, `itchat`, `json`, `datetime` 这些库
- 图灵api, [接口文档](https://www.kancloud.cn/turing/www-tuling123-com/718227)

```
http://www.tuling123.com/openapi/api
```

### 参数解释:

- `GROUP_NAME_WHITE_LIST` : 群聊白名单
- `GROUP_NAME_BLACK_LIST` : 群聊黑名单
- `SINGLE_NAME_WHITE_LIST` : 私聊白名单
- `SINGLE_NAME_BLACK_LIST` : 私聊黑名单
- `ALLOW_GROUP` : 允许群聊
- `ALLOW_SINGLE` : 允许私聊
