from django.shortcuts import render
from django.http import HttpResponse

from .models import ImageModel
from .serializers import ImageModelSerializer

# Create your views here.
from GestureLearner import *
    

def make_predict(request):
    if request.method == 'POST':
        binary_data = request.body
        result = predict(binary_data)
        return HttpResponse(result)