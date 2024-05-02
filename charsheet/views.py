from django.shortcuts import render
from .models import Character

# Create your views here.
def char_list(request):    
    return render(request, 'charsheet/char_list.html', {})

def get_data(request):
    my_data = Character.objects.all()
    return render(request, 'charsheet/get_data.html', {'my_data':my_data})