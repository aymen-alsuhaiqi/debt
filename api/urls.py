from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/crud_customer/',views.crud_customer),
    path('api/v1/crud_customer/<int:cid>/',views.crud_customer),
    path('api/v1/crud_dept/<int:cid>/',views.crud_dept),
    path('api/v1/clear_depts/<int:cid>',views.clear_depts),
]
