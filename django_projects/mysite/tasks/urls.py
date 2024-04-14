# tasks/urls.py
from django.urls import path
from .views import register_view, task_list, add_task, login_view, logout_view, delete_task, index_view, calendar_weather

urlpatterns = [
    path('', index_view, name='index'),
    path('task-list/', task_list, name='task_list'),
    path('add-task/', add_task, name='add_task'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('calendar/', calendar_weather, name='calendar')

]