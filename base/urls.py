from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index),
    path('data', views.testdata),
    path('gallery', views.imgView.as_view()),

]
