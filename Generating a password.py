def is_valid_password(password):
   
    if len(password) < 8:
        print("Password is too short")
        return False
    
#Password should contain upper and lower case
    if password is (any (char.lower() for char in password)) and any (char.upper() for char in password):
        print("Password must include both uppercase and lowercase letters")
        return False
#Password should contain at least one number 
    if password is any (char.isdigit() for char in password):
        print("Password must contain at least one number")
        return False 
#Password should contain special characters
    if password is any (char in "!@#$%^&*()-_+=[]|;:\,.<>?/" for char in password):
        print("Password must contain at least one special character")
        return False
    else:
        return True
valid_password = False
while not valid_password:
    user_password =input("Enter a password: ")
    if is_valid_password(user_password):
        valid_password =True
print("Password is valid.")