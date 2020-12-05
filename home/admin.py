from django.contrib import admin
from .models import product,new_models


class product_admin(admin.ModelAdmin):
    list_display=['name','price','image','detail','offer','price']

class new_admin(admin.ModelAdmin):
    list_display=['item','img','description','money','discount']


# Register your models here.
admin.site.register(product,product_admin),
admin.site.register(new_models,new_admin)
