import re

def normalize_phone(phone_number):
    """
    "The function takes a phone number in string format. Removes unnecessary characters. 
     Trims number to the required minimum, and adds international code. 
     Return -> formatted phone number.
    """
    pattern = r"[^+\d]"
    code = "+38"
    
    formated_number = re.sub(pattern, '', phone_number)
    formated_number = formated_number[-10:] 
    formated_number = code + formated_number
   
    return formated_number  


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
