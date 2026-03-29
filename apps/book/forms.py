from django import forms
from .models import Book, Catagory


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CatagoryFrom(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = '__all__'
