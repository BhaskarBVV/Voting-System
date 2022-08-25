import user.operations as op
input_line="Enter your {}....:"
roles={
    0:["Edit details","Give vote","Check on going Elections","Log out"], #user
    1:["Check on going Elections","Start Elections","Add Party","Register user","Check if user is approved","Make admin","Close Elections","Results","Log out"]  #admin

}
role_function_mapping={
    "Edit details": op.AllOperation.edit_details,
    "Give vote":op.AllOperation.give_vote,
    "Check on going Elections":op.AllOperation.check_on_going_elections,
    "Start Elections":op.AllOperation.start_election,
    "Add Party":op.AllOperation.add_party,
    "Check if user is approved":op.AllOperation.is_approved,
    "Make admin":op.AllOperation.make_admin,
    "Close Elections":op.AllOperation.close_elections,
    "Results":op.AllOperation.results,
    "Log out":op.AllOperation.log_out,
    "Register user":op.AllOperation.register_new_user,
}