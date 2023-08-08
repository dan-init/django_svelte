from django.shortcuts import render
from django.http import HttpResponse
from .models import TestResults
# Create your views here.

def home(request):
    test_result = TestResults.objects.all()
    return render(request, 'cdt_app.html', {'test_result':test_result})