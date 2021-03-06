# Generated by Django 3.2 on 2021-05-23 18:15

from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210523_1447'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='stock',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, default= django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='no_of_med',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='no_of_strips',
            field=models.CharField(default='', max_length=50),
        ),
    ]
