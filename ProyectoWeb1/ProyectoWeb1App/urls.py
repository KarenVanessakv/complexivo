from django.urls import path
from ProyectoWeb1App import views

urlpatterns = [
    path('', views.home, name="Home"),

]
