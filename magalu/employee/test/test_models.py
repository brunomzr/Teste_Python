from django.test import TestCase

from ..validates import isValidEmail
from ..models import Employee

# MODELS
class EmployeeTestCase(TestCase):


    # Exec Teste_Python\magalu>python manage.py test
    def test_can_create_employee(self):
        self.employee = Employee.objects.create(first_name="Joao", last_name="Silva", email="joao@labs.com",department="TI")
        self.assertEqual(self.employee.first_name, "Joao")
        self.assertEqual(self.employee.last_name, "Silva")
        self.assertEqual(self.employee.email, "joao@labs.com")
        self.assertEqual(self.employee.department, "TI")

    def test_val_email(self):
        self.employee = Employee.objects.create(first_name="Joao", last_name="Silva", email="123!#",
                                                department="TI")
        print(self.employee.email)
        print(isValidEmail(self.employee.email))
        self.assertEqual(isValidEmail(self.employee.email),True)