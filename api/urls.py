from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/cr/',views.crud_customer),
    path('api/v1/cr/<int:cid>/',views.crud_customer),
    path('api/v1/crud_dept/<int:cid>/',views.crud_dept),
]
