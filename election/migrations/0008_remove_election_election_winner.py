# Generated by Django 3.2 on 2021-04-10 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0007_alter_election_election_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='election_winner',
        ),
    ]
