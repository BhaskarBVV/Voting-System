import user.operations as op
input_line="Enter your {}....:"
roles={
    0:["Edit details","Give vote","Is Approved by Admin","Become Admin"], #user
    1:["Check on going Elections","Start Elections","Add Party","Approval","Make admin","Close Elections","Results"]  #admin
}
role_function_mapping={
    "Edit details": op.AllOperation.edit_details,
    "Give vote":op.AllOperation.give_vote,
    "Is Approved by Admin":op.AllOperation.is_approved_by_admin,
    "Become Admin":op.AllOperation.become_admin,
    "Check on going Elections":op.AllOperation.check_on_going_elections,
    "Start Elections":op.AllOperation.start_election,
    "Add Party":op.AllOperation.add_party,
    "Approval":op.AllOperation.is_approved,
    "Make admin":op.AllOperation.make_admin,
    "Close Elections":op.AllOperation.close_elections,
    "Results":op.AllOperation.results
}