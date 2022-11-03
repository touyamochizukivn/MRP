from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import *
from django.urls import reverse

from core.models import *
from core.forms import *


def dashboard(request):
    return render(request, 'dashboard.html')

###################################################################################################
def component_list(request):
    return render(request, "component/list.html", {'components': Component.objects.all()})

def component_detail(request, id):
    return render(request, "component/detail.html", {'component': Component.objects.get(id=id)})

def component_add(request):
    form = ComponentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/component/list')
    return render(request, "component/add.html", {'form': form})

def component_edit(request, id):
    obj = get_object_or_404(Component, id=id)
    form = ComponentForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/component/edit/' + str(id))
    return render(request, "component/edit.html", {'form': form})

def component_delete(request, id):
    Component.objects.get(id=id).delete()
    return redirect("/component/list")
###################################################################################################
def component_type_list(request):
    return render(request, "component_type/list.html", {'component_types': ComponentType.objects.all()})

def component_type_detail(request, id):
    return render(request, "component_type/detail.html", {'component_type': ComponentType.objects.get(id=id)})

def component_type_add(request):
    form = ComponentTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/component_type/list')
    return render(request, "component_type/add.html", {'form': form})

def component_type_edit(request, id):
    obj = get_object_or_404(ComponentType, id=id)
    form = ComponentTypeForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/component_type/edit/' + str(id))
    return render(request, "component_type/edit.html", {'form': form})

def component_type_delete(request, id):
    ComponentType.objects.get(id=id).delete()
    return redirect("/component_type/list")
###################################################################################################
def quotation_list(request):
    return render(request, "quotation/list.html", {'quotations': Quotation.objects.all()})

def quotation_detail(request, id):
    quotation = Quotation.objects.get(id=id)
    return render(request, "quotation/detail.html", {'quotation': quotation})

def quotation_add(request):
    quotation_form = QuotationForm(request.POST or None)
    if request.method == 'POST':
        formset = QuotationLineFormSet(data=request.POST)
        if formset.is_valid() and quotation_form.is_valid():
            for x in formset.cleaned_data:
                x['id'] = quotation_form.cleaned_data.get('id')
                print(x)
            # formset.save()
            from django.urls import reverse_lazy
            return redirect(reverse_lazy("quotation_add"))
        return render(request, {'quotation_line_formset': formset})
    formset = QuotationLineFormSet(queryset=QuotationLine.objects.none())
    return render(request, "quotation/add.html", {'quotation_line_formset': formset, 'quotation_form': quotation_form})

class QuotationAdd(CreateView):
    template_name = 'quotation/add.html'
    model = Quotation
    # form_class = QuotationForm
    fields = ['customer', 'status']
    def get_success_url(self):
        return reverse('quotation_list')
    def get_context_data(self):
        context = super().get_context_data()
        if self.request.POST:
            context['quotation_lines'] = QuotationLineFormSet(self.request.POST)
        else:
            context['quotation_lines'] = QuotationLineFormSet()
        return context
    def form_valid(self, form):
        context = self.get_context_data()
        quotation_lines = context['quotation_lines']
        from django.db import transaction
        with transaction.atomic():
            self.object = form.save()
            if quotation_lines.is_valid():
                quotation_lines.instance = self.object
                quotation_lines.save()
        return super().form_valid(form)

def quotation_edit(request, id):
    quotation = get_object_or_404(Quotation, id=id)
    form = QuotationForm(request.POST or None, instance = quotation)
    for x in quotation.quotation_lines.all():
        print(x)
    if form.is_valid():
        # form.save()
        return redirect('/quotation/edit/' + str(id))
    return render(request, "quotation/edit.html", {'form': form})

def quotation_create_form(request):
    return render(request, "quotation/form.html", {'form': QuotationLineForm()})

def quotation_delete(request, id):
    Quotation.objects.get(id=id).delete()
    return redirect("/quotation/list")
###################################################################################################