x = 1
while x <= 5:
    print(x)
    x += 1

states = ['Abuja', 'Lagos', 'Port Harcourt', 'Kano', 'Kaduna']
x = 0
while x < len(states):
    print(states[x])
    x += 1

total = 0
x = 1
while x <= 30:
    total += x
    x += 1
print(total)


x = 1
while x <= 20:
    if x % 2 == 0:
        print(x)
    x += 1

# 1,
# 2, 
# 3,
# .
# .
# .
# 10
x = 1
while x <= 10:
    if x < 10:
        print(f'{x},')
    else:
        print(f'{x}')

