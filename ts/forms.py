from django.forms import ModelForm, inlineformset_factory

from .models import Child, Parent

ChildrenFormset = inlineformset_factory(Parent, Child, fields=('name',))