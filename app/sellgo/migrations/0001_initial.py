# Generated by Django 3.1.1 on 2020-09-30 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CsvProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_date', models.DateTimeField(auto_created=True, editable=False)),
                ('title', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellgo.customer')),
            ],
        ),
    ]
