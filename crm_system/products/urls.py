from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('products/create', TemplateView.as_view(template_name='products/products-create.html'), name='products_new'),
    path('products/delete', TemplateView.as_view(template_name='products/products-delete.html'), name='products_delete'),
    path('products/detail', TemplateView.as_view(template_name='products/products-detail.html'), name='products_detail'),
    path('products/edit', TemplateView.as_view(template_name='products/products-edit.html'), name='products_edit'),
    path('products/list', TemplateView.as_view(template_name='products/products-list.html'), name='products_list'),
]