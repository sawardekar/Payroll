from rest_framework import serializers
from staff import models


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer define employee create/edit using employee table
    """
    id = serializers.ReadOnlyField(required=False)
    creation_date = serializers.DateTimeField(required=False)
    edited_on = serializers.DateTimeField(required=False)
    created_by = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    edited_by = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = models.Employee
        fields = '__all__'