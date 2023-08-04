from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.vehicle_id

class Engineer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
        
class Drivetrace(models.Model):
    drivetrace_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.drivetrace_name
    
class TestResults(models.Model):
    test_name = models.CharField(max_length=255)
    test_datetime = models.DateTimeField()
    cell = models.CharField(max_length=5)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    drivetrace =models.ForeignKey(Drivetrace, on_delete=models.SET_NULL, null=True)
    engineer = models.ForeignKey(Engineer, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    iwr = models.DecimalField(max_digits=19, decimal_places=9)
    rmsse = models.DecimalField(max_digits=19, decimal_places=9)
    total_co = models.DecimalField(max_digits=19, decimal_places=9)
    total_co2 = models.DecimalField(max_digits=19, decimal_places=9)

    def __str__(self) -> str:
        return self.test_name