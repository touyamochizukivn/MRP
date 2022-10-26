from django.contrib import admin
from django.urls import path, include

from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', dashboard, name='dashboard'),

    # component
    path('component/add', component_add, name='component_add'),
    path('component/list', component_list, name='component_list'),
    path('component/<int:id>', component_detail, name='component_detail'),
    path('component/edit/<int:id>', component_edit, name='component_edit'),
    path('component/delete/<int:id>', component_delete, name='component_delete'),
    # component_type
    path('component_type/add', component_type_add, name='component_type_add'),
    path('component_type/list', component_type_list, name='component_type_list'),
    path('component_type/<int:id>', component_type_detail, name='component_type_detail'),
    path('component_type/edit/<int:id>', component_type_edit, name='component_type_edit'),
    path('component_type/delete/<int:id>', component_type_delete, name='component_type_delete'),
]
