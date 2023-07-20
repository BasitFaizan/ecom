from django.contrib import admin
from productpage.models import products
# Register your models here.


class ProductAdmin(admin.ModelAdmin):  # new
    readonly_fields = ['img_preview']


admin.site.register(products,ProductAdmin)
