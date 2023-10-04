from django.urls import path
from . import views as view


urlpatterns = [
    path('', view.home_view, name='home'),
    path('login', view.login_view, name='login'),
    path('logout', view.logout_view, name='logout'),
    path('entradas', view.entradas_view, name='entradas'),
    path('saidas', view.saidas_view, name='saidas'),
    path('config', view.config_view, name='config'),
    path('salvar_movimento/', view.salvar_movimento, name='salvar_movimento'),
    path('editar_movimento/<int:movimento_id>/', view.editar_movimento, name='editar_movimento'),
    path('excluir_movimento/<int:movimento_id>/', view.excluir_movimento, name='excluir_movimento'),
    path('qualquer_requisicao/', view.qualquer_requisicao, name='qualquer_requisicao'),
    # path('salvar_movimento_entradas/', view.salvar_movimento_entradas, name='salvar_movimento_entradas'),
    # path('salvar_movimento_Saidas/', view.salvar_movimento_saidas, name='salvar_movimento_saidas'),
]