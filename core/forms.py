
from django import forms
from core.models import *
 
 
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
        fields = ['date', ]


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['customer', 'is_canceled']

class StatementLineForm(forms.ModelForm):
    class Meta:
        model = StatementLine
        fields = ['product', 'price', 'quantity', ]