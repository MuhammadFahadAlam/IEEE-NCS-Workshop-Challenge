# Generated by Django 3.1.4 on 2021-05-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('country', models.CharField(default='Pakistan', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=30)),
                ('date', models.DateField()),
                ('country', models.CharField(default='Pakistan', max_length=30)),
                ('contact', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='user', max_length=100)),
                ('Email', models.CharField(default='email', max_length=50)),
                ('Subject', models.CharField(default='subject', max_length=100)),
                ('Message', models.CharField(default='message', max_length=500)),
            ],
        ),
    ]
