import session.registration as r
from utilities.utility import util as util
import user.user_choice as user_choice
import datetime
import validations.validation as validate
import configuration.config as config
from tabulate import tabulate
from  colprint.colprint import newprint as col

class AllOperation:

    # jab election start honge tab voteRecord table clear kri jayegi, to store votes for current new election
    # jab election end honge tab voteRecord se votes count hoke, result table main update kiye jayenege
    def check_on_going_elections(admin_id):
        sql_command = f'select status from Election_Year where year={datetime.date.today().year}'
        result = util.fetch_data(sql_command)
        if len(result) == 0:
            col.col_print(
                f"\n---Elections of {datetime.date.today().year} are not yet started---\n","red")
        elif result[0][0] == 1:
            col.col_print(
                f"\n---Yes Elections of {datetime.date.today().year} are going on---\n","green")
        else:
            col.col_print(
                f"\n---No Elections of {datetime.date.today().year} are over---\n","red")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def start_election(admin_id):
        cur_year = datetime.date.today().year
        sql_command = f'select status from Election_Year where year={datetime.date.today().year}'
        result = util.fetch_data(sql_command)
        if len(result) != 0:
            if result[0][0] == 2:
                col.col_print(f"\n---Elections of {cur_year} are over---\n","red")
                return True
            else:
                col.col_print(
                    f'\n---Elections of {cur_year} have already been started---\n',"red")
                return True

        sql_command = f'insert into Election_Year values({cur_year},{1})'
        util.write_data(sql_command)
        sql_command = f'delete from VoteRecord where user_id!=-1'
        util.write_data(sql_command)
        col.col_print(f"\n---Elections of {cur_year} have begun---\n","green")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------


    def close_elections(admin_id):
        cur_year = datetime.date.today().year
        sql_command = f'select status from Election_Year where year={datetime.date.today().year}'
        result = util.fetch_data(sql_command)
        if len(result) == 0:
            col.col_print(
                f'\n---Elections of {cur_year} have not been started yet---\n',"red")
        elif result[0][0] == 1:
            sql_command = f'Update Election_Year set status=2 where year={cur_year}'
            util.write_data(sql_command)
            AllOperation.fetch_and_store_results(cur_year)
            col.col_print(f'\n---Elections of {cur_year} have been closed---\n',"green")
        elif result[0][0] == 2:
            col.col_print(
                f'\n---Elections of {cur_year} have already been closed---\n',"red")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def fetch_and_store_results(year):
        sql_command = "select * from Party"
        all_parties = util.fetch_data(sql_command)
        # print(all_parties)
        winning_parties = []
        max_votes = 0
        for i in all_parties:
            cur_party = i[0]
            party_name = i[1]
            # print(cur_party)
            sql_command = f'select count(*) from VoteRecord where vote_id={cur_party}'
            no_of_votes = util.fetch_data(sql_command)[0][0]
            # print(no_of_votes)
            if no_of_votes == max_votes:
                winning_parties.append(party_name)
            elif no_of_votes > max_votes:
                winning_parties.clear()
                winning_parties.append(party_name)
                max_votes = no_of_votes
            sql_command = f'insert into Result values({cur_party},{year},{no_of_votes})'
            util.write_data(sql_command)
        col.col_print(
            f"\n---Here's the list of parties with maximum votes : {max_votes}---\n","green")
        for i in winning_parties:
            print(i, end="\n")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def add_party(admin_id):
        party_name = input("Enter the name of the Party : ")
        party_id = util.get_number_of_records("Party")[0][0]+1
        sql_command = f'insert into Party values({party_id},"{party_name}")'
        try:
            util.write_data(sql_command)
        except:
            col.col_print("\n---Party already exists---\n","red")
        else:
            col.col_print(
                f"\n---Successfully added the party '{party_name}'---\n","green")
        return True

    def get_user_id():
        user_id = input("Enter your Id : ")
        try:
            user_id = int(user_id)
        except:
            col.col_print("Invalid user Id","red")
            return AllOperation.get_user_id()
        else:
            return user_id

