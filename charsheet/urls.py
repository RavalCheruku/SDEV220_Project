from django.urls import path
from .views import char_list, get_data, char_detail, char_new, char_edit, char_delete

urlpatterns = [
    path('', char_list, name='char_list'),
    path('', get_data, name='get_data'),
    path('char/<int:pk>/', char_detail, name='char_detail'),
    path('char/new/', char_new, name='char_new'),
    path('char/<int:pk>/edit', char_edit, name='char_edit' ),
    path('char/<int:pk>/delete/', char_delete, name='char_delete')
]