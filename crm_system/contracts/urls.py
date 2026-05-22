from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('contracts/create', TemplateView.as_view(template_name='contracts/contracts-create.html'), name='contracts_new'),
    path('contracts/delete', TemplateView.as_view(template_name='contracts/contracts-delete.html'), name='contracts_delete'),
    path('contracts/detail', TemplateView.as_view(template_name='contracts/contracts-detail.html'), name='contracts_detail'),
    path('contracts/edit', TemplateView.as_view(template_name='contracts/contracts-edit.html'), name='contracts_edit'),
    path('contracts/list', TemplateView.as_view(template_name='contracts/contracts-list.html'), name='contracts_list'),
]