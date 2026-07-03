from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('about/', views.about, name='about'),
    path('causes/', views.causes, name='causes'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('exit/', views.exit, name='exit'),

]