from django.urls import path, include
from tweet import views

urlpatterns = [
    path('', views.index, name='index'),
]
