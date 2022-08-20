"""protector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from inventory.views import InventoryCreateView, InventoryUpdateView, InventoryDeleteView
from inventory.views import InventoryListView, InventoryDetailView


urlpatterns = [
    path('', TemplateView.as_view(template_name="_index.html"), name='index'),
    path('_index.html', TemplateView.as_view(template_name="_index.html"), name='index'),
    path('inventory/', InventoryListView.as_view(template_name="_inventory.html"), name='inventory'),
    # path('new/', InventoryCreateView.as_view(), name='_edit_product'),
    # path('inventory/<int:pk>/detail/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory/create/', InventoryCreateView.as_view(), name='inventory_create'),
    path('inventory/<int:pk>/update/', InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory_delete'),
]
