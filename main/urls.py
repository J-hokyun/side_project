from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name  ='home'),
    path('find/', views.FindView.as_view(), name  ='find'),
    path('health_check/', views.health_check, name='health_check'),
]
