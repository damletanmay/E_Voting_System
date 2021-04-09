# Generated by Django 3.2 on 2021-04-09 02:56

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_voter_voted_elections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='voted_elections',
            field=django_mysql.models.ListTextField(models.IntegerField(), blank=True, default=None, size=1000),
        ),
    ]