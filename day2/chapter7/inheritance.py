class Employee():
    pay_raise = 0.10

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        increase = self.pay_raise * self.p
        return increase + self.p


class Developer(Employee):
    def detail(self):
        print('Here are the details of this Employee')
        det = 'Firstname:' + self.f + '\n'
        det += 'Lastname:' + self.l + '\n'
        det += 'Pay:' + str(self.p) + '\n'
        print(det)

d1 = Developer('Alabi', 'Adebayo', 5000)
print(d1.salary())
print(d1.f)
print(d1.detail())
