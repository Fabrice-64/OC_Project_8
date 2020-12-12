from django.contrib import admin
from .models import Store, Product, Category
# Register your models here.

@admin.register(Store)
class AdminStore(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

    actions = ['download_products']
    def download_products(self, request, queryset):
        pass
    download_products.short_description = "Populate the DB with Products"


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'brand', 'code', 'nutrition_score')
    ordered = ('name',)
    
    


