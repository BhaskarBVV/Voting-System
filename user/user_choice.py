class options:

    def get_choice(available_op):
        for idx,i in enumerate(available_op,0):
            print(f"Enter {idx} to {i}")
        choice=input("Enter your choice : ")
        try:
            choice=int(choice)
            if not choice in range(len(available_op)):
                print("\n---Opps, its an Invalid Choice, try again...\n")
                return options.get_choice(available_op)

        except:
            print("\nInvalid input, please enter a valid number")
            options.get_choice(available_op)
        else:
            # print(available_op[choice])
            return available_op[choice]
        
