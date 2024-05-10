from django import forms
from .models import Character

ALIGN_CHOICES=(
    ("Lawful Good","Lawful Good"),
    ("Lawful Neutral","Lawful Neutral"),
    ("Lawful Evil","Lawful Evil"),
    ("Neutral Good","Neutral Good"),
    ("True Neutral","True Neutral"),
    ("Neutral Evil","Neutral Evil"),
    ("Chaotic Good","Chaotic Good"),
    ("Chaotic Neutral","Chaotic Neutral"),
    ("Chaotic Evil","Chaotic Evil"),
)

BACK_CHOICES=(
    ("Acolyte","Acolyte"),
    ("Charlatan","Charlatan"),
    ("Criminal","Criminal"),
    ("Entertainer","Entertainer"),
    ("Folk Hero","Folk Hero"),
    ("Guild Artisan","Guild Artisan"),
    ("Hermit","Hermit"),
    ("Outlander","Outlander"),
    ("Noble","Noble"),
    ("Sage","Sage"),
    ("Sailor","Sailor"),
    ("Soldier","Soldier"),
    ("Urchin","Urchin"),
)

class CharacterForm(forms.ModelForm):
    Alignment = forms.ChoiceField(choices=ALIGN_CHOICES)
    Background = forms.TypedChoiceField(choices=BACK_CHOICES)

    class Meta:
        model = Character
        fields = ('Name', 'Race', 'Class', 'Background', 'Alignment', 'Level', 'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma',)
        




    