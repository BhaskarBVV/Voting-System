import maskpass
from configuration.config import input_line as il
import bcrypt
import utilities.utility as utility
class Register:

    def reg_new_user():

        name=input(il.format("Name"))
        fathers_name=input(il.format("Father's Name"))
        aadhar_number= int(input(il.format("Aadhaar Card")))
        age=int(input(il.format("Age")))
        contact=int(input(il.format("Phone number")))
        email=input(il.format("Email"))
        city=input(il.format("City"))
        gender=input(il.format("Gender M/F"))

        password=maskpass.advpass().encode('utf-8')
        password=str(bcrypt.hashpw(password, bcrypt.gensalt()).decode())
        
        number_of_records=utility.util.get_number_of_records()[0][0]
        new_user_id = number_of_records + 1
        # print(type(number_of_records))
        is_addition_successful=utility.util.add_new_record([new_user_id, name, fathers_name, 
                                aadhar_number, age, contact,email, city,password,gender])
        return [is_addition_successful, new_user_id]
        