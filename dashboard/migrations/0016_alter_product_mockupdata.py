# Generated by Django 3.2.5 on 2021-07-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20210714_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mockupData',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]