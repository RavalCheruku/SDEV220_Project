from django.db import models

# Create your models here.
class Character(models.Model):
    Name = models.CharField(max_length=50)
    Race = models.CharField(max_length=30)
    Class = models.CharField(max_length=30)
    Level = models.PositiveIntegerField()
    Background = models.CharField(max_length=30)
    Alignment = models.CharField(max_length=30)
    Strength = models.IntegerField(null=True)
    Dexterity = models.IntegerField(null=True)
    Constitution = models.IntegerField(null=True)
    Intelligence = models.IntegerField(null=True)
    Wisdom = models.IntegerField(null=True)
    Charisma = models.IntegerField(null=True)

#function to make the name of the object as the character name
    def __str__(self):
        return self.Name
    

