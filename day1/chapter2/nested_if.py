word1 = 'ben#$12dict'
word1 = 'bendict'
# word2 = 'benedict'
# print(word1.isalpha())
# print(word2.isalpha())

if word1.isalpha():
    if len(word1) > 5:
        print('Weldone maa')

# write a program in python to check if username 
# and pasword is correct then print welcome to dashboard
# else print username and password do not match

username = input('Enter username: ')
password = input('Enter password: ')

db_username='benedict'
db_password='password'

if username == db_username and password == db_password:
    print('Welcome to dasbord')
else:
    print('Username and Password do not match')
