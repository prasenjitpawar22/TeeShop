# Generated by Django 3.2.5 on 2021-07-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20210714_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mockupImg',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
