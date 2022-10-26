from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

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