from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='topfive-home'),
    path('topfive/', views.my_top_five, name='topfive-my_top_five')
]