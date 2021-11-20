from django.contrib import admin
from .models import Contact, Product,Checkout,Tracker,productComments,Cartrecord



class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','price','pub_date']

class CartdataAdmin(admin.ModelAdmin):
    list_display=['cart_user']

admin.site.register(Product,ProductAdmin)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(Tracker)
admin.site.register(productComments)
admin.site.register(Cartrecord,CartdataAdmin)