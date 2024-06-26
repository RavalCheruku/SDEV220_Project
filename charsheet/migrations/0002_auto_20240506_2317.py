# Generated by Django 3.2.25 on 2024-05-07 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Strength', models.IntegerField()),
                ('Dexterity', models.IntegerField()),
                ('Constitution', models.IntegerField()),
                ('Intelligence', models.IntegerField()),
                ('Wisdom', models.IntegerField()),
                ('Charisma', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='character',
            old_name='alignment',
            new_name='Alignment',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='background',
            new_name='Background',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='char_class',
            new_name='Class',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='char_lvl',
            new_name='Level',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='char_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='char_race',
            new_name='Race',
        ),
        migrations.RemoveField(
            model_name='character',
            name='char_char',
        ),
        migrations.RemoveField(
            model_name='character',
            name='char_con',
        ),
        migrations.RemoveField(
            model_name='character',
            name='char_dex',
        ),
        migrations.RemoveField(
            model_name='character',
            name='char_int',
        ),
        migrations.RemoveField(
            model_name='character',
            name='char_str',
        ),
        migrations.RemoveField(
            model_name='character',
            name='char_wis',
        ),
    ]
