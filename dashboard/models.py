from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    user = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to = "images/")
    title = models.CharField(max_length=30, blank=True, null=True)
    colors = models.CharField(max_length=200, default='white')
    view_color = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField()
    mockupImg = models.ImageField(null=True, blank=True, upload_to = "images/")
    mockupImgPink = models.ImageField(null=True, blank=True, upload_to = "images/")
    mockupDataPink = models.TextField(blank=True)
    mockupImgBlue = models.ImageField(null=True, blank=True, upload_to = "images/")
    mockupImgPurple = models.ImageField(null=True, blank=True, upload_to = "images/")
    mockupImgGrey = models.ImageField(null=True, blank=True, upload_to = "images/")
    mockupImgBrown = models.ImageField(null=True, blank=True, upload_to = "images/")
    mockupData = models.TextField(blank=True)