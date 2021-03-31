### 服务依赖
1. 数据库配置：mysql或其他关系型数据库
2. 依赖包安装 pip install -r requirements.txt

#
### docker 部署

```dockerfile
docker run -dti \
--name {容器名} \
--restart always \
-p {宿主机服务端口}:8000 \
-v {宿主机项目路径}:/root \
-v {宿主机日志路径}:/root/logs \
nf_django22:1.1  # docker打包镜像
```


#
### 项目配置
1.在./user_backend_demo/settings.py中配置项目数据库及项目相关设定信息（settings_eg.py为项目配置模板文件）

#
### 项目运行
1. 使用docker exec -it {容器名称} bash 进入容器
2. 进入项目目录
3. 初始化数据库python-admin migrate（user 中的model可以不用迁移）
4. 启动django后端服务： python manage.py runserver 0.0.0.0:8000
