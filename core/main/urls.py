from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('deals', views.deals, name='deals'),
    path('reservation', views.reservation, name='reservation'),
]