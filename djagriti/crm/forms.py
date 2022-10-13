import phonenumbers
from django import forms

from crm.models import *


class OrderForm(forms.ModelForm):
    # def __int__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['order_napr'].empty_label = "ВЛвллв"

    class Meta:
        model = Order
        fields = ['order_name', 'order_phone', 'order_napr', 'order_price', 'date']
        widgets = {
            'order_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя', 'pattern': '^[А-Яа-яЁё\s]+$', "title": "Только кириллические символы"}),
            'order_phone': forms.TextInput(
                attrs={'type': 'tel', 'class': 'form-control', 'placeholder': 'Номер телефона'}),
            'order_napr': forms.Select(attrs={'class': 'form-select'}),
            'order_price': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Дата и время'})
        }

    def clean_order_phone(self):
        phone_number = self.cleaned_data.get("order_phone")
        z = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(z):
            raise forms.ValidationError("Такого номера телефона не существует")
        return phone_number
