
even_numbers = []
for n in range(20):
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers)

even_numbers = [n for n in range(20) if (n % 2 == 0)]
print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 4]
even = [n for n in numbers if (n % 2 == 0)]
print(even)

