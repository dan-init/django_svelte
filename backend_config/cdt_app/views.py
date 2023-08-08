from django.shortcuts import render
from django.http import HttpResponse
from .models import TestResults
from .filters import TestResultsFilter
# Create your views here.

def home(request):
    
    test_result = TestResults.objects.all()
    myFilter = TestResultsFilter(request.GET, queryset=test_result)
    test_result = myFilter.qs

    context = {'test_result': test_result, 'myFilter':myFilter}
    
    return render(request, 'cdt_app.html', context)