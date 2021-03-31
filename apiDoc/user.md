### 行业模块

说明：
除了 “1、用户登录”，“2、验证是否已登录”， “3、创建用户” 外，其他接口调用时需要在header中添加x-CSRFToken，其值等于登录接口返回的csrftoken，否则报错“CSRF Failed: CSRF token missing or incorrect.”，具体见https://segmentfault.com/a/1190000016493704

#### 1、用户登录

- 简要描述：行业列表接口，默认按创建升序排列

- 请求URl：http://[DOMAIN]/user/login/

- 请求方式：*POST*

- 请求示例
```json
{
    "userName": "user1",
    "pwd": "123"
}
```

- 参数列表

| 参数名   | 必传 | 类型 | 说明                  |
| -------- | ---- | ---- | --------------------- |
| userName | 是   | str  | 用户名                |
| pwd      | 是   | str  | 密码                  |

- 返回示例
```json
{
  "data": {
    "username": "yewh",
    "groupId": 2,
    "group": "auditor",
    "resourcePermission": [
      {
        "id": 1,
        "name": "industry",
        "alias": "行业"
      },
      ...
    ],
    "actionPermission": [
      {
        "id": 19,
        "resourceId": 3,
        "resourceAlias": "指标",
        "actionId": 1,
        "actionAlias": "编辑"
      },
      ...
    ]
  },
  "total": 27,
  "msg": ""
}
```
- 返回参数说明

| 参数名           | 类型 | 说明              |
| ---------------- | ---- | ----------------- |
| username         | str  | 用户名            |
| groupId          | int  | 组id              |
| group            | str  | 组名              |
| resourcePermission | list  | 资源权限            |
| name             | str  | 资源名            |
| alias            | str  | 资源别称          |
| actionPermission  list  | 动作权限          |
| resourceId       | int  | 资源id            |
| resourceAlias    | str  | 资源别称          |
| actionId         | int  | 动作id            |
| actionAlias      | str  | 动作别称          |


- 响应状态码

| 状态码 | 说明             |
| ------ | ---------------- |
| 200    | 登录成功       |
| 400    | 传参错误         |
| 409    | 错误         |

#### 2、验证是否已登录

- 简要描述：一般只用于其他后端服务验证，前端不需要调用
- 请求URl：http://[DOMAIN]/user/login
- 请求方式：*GET*


- 返回示例
```json
{
  "data": [
    "login"
  ],
  "total": 1,
   "msg": ""
}
```

- 响应状态码

| 状态码 | 说明             |
| ------ | ---------------- |
| 200    | 已登录       |
| 400    | 传参错误         |
| 409    | 错误或未登录         |

#### 3、创建用户

- 简要描述：修改行业
- 请求URl：http://[DOMAIN]/user/
- 请求方式：*POST*
- 请求示例
```json
{
  "userName": "user",
  "email": "xxxx",
  "pwd": "123"
}
```
- 请求参数说明

| 参数名     |必传 | 类型 | 说明     |
| ---------- | --- | ---- | -------- |
| userName   | 是  |str   | 用户名   |
| email      | 是  |str   | 邮箱     |
| pwd        | 是  |str   | 密码     |

- 返回示例
```json
{
  "data": [
    "success"
  ],
  "total": 1,
   "msg": ""
}
```

- 响应状态码

| 状态码 | 说明             |
| ------ | ---------------- |
| 201    | 创建成功       |
| 400    | 传参错误         |
| 409    | 错误         |


#### 4、修改密码

- 简要描述：场馆按距离升序排列

- 请求URl：http://[DOMAIN]/user/pwd

- 请求方式：*PUT*

- 请求示例
```json
{
  "oldPwd": "123",
  "newPwd": "1234"
}
```

- 请求参数说明

  | 参数名    | 必传 | 类型 | 说明                     |
  | --------- | ---- | ---- | ------------------------ |
  | oldPwd    | 是   | str  | 旧密码                   |
  | newPwd    | 是   | str  | 新密码                   |
  
- 返回示例
```json
{
  "data": [
    "success"
  ],
  "total": 1,
   "msg": ""
}
```

- 响应状态码

| 状态码 | 说明             |
| ------ | ---------------- |
| 202    | 操作成功       |
| 400    | 传参错误         |
| 409    | 操作失败         |


#### 5、登出

- 简要描述：场馆按距离升序排列

- 请求URl：http://[DOMAIN]/user/logout

- 请求方式：*POST*


  
- 返回示例
```json
{
  "data": [
    "logout"
  ],
  "total": 1,
   "msg": ""
}
```

- 响应状态码

| 状态码 | 说明             |
| ------ | ---------------- |
| 200    | 登出成功       |
| 400    | 传参错误         |
| 409    | 操作失败         |

#### 6、获取用户名

- 简要描述：通过session获取用户名
- 请求URl：http://[DOMAIN]/user/username
- 请求方式：*GET*


- 返回示例
```json
{
  "data": {
    "username": "username"
  },
  "total": 1,
   "msg": ""
}