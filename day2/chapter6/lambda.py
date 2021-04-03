
add = lambda x, y: x + y
print(add(5, 6))
number = lambda x: x + 2
print(number(5))


def print_even(number):
    for n in range(number+1):
        if n % 2 == 0:
            print(n)

print_even = lambda num: [n for n in range(num+1) if (n % 2 == 0)]
print(print_even(20))
