# Generated by Django 3.1.7 on 2021-06-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20210610_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accbill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('Medicine_Name', models.CharField(max_length=50)),
                ('No_of_strips', models.CharField(max_length=12)),
                ('NO_of_medicine', models.CharField(max_length=12)),
                ('mednameprice', models.CharField(max_length=50)),
                ('stripsprice', models.CharField(max_length=12)),
                ('nomedprice', models.CharField(max_length=12)),
                ('total', models.CharField(max_length=12)),
            ],
        ),
        
    ]