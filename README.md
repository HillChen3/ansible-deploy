# flask-ansible

#### 介绍
Flask实现Ansible和Ansible-Playbook的配置+部署系统，同时带有简单的服务器管理系统和认证系统。本项目需要把Python3安装到/usr/local/python目录下，ansible和ansible-playbook也是安装在此目录下。

#### 软件架构
本项目使用的Python为Python3.6版本，数据库使用Mysql，后端使用Flask，前端框架使用Bootstrap实现。本项目依赖的Python库极少，直接使用的pymysql操作Mysql数据库，项目安装方便。


#### 安装教程

1. 创建数据库。数据库的用户名密码可以自行更改，更改后需要修改项目中的config.yml配置文件

```
  create database devops;  
  grant all privileges on *.* to 'shijiange'@'127.0.0.1' identified by 'shijiangepwd';  
  flush privileges;
```

2. 导入数据

```
  set names utf8;
  source Flask-Ansible.sql;
```

3. Python3依赖安装
```  
  pip3 install -r requirements.txt
```
4. 运行Flask项目
```  
  python3 app.py
```

#### 使用说明

1. 认证系统：登录界面没优化，比较丑。默认用户名密码shijiange/shijiangepwd，可自行到user表添加或删除用户
![需要登录](https://images.gitee.com/uploads/images/2019/0710/111040_c8e2f6e3_129867.png "认证.png")
```
insert into user (username,password) values ('xxx', md5('xxxx'));
```
2. 服务器管理系统：支持Excel导入
![服务器管理系统](https://images.gitee.com/uploads/images/2019/0710/111256_364aa699_129867.png "服务器管理.png")

3. Ansible和Playbook配置系统+可视部署系统
![Ansible配置管理](https://images.gitee.com/uploads/images/2019/0710/111415_7c10e8ad_129867.png "Ansible配置管理.png")
![Ansible执行说明](https://images.gitee.com/uploads/images/2019/0710/111449_c7e23e77_129867.png "Ansible执行说明.png")
![Playbook配置管理](https://images.gitee.com/uploads/images/2019/0710/111629_00b26a56_129867.png "Playbook配置管理.png")
![Playbook执行说明](https://images.gitee.com/uploads/images/2019/0710/111704_67af05d0_129867.png "Playbook执行说明.png")

#### 如何实现的在线教程地址
  https://edu.51cto.com/sd/cb410

#### Django实现的Ansible的新项目: django-ansible
用Flask实现起来管理比较不方便，使用Django改善了下项目，链接地址：[https://gitee.com/shijiange/django-ansible](https://gitee.com/shijiange/django-ansible)
