from django import forms
from .models import Character

ALIGN_CHOICES=(
    ("1","Lawful Good"),
    ("2","Lawful Neutral"),
    ("3","Lawful Evil"),
    ("4","Neutral Good"),
    ("5","True Neutral"),
    ("6","Neutral Evil"),
    ("7","Chaotic Good"),
    ("8","Chaotic Neutral"),
    ("9","Chaotic Evil"),
)

BACK_CHOICES=(
    ("1","Acolyte"),
    ("2","Charlatan"),
    ("3","Criminal"),
    ("4","Entertainer"),
    ("5","Folk Hero"),
    ("6","Guild Artisan"),
    ("7","Hermit"),
    ("8","Outlander"),
    ("9","Noble"),
    ("10","Sage"),
    ("11","Sailor"),
    ("12","Soldier"),
    ("13","Urchin"),
)

class CharacterForm(forms.ModelForm):
    Alignment = forms.ChoiceField(choices=ALIGN_CHOICES)
    Background = forms.TypedChoiceField(choices=BACK_CHOICES)

    class Meta:
        model = Character
        fields = ('Name', 'Race', 'Class', 'Background', 'Alignment', 'Level', 'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma',)
        




    