from django.urls import path
from .views import dropdown_view
from . import views

urlpatterns = [
    path('', views.dropdown_view,name='list'),
    
]
