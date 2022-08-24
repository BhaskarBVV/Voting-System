import mysql.connector

class Utility:
    def find_id(ID):
        connection=mysql.connector.connect(host='localhost', user='root', passwd='1234', database='project2')
        my_cursor=connection.cursor()
        sql_command='select * from user where UserId={}'.format(str(ID))
        print(sql_command)
        my_cursor.execute(sql_command)
        result=my_cursor.fetchall()
        return result
        
    def get_number_of_records():
        connection=mysql.connector.connect(host='localhost', user='root', passwd='1234', database='project2')
        my_cursor=connection.cursor()
        sql_command="select count(*) from user;"
        my_cursor.execute(sql_command)
        result=my_cursor.fetchall()
        return result
    
    def add_new_record(user_record):
        connection=mysql.connector.connect(host='localhost', user='root', passwd='1234', database='project2')
        my_cursor=connection.cursor()
        for i in user_record:
            print(type(i))
        sql_command=f'insert into project2.User values({user_record[0]},"{user_record[1]}","{user_record[2]}","{user_record[3]}","{user_record[4]}","{user_record[5]}","{user_record[6]}","{user_record[7]}","{user_record[8]}","{user_record[9]}");'
        my_cursor.execute(sql_command)
        connection.commit()

    
    # def read_command(sql_command):
    #     connection=mysql.connector.connect(host='localhost', user='root', passwd='1234', database='project2')
    #     my_cursor=connection.cursor()
    #     # sql_command='select * from user where Id={}'.format(str(ID))
    #     # print(sql_command)
    #     my_cursor.execute(sql_command)
    #     result=my_cursor.fetchall()
    #     return result