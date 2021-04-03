def hello():
    print('Hello people!!')

hello()

def greetings(name, salute):
    print(f'Good {salute} Mr. {name}')

greetings('Benedict', 'morning')
greetings('Alabi', 'afternoon')
greetings('Tope', 'night')

def add(num1, num2):
    summation = num1 + num2
    print(summation)


add(5, 6)
add(15, 7)
add(11, 10)

# Create a function that will print out these
# My name is Benedict, I am 42years old and Fair in Complexion
# Where Benedict, 42 and Fair are arguments of the function
# print for three different persons

def person(name, age, complexion):
    print(f'My name is {name}, I am {age}years old and {complexion} in Complexion')

person('Benedict', 42, 'Fair')
person('Alabi', 52, 'Dark')

# createa a function to determine the area of a triangle
# area = 1/2 * base * heigth
# call for three different values
# (base=200, heigth=100), 
# (base=300, heigth=200), 
# (base=400, heigth=300)

def area_triangle(base, heigth):
    area = 0.5 * base * heigth
    print(area)

area_triangle(200, 100)
area_triangle(300, 200)
area_triangle(400, 300)

def print_even(number):
    for n in range(number+1):
        if n % 2 == 0:
            print(n)

print('FOR TWENTY')
print_even(20)
print('FOR THIRTY')
print_even(20)


def multiplication(number, start, stop):
    for start in range(start, stop+1):
        result =  number * start
        print(f'{number} X {start} = {result}')

multiplication(2, 3, 12)
multiplication(4, 2, 10)

