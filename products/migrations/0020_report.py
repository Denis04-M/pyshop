# Generated by Django 2.1.7 on 2021-11-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('month', models.ImageField(blank=True, null=True, upload_to='')),
                ('items_sold', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
