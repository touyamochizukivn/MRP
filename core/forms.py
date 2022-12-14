
from django import forms
from core.models import *
 
 
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'

class ComponentTypeForm(forms.ModelForm):
    class Meta:
        model = ComponentType
        fields = '__all__'

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'
class QuotationLineForm(forms.ModelForm):
    class Meta:
        model = QuotationLine
        fields = ('product', 'price', 'quantity')


class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = '__all__'

class SaleOrderLineForm(forms.ModelForm):
    class Meta:
        model = SaleOrderLine
        fields = ('product', 'price', 'quantity')

from django.forms import MultipleChoiceField, Select, TextInput, modelformset_factory, inlineformset_factory
# QuotationLineFormSet = modelformset_factory(
#     QuotationLine, fields=('product', 'price', 'quantity'), extra=1
# )

QuotationLineFormSet = inlineformset_factory(Quotation, QuotationLine, max_num=2, fields=('__all__'), widgets={
    'product': Select(attrs={'class': 'form-control'}),
    'price': TextInput(attrs={'class': 'form-control'}),
    'quantity': TextInput(attrs={'class': 'form-control'}),
})
