import Session.auth as begin_session
class Main:

    def entry_loop(self):
        print("\n========================**DASHBOARD**==============================\n")
        print("Enter 1 to Sign Up")
        print("Enter 2 to Sign In")
        print("Enter 0 to exit")

        entry_choice = input("Enter your choice : ")
        if entry_choice.isdigit() and  int(entry_choice) == 1:
            begin_session.Auth.sign_up()
        elif entry_choice.isdigit() and  int(entry_choice) == 2:
            begin_session.Auth.login()
        elif entry_choice.isdigit() and  int(entry_choice) == 0:
            print("\n=================** THANK YOU FOR VISITING**===================\n")
            exit()
        else:
            print("Invalid choice, try again...")

        



A = Main()
while True:
    A.entry_loop()
