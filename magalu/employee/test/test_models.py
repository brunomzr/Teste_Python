import django.test

from magalu.employee.models import Employee

# MODELS
class EmployeeTestCase(django.test.TestCase):
    def test_can_create_employee(self):
        self.employee = Employee.objects.create(first_name="Joao", last_name="Silva", email="joao@labs.com",department="TI")
        self.assertEqual(self.employee.first_name, "Joao")
        self.assertEqual(self.employee.last_name, "Silva")
        self.assertEqual(self.employee.email, "joao@labs.com")
        self.assertEqual(self.employee.department, "TI")