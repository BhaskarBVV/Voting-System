import mysql.connector

class Util:

    def start_connection():
        connection=mysql.connector.connect(host='localhost', user='root', passwd='root', database='project2')
        my_cursor=connection.cursor()
        return (connection, my_cursor)


    def fetch_data(sql_command):
        connection, my_cursor=Util.start_connection()
        my_cursor.execute(sql_command)
        result=my_cursor.fetchall()
        connection.close()
        return result

    def write_data(sql_command):
        connection, my_cursor=Util.start_connection()
        my_cursor.execute(sql_command)
        connection.commit()
        connection.close()

    def find_id(id):
        sql_command='select * from User where user_id={}'.format(str(id))
        return Util.fetch_data(sql_command)
        
    def get_number_of_records(table_name):
        sql_command=f'select count(*) from {table_name};'
        return Util.fetch_data(sql_command)
    
    def add_new_record(user_record):
        sql_command=f'''insert into project2.User values({user_record[0]},"{user_record[1]}","{user_record[2]}",
                    {user_record[3]},"{user_record[4]}",{user_record[5]},"{user_record[6]}","{user_record[7]}","{user_record[8]}","{user_record[9]}");'''
        Util.write_data(sql_command)
        sql_command=f'insert into project2.Role values({user_record[0]},{0});'
        Util.write_data(sql_command)
        sql_command=f'insert into project2.Approval values({user_record[0]},{0});'
        Util.write_data(sql_command)
        return True

    def get_user_type(id):
        sql_command=f'select role_id from Role where user_id="{id}"'
        return Util.fetch_data(sql_command)
        
    def check_is_user_approved(id):
        sql_command=f'select is_approved from Approval where user_id={id}'
        return Util.fetch_data(sql_command)

    

    