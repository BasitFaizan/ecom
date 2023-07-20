from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class products(models.Model):
    prod_ids = models.IntegerField()
    prod_name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    prod_desc = models.TextField()
    prod_img_1 = models.ImageField(upload_to="prodImg")
    prod_img_2 = models.ImageField(upload_to="prodImg")
    prod_img_3 = models.ImageField(upload_to="prodImg")
    category = models.CharField(max_length=10)
    subCategory = models.CharField(max_length=10,default='')

    def __str__(self):
        return self.prod_name
    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.product_img.url}" width = "300"/>')