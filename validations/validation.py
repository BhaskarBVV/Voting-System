import math
# from configuration.config import input_line as il
import re
il = "Enter your {}....:" 
class Validate:

    def validate_input(val, digits):
        user_input = input(il.format(val))
        try:
            user_input = int(user_input)
        except:
            print(f"Invalid {val}, please enter a valid {digits} digit {val}")
            return Validate.validate_input(val, digits)
        else:
            if math.floor(math.log10(user_input)+1) == digits:
                return user_input
            print(f"Invalid {val}, please enter a valid {digits} digit {val}")
            return Validate.validate_input(val, digits)

    def validate_email():
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = input(il.format("Email"))
        if not re.fullmatch(regex, email):
            print("Invalid email, please enter a valid email.")
            return Validate.validate_email()
        else:
            return email