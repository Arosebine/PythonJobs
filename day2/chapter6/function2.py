def office(name, color='Yellow'):
    print(f'The name of my office is {name} and the color is {color}')

office('MTN')
office('Alabian', 'Sky Blue')


def multiplication(number, start=1, stop=12):
    for start in range(start, stop+1):
        result = number * start
        print(f'{number} X {start} = {result}')



multiplication(2)
multiplication(3, 4, 10)


def add_numbers(num1, num2):
    add = num1 + num2
    print(add)

def summation(num1, num2):
    add = num1 + num2
    return add

add_numbers(5, 4)
var = summation(10, 5)
print(var)
if var == 15:
    print('Hello people')
