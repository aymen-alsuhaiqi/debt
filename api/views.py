from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *
# Create your views here.


@api_view(['GET', 'POST','PATCH','DELETE'])
def crud_customer(request,cid=None):
    if request.method == 'POST':
        serializer = CustomerSerializer(request.data)
        if serializer:
            data = request.data
            customer = Customer.objects.all().filter(name=data['name']).exists()
            if customer:
                return Response('This customer is already exists',status=401)
            serializer.create(request.data)
            new_customer = CustomerSerializer(Customer.objects.get(name=request.data['name']))

            print("__🔻🔻🔻__ ~ file: views.py:20 ~ new_customer:", new_customer)
            return Response({
                                'message':'The customer was created successfully',
                                'response':new_customer.data,
                             }, status=201)
        
    elif request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'PATCH':
        if not cid:
            return Response('Customer ID is required', status=400)
        try:
            customer = Customer.objects.get(id=cid)
        except Exception as e:
            return Response('Customer not found', status=404)
        serializer = CustomerSerializer(customer)
        if serializer:
            try:
                is_exists = None
                is_exists = Customer.objects.get(name=request.data['name'])
            except Exception as e:
                pass
            if is_exists and is_exists != customer:
                return Response('This customer is already exists', status=401)
            serializer.update(customer,request.data)
            return Response({
                                'message':'Customer updated successfully',
                                'response':serializer.data,
                             }, status=200)
        return Response('Customer not found', status=404)
    elif request.method == 'DELETE':
        if not cid:
            return Response('Customer ID is required', status=400)
        customer = Customer.objects.get(id=cid)
        customer.delete()
        return Response('Customer deleted successfully', status=204)
    
@api_view(['POST', 'GET'])
def crud_dept(request,cid=None):
    if request.method == 'POST':
        serializer = DeptSerializer(request.data)
        if serializer:
            try:
                customer = Customer.objects.get(id=cid)
            except Exception as e:
                return Response('Customer not found', status=404)
            data = {
                    'customer': customer,
                    'amount': request.data['amount']
                }        
            serializer.create(data)
            return Response('The department was created successfully', status=201)
    elif request.method == 'GET':
        try:
            customer = Customer.objects.get(id=cid)
        except Exception as e:
            return Response('Customer not found', status=404)
        depts = Dept.objects.all().filter(customer=customer)
        serializer = DeptSerializer(depts, many=True)
        total = 0
        for dept in depts:
            total += dept.amount
        data = {
            'customer':customer.name,
            'total': total,
            'depts':serializer.data,
        }
        return Response(data, status=200)
    