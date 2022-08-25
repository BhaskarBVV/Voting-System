class options:

    def get_choice(available_op):
        for idx,i in enumerate(available_op,0):
            print(f"Enter {idx} to {i}")
        choice=input("Enter your choice : ")
        try:
            choice=int(choice)
        except:
            print("\nInvalid input, please enter a valid number")
            options.get_choice(available_op)
        else:
            return available_op[choice]
        
