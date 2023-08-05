from rest_framework import serializers
from cdt_app.models import * 

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResults
        fields = ['id', 'test_name', 'test_datetime', 'cell', 'vehicle_id', 'drivetrace', 'engineer', 'iwr', 'rmsse', 'total_co', 'total_co2']