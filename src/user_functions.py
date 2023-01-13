# The simplest function to get the user email (copy to src/user_functions.py)
#def get_email_from_input():
#    """ Contains '@' and '.' """
#    return input("Write down your email: ")

#import re

# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input('Write down your email: ')

    if ('@' not in email or '.' not in email):
        print('Email is not valid.')
    else:
        return email
		
def get_user_name_from_input():
   """ Not empty string. No spaces. """
   username = input('Create your user name: ')
   
   if (not username or ' ' in username):
       print('Username is not valid.')
   else:
       return username
    
def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    password = input("Create your password: ")
    
    if (len(password) < 8 or " " not in password):
        print('Password is not valid.')
    else:
        return password