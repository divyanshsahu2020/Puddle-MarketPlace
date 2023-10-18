from django import forms
from .models import Item
input_class='w-full py-4 py-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','Name','Description','price','image')
        widgets={
            'category':forms.Select(attrs={
                'class':'w-full py-4 py-6 rounded-xl border'
            }),
            'Name':forms.TextInput(attrs={
                'class':input_class
            }),
            'Description':forms.TextInput(attrs=
                                          {
                                              'class':input_class
                                          }),
            'price':forms.TextInput(attrs={
                'class':input_class
            }),
            'image':forms.FileInput(attrs={
                'class':input_class
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','Name','Description','price','image','is_sold')
        widgets={
            'category': forms.Select(attrs={
                'class': 'w-full py-4 py-6 rounded-xl border'
            }),
            'Name':forms.TextInput(attrs={
                'class':input_class
            }),
            'Description':forms.TextInput(attrs=
                                          {
                                              'class':input_class
                                          }),
            'price':forms.TextInput(attrs={
                'class':input_class
            }),
            'image':forms.FileInput(attrs={
                'class':input_class
            })
        }