from django.contrib import admin
from .models import *

# Register your models here.
class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra=1

class ProductInline(admin.StackedInline):
    model = Product
    extra= 1

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering= ['name']
    inlines=[SubCategoryInline, ProductInline]

class ProductImageInline(admin.StackedInline):
    model=ProductImage

class CommentInline(admin.StackedInline):
    model=Comments


class ProductModelAdmin(admin.ModelAdmin):
    list_display=["name",]
    inlines=[ProductImageInline, CommentInline]
    
    @admin.display(description="Is Available", boolean=True)
    def available(self, obj):
        return (obj.total_products<obj.sold_products)
    
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(SubCategory)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(ProductImage)
admin.site.register(Comments)
admin.site.register(Rating)
admin.site.register(ColorVarient)
admin.site.register(SizeVarient)
