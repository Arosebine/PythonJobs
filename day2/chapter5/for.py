print(range(10))
print(range(1, 12))

for n in range(10):
    print(n)

for n in range(3, 10):
    print(n)
print('BREAK')
for n in range(3, 10, 3):
    print(n)


states = ['Lagos', 'Port Harcourt', 'Abuja', 'Ibadan', 'Kano']

for s in states:
    print(s)

for n in range(20):
    if n % 2 == 0:
        print(n)


states = {
    'Imo':'Owerri',
    'Abia':'Umuahia',
    'Lagos':'Ikeja',
    'Plateau':'Jos',
    'Kaduna':'Kaduna'
}

print(states['Imo'])

print('KEYS')
for s in states:
    print(s)

print('VALUES')
for s in states:
    print(states[s])

print('KEYS & VALUES')
for s, c in states.items():
    print(s, c)
