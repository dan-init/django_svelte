from django.contrib import admin
from .models import Vehicle, Driver, Drivetrace, Engineer, TestResults, Cell

# Register your models here.
admin.site.register(Cell)
admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(Drivetrace)
admin.site.register(Engineer)
admin.site.register(TestResults)