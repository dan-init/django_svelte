from cdt_app.models import *
from django.http import JsonResponse
from cdt_app.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets


class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResults.objects.all()
    serializer_class = TestResultSerializer

@api_view(['GET'])
def test_result_list(request):

    if request.method == 'GET':
        test_results = TestResults.objects.all()
        serializer = TestResultSerializer(test_results, many = True)
        return Response(serializer.data)
    
@api_view(['GET'])
def test_result_detail(request, id):

    try:    
        test_result = TestResults.objects.get(pk=id)
    except TestResults.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TestResultSerializer(test_result)
        return Response(serializer.data)