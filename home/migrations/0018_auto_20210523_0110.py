# Generated by Django 3.2 on 2021-05-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210523_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm', models.CharField(max_length=20)),
                ('feedback', models.CharField(max_length=50)),
                ('suggetion', models.CharField(max_length=50)),
            ],
        ),
        
    ]
