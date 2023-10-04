from django.contrib import admin
from django.utils.html import format_html
from app.models import Usuario, Categoria, Movimento, SaldoInicial


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'cidade', 'imagem')
    list_filter = ('estado',)
    # search_fields = ('firt_name', 'last_name', 'cidade', 'estado')
    list_per_page = 30
    ordering = ('first_name',)

    @staticmethod
    def imagem(obj):
        to_return = "Nenhuma"
        if obj.foto and obj.foto.url:
            to_return = format_html('<img src="{}" width=auto height=40/>'.format(obj.foto.url))
        return to_return


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'descricao', 'data_criacao')
    list_filter = ('tipo',)
    search_fields = ('tipo',)
    list_per_page = 30
    ordering = ('tipo', 'descricao')


@admin.register(Movimento)
class MovimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'categoria', 'data_movimento', 'descricao', 'valor', 'data_criacao')
    list_filter = ('categoria',)
    search_fields = ('categoria',)
    list_per_page = 30
    ordering = ('id',)
    
    
@admin.register(SaldoInicial)
class MovimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor_inicial', 'data_criacao')
    ordering = ('id',)
