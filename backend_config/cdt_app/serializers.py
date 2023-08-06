from rest_framework import serializers
from cdt_app.models import * 

class TestResultSerializer(serializers.ModelSerializer):


    class Meta:
        model = TestResults
        fields = ['id', 'test_name', 'test_datetime', 'cell', 'vehicle_id', 'drivetrace', 'driver', 'engineer', 'iwr', 'rmsse', 'total_co', 'total_co2']


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['driver'] = instance.driver.first_name + " " + instance.driver.last_name  # or replace the name with your pricing name field
        data['vehicle_id'] = instance.vehicle_id.vehicle_id
        data['drivetrace'] = instance.drivetrace.drivetrace_name
        data['engineer'] = instance.engineer.first_name + " " + instance.engineer.last_name
        return data