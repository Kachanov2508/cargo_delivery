from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['pick_up', 'deliver', 'weight', 'size', 'date', 'name', 'phone', 'email']
        widgets = {
            'pick_up': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Откуда забираем',}),
            'deliver': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Куда доставляем'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Вес', 'v-model': 'cargo_weight'}),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Объем', 'v-model': 'cargo_size'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
