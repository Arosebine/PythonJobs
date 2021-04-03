
def square(number):
    return number**2

result = list(map(square, range(11)))
print(result)




def print_num(data):
    cast = str(data)
    if cast.isnumeric():
        return cast


items = ['string1', 50, 'string2', 70, 100, 'string3']
filter_result = list(filter(print_num, items))
print(filter_result)

filter_num = list(filter(lambda x: True if (x % 2 == 0) else False, range(10)))
print(filter_num)

