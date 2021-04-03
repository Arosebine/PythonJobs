class CarMotor():
    wheels = 4
    doors = 4

    def __init__(self):
        print('This is a constructor')

    def detail(self, name, color):
        print(
            f'Here are the car details, name is {name}, color {color} wheels is {self.wheels}')


c1 = CarMotor()
c1.detail('Mazda', 'Yellow')
