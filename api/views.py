from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ImageModel
from .serializers import ImageModelSerializer

# Create your views here.
from GestureLearner import *


class ImageModelAPIView(APIView):
    def get(self, request):
        mymodels = ImageModel.objects.all()
        serializer = ImageModelSerializer(mymodels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = self.make_predict(serializer.data.image)
            return Response(result, status=201)
        return Response(serializer.errors, status=400)
    
    def make_predict(self, data):
        return predict(data)
    

def make_predict(request):
    if request.method == 'POST':
        binary_data = request.body
        result = predict(binary_data)
        return HttpResponse(result)