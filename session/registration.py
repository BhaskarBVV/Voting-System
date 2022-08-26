import maskpass
import math
from configuration.config import input_line as il
import bcrypt
import utilities.utility as utility
import re
import validations.validation as validate

class Register:

    def reg_new_user():

        name = input(il.format("Name"))
        fathers_name = input(il.format("Father's Name"))
        
        aadhar_number = validate.Validate.validate_input("Aadhaar Card", 12)
        dob = validate.Validate.validate_dob()
        contact = validate.Validate.validate_input("Phone number", 10)
        email = validate.Validate.validate_email()
        city = input(il.format("City"))
        gender = input(il.format("Gender M/F"))

        password = maskpass.advpass().encode('utf-8')
        password = str(bcrypt.hashpw(password, bcrypt.gensalt()).decode())

        number_of_records = utility.util.get_number_of_records("User")[0][0]
        new_user_id = number_of_records + 1
        try:
            is_addition_successful = utility.util.add_new_record([new_user_id, name, fathers_name,
                                                              aadhar_number, dob, contact, email, city, password, gender])
        except:
            print("\n----Aadhar number already exists, enter correct Aadhar card number...\n")
            return[False,-1]
        
        return [is_addition_successful, new_user_id]

    
