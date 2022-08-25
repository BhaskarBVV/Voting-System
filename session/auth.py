import session.registration as registration
import bcrypt
import maskpass
from utilities.utility import util
import configuration.config as cf
from user.user_choice import options


class Auth:

    def login():
        user_id = input("Enter your Id : ")
        current_user_from_db = 0
        try:
            current_user_from_db = list(util.find_id(user_id))
        except:
            print("Invalid command, try again....")
            Auth.login()
        else:
            if len(current_user_from_db) == 0:
                print("No such user found, try again...")
                return
            stored_pass = current_user_from_db[0][8]
            if Auth.validate_pass(stored_pass) == False:
                return
            user_type = util.get_user_type(user_id)[0][0]
            if user_type != 1:
                if util.check_is_user_approved(user_id)[0][0] == 0 or False:
                    print("You are not yet approved, please wait until approval")
                    return
            print(f"\n---------Welcome {current_user_from_db[0][1]}---------\n")
            is_logged_in=True
            while is_logged_in:
                is_logged_in=Auth.display_options(user_type)
    
    def display_options(user_type):
        available_operations = cf.roles[user_type]
        user_choice = options.get_choice(available_operations)
        return cf.role_function_mapping[user_choice]()

    def validate_pass(stored_pass):
        input_password = maskpass.advpass().encode('utf-8')
        tries = 2

        while not bcrypt.checkpw(input_password, stored_pass.encode('utf-8')):
            if tries == 0:
                print("Incorrect password, try again !")
                return False
            print(f'Invlaid password, {tries} tries left')
            tries -= 1
            input_password = maskpass.advpass().encode('utf-8')
        else:
            return True

    def sign_up():
        result = registration.Register.reg_new_user()
        if result[0] == True:
            print(f'''Successfully regiistered\n
            Your UserId is : {result[1]}, please remember it !!''')
