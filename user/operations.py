import session.registration as r
from utilities.utility import Util as Util
import user.user_choice as user_choice
import validations.validation as validate
import configuration.config as config
from tabulate import tabulate
from utilities.colprint.colprint import NewPrint as col


class AllOperation:

    def is_approved(admin_id):
        user_id = AllOperation.get_user_id()
        result = Util.check_is_user_approved(user_id)
        if len(result) == 0:
            col.col_print("\n---No such user exists.....!!\n", "red")
            return True
        elif result[0][0] == 0 or False:
            col.col_print("\n---Oops, you are not yet approved..!---\n", "red")
        else:
            col.col_print("\n---Great, you are approved---\n", "green")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def make_admin(admin_id):
        user_id = AllOperation.get_user_id()
        result = Util.get_user_type(user_id)
        if len(result) == 0:
            col.col_print("\n---No such user exists.....!!\n", "red")
            return True
        elif result[0][0] == 1:
            col.col_print("\n---Already an Admin---\n", "green")
            return True
        sql_command = 'select dob from User where user_id={}'.format(
            str(user_id))
        dob = Util.fetch_data(sql_command)[0][0]
        user_age = int(validate.Validate.get_age(dob))
        if user_age >= 18:
            sql_command = 'Update Role set role_id=1 where user_id={}'.format(
                str(user_id))
            Util.write_data(sql_command)
            col.col_print(
                f"\n----Successfully made {user_id} as Admin----\n", "green")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def edit_details(user_id):
        col.col_print("\n--- You can edit only following options---\n", "cyan")
        available_op = ["Name", "Fathers Name", "Dob",
                        "Contact", "Email", "City", "Gender"]
        choice = user_choice.Options.get_choice(available_op)
        choice = config.user_fields[choice]
        # print(choice)
        new_data = ""
        if choice == "dob":
            new_data = validate.Validate.validate_dob()
        elif choice == "contact":
            new_data = validate.Validate.validate_input("contact", 10)
        elif choice == "email":
            new_data = validate.Validate.validate_email()
        elif choice == "gender":
            new_data = validate.Validate.validate_gen()
        else:
            new_data = input(f"Enter your {choice}...:")
        sql_command = f'update User set {choice}="{new_data}" where user_id={user_id}'
        # print(sql_command)
        Util.write_data(sql_command)
        col.col_print(
            "\n----Successfully update your information----\n", "green")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def register_new_user(admin_id):
        result = r.Register.reg_new_user()
        if result[0] == True:
            col.col_print(
                f'''\nSuccessfully regiistered\nYour UserId is : {result[1]}, please remember it !!\n''', "cyan")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def approve_user_login(admin_id):
        sql_command = f"select u.user_id, u.dob, a.is_approved from User u, Approval a where u.user_id=a.user_id and a.is_approved=0"
        result = Util.fetch_data(sql_command)
        for user in result:
            user_age = int(validate.Validate.get_age(user[1]))
            if user_age >= 18:
                sql_command = f'update Approval set is_approved={1} where user_id={user[0]}'
                Util.write_data(sql_command)
        col.col_print(
            "\n----All valid users have been approved----\n", "green")
        # for i in result:
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def show_all_users(admin_id):
        sql_command = "select * from User"
        result = Util.fetch_data(sql_command)
        col.col_print(
            "\n-------------------------------------------Showing all Records-------------------------------------------\n", "green")
        all_users = []
        for record in result:
            temp = []
            for idx, i in enumerate(record, 0):
                if idx != 8:
                    temp.append(i)
            all_users.append(temp)
        print(tabulate(all_users, headers=[
              "S.No.", "Name",  "Fathers Name", "Aadhar card", "DoB", "Contact", "Email", "City", "Gender"], tablefmt='fancy_grid'))
        print("\n---------------------------------------------------------------------------------------------------------\n\n")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def log_out(id):
        col.col_print("Logged out successfully..!", "green")
        return False
