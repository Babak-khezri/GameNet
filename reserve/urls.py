from django.urls import path
from . import views

app_name = 'reserve'

urlpatterns = [
    path('reserve_system',views.reserve_system_view,name='reserve_system'),
    path('close_time/<int:pk>',views.close_time_view,name='close_time'),
    path('calc_total_cost/<int:pk>',views.calc_total_cost,name='calc_total_cost'),
]
