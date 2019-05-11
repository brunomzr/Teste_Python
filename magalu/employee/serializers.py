from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'department')

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