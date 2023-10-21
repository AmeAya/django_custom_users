from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('log_in/', logInView, name='log_in_url'),
    path('log_out/', logOutView, name='log_out_url'),
    path('registration/', registrationView, name='registration_url'),
    path('about_us/', TemplateView.as_view(template_name='about_us.html'), name='about_us_url'),
]
