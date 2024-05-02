from django.db import models

# Create your models here.
class Character(models.Model):
    char_name = models.CharField(max_length=50)
    char_race = models.CharField(max_length=30)
    char_class = models.CharField(max_length=30)
    char_lvl = models.PositiveIntegerField()
    background = models.CharField(max_length=30)
    alignment = models.CharField(max_length=30)
    char_str = models.IntegerField()
    char_dex = models.IntegerField()
    char_con = models.IntegerField()
    char_int = models.IntegerField()
    char_wis = models.IntegerField()
    char_char = models.IntegerField()

#function to make the name of the object as the character name
    def __str__(self):
        return self.char_name
