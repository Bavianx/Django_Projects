from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='JobTasks'),
    path('update/<int:pk>/', views.update_job, name='updated_job'),
]
    
