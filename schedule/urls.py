from django.urls import path
from .views import schedule_list, add_schedule, delete_schedule, add_route, edit_schedule, add_stop

urlpatterns = [
    path('', schedule_list, name='schedule_list'),
    path('add/', add_schedule, name='add_schedule'),
    path('add/route/', add_route, name='add_route'),
    path('delete/schedule/<int:schedule_id>/', delete_schedule, name='delete_schedule'),
    path('edit/schedule/<int:schedule_id>/', edit_schedule, name='edit_schedule'),
    path('add/stop/', add_stop, name='add_stop'),
]