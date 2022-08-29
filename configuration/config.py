import user.operations as op

input_line = "Enter your {}....:"

dashboard = "\n=======================**DASHBOARD**=============================\n"

Invalid = "\n---Opps, its an Invalid Choice, try again...\n"

roles = {
    0: ["Edit_details", "Give_vote", "Check_on_going_Elections", "Log_out"],  # user
    1: ["Check_on_going_Elections", "Start_Elections", "Add_Party", "Register_user",
        "Edit_details", "Approve_the_user_for_login", "Show_all_Users", "Check_if_user_is_approved",
        "Make_admin", "Close_Elections", "Election_Results", "Log_out"]  # admin

}
role_function_mapping = {
    "Edit_details": op.AllOperation.edit_details,
    "Give_vote": op.AllOperation.give_vote,
    "Check_on_going_Elections": op.AllOperation.check_on_going_elections,
    "Start_Elections": op.AllOperation.start_election,
    "Add_Party": op.AllOperation.add_party,
    "Check_if_user_is_approved": op.AllOperation.is_approved,
    "Make_admin": op.AllOperation.make_admin,
    "Close_Elections": op.AllOperation.close_elections,
    "Election_Results": op.AllOperation.results,
    "Log_out": op.AllOperation.log_out,
    "Register_user": op.AllOperation.register_new_user,
    "Approve_the_user_for_login": op.AllOperation.approve_user_login,
    "Show_all_Users": op.AllOperation.show_all_users
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

main_menu = ["Exit", "Sign_Up", "Sign_In"]
