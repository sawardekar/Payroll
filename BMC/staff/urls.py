from django.urls import path, include
from staff import views
from staff import api_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('emp', views.emp, name='emp'),
    path('logout', views.user_logout, name='logout'),
    path('emp_create', api_views.EmployeeAPI.as_view()),
    path('emp_create/<int:pk>', api_views.EmployeeAPI.as_view()),
    ]