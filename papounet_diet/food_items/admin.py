from django.contrib import admin
from .models import Store, Product, Category
# Register your models here.

@admin.register(Store)
class AdminStore(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

    actions = ['download_stores']
    def download_stores(self, request, queryset):
        download_stores.short_description = "Populate the DB with Stores"
        queryset.create(name="Cora")
        queryset.save()




@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'brand', 'code', 'nutrition_score')
    ordered = ('name',)


admin.site.register(Category)