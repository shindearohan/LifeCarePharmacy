# Generated by Django 3.1.7 on 2021-05-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=12)),
                ('re_password', models.TextField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=40),
        ),
    ]
