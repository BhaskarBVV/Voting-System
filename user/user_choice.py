class options:

    def __init__(self):
        #just doit
        pass
    def get_choice(self, available_op):
        for idx,i in enumerate(available_op,0):
            print(f"Enter {idx} to {i}")
        try:
            choice=int(input("Enter your choice : "))
        except TypeError:
            print("Invalid input, please enter a valid number")
            self.get_choice(available_op)
        else:
            return available_op[choice]