from django import forms
from django.forms import ModelForm, TextInput, FileInput, NumberInput
from .models import Product


#form for design page
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = (
        'name', 'user',
        'title', 'image',
        'colors', 'view_color',
        'price', 'mockupImg',
        'mockupImgPink', 'mockupDataPink', 
        'mockupImgPurple',
        'mockupImgBlue', 'mockupImgGrey',
        'mockupImgBrown', 'mockupData'
        )

        widgets = {
            'name': TextInput(attrs={
                'id': 'product-name',
                'value': 't-shirt'
            }),
            'user': TextInput(attrs={
                'id': 'user-name',
                'value': 'user'
            }),
            'image': FileInput(attrs={
                'id':"upload_file",
                'required': 'True'
            }),
            'title': TextInput(attrs={
                'id':"product-title",
                'required': 'True',
                'autocomplete':'off'
            }),
            'colors': TextInput(attrs={
                'id':"product_colors",
            }),
            'view_color': TextInput(attrs={
                'id':"main-product-color",
            }),
            'price': NumberInput(attrs={
                'class':"price-input",
                'id':"price_input",
                'min':'500'
            }),
            'mockupImg': FileInput(attrs={
                'class':"mockup-input",
                'id':"mockup_input",
                # 'required':'Flase'
            }),
            'mockupImgPink': FileInput(attrs={
                'class':"mockup-input",
                'id':"mockupPink_input",
                # 'required':'Flase'
            }),
            'mockupImgPurple': FileInput(attrs={
                'class':"mockup-input",
                'id':"mockupPurple_input",
                # 'required':'Flase'
            }),
            'mockupImgGrey': FileInput(attrs={
                'class':"mockup-input",
                'id':"mockupGrey_input",
                # 'required':'Flase'
            }),
            'mockupImgBlue': FileInput(attrs={
                'class':"mockup-input",
                'id':"mockupBlue_input",
                # 'required':'Flase'
            }),
            'mockupImgBrown': FileInput(attrs={
                'class':"mockup-input",
                'id':"mockupBrown_input",
                # 'required':'Flase'
            }),
            'mockupDataPink': TextInput(attrs={
                'class':"mockup-data",
                'id':"mockup_dataPink",
                # 'required':'Flase'
            }),
            'mockupData': TextInput(attrs={
                'class':"mockup-data",
                'id':"mockup_data",
                # 'required':'Flase'
            }),
        }
#form for create page
# class CreatePageForm(forms.Form):
#     Product_title = forms.CharField(widget=TextInput(attrs={'class':'product-title'}))