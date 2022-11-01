from django.shortcuts import redirect, render
from django.views.generic import *
from django.db import transaction
from django.urls import reverse
from .forms import *
from .models import *


class ParentList(ListView):
    model = Parent


class ParentCreate(CreateView):
    template_name= 'parent_form.html'
    model = Parent
    fields = ['name']

    def get_success_url(self):
        return reverse('ts')

    def get_context_data(self):
        context = super().get_context_data()
        if self.request.POST:
            context['children'] = ChildrenFormset(self.request.POST)
        else:
            context['children'] = ChildrenFormset()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        children = context['children']
        with transaction.atomic():
            self.object = form.save()
            if children.is_valid():
                children.instance = self.object
                children.save()
        return super().form_valid(form)

