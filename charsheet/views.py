from django.shortcuts import render
from .models import Character

# Create your views here.
def char_list(request):
    char = Character.objects.order_by('char_name')    
    return render(request, 'charsheet/char_list.html', {'char':char})

def get_data(request):
    my_data = Character.objects.all()
    return render(request, 'charsheet/get_data.html', {'my_data':my_data})