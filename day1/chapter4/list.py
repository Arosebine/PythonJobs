person = ['Benedict', 37, 'Fair', 'Developer']

# Write a program in Python that will print out
# My name is Benedict, I am 37years old and Fair in complexion
# where Benedict, 37 and Fair are Items in the list
print(f'My name is {person[0]}, I am {person[1]} old and {person[2]}')

# access_control = ['admin', 'superadmin', 'guest']
# write a program in python that will print out 'Welcome to admin dashboard'
# if the user is admin or 'Welcome to superadmin dashboard' or 
# 'Welcome to guest dashboard'

# user = input('User access: ')

# if access_control[0] == user:
#     print(f'Welcome to {access_control[0]} dashboard')
# elif access_control[1] == user:
#     print(f'Welcome to {access_control[1]} dashboard')
# elif access_control[2] == user:
#     print(f'Welcome to {access_control[2]} dashboard')
# else:
#     print('No access for you')

# CHANGE PASSWORD CLASSWORK
# Create a list containing username and password,
# if the length of password is greater than
# 8 check if the password and confirm password are 
# the same and if true change the password to a new
# one and print password changed successfully 
# else print passwords do not match and print 
# password is less than 8 characters

data = ['benedict', 'pass123456']
password = input('Enter Password: ')
password_confirm = input('Enter Password: ')

if len(password) > 8:
    if password == password_confirm:
        data[1] = password
        print('Password changed successfully')
        print(data)
    else:
        print('Passwords do not match')
else:
    print('Password is less than 8')


