在线词典

两级页面，
可以实现用户的注册与登录存储至数据库加密
可以实现对单词的查询和查看历史记录等功能

由server端和client组成
采用mysql为存储仓库
dict数据库下有三个表：

words（id,word,mean）
user(id,name,passwd)
hist(id,name,word,time)

words 为文件 dict.txt 存入：exc.py

1.确定好技术方案（套接字，并发，细节确定）
	
	* tcp套接字
	* process多进程
	* 历史记录：前10条
	* 注册成功  直接登录

2.数据表进行建立（dict:wrods）
	
	* 用户  user —> id name passwd
 
		create table user(id int primary key auto_increment,name varchar(32) not null,
		passwd varchar(128) not null);

		
	* 历史记录 hist —> id name word time

		create table hist(id int primary key auto_increment,name varchar(32) not null,
		word varchar(28) not null,time datetime default now());

3.结构设计：几个模块 封装设计
	
	客户端
	
	服务端：逻辑请求处理，数据库操作处理

	函数封装：直接写一个功能程序提供给使用者使用。使用者直接允许，而不是需要使用我的代码的某一部分。

4.功能分析 和 通信搭建

	* 网络搭建
	* 注册
	* 登录
	* 查单词
	* 历史记录

5.罗列功能逻辑（每个功能确定服务端和客户端该做什么，编写代码测试）
	注册	客户端：  输入注册信息
		               发送请求给服务器
		               得到服务器反馈

		 服务端：  接受请求
			判断是否允许注册
			允许注册将信息存入数据库
			给客户端反馈结果

	登录	客户端：  输入用户名密码
		               发送请求给服务器
		               得到服务器反馈

		 服务端：  接受请求
			判断是否允许登录
			发送结果

	查单词	 客户端：  输入单词
			发送请求
			等待接受结果

		 服务端：  接受请求
			查找单词
			发送结果
			插入历史记录
	
	历史记录     客户端：

6.设定客户端服务端请求协议
	
	注册	R
	
	登录	L

	查单词	Q	

	历史记录	H

	退出	E

			
cookie:

   import getpass

   getpass.getpass()
   功能:　隐藏输入内容
   参数:  提示行

进行密码加密

In [3]: import hashlib

In [4]: passwd = 'abc123'

生成加密对象
hash = hashlib.md5()

hash = hashlib.md5(b"#-the,L")　＃ 加盐处理


进行密码加密
In [6]: hash.update(passwd.encode())

获取加密后的内容
In [7]: hash.hexdigest()
