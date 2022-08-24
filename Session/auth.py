import Session.registration as registration
import bcrypt
import maskpass
import Utilities.utility as utility
import configuration.config as cf
import user.user_choice

class Auth:

    def login():
        user_id = input("Enter your Id : ")
        current_user_from_db = list(utility.util.find_id(user_id))

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

        user_type=utility.util.get_user_type(user_id)
        user_type=user_type[0][0]
        print(user_type)
        # available_operations=cf.roles[user_type]
        # user_choice=user.user_choice.options.get_choice(available_operations)
        # cf.role_function_mapping[user_choice]
    



    def sign_up():
        result=registration.Register.reg_new_user()
        if result[0]==True:
            print(f'''Successfully regiistered\n
            Your UserId is : {result[1]}, please remember it !!''')