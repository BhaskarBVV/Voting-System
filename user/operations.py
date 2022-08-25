from utilities.utility import util as util
import datetime
class AllOperation:
    
    def check_on_going_elections():
        sql_command=f'select status from Election_Year where year={datetime.date.today().year}'
        result=util.fetch_data(sql_command)
        print(type(result[0][0]))
        if len(result)==0:
            print(f"\n---Elections of {datetime.date.today().year} are not yet started---\n")
        elif result[0][0]==1:
            print(f"\n---Yes Elections of {datetime.date.today().year} are going on---\n")
        else:
            print(f"\n---No Elections of {datetime.date.today().year} are over---\n")
        return True
        
    
    def start_election():
        # start elections
        pass
    
    def add_party():
        party_name=input("Enter the name of the Party : ")
        party_id=util.get_number_of_records("Party")[0][0]+1
        sql_command=f'insert into Party values({party_id},"{party_name}")'
        try:
            util.write_data(sql_command)
        except:
            print("\n---Party already exists---\n")
        else:
            print(f"\n---Successfully added the party '{party_name}', and party_id is '{party_id}'---\n")
        return True
        
    def is_approved():
        user_id=input("Enter your Id : ")
        try:
            user_id=int(user_id)
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
        user_id=input("Enter your Id : ")
        try:
            user_id=int(user_id)
        except:
            print("Invalid user Id")
            return AllOperation.make_admin()
        else:
            if util.get_user_type(user_id)[0][0]==1:
                print("\n---Already an Admin---\n")
                return True
            sql_command='select age from User where user_id={}'.format(str(user_id))
            user_age=util.fetch_data(sql_command)[0][0]
            if user_age>=18:
                sql_command='Update Role set role_id=1 where user_id={}'.format(str(user_id))
                util.write_data(sql_command)
                print(f"Successfully made {user_id} as Admin")
        return True

    def close_elections():
        # close elections and count votes
        pass
        
    def results():
        # update results table
        pass
    def edit_details():
        #If user want to edit details
        pass
    
    def give_vote():
        # Give vote to the party
        pass
    
    def is_approved_by_admin():
        # is apporved by admin to login or register
        pass
    
    def register_new_user():
        # Register.reg_new_user()
        # return True
        pass

    def log_out():
        print("Logged out successfully..!")
        return False
