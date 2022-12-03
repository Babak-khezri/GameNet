from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('employee_list/', views.employee_list_view, name='employee_list'),
    path('forget_password/', views.forget_password_view, name='forget_password'),
]
