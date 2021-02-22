
class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first =  first
        self.last = last
        self.pay = pay

        #Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)    

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   


    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
            
        else:
            return 'Bad Response' 

    
    #@classmethod
    #def set_raise_amount(cls, amount):
    #    cls.raise_amount = amount   

#class Developer(Employee):
#    raise_amount = 1.10

#    def __init__(self, first, last, pay, prog_lang):
#        super().__init__(first, last, pay)
  #      self.prog_lang = prog_lang

   


    #def __str__(self):
    #    return '{} - {}'.format(self.full_name(), self.email)

    #def __repr__(self):
    #    return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)   

#    def __add__(self, other):
#        return self.pay + other.pay        

#    def __len__(self):
#        return len(self.full_name())


#dev_1 = Developer('Ibrahim', 'Naveed', 50000, 'Python')
#dev_2 = Developer('Test', 'User', 60000, 'Java')

#print(dev_1.email)
#dev_1.first = 'Sym'
#print(dev_1.email)

#print(len(dev_1))

