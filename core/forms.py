
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
        fields = '__all__'


class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = '__all__'

class SaleOrderLineForm(forms.ModelForm):
    class Meta:
        model = SaleOrderLine
        fields = '__all__'

from django.forms import modelformset_factory, inlineformset_factory
# QuotationLineFormSet = modelformset_factory(
#     QuotationLine, fields=('product', 'price', 'quantity'), extra=1
# )

QuotationLineFormSet = inlineformset_factory(Quotation, QuotationLine, fields=('__all__'))