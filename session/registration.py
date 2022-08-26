import maskpass
import math
from configuration.config import input_line as il
import bcrypt
import utilities.utility as utility
import re


class Register:

    def reg_new_user():

        name = input(il.format("Name"))
        fathers_name = input(il.format("Father's Name"))

        aadhar_number = Register.validate_input("Aadhaar Card", 12)
        age = Register.validate_input("Age", 2)
        contact = Register.validate_input("Phone number", 10)
        email = Register.validate_email()
        city = input(il.format("City"))
        gender = input(il.format("Gender M/F"))

        password = maskpass.advpass().encode('utf-8')
        password = str(bcrypt.hashpw(password, bcrypt.gensalt()).decode())

        number_of_records = utility.util.get_number_of_records("User")[0][0]
        new_user_id = number_of_records + 1
        try:
            is_addition_successful = utility.util.add_new_record([new_user_id, name, fathers_name,
                                                              aadhar_number, age, contact, email, city, password, gender])
        except:
            print("\n----Aadhar number already exists, enter correct Aadhar card number...\n")
            return[False,-1]
        return [is_addition_successful, new_user_id]

    def validate_input(val, digits):
        user_input = input(il.format(val))
        try:
            user_input = int(user_input)
        except:
            print(f"Invalid {val}, please enter a valid {digits} digit {val}")
            return Register.validate_input(val, digits)
        else:
            if math.floor(math.log10(user_input)+1) == digits:
                return user_input
            print(f"Invalid {val}, please enter a valid {digits} digit {val}")
            return Register.validate_input(val, digits)

    def validate_email():
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = input(il.format("Email"))
        if not re.fullmatch(regex, email):
            print("Invalid email, please enter a valid email.")
            return Register.validate_email()
        else:
            return email
