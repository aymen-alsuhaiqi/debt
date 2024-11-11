from django.urls import path
from . import views
from .swagger import schema_view

urlpatterns = [
    path('api/v1/crud_customer/',views.cr_customer),
    path('api/v1/crud_customer/<int:cid>/',views.ud_customer),
    path('api/v1/crud_dept/<int:cid>/',views.crud_dept),
    path('api/v1/clear_depts/<int:cid>',views.clear_depts),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
