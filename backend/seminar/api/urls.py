from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('', views.list_papers, name='listcreate'),
    path('compute/', views.compute_linear_algebra_expression, name='compute'),
    ]
