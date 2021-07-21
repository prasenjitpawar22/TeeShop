# Generated by Django 3.2.5 on 2021-07-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_product_mockupdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mockupImgBlue',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='mockupImgBrown',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='mockupImgGrey',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='mockupImgPink',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='mockupImgPurple',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]