import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')    



    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Ibrahim', 'Naveed', 50000)
        self.emp_2 = Employee('Sym', 'Piracha', 60000)

    
    def tearDown(self):
        print('tearDown\n')
        

    def test_email(self):
        
        print('testing email')
        self.assertEqual(self.emp_2.email, 'Sym.Piracha@email.com')
        self.assertEqual(self.emp_1.email, 'Ibrahim.Naveed@email.com')

        self.emp_1.first = 'Saad'
        self.emp_2.first = 'Ali'

        self.assertEqual(self.emp_2.email, 'Ali.Piracha@email.com')
        self.assertEqual(self.emp_1.email, 'Saad.Naveed@email.com')


    def test_fullname(self):
        print('testing fullname')
    

        self.assertEqual(self.emp_2.full_name, 'Sym Piracha')
        self.assertEqual(self.emp_1.full_name, 'Ibrahim Naveed')

        self.emp_1.first = 'Saad'
        self.emp_2.first = 'Ali'

        self.assertEqual(self.emp_2.full_name, 'Ali Piracha')
        self.assertEqual(self.emp_1.full_name, 'Saad Naveed')

    def test_apply_raise(self):
        print('testing raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)




if __name__ == '__main__':
     unittest.main()       

