# Generated by Django 3.2 on 2021-05-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_stock_companyname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medname', models.CharField(max_length=50)),
                ('companyname', models.CharField(max_length=50)),
                ('batchno', models.CharField(max_length=20)),
                ('mfd', models.DateField()),
                ('exd', models.DateField()),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
    ]
