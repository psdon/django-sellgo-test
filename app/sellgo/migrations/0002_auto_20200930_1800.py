# Generated by Django 3.1.1 on 2020-09-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellgo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvproduct',
            name='uploaded_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
