# Generated by Django 3.1.6 on 2021-04-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_auto_20210406_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party_logo',
            field=models.ImageField(default=None, upload_to='candidates/'),
        ),
    ]