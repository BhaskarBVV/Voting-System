import admin

class AdminOp:
    def list_of_op(self):
        print("Enter 1 to see if there is any ongoing elections: ")
        print("If Not than Press 2 to start elections: ")
        print("Press 3 to add party: ")
        print("Press 4 to approve user: ")
        print("Press 5 if user want to become admin: ")
        print("Press 6 to close elections: ")
        print("Press 7 to see Results: ")
        try:
            choice=int(input("Enter choice: "))
        except TypeError:
            print("Wrong Input!! Please enter again!")
            list_of_op()
        else:
            match choice:
                case 1: 
                    checkOngoingElections()
                
                case 2:
                    startElection()
                    
                case 3:
                    addParty()
                    
                case 4:
                    isApproved()
                    
                case 5:
                    makeAdmin()
                    
                case 6:
                    closeEections()
                    
                case 7:
                    results()
                case default:
                    print("Invalid Input!!")
                    print("Please try again!!")
                    list_of_op()
                
                

    #print the list of all operations, get choice from admin.
    # validate the choice.
    # apply switch case on admin_choice and call function respectively from admin.py
