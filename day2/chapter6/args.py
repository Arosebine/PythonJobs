def add(num1, num2):
    add = num1 + num2
    print(add)

# add(3, 2, 5)

def summation(*args):
    total = 0
    for x in args:
        total += x
    print(total)

summation(3, 2, 5, 5)

def print_letters(*args):
    for p in args:
        print(p)


# def print_letters(*args):
#     print(args)
    

print_letters('Letter 1', 'Letter 2', 'Letter 2')

name, age, salary = ['Benedict', 42, 50000]
print(name)
print(age)
print(salary)
