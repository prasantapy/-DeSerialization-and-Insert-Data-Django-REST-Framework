from django.shortcuts import render
import io
from .serializers import Student_serializers
from rest_framework.parsers import JSONParser
from django.http  import HttpResponse
from rest_framework .renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method =='POST':
        json_data = request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=Student_serializers(data=pythondata)
    
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data create'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')