from django.urls import path
from .views import char_list, get_data

urlpatterns = [
    path('', char_list, name='char_list'),
    path('', get_data, name='get_data'),
]