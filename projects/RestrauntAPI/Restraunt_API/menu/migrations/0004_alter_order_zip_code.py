# Generated by Django 3.2.7 on 2022-06-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]