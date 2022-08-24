import mysql.connector

class util:

    def start_connection():
        connection=mysql.connector.connect(host='localhost', user='root', passwd='1234', database='project2')
        my_cursor=connection.cursor()
        return (connection, my_cursor)


    def fetch_data(sql_command):
        connection, my_cursor=util.start_connection()
        my_cursor.execute(sql_command)
        result=my_cursor.fetchall()
        connection.close()
        return result

    def write_data(sql_command):
        connection, my_cursor=util.start_connection()
        my_cursor.execute(sql_command)
        my_cursor.execute(sql_command)
        connection.commit()
        connection.close()

    def find_id(ID):
        sql_command='select * from user where UserId={}'.format(str(ID))
        return util.fetch_data(sql_command)
        
    def get_number_of_records():
        sql_command="select count(*) from user;"
        return util.fetch_data(sql_command)
    
    def add_new_record(user_record):
        sql_command=f'''insert into project2.User values({user_record[0]},"{user_record[1]}","{user_record[2]}",
                    {user_record[3]},{user_record[4]},{user_record[5]},"{user_record[6]}","{user_record[7]}","{user_record[8]}","{user_record[9]}");'''
        util.write_data(sql_command)
        sql_command=f'insert into project2.Role values({user_record[0]},{0});'
        util.write_data(sql_command)
        return True

    def get_user_type(id):
        sql_command=f'select RoleId from Role where UserId="{id}"'
        return util.fetch_data(sql_command)
        