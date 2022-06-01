# Generated by Django 2.1.7 on 2021-10-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_customer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]