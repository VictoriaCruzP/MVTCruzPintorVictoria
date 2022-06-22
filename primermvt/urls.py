from django.urls import path
from .views import inicio, fecha, mi_template

urlpatterns = [
    path('', inicio),
    path('fecha/', fecha),
    path('datos/', mi_template),
]