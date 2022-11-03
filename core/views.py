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
    quotation_line = get_object_or_404(QuotationLine, id=id)
    form = QuotationLineForm(request.POST or None, instance = quotation_line)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/quotation/' + str(quotation_line.quotation.id))
    return render(request, "quotation/edit.html", {'form': form, 'quotation_line': quotation_line})

def quotation_delete(request, id):
    Quotation.objects.get(id=id).delete()
    return redirect("/quotation/list")

def quotation_update_status(request, id):
    quotation = Quotation.objects.get(id=id)
    quotation.status = "Pending"
    quotation.save()
    return redirect("/quotation/list")
###################################################################################################

def sale_order_list(request):
    return render(request, "sale_order/list.html", {'sale_orders': SaleOrder.objects.all()})

def sale_order_detail(request, id):
    sale_order = SaleOrder.objects.get(id=id)
    return render(request, "sale_order/detail.html", {'sale_order': sale_order})

def sale_order_add(request, id):
    quotation = Quotation.objects.get(id=id)
    quotation_lines = quotation.quotation_lines.all()
    sale_order = SaleOrder.objects.create(
        quotation = quotation,
        customer = quotation.customer,
        date = quotation.date,
    )
    for quotation_line in quotation_lines:
        SaleOrderLine.objects.create(
            sale_order = sale_order,
            product = quotation_line.product,
            price = quotation_line.price,
            quantity = quotation_line.quantity,
        )
    return redirect("/sale_order/" + str(sale_order.id))

def sale_order_edit(request, id):
    sale_order_line = get_object_or_404(SaleOrderLine, id=id)
    form = SaleOrderLineForm(request.POST or None, instance = sale_order_line)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sale_order/' + str(sale_order_line.sale_order.id))
    return render(request, "sale_order/edit.html", {'form': form, 'sale_order_line': sale_order_line})

def sale_order_delete(request, id):
    SaleOrder.objects.get(id=id).delete()
    return redirect("/sale_order/list")
###################################################################################################