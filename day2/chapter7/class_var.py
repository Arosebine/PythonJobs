class Employee():
    pay_raise = 0.10

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        increase = self.pay_raise * self.p
        return increase + self.p

e1 = Employee('Benedict', 'Uwazie', 2000)
print(e1.pay_raise)
print(e1.f)
print(e1.l)
print(e1.salary())
e2 = Employee('Joshua', 'Ebhoria', 1500)
print(e2.salary())
        