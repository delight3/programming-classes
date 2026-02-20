from django.urls import path
from . import views

urlpatterns =[
    path('', views.greeting, name='greeting'),
    path('index/', views.index, name='index'),
    path('index/details/<int:id>', views.details, name='details'),
    path('about/', views.about, name='about'),
] 