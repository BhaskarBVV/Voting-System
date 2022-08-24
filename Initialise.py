import mysql.connector
import bcrypt

class Initialise:
    def set_tables():
        conn=mysql.connector.connect(host='localhost', user='root', passwd='1234', database='project2')
        my_cursor=conn.cursor()

        
        sql='delete from user where Id!=-1;'
        my_cursor.execute(sql)
        conn.commit()

        sql='delete from Role where UserId!=-1;'
        my_cursor.execute(sql)
        conn.commit()

        sql='delete from Approval where UserId!=-1;'
        my_cursor.execute(sql)
        conn.commit()

        sql='delete from VoteRecord where UserId!=-1;'
        my_cursor.execute(sql)
        conn.commit()

        sql='delete from Party where PartyID!=-1;'
        my_cursor.execute(sql)
        conn.commit()


        admin_pass="".join(str(bcrypt.hashpw("1234".encode('utf-8'), bcrypt.gensalt()).decode()))
        sql=f'insert into user values(1,"Admin","father",432893,22,1234567890,"abc@gmail.com","XYZ", "{admin_pass}");'
        my_cursor.execute(sql)
        conn.commit()




        
        