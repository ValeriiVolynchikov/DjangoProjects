from django.contrib import admin
from django.core.exceptions import ValidationError
from catalog.models import Category, Product, Contact
from .forms import ProductForm


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ("id", "name", "price", "category", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "description")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone")
    search_fields = ("name", "phone", "email")
