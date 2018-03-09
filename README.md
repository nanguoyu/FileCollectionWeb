# FileCollectionWeb
upload file to qiniu form web.
免登陆在线web收集文件并上传至七牛

## 说明
```
这是一个轻量级文件收集程序，旨在提供免登陆文件收集服务
```

## 部署
```
web由Flask、UWSGI、Nginx实现，请自行查阅，等俺病好了再更新细节。
1.将上传至服务器
2.配置七牛信息
3.配置uwsgi
4.配置Nginx
5.开screen,启动程序

```
##示例
uwsgiconfig.ini：
```
[uwsgi]

# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:8010

# 指向网站目录
chdir = your web file directory

# python 启动程序文件
wsgi-file = manage.py 

# python 程序内用以启动的 application 变量名
callable = app 

# 处理器数
processes = 4

# 线程数
threads = 2

#状态检测地址
stats = 127.0.0.1:9200
```

yourdomina.conf:
```
server
    {
        listen 80;
        #listen [::]:80;
        server_name file.nanguoyu.us;
        index index.html index.htm  default.html default.htm ;
        root  /home/www/yourdomina;

        include other.conf;
        #error_page   404   /404.html;
        include enable-php.conf;

		location / {

			include        uwsgi_params;     

			uwsgi_pass     127.0.0.1:8010;
							
			uwsgi_param UWSGI_PYHOME /usr/bin/python;
			
			uwsgi_param UWSGI_CHDIR  /home/www/yourdomina;

			uwsgi_param UWSGI_SCRIPT manage:app;     

		}

        access_log  /home/www/yourdomina/file.yourdomina.log;
    }
```

七牛配置
```
        self._access_key = '七牛 Access Key'
        self._secret_key = '七牛 Secret Key'
        self._bucket_name = '七牛空间名称'
        domain = '七牛空间对应域名'
```

## 启动
```
Screen -S FileCollectionWeb

uwsgi uwsgiconfig.ini

```

##TODO
- [x] 文件上传
- [ ] 邮件通知
- [ ] 取件二维码


## 许可
The MIT License (MIT). 详情见 __License文件__