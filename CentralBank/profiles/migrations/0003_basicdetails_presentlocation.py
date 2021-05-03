# Generated by Django 3.2 on 2021-05-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210330_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('sex', models.CharField(default=None, max_length=1)),
                ('annual_income', models.IntegerField(default=0)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('mobile', models.IntegerField(default=0)),
                ('occupation', models.CharField(default=None, max_length=50)),
                ('DOB', models.DateField(default=None)),
                ('user_name', models.CharField(default=None, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PresentLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='India', max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('user_name', models.CharField(default=None, max_length=150)),
            ],
        ),
    ]
