from tabulate import tabulate
class options:

    def get_choice(available_op):
        # for idx,i in enumerate(available_op,0):
        #     print(f"Enter {idx} to {i}")
        print("Select from Available options : ")
        print(tabulate([[idx,x] for idx,x in enumerate(available_op,0)], headers=["Enter","Operation"],tablefmt='fancy_grid'))
        choice=input("Enter your choice : ")
        try:
            choice=int(choice)
            if not choice in range(len(available_op)):
                print("\n---Opps, its an Invalid Choice, try again...\n")
                return options.get_choice(available_op)

        except:
            print("\n---Opps, its an Invalid Choice, try again...\n")
            options.get_choice(available_op)
        else:
            # print(available_op[choice])
            return available_op[choice]
        
