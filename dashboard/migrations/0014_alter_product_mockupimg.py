# Generated by Django 3.2.5 on 2021-07-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_product_mockupimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mockupImg',
            field=models.ImageField(blank=True, default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]
