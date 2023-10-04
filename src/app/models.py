from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
from django.utils import timezone


estados_brasil = [
    ('AC', 'ACRE'),
    ('AL', 'ALAGOAS'),
    ('AP', 'AMAPÁ'),
    ('AM', 'AMAZONAS'),
    ('BA', 'BAHIA'),
    ('CE', 'CEARÁ'),
    ('DF', 'DISTRITO FEDERAL'),
    ('ES', 'ESPÍRITO SANTO'),
    ('GO', 'GOIÁS'),
    ('MA', 'MARANHÃO'),
    ('MT', 'MATO GROSSO'),
    ('MS', 'MATO GROSSO DO SUL'),
    ('MG', 'MINAS GERAIS'),
    ('PA', 'PARÁ'),
    ('PB', 'PARAÍBA'),
    ('PR', 'PARANÁ'),
    ('PE', 'PERNAMBUCO'),
    ('PI', 'PIAUÍ'),
    ('RJ', 'RIO DE JANEIRO'),
    ('RN', 'RIO GRANDE DO NORTE'),
    ('RS', 'RIO GRANDE DO SUL'),
    ('RO', 'RONDÔNIA'),
    ('RR', 'RORAIMA'),
    ('SC', 'SANTA CATARINA'),
    ('SP', 'SÃO PAULO'),
    ('SE', 'SERGIPE'),
    ('TO', 'TOCANTINS')
]

tipo_operacao_choices = [("P", "Pagamento"),
                         ("R", "Recebimento")]


class Usuario(AbstractUser):
    class Meta:
        verbose_name_plural = "Usuários"
        verbose_name = "Usuário"

    foto = models.ImageField(upload_to='fotos_usuarios', null=True, blank=True)
    cep = models.CharField('CEP', max_length=9, blank=True)
    rua = models.CharField('Rua', max_length=200, blank=True)
    numero = models.CharField('Número', max_length=10, blank=True)
    complemento = models.CharField('Complemento', max_length=200, blank=True)
    cidade = models.CharField('Cidade', max_length=200, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    estado = models.CharField('Estado', max_length=2, choices=estados_brasil, blank=True, null=True)
    data_criacao = models.DateField('Data de Inclusão', default=datetime.now, blank=True)

    # Parte II do modelo
    total_entradas = models.DecimalField('Total Entradas', max_digits=10, decimal_places=2, blank=True, null=True)
    total_saidas = models.DecimalField('Total Saídas', max_digits=10, decimal_places=2, blank=True, null=True)

    def get_entradas_total_30_dias(self):
        data_atual = timezone.now()
        data_inicial = data_atual - timezone.timedelta(days=30)

        total_entrada_30_dias = Movimento.objects.filter(
            usuario=self.id,
            data_movimento__range=(data_inicial, data_atual),
            categoria__tipo='R'
        ).aggregate(total=Sum('valor'))['total'] or 0

        self.total_entradas = total_entrada_30_dias
        self.save()
        return f'R$ {self.total_entradas:,.2f}'

    def get_saidas_total_30_dias(self):
        data_atual = timezone.now()
        data_inicial = data_atual - timezone.timedelta(days=30)

        total_saidas_30_dias = Movimento.objects.filter(
            usuario=self.id,
            data_movimento__range=(data_inicial, data_atual),
            categoria__tipo='P'
        ).aggregate(total=Sum('valor'))['total'] or 0

        self.total_saidas = total_saidas_30_dias
        self.save()
        return f'R$ {self.total_saidas:,.2f}'

    def saldo_final(self):
        return self.total_entradas - self.total_saidas


class Categoria(models.Model):
    class Meta:
        verbose_name_plural = "Categoria"
        verbose_name = "Categorias"

    tipo = models.CharField('Tipo', max_length=1, choices=tipo_operacao_choices, default="P")
    descricao = models.CharField('Descrição', max_length=100)
    data_criacao = models.DateField('Data de Inclusão', default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.tipo} - ({self.descricao})'


class Movimento(models.Model):
    class Meta:
        verbose_name_plural = "Movimento"
        verbose_name = "Movimentos"

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_movimento = models.DateField('Data do Movimento', default=datetime.now, blank=True)
    descricao = models.CharField('Descrição', max_length=100)
    valor = models.DecimalField('Valor da operação', max_digits=10, decimal_places=2)
    data_criacao = models.DateField('Data de Inclusão', default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.categoria.descricao} - {self.descricao} ({self.valor})'


class SaldoInicial(models.Model):
    valor_inicial = models.DecimalField('Valor Inicial', max_digits=10, decimal_places=2)
    data_criacao = models.DateField('Data de Inclusão', default=datetime.now, blank=True)

    def __str__(self):
        return '%s', self.valor_inicial
