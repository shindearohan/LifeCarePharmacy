# Generated by Django 3.2 on 2021-05-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20210508_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('contact_number', models.IntegerField(blank=True, unique=True)),
                ('feedback', models.CharField(max_length=250)),
                ('suggestions', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
