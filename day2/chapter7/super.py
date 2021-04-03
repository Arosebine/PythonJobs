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

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog = prog_lang

    def detail(self):
        print('Here are the details of this Employee')
        det = 'Firstname:' + self.f + '\n'
        det += 'Lastname:' + self.l + '\n'
        det += 'Pay:' + str(self.p) + '\n'
        print(det)


d1 = Developer('Favour', 'Enang', 5000, 'JS')
print(d1.prog)



