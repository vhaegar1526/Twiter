# Generated by Django 3.2.7 on 2021-09-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]