#-------------------------------------------------------------------------------------------------------------------------------------

    def is_approved(admin_id):
        user_id = AllOperation.get_user_id()
        result = util.check_is_user_approved(user_id)
        if len(result) == 0:
            col.col_print("\n---No such user exists.....!!\n","red")
            return True
        elif result[0][0] == 0 or False:
            col.col_print("\n---Oops, you are not yet approved..!---\n","red")
        else:
            col.col_print("\n---Great, you are approved---\n","green")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def make_admin(admin_id):
        user_id = AllOperation.get_user_id()
        result = util.get_user_type(user_id)
        if len(result) == 0:
            col.col_print("\n---No such user exists.....!!\n","red")
            return True
        elif result[0][0] == 1:
            col.col_print("\n---Already an Admin---\n","green")
            return True
        sql_command = 'select dob from User where user_id={}'.format(
            str(user_id))
        dob = util.fetch_data(sql_command)[0][0]
        user_age = int(validate.Validate.get_age(dob))
        if user_age >= 18:
            sql_command = 'Update Role set role_id=1 where user_id={}'.format(
                str(user_id))
            util.write_data(sql_command)
            col.col_print(f"\n----Successfully made {user_id} as Admin----\n","green")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def results(admin_id):
        # will show the result of past elections.
        year = input(
            "\nEnter the Election year whose result is to be displayed : ")
        try:
            year = int(year)
        except:
            col.col_print("\n---Opps, Invalid year, try again---\n","red")
            AllOperation.results(admin_id)
        else:
            sql_command = f"select P.party_name, R.votes from Result R, Party P where election_year={year} and P.party_id=R.party_id"
            result = util.fetch_data(sql_command)
            if len(result) == 0:
                col.col_print(f"\n---No record found for year {year}---\n","red")
                return True
            col.col_print("\n---Showing Party names and their votes---","green")
            for i in result:
                print(i[0], i[1])
            print("\n")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def edit_details(user_id):
        col.col_print("\n--- You can edit only following options---\n","cyan")
        available_op = ["Name", "Fathers Name", "Dob",
                        "Contact", "Email", "City", "Gender"]
        choice = user_choice.options.get_choice(available_op)
        choice=config.user_fields[choice]
        # print(choice)
        new_data = ""
        if choice == "dob":
            new_data = validate.Validate.validate_dob()
        elif choice == "contact":
            new_data = validate.Validate.validate_input("contact", 10)
        elif choice == "email":
            new_data = validate.Validate.validate_email()
        elif choice=="gender":
            new_data=validate.Validate.validate_gen()
        else:
            new_data = input(f"Enter your {choice}...:")
        sql_command = f'update User set {choice}="{new_data}" where user_id={user_id}'
        # print(sql_command)
        util.write_data(sql_command)
        col.col_print("\n----Successfully update your information----\n","green")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def give_vote(user_id):
        cur_year = datetime.date.today().year
        sql_command = f'select status from Election_Year where year={datetime.date.today().year}'
        result = util.fetch_data(sql_command)
        if len(result) == 0:
            col.col_print(
                f'\n---Elections of {cur_year} have not been started yet---\n',"red")
        elif result[0][0] == 1:
            sql_command = f'select * from VoteRecord where user_id={user_id}'
            has_voted = util.fetch_data(sql_command)
            if len(has_voted) != 0:
                col.col_print("\n---You have already voted !---\n","green")
                return True
            sql_command = "select * from Party"
            all_parties = util.fetch_data(sql_command)
            for i in all_parties:
                party_id = i[0]
                party_name = i[1]
                print(party_id, " ", party_name)
            voter_choice = input("Enter the party of your choice : ")
            while not (voter_choice.isdigit() and int(voter_choice) >= 1 and int(voter_choice) <= len(all_parties)):
                col.col_print("Invalid party Id, try again","red")
                voter_choice = input("Enter the party of your choice : ")
            sql_command = f'insert into VoteRecord values({user_id},{1},{voter_choice})'
            util.write_data(sql_command)
        elif result[0][0] == 2:
            col.col_print(
                f'\n---Elections of {cur_year} have already been closed---\n',"red")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def register_new_user(admin_id):
        result = r.Register.reg_new_user()
        if result[0] == True:
            col.col_print(f'''Successfully regiistered\n
            Your UserId is : {result[1]}, please remember it !!\n''',"green")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def approve_user_login(admin_id):
        sql_command = f"select u.user_id, u.dob, a.is_approved from User u, Approval a where u.user_id=a.user_id and a.is_approved=0"
        result = util.fetch_data(sql_command)
        for user in result:
            user_age = int(validate.Validate.get_age(user[1]))
            if user_age >= 18:
                sql_command = f'update Approval set is_approved={1} where user_id={user[0]}'
                util.write_data(sql_command)
        col.col_print("\n----All valid users have been approved----\n","green")
        # for i in result:
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def show_all_users(admin_id):
        sql_command = "select * from User"
        result = util.fetch_data(sql_command)
        col.col_print("\n--------------------------------------Showing all Records--------------------------------------","green")
        all_users=[]
        for record in result:
            temp=[]
            for idx,i in enumerate(record,0):
                if idx!=8:
                    temp.append(i)
            all_users.append(temp)
        print(tabulate(all_users, headers=["S.No.","Name",  "Fathers Name","Aadhar card","DoB","Contact","Email","City","Gender"]))
        print("\n-----------------------------------------------------------------------------------------------")
        return True

#-------------------------------------------------------------------------------------------------------------------------------------

    def log_out(id):
        col.col_print("Logged out successfully..!","green")
        return False
