# Generated by Django 2.1.7 on 2021-11-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='items_sold',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='month',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]