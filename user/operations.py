from utilities.utility import util as util
class AllOperation:
    
    def check_on_going_elections():
        #if yes than only add user or allow user to login or register
        pass
    
    def start_election():
        # start elections
        pass
    
    def add_party():
        party_name=input("Enter the name of the Party : ")
        party_id=util.get_number_of_records("Party")[0][0]+1
        sql_command=f'insert into Party values({party_id},"{party_name}")'
        util.write_data(sql_command)
        print(f"Successfully added the party '{party_name}', and party_id is '{party_id}'")
    
    def is_approved():
        #check if elections are ongoing tha approve 
        # else not approve and update approval table
        pass
    
    def make_admin():
        #ask to become admin
        pass
    
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
    
    def become_admin():
        #Request to become admin
        pass
    def log_out():
        print("Logged out successfully..!")
        return