
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