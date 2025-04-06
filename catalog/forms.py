from django import forms
from .models import Product


# class ProductForm(forms.ModelForm):
#     new_category_name = forms.CharField(
#         max_length=100,
#         required=False,
#         label='Новая категория',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите новую категорию (если нужная категория отсутствует)',
#         }),
#         help_text='Заполните это поле, если нужной категории нет в списке'
#     )
#
#     class Meta:
#         model = Product
#         fields = ['category', 'name', 'description', 'price', 'image']
#         widgets = {
#             'category': forms.Select(attrs={'class': 'form-control'}),
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название продукта'
#             }),
#             'description': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите описание продукта',
#                 'rows': 3
#             }),
#             'price': forms.NumberInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите цену продукта',
#                 'step': '0.01'
#             }),
#             'image': forms.ClearableFileInput(attrs={
#                 'class': 'form-control'
#             })
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Гарантируем, что у всех полей будут id
#         self.auto_id = 'id_%s'
#
# from django import forms
# from .models import Product


# class ProductForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.auto_id = 'id_%s'  # Явное указание формата ID
# Временное решение в forms.py
# class ProductForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name in self.fields:
#             self.fields[field_name].widget.attrs['id'] = f'id_{field_name}'
#
#         # Унифицированные классы для всех полей
#         for field_name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'form-control'})
#
#             if field_name == 'description':
#                 field.widget.attrs.update({'rows': 3})
#             elif field_name == 'price':
#                 field.widget.attrs.update({'step': '0.01'})
#
#     new_category_name = forms.CharField(
#         required=False,
#         label="Новая категория (если нет в списке)",
#         help_text="Оставьте пустым, если выбираете существующую категорию"
#     )
#
#     class Meta:
#         model = Product
#         fields = ['category', 'new_category_name', 'name', 'description', 'price', 'image']
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    new_category_name = forms.CharField(
        required=False,
        label="Новая категория",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_new_category_name'  # Явное задание ID
        })
    )

    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image']

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_category'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'id_description',
                'rows': 3
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'id_price',
                'step': '0.01'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'id_image'
            })
        }