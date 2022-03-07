from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='safety-home'),
    path('app/', views.app, name='safety-app'),
    path('compenents/', views.compenents, name='safety-compenents'),
    path('intrue/', views.intrue, name='safety-intrue'),
    path('new_intrue/', views.new_intrue, name='safety-new-intrue'),
]