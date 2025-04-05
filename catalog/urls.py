from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_info, add_product, edit_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path("product_info/<int:pk>/", product_info, name="product_info"),
    path("add_product/", add_product, name="add_product"),
    path('edit-product/<int:pk>/', edit_product, name='edit_product'),
]
