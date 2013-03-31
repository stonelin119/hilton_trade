from django.contrib import admin

from product.models import ProductCategory, ProductInfo, ProductInfoDetail, ProductType 

class ProductTypeInline(admin.TabularInline):
	model = ProductType

class ProductCategoryAdmin(admin.ModelAdmin):
	inlines = [ProductTypeInline]

class ProductInfoDetailInline(admin.TabularInline):
	model = ProductInfoDetail

class ProductInfoAdmin(admin.ModelAdmin):
	inlines = [ProductInfoDetailInline]

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
