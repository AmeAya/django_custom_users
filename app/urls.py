from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('log_in/', LoginView.as_view(template_name='log_in.html'), name='log_in_url'),
    path('log_out/', LogoutView.as_view(), name='log_out_url'),
    path('about_us/', TemplateView.as_view(template_name='about_us.html'), name='about_us_url'),
]
