# Generated by Django 3.0.9 on 2020-09-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='Department',
            field=models.CharField(choices=[('ece', 'ECE'), ('cse', 'CSE'), ('it', 'IT')], default='ECE', max_length=10),
        ),
        migrations.AddField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
