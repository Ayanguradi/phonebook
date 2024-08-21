from django import forms
from .models import Shop, ShopImage, Category, Subcategory

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'category',
            'subcategory',
            'name',
            'address',
            'phone_number',
            'email',
            'website',
            'description',
            'opening_hours',
        ]

class ShopImageForm(forms.ModelForm):
    class Meta:
        model = ShopImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False





# from django import forms
# from .models import Shop, ShopImage

# class ShopForm(forms.ModelForm):
#     class Meta:
#         model = Shop
#         fields = [
#             'category',
#             'subcategory',
#             'name',
#             'address',
#             'phone_number',
#             'email',
#             'website',
#             'description',
#             'opening_hours',
#         ]

# class ShopImageForm(forms.ModelForm):
#     class Meta:
#         model = ShopImage
#         fields = ['image']
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['image'].required = False



