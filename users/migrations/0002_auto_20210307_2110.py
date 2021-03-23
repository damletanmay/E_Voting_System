# Generated by Django 3.1.6 on 2021-03-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdatabase',
            name='city',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='district',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='fname',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='lname',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='mname',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='phone_no',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='state',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='taluka',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='village',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='userdatabase',
            name='user_img',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='userdatabase',
            name='voting_number',
            field=models.TextField(default=None),
        ),
    ]