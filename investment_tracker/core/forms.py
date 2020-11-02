from django import forms
from .models import Investment, Product, Expense

class InvestmentForm(forms.ModelForm):

    class Meta:
        model = Investment
        fields = '__all__'

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = '__all__'