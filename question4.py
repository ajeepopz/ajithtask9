import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

#Mobile Number of Bangladesh:
def validate_bangladesh_mobile_number(number):
    pattern = r'^\+8801[3-9]\d{8}$'
    return re.match(pattern, number) is not None

#Telephone Number of USA:

def validate_usa_telephone_number(number):
    pattern = r'^\+1 \(\d{3}\) \d{3}-\d{4}$'
    return re.match(pattern, number) is not None

#Alphanumeric Password (Upper case, lower case, special characters, and numbers):

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pattern, password) is not None

# Example usage
email = "test@example.com"
print(validate_email(email))

mobile_number = "+8801712345678"
print(validate_bangladesh_mobile_number(mobile_number))

telephone_number = "+1 (123) 456-7890"
print(validate_usa_telephone_number(telephone_number))

password = "Abcd@1234"
print(validate_password(password))
