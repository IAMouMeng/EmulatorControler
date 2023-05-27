# MonitorController
Web Api 操作mumu模拟器 开机|关机|重启|重置

# 主机操作

## GET 获取列表

GET /server/list

## GET 获取使用率

GET /server/rate

# 模拟器操作

## POST 获取信息

POST /emulator/info

> Body 请求参数

```json
{
  "name": "MuMuPlayer-12.0-1"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» name|body|string| 是 | 模拟器名称|none|

## POST 云机控制

POST /emulator/operate/{action}

> Body 请求参数

```json
{
  "name": "MuMuPlayer-12.0-1"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|action|path|string| 是 ||['start','stop','reset']|
|body|body|object| 否 ||none|
|» name|body|string| 是 | 云机名称|none|

