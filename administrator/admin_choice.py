import administrator.admin as admin 

class AdminOp:
    def list_of_op():
        print("Enter 1 to see if there is any ongoing elections: ")
        print("If Not than Press 2 to start elections: ")
        print("Press 3 to add party: ")
        print("Press 4 to approve user: ")
        print("Press 5 if user want to become admin: ")
        print("Press 6 to close elections: ")
        print("Press 7 to see Results: ")
        try:
            choice=int(input("Enter choice: "))
        except:
            print("Wrong Input!! Please enter again!")
            admin.list_of_op()
        else:
            match choice:
                case 1: 
                    admin.check_on_going_elections()
                
                case 2:
                    admin.start_election()
                    
                case 3:
                    admin.add_party()
                    
                case 4:
                    admin.is_approved()
                    
                case 5:
                    admin.make_admin()
                    
                case 6:
                    admin.close_elections()
                    
                case 7:
                    admin.results()
                    
                case default:
                    print("Invalid Input!!")
                    print("Please try again!!")
                    admin.list_of_op()