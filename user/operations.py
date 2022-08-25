import re
from utilities.utility import util as util
import datetime


class AllOperation:

    # jab election start honge tab voteRecord table clear kri jayegi, to store votes for current new election
    # jab election end honge tab voteRecord se votes count hoke, result table main update kiye jayenege
    def check_on_going_elections():
        sql_command = f'select status from Election_Year where year={datetime.date.today().year}'
        result = util.fetch_data(sql_command)
        if len(result) == 0:
            print(
                f"\n---Elections of {datetime.date.today().year} are not yet started---\n")
        elif result[0][0] == 1:
            print(
                f"\n---Yes Elections of {datetime.date.today().year} are going on---\n")
        else:
            print(
                f"\n---No Elections of {datetime.date.today().year} are over---\n")
        return True

    def start_election():
        cur_year = datetime.date.today().year
        sql_command = f'select status from Election_Year where year={datetime.date.today().year}'
        result = util.fetch_data(sql_command)
        if len(result) != 0:
            print(
                f'\n---Elections of {cur_year} have already been started---\n')
            return True
        sql_command = f'insert into Election_Year values({cur_year},{1})'
        util.write_data(sql_command)
        sql_command = f'delete from VoteRecord where user_id!=-1'
        util.write_data(sql_command)
        print(f"\n---Elections of {cur_year} have begun---\n")
        return True

    def close_elections():
        cur_year = datetime.date.today().year
        sql_command = f'select status from Election_Year where year={datetime.date.today().year}'
        result = util.fetch_data(sql_command)
        if len(result) == 0:
            print(
                f'\n---Elections of {cur_year} have not been started yet---\n')
        elif result[0][0] == 1:
            sql_command = f'Update Election_Year set status=2 where year={cur_year}'
            util.write_data(sql_command)
            AllOperation.fetch_and_store_results(cur_year)
            print(f'\n---Elections of {cur_year} have been closed---\n')
        elif result[0][0] == 2:
            print(f'\n---Elections of {cur_year} have already been closed---\n')
        return True

    def fetch_and_store_results(year):
        sql_command = "select * from Party"
        all_parties = util.fetch_data(sql_command)
        # print(all_parties)
        winning_parties=[]
        max_votes=0
        for i in all_parties:
            cur_party = i[0]
            party_name=i[1]
            # print(cur_party)
            sql_command = f'select count(*) from VoteRecord where vote_id={cur_party}'
            no_of_votes = util.fetch_data(sql_command)[0][0]
            # print(no_of_votes)
            if no_of_votes==max_votes:
                winning_parties.append(party_name)
            elif no_of_votes>max_votes:
                winning_parties.clear()
                winning_parties.append(party_name)
                max_votes=no_of_votes
            sql_command=f'insert into Result values({cur_party},{year},{no_of_votes})'
            util.write_data(sql_command)
        print(f"\n---Here's the list of parties with maximum votes : {max_votes}---\n")
        for i in winning_parties:
            print(i, end="\n")    
        return True

    def add_party():
        party_name = input("Enter the name of the Party : ")
        party_id = util.get_number_of_records("Party")[0][0]+1
        sql_command = f'insert into Party values({party_id},"{party_name}")'
        try:
            util.write_data(sql_command)
        except:
            print("\n---Party already exists---\n")
        else:
            print(
                f"\n---Successfully added the party '{party_name}', and party_id is '{party_id}'---\n")
        return True

    def is_approved():
        user_id = input("Enter your Id : ")
        try:
            user_id = int(user_id)
        except:
            print("Invalid user Id")
            return AllOperation.is_approved()
        else:
            if util.check_is_user_approved(user_id)[0][0] == 0 or False:
                print("\n---Oops, you are not yet approved..!---\n")
            else:
                print("\n---Great, you are approved---\n")
        return True

    def make_admin():
        user_id = input("Enter your Id : ")
        try:
            user_id = int(user_id)
        except:
            print("Invalid user Id")
            return AllOperation.make_admin()
        else:
            if util.get_user_type(user_id)[0][0] == 1:
                print("\n---Already an Admin---\n")
                return True
            sql_command = 'select age from User where user_id={}'.format(
                str(user_id))
            user_age = util.fetch_data(sql_command)[0][0]
            if user_age >= 18:
                sql_command = 'Update Role set role_id=1 where user_id={}'.format(
                    str(user_id))
                util.write_data(sql_command)
                print(f"Successfully made {user_id} as Admin")
        return True

    def results():
        pass

    def edit_details():
        # If user want to edit details
        pass

    def give_vote():
        cur_year = datetime.date.today().year
        sql_command = f'select status from Election_Year where year={datetime.date.today().year}'
        result = util.fetch_data(sql_command)
        if len(result) == 0:
            print(f'\n---Elections of {cur_year} have not been started yet---\n')
        elif result[0][0] == 1:
            user_id=AllOperation.get_user_id()
            sql_command=f'select * from VoteRecord where user_id={user_id}'
            has_voted=util.fetch_data(sql_command)
            if len(has_voted)!=0:
                print("\n---You have already voted !---\n")
                return True
            sql_command = "select * from Party"
            all_parties = util.fetch_data(sql_command)
            for i in all_parties:
                party_id = i[0]
                party_name=i[1]
                print(party_id, " ", party_name)
            voter_choice=input("Enter the party of your choice : ")
            while not (voter_choice.isdigit() and int(voter_choice) >=1 and int(voter_choice)<=len(all_parties)):
                print("Invalid party Id, try again")
                voter_choice=input("Enter the party of your choice : ")
            sql_command=f'insert into VoteRecord values({user_id},{1},{voter_choice})'
            util.write_data(sql_command)
        elif result[0][0] == 2:
            print(f'\n---Elections of {cur_year} have already been closed---\n')
        return True

    def get_user_id():
        user_id = input("Enter your Id : ")
        try:
            user_id = int(user_id)
        except:
            print("Invalid user Id")
            return AllOperation.get_user_id()
        else:
            return user_id

    def register_new_user():
        # Register.reg_new_user()
        # return True
        pass

    def approve_user_login():
        pass

    def log_out():
        print("Logged out successfully..!")
        return False
