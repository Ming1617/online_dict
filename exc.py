"""
    存入数据库
"""
import re
import pymysql

#连接数据库
db=pymysql.connect(host="localhost",
                   port=3306,
                   user='root',
                   password='  ',#密码
                   database='dict',
                   charset='utf8')

# 获取游标（操作数据库，执行sql语句，承载直接执行结果）
cur=db.cursor()
f = open("dict.txt", encoding="utf-8")
# 写数据库
try:
    # 写sql语句执行
    # 插入操作
    sql = "insert into words (word,mean)  \
            values (%s,%s)"
    # 每次获取一行

    for line in f:
        # 获取单词和解释
        tup=re.findall(r'(\S+)\s(.*)',line)[0]

        # 可以使用列表直接给sql语句的values传值
        cur.execute(sql,[tup[0],tup[1]])#执行

        db.commit()  # 提交
except Exception as e:
    db.rollback()  # 退回到commit执行之前的数据库状态
    print(e)

# 关闭数据库
f.close()
cur.close()  # 关闭游标
db.close()  # 关闭数据库