from django.test import TestCase

from ..validates import isValidEmail
from ..models import Employee, Department

# MODELS
class DepartmentTestCase(TestCase):

    # Exec Teste_Python\magalu>python manage.py test
    def test_can_create_department(self):
        self.department = Department.objects.create(name="TIC", description="Test")
        self.assertEqual(self.department.name, "TIC")
        self.assertEqual(self.department.description, "Test")
        print('OK')

class EmployeeTestCase(TestCase):

    #Exec Teste_Python\magalu>python manage.py test
    def test_can_create_employee(self):
        self.department = Department.objects.create(name="TI", description="Teste")
        self.employee = Employee.objects.create(first_name="Joao", last_name="Silva", email="joao@labs.com",
                                                department=self.department)
        self.assertEqual(self.employee.first_name, "Joao")
        self.assertEqual(self.employee.last_name, "Silva")
        self.assertEqual(self.employee.email, "joao@labs.com")
        self.assertEqual(self.employee.department, self.department)

    def test_val_email(self):
        self.department = Department.objects.create(name="TI", description="Teste")
        self.employee = Employee.objects.create(first_name="Joao", last_name="Silva", email="brunomzr@email.com",
                                                department=self.department)
        print(self.employee.email)
        print(isValidEmail(self.employee.email))
        if isValidEmail(self.employee.email):
            print('Valid email')
        else:
            print('Invalid email')
            self.assertEqual(isValidEmail(self.employee.email), True)