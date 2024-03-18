#PROGRAM TO CHECK THE STRENGTH OF PASSWORD BASED ON CONDITIONS

def password_checker(password):
    n=len(password)
    count=0
    special_symbol=['@','#','$','&']
    if(n<8 or n>24):
        print("Password should be between 8 to 24 characters:")
    else:
        count+=1
    if not any(x.isupper()for x in password):
        print("Password should contain atleast one uppercase letter")
    else:
        count+=1
    if not any(x.islower() for x in password):
        print("Password should contain atleast one lowercase letter")
    else:
        count+=1
    if not any(x.isalnum() for x in password):
        print("Password should contain atleast one number")
    else:
        count+=1
    if not any(x in special_symbol for x in password):
        print("Password should have atleast one special symbol")
    else:
        count+=1
    return count

password=input("Enter the password:")
strenght=password_checker(password)
if(strenght>=4):
    print("Strong password")
elif(strength>=2):
    print("Weak Password")
else:
    print("Invalid Password")
