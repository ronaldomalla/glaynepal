from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('apply_form',views.apply_form,name='apply_form'),
    path('contact',views.contact,name='contact'),
    path('service',views.service,name='service'),
    path('product',views.product,name='product'),

]
