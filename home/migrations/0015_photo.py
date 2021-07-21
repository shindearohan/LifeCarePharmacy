# Generated by Django 3.2 on 2021-05-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
            ('home', '0010_alter_update_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medical_Name', models.CharField(default='', max_length=50)),
                ('Medicine_Name', models.CharField(max_length=50)),
                ('No_of_strips', models.CharField(max_length=12)),
                ('NO_of_medicine', models.CharField(max_length=12)),
                ('photo', models.ImageField(upload_to='photoimage')),
            ],
        ),
    ]
