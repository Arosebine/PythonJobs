name = "Benedict"
state = 'Lagos'

quote1 = "Get rich or die trying by '50 Cent' "
quote2 = 'Get rich or die trying by "50 Cent" '
quote3 = "Get rich or die trying by \"50 Cent\" "
print(quote1)
print(quote2)
print(quote3)

fname = 'Benedict'
lname = 'Uwazie'
full_name = fname +' '+ lname
print(full_name)

# My name is Benedict, I am 12years old and I live in Berlin
# Write a python program to print the string above where
# Benedict, 12 and Berlin are variables

name = 'Alabi'
age = 45
location = 'Lagos'
sentence1 = 'My name is '+' '+name+', '+'I am '+str(age)+'years old and I live in '+' '+location
print(sentence1)

sentence2 = 'My name is {}, I am {}years old and I live i {}'.format(name, age, location)
print(sentence2)

sentence3 = f'My name is {name}, I am {age}years old and I live i {location}'
print(sentence3)
