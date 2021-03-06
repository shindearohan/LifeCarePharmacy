# Generated by Django 3.2 on 2021-06-01 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20210530_2129'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='photo',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
