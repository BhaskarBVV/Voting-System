import maskpass
from configuration.config import input_line as il
import bcrypt
import utilities.utility as utility
import validations.validation as validate
from  colprint.colprint import NewPrint as col

class Register:

    def reg_new_user():
        
        all_aadhar=[]
        sql_command=f'select aadhaar_number from User'
        result=utility.Util.fetch_data(sql_command)
        for i in result:
            all_aadhar.append(i[0])
            
        name = input(il.format("Name"))
        fathers_name = input(il.format("Father's Name"))
        aadhar_exists=True
        while aadhar_exists:
            aadhar_number = validate.Validate.validate_input("Aadhaar Card", 12)
            if aadhar_number not in all_aadhar:
                aadhar_exists=False
            else:
                col.col_print("\n---Aadhar already Exists---\n","red")
            
        dob = validate.Validate.validate_dob()
        contact = validate.Validate.validate_input("Phone number", 10)
        email = validate.Validate.validate_email()
        city = input(il.format("City"))
        gender = validate.Validate.validate_gen()

        password = maskpass.advpass().encode('utf-8')
        password = str(bcrypt.hashpw(password, bcrypt.gensalt()).decode())

        number_of_records = utility.Util.get_number_of_records("User")[0][0]
        new_user_id = number_of_records + 1
        try:
            is_addition_successful = utility.Util.add_new_record([new_user_id, name, fathers_name,
                                                              aadhar_number, dob, contact, email, city, password, gender])
        except:
            print("\n----Aadhar number already exists, enter correct Aadhar card number...\n")
            return[False,-1]
        
        return [is_addition_successful, new_user_id]

    
