# Generated by Django 3.1.6 on 2021-03-07 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210307_2113'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voters',
            new_name='Voter',
        ),
    ]