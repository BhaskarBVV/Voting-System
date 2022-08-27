import user.operations as op

input_line = "Enter your {}....:"
dashboard="\n=======================**DASHBOARD**=============================\n"
Invalid="\n---Opps, its an Invalid Choice, try again...\n"
roles = {
    0: ["Edit details", "Give vote", "Check on going Elections", "Log out"],  # user
    1: ["Check on going Elections", "Start Elections", "Add Party", "Register user","Edit details","Approve the user for login", "Show all Users", "Check if user is approved", "Make admin", "Close Elections", "Election Results", "Log out"]  # admin

}
role_function_mapping = {
    "Edit details": op.AllOperation.edit_details,
    "Give vote": op.AllOperation.give_vote,
    "Check on going Elections": op.AllOperation.check_on_going_elections,
    "Start Elections": op.AllOperation.start_election,
    "Add Party": op.AllOperation.add_party,
    "Check if user is approved": op.AllOperation.is_approved,
    "Make admin": op.AllOperation.make_admin,
    "Close Elections": op.AllOperation.close_elections,
    "Election Results": op.AllOperation.results,
    "Log out": op.AllOperation.log_out,
    "Register user": op.AllOperation.register_new_user,
    "Approve the user for login": op.AllOperation.approve_user_login,
    "Show all Users": op.AllOperation.show_all_users
}

user_fields = {
    "Name": "name",
    "Fathers Name": "father_Name",
    "Dob": "dob",
    "Contact": "contact",
    "Email": "email",
    "City": "city",
    "Gender": "gender"
}

main_menu=["Exit","Sign Up","Sign In"]
                        
