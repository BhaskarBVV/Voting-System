from tabulate import tabulate
import fontstyle
class Options:

    def col(text,col):
        return fontstyle.apply(text,col)

    def get_choice(available_op):
        print("Select from Available options : ")
        print(tabulate([[idx,x] for idx,x in enumerate(available_op,0)], headers=["Enter","Operation"],tablefmt='fancy_grid'))
        choice=input("Enter your choice : ")
        try:
            choice=int(choice)
            if not choice in range(len(available_op)):
                print(Options.col("\n---Opps, its an Invalid Choice, try again...\n", 'Red'))
                return Options.get_choice(available_op)

        except:
            print(Options.col("\n---Opps, its an Invalid Choice, try again...\n", 'Red'))
            return Options.get_choice(available_op)
        else:
            return available_op[choice]
    
        
