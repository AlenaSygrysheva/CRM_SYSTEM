from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='_base.html'), name='base_page'),
    path('users/', TemplateView.as_view(template_name='users/index.html'), name='users_index'),
    path('registration/', TemplateView.as_view(template_name='registration/login.html'), name='user_login'),
]