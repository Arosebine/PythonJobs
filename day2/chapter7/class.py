class CarMotor():
    wheels = 4
    doors = 4

    def detail(self, name, color):
        print(f'Here are the car details, name is {name}, color {color} wheels is {self.wheels}')
    
c1 = CarMotor()
print(c1.wheels)
c1.detail('BMW', 'Black')
c2 = CarMotor()
print(c2.wheels)
c2.detail('MAZDA', 'Yellow')
