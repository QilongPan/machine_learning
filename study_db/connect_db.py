# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="127.0.0.1",user="root",password="",database="my_data")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义要执行的SQL语句
sql = "select * from result limit 10;"
# 执行SQL语句
cursor.execute(sql)
#fetchone获取一条数据
many = cursor.fetchmany(3)
print(many)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
