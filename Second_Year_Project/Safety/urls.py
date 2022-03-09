from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app, name='safety-app'),
    path('reset_password/', views.reset_password, name='safety-reset-password'),
    path('confirm_reset/', views.confirm_reset, name='safety-conf-reset'),
    path('compenents/', views.compenents, name='safety-compenents'),
    path('intrue/', views.intrue, name='safety-intrue'),
    path('new_intrue/', views.new_intrue, name='safety-new-intrue'),
    path('manage_account/', views.manage_account, name='safety-manage-account'),
]
