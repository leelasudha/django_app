# Generated by Django 3.0.9 on 2020-09-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Branch', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Join_Date', models.DateField()),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
    ]
