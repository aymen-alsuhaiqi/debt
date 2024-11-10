from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *
# Create your views here.


@api_view(['GET', 'POST'])
def cr_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(request.data)
        print("__🔻🔻🔻__ ~ file: views.py:17 ~ serializer:", serializer)
        if serializer:
            data = request.data
            customer = Customer.objects.all().filter(name=data['name']).exists()
            if customer:
                return Response('This customer is already exists',status=401)
            serializer.create(request.data)
            return Response('The customer was created succesfuly', status=201)
        
    elif request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data, status=200)