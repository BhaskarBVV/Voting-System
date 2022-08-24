import mysql.connector

conn=mysql.connector.connect(host='localhost', user='root', passwd='1234', database='project2')
my_cursor=conn.cursor()
sql='select * from user'
my_cursor.execute(sql)
result=my_cursor.fetchall()
for i in result: 
    print(i)

print("Successfully executed")