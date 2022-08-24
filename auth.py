import UserType
import bcrypt
import maskpass
import util
class Auth:
    def login():
        Id = input("Enter your Id : ")
        
        current_user = list(util.Utility.find_id(Id))
        Current_user_pass=current_user[0][8]
        if len(current_user)==0:
            print("No such user fouund, try again...")
            return
        
        # print("this is password",current_user[0][8], password is at the 8th index, 
        # and the Sql.fetchall()retuns list, so we are accessing a 2d list, with only one row)
        password=maskpass.advpass().encode('utf-8')
        tries = 2
        while not bcrypt.checkpw(password, Current_user_pass.encode('utf-8')):
            if tries == 0:
                print("Incorrect password, try again !")
                return False
            print(f'Invlaid password, {tries} tries left')
            tries -= 1
            password= maskpass.advpass().encode('utf-8')

        print(f"Hello {current_user[0][1]}")
        
        # user_type=UserType.Role.get_user_type(Id)
        # match user_type:
        #     case 1:
        #         pass
        #         # admin()
        #     case 2:
        #         pass
        #         # normaluser()
    

    def Sign_up():
        name=input("Enter the name.... : ")
        fathers_name=input("Enter your Father's name.... : ")
        Aadhar_number= int(input("Enter your Aadhaar Card number.... : "))
        age=int(input("Enter your Age.... : "))
        contact=int(input("Enter your Phone number.... : "))
        Email=input("Enter your Email.... : ")
        City=input("Enter your City.... : ")
        gender=input("Enter your Gender (M for male, F for female).... : ")
        password=maskpass.advpass().encode('utf-8')
        password=str(bcrypt.hashpw(password, bcrypt.gensalt()).decode())
        number_of_records=util.Utility.get_number_of_records()[0][0]
        number_of_records+=1
        # print(type(number_of_records))
        util.Utility.add_new_record([number_of_records, name, fathers_name, Aadhar_number, age, contact,Email, City,password,gender])