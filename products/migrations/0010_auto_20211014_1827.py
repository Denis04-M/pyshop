# Generated by Django 2.1.7 on 2021-10-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20211014_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]