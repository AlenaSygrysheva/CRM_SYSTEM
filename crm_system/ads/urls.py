from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('ads/create', TemplateView.as_view(template_name='ads/ads-create.html'), name='ads_new'),
    path('ads/delete', TemplateView.as_view(template_name='ads/ads-delete.html'), name='ads_delete'),
    path('ads/detail', TemplateView.as_view(template_name='ads/ads-detail.html'), name='ads_detail'),
    path('ads/edit', TemplateView.as_view(template_name='ads/ads-edit.html'), name='ads_edit'),
    path('ads/list', TemplateView.as_view(template_name='ads/ads-list.html'), name='ads_list'),
    path('ads/statistic', TemplateView.as_view(template_name='ads/add-statistic.html'), name='ads_statistic'),
]