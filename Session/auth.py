import Session.registration as registration
import administrator.admin_choice as admin_choice
import bcrypt
import Regular_user.user_choice as user_choice
import maskpass
import Utilities.utility as utility

class Auth:

    def login():
        Id = input("Enter your Id : ")
        current_user_from_db = list(utility.util.find_id(Id))

        if len(current_user_from_db)==0:
            print("No such user fouund, try again...")
            return
        stored_pass=current_user_from_db[0][8]
        input_password=maskpass.advpass().encode('utf-8')
        tries = 2

        while not bcrypt.checkpw(input_password, stored_pass.encode('utf-8')):
            if tries == 0:
                print("Incorrect password, try again !")
                return False
            print(f'Invlaid password, {tries} tries left')
            tries -= 1
            input_password= maskpass.advpass().encode('utf-8')

        print(f"Hello {current_user_from_db[0][1]}")

        user_type=utility.util.get_user_type(Id)
        user_type=user_type[0][0]
        # print(user_type)
        match user_type:
            case 0:
                user_choice.UserOp.list_of_op()
            case 1:
                admin_choice.AdminOp.list_of_op()
    



    def sign_up():
        result=registration.Register.reg_new_user()
        if result[0]==True:
            print(f'''Successfully regiistered\n
            Your UserId is : {result[1]}, please remember it !!''')