
################ mysql ##################
import pymysql

### 连接数据库
db = pymysql.connect(host='localhost',
                     user='user',
                     password='passwd',
                     database='databases',
                     port=3306,
                     charset='utf-8')

### 获取游标 （cursor）
cursor = db.cursor()

cursor.close()


db.close()



################ redis ##################
