from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('customers/create', TemplateView.as_view(template_name='customers/customers-create.html'), name='customers_new'),
    path('customers/delete', TemplateView.as_view(template_name='customers/customers-delete.html'), name='customers_delete'),
    path('customers/detail', TemplateView.as_view(template_name='customers/customers-detail.html'), name='customers_detail'),
    path('customers/edit', TemplateView.as_view(template_name='customers/customers-edit.html'), name='customers_edit'),
    path('customers/list', TemplateView.as_view(template_name='customers/customers-list.html'), name='customers_list'),
]