import session.auth as begin_session
import pyfiglet
class Main:

    def entry_loop():
        print("\n=======================**DASHBOARD**=============================\n")
        print("Enter 1 to Sign Up")
        print("Enter 2 to Sign In")
        print("Enter 0 to exit")

        entry_choice = input("Enter your choice : ")
        if entry_choice.isdigit() and  int(entry_choice) == 1:
            begin_session.Auth.sign_up()
        elif entry_choice.isdigit() and  int(entry_choice) == 2:
            begin_session.Auth.login()
        elif entry_choice.isdigit() and  int(entry_choice) == 0:
            print(pyfiglet.figlet_format("THANKS \nFOR VISITING"))
            exit()
        else:
            print("Invalid choice, try again...")

        
print(pyfiglet.figlet_format("V o t i n g   \nS y s t e m"))
while True:
    Main.entry_loop()
