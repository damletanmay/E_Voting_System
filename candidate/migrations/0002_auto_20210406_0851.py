# Generated by Django 3.1.6 on 2021-04-06 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='party_leader',
            new_name='party_leader_name',
        ),
    ]