from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('leads/create', TemplateView.as_view(template_name='leads/leads-create.html'), name='leads_new'),
    path('leads/delete', TemplateView.as_view(template_name='leads/leads-delete.html'), name='leads_delete'),
    path('leads/detail', TemplateView.as_view(template_name='leads/leads-detail.html'), name='leads_detail'),
    path('leads/edit', TemplateView.as_view(template_name='leads/leads-edit.html'), name='leads_edit'),
    path('leads/list', TemplateView.as_view(template_name='leads/leads-list.html'), name='leads_list'),
]