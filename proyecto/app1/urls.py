from django.urls import path
#from .views import listar_carrera
from . import views

urlpatterns = [
    path('carreras/', views.listar_carrera)
] 