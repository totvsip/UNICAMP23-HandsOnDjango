from django.urls import path
from . import views as view

urlpatterns = [
    path('', view.home_view, name='home'),
    path('login', view.login_view, name='login'),
    path('entradas', view.entradas_view, name='entradas'),
    path('saidas', view.saidas_view, name='saidas'),
    path('config', view.config_view, name='config'),
]
