# Generated by Django 3.1.6 on 2021-04-06 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_voter_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='user_img',
            field=models.ImageField(default=None, upload_to='images/voters'),
        ),
    ]
