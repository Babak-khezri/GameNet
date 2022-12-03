from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('system_list',views.system_list_view,name='system_list'),
    path('system_update/<pk>',views.SystemUpdateView.as_view(),name='system_update'),
    path('system_delete/<pk>',views.system_delete_view,name='system_delete'),
]
