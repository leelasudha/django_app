# Generated by Django 3.0.9 on 2020-09-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_remove_faculty_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='Department',
            field=models.CharField(choices=[('ece', 'ECE'), ('cse', 'CSE'), ('it', 'IT')], default='----', max_length=10),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='mobile',
            field=models.CharField(help_text='Enter 10 digit number', max_length=10),
        ),
    ]
