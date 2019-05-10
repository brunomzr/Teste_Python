from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"employees": serializer.data})

    def post(self, request):
        employee = request.data.get('employee')

        # Create an employee from the above data
        serializer = EmployeeSerializer(data=employee)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' created successfully".format(employee_saved.title)})

    def put(self, request, pk):
        saved_employee = get_object_or_404(Employee.objects.all(), pk=pk)
        data = request.data.get('employee')
        serializer = EmployeeSerializer(instance=saved_employee, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' updated successfully".format(employee_saved.title)})


    def delete(self, request, pk):
        # Get object with this pk
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        employee.delete()
        return Response({"message": "Employee with id `{}` has been deleted.".format(pk)},status=204)