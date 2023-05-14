from django.contrib import admin
from .models import Category,Products

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated','category','store','location']
    list_editable = ['price','available','stock','category']
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Products,ProductAdmin)

# Register your models here.
