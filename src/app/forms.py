from django.forms import ModelForm
from .models import Movimento, Categoria
from django import forms


class MovimentoForm(ModelForm):
    # Aqui ainda há a possibilidade de personalizar ou adicionar campos, exemplo:
    descricao = forms.CharField(label='Descrição', max_length=100, required=False,
                                widget=forms.Textarea())
    categoria = forms.ModelChoiceField(
        label='Categoria',
        queryset=Categoria.objects.all(),  # QuerySet que define as opções
        widget=forms.Select
    )

    class Meta:
        model = Movimento
        fields = ('categoria', 'descricao', 'valor',)

    def __init__(self, *args, initial_value=None, **kwargs):
        super(MovimentoForm, self).__init__(*args, **kwargs)

        if initial_value:
            if initial_value == 'P' or initial_value == 'saida':
                categorias = Categoria.objects.filter(tipo='P')
            else:
                categorias = Categoria.objects.filter(tipo='R')

            self.fields['categoria'].queryset = categorias
