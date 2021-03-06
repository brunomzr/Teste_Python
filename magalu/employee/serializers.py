from rest_framework import serializers

from .validates import isValidEmail
from .models import Employee, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name','description')

class EmployeeSerializer(serializers.ModelSerializer):

    def validate_email(self,value):
        print(value)
        if not isValidEmail(value):
            raise serializers.ValidationError('Invalid Email.')
        return value

    class Meta:
        model = Employee
        fields = ('id','first_name', 'last_name', 'email', 'department','created_at','updated_at')

    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    # email = serializers.CharField()
    # department = serializers.CharField()
    #
    # def create(self):
    #     return Employee.objects.create(self)
    #
    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.department = validated_data.get('department', instance.department)
    #
    #     instance.save()
    #     return instance