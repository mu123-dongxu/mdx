'''
insert_word.py

'''

import pymysql

db=pymysql.connect(user='root',
                   passwd='123456',
                   database='stu',
                   charset='utf8')
#获取游标
cur=db.cursor()
#执行ｓｑｌ语句
f=open('dict.txt')
sql="insert into words(word,mean)\
 values (%s,%s);"
for line in f:
    tmp=line.split(' ',1)
    print(tmp)
    word=tmp[0]
    mean=tmp[1].strip()
    cur.execute(sql,[word,mean])
# try:


#修改操作
# sql="updata class_1 set score=91 \
# where name='xiaogang'"
cur.execute(sql)
#删除操作
# sql="updata class_1 set score=91 \
# where name='xiaogang'"
cur.execute(sql)
#执行完同步到数据库
db.commit()


cur.close()
db.close()