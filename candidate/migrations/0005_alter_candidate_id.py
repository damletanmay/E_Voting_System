# Generated by Django 3.2 on 2021-04-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0004_alter_candidate_party_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]