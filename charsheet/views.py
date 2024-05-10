from django.shortcuts import render, get_object_or_404, redirect
from .models import Character
from .forms import CharacterForm

# Create your views here.
def char_list(request):
    char = Character.objects.order_by('Name')    
    return render(request, 'charsheet/char_list.html', {'char':char})

def get_data(request):
    my_data = Character.objects.all()
    return render(request, 'charsheet/get_data.html', {'my_data':my_data})

def char_detail(request, pk):
    char = get_object_or_404(Character, pk=pk)
    proficiency_modifier= calculate_proficiency_modifier(char.Level)
    saving_throws = [
        {"name": "Strength", "default_value": char.Strength},
        {"name": "Dexterity", "default_value": char.Dexterity},
        {"name": "Constitution", "default_value": char.Constitution},
        {"name": "Intelligence", "default_value": char.Intelligence},
        {"name": "Wisdom", "default_value": char.Wisdom},
        {"name": "Charisma", "default_value": char.Charisma},
    ]
    skills = [
        {"name":"Acrobatics", "ability": char.Dexterity},
        {"name":"Animal Handling", "ability": char.Wisdom},
        {"name":"Arcana", "ability": char.Intelligence},
        {"name":"Athletics", "ability": char.Strength},
        {"name":"Deception", "ability": char.Charisma},
        {"name":"History", "ability": char.Intelligence},
        {"name":"Insight", "ability": char.Wisdom},
        {"name":"Intimidation", "ability": char.Charisma},
        {"name":"Investigation", "ability": char.Intelligence},
        {"name":"Medicine", "ability": char.Wisdom},
        {"name":"Nature", "ability": char.Intelligence},
        {"name":"Perception", "ability": char.Wisdom},
        {"name":"Performance", "ability": char.Charisma},
        {"name":"Persuasion", "ability": char.Charisma},
        {"name":"Religion", "ability": char.Intelligence},
        {"name":"Sleight of Hand", "ability": char.Dexterity},
        {"name":"Stealth", "ability": char.Dexterity},
        {"name":"Survival", "ability": char.Wisdom},
    ]
    print("Proficiency Modifier:", proficiency_modifier)
    return render(request, 'charsheet/char_detail.html', {'char': char, 'saving_throws': saving_throws, 'proficiency_modifier': proficiency_modifier, 'skills': skills})

def calculate_proficiency_modifier(level):
    if level < 5:
        return 2
    elif level < 9:
        return 3
    elif level < 13:
        return 4
    elif level < 17:
        return 5
    else:
        return 6

def char_new(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            char = form.save()
            return redirect('char_list')
            
        else:
            print("POST data:", request.POST)
            print(form.errors)
    else:
        form = CharacterForm()
    return render(request, 'charsheet/char_new.html', {'form':form})

def char_edit(request, pk):
    char = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        form = CharacterForm(request.POST, instance=char)
        if form.is_valid():
            char = form.save()
            return redirect('char_detail', pk=char.pk)
    else:
        form = CharacterForm(instance=char)
    return render(request, 'charsheet/char_new.html', {'form': form})

def char_delete(request, pk):
    char = get_object_or_404(Character, pk=pk)
    char.delete()
    return redirect('char_list')


    
