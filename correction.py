# Create a python list with email and password
# display an error message if email is not in the
# list, if the email is in the list check if the
# two password fields matches, and if it does, change the
# password to a new one and dispplay success message
# data = ['myemail@gmail.com', 'pass123456']
# email = input('Enter Email: ')
# password1 = input('Enter Password1: ')
# password2 = input('Enter Password2: ')

# if email != data[0]:
#     print(f'{email} is not in the database')
# elif email == data[0]:
#     if password1 == password2:
#         data[1] = password1
#         print('Passwords changed successfully')
#         print(data)
#     else:
#         print('Passwords do not match!!')


# Assignment 1
# 1. Using any of the conditional statement learnt to write a simple Python program that will output the score and remark eg “Your score is 76 and this is Excellence” using the algorithm below. Make sure that invalid score such value greater than 100 or less than 1 are detected and reported
#  0 – 34 = Fail
#  35 – 44 = Pass
#  45 – 49 = Fair
#  50 – 59 = Good
#  60 – 69 = Very Good
#  70 – 100 = Excellence

score = 15
if score >= 0 and score < 35:
    grade = 'Fail'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 35 and score < 45:
    grade = 'Pass'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 45 and score < 50:
    grade = 'Fair'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 50 and score < 60:
    grade = 'Good'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 60 and score < 70:
    grade = 'Very Good'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 70 and score <= 100:
    grade = 'Excellent'
    print(f'Your score is {score} and your grade is {grade}')
else:
    print('Invalid score')
# 2. Write a program in python that will print the lowest 
# number among three numbers supplied
num1 = 10
num2 = 6
num3 = 7

if num1 > num2 and num1 > num3:
    print(f'{num1} is greater than {num2} and {num3}')
elif num2 > num1 and num2 > num3:
    print(f'{num2} is greater than {num1} and {num3}')
elif num3 > num1 and num3 > num2:
    print(f'{num3} is greater than {num1} and {num2}')

# Assignment 2
# 1. Create a multiplication table program using while loop, 
# this will be done in such a way that when a user supplies any 
# number the multiplication table of that number will be created.

x = 1
number = 3
while x <= 12:
    result = number * x
    print(f'{number} X {x} = {result}')
    x += 1
# 2. Write a program in python that tells if the name you supplied is in a list or the name is not in a list.
# 3. Write a program in python that sums all the numbers from 1 to 30
# 4. Write a program that sums all the numbers in a list 10, 20, 30, 40, 70, 200, 300 and also determine the average.
