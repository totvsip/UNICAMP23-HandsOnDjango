UNICAMP - HANDS ON

# HANDS ON DJANGO FRAMEWORK by TOTVS IP/TM

## 1. Acessar nosso ambiente de desenvolvimento na nuvem

### 1.1 Acesse o link abaixo

[//]: # (```url)

[//]: # (https://console.aws.amazon.com)

[//]: # (```)
### [https://917863364290.signin.aws.amazon.com/console](https://917863364290.signin.aws.amazon.com/console)

### 1.2 Insira seu usuário e senha para acessar o AWS
![Alt text](images/cloud9-02.png?raw=true "cloud9-02")

### 1.3 Clique na barra de pesquisa(Search) na parte superior da página

![Alt text](images/cloud9-03.png?raw=true "cloud9-03")

### 1.4 Escreva 'cloud9' e selecione a primeira opção

![Alt text](images/cloud9-04.png?raw=true "cloud9-04")

### 1.5 Acesse o 'cloud9' e expanda o menu lateral
![Alt text](images/cloud9-05.png?raw=true "cloud9-05")

### 1.6 Clique na opção 'Compartilhados comigo' no menu lateral a esquerda

![Alt text](images/cloud9-06.png?raw=true "cloud9-06")

### 1.7 Clique em 'em aberto' na coluna de 'Cloud9 IDE' do ambiente que deseja acessar

![Alt text](images/cloud9-07.png?raw=true "cloud9-07")

### 1.8 Ao fim do passo 1, o ambiente deve estar assim:
![Alt text](images/cloud9-08.png?raw=true "Cloud9-08")

### Ajustes:

#### Utilize "Ctrl +" para aumentar o tamanho da tela.

## 2. Criar um diretório para o projeto e acessá-lo

### 2.1 Criar o diretório

#### Utilizaremos o terminal a partir deste ponto. O terminal é um ambiente onde podemos inserir códigos e comandos escrevendo-os e, em seguida, pressionando "Enter" para executá-los.

![Alt text](images/cloud9-09.png?raw=true "cloud9-09")

#### O comando 'mkdir' cria um diretório no ambiente.

```bash
mkdir djangounicamp
```

![Alt text](images/cloud9-10.png?raw=true "cloud9-10")

#### O comando irá criar uma pasta com o nome "djangounicamp", que pode ser acessada pela lateral esquerda.

![Alt text](images/cloud9-11.png?raw=true "cloud9-11")

### 2.2 Acessar o diretório

#### O comando "cd" permite navegar entre as pastas, vamos acessar a pasta "djangounicamp", onde o projeto será criado.

```bash
cd djangounicamp
```

![Alt text](images/cloud9-12.png?raw=true "Cloud9-12")

#### Podemos visualizar que a pasta foi acessada pelo terminal.

![Alt text](images/cloud9-13.png?raw=true "Cloud9-13")

#### Dessa forma, sempre que criarmos algo do projeto, será dentro dessa pasta.

### 2.3 Favoritar o diretório criado

![Alt text](images/cloud9-14.png?raw=true "Cloud9-14")

### Observação: clique com o botão direito do mouse e selecione a opção "Add to Favorites".

### 2.4 Verifique a versão do Python utilizando o código abaixo, no terminal 

```bash
python3 --version
```
![Alt text](images/cloud9-15.png?raw=true "Cloud9-15")
#### Observação: a versão desejada, é o Python 3.10.12.

># Não use o código abaixo, ele serve apenas para exemplo
>### 2.5  Nesse momento o, ideal seria criar um ambiente virtual, que poderia ser feito da forma abaixo, no entando, vamos utilizar o ambiente do Cloud9 para que o Debug seja realizado de forma mais simples e compatível.
>#### Criar o ambiente virtual
>```bash
>python3 -m venv venv
>```         
>#### Ativar o ambiente virtual
>```bash
>source venv/bin/activate
>```



## 3. Instalação do Django e configuração inicial

### 3.1 Utilize o código abaixo no terminal para realizar a instalação do Django

#### Observação: "pip install" é o comando padrão para instalação no Python.

```bash
pip install django
```

![Alt text](images/cloud9-16.png?raw=true "Cloud9-16")

#### Além do Django, devemos também instalar a biblioteca 'Pillow', pois iremos usar no decorrer do projeto.
```bash
pip install pillow
```

### 3.2 Criar um projeto adicionando o código abaixo no terminal

```bash
django-admin startproject core .
```
![Alt text](images/cloud9-17.png?raw=true "Cloud9-17")

### 3.3 Criar uma aplicação

#### Uma aplicação é um conjunto de códigos que interage com várias partes do framework.

```bash
python manage.py startapp app
```
![Alt text](images/cloud9-18.png?raw=true "Cloud9-18")

### Sempre após a criação de um novo aplicativo, devemos aplicar o seu nome aos 'INSTALLED_APPS', dentro do arquivo './core/settings.py'.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app', # Novo app adicionado
]
```

### 3.4 Alterar o arquivo './core/settings.py'

#### Altere a permissão dos hosts para aceitar a conexão de qualquer host, substituindo a linha abaixo no arquivo './core/settings.py'
#### **Caminho para o arquivo: './core/settings.py'** 

#### **Por padrão, o 'ALLOWED_HOSTS = []' se encontra na linha 28 de './core/settings.py'**

![Alt text](images/cloud9-19.png?raw=true "Cloud9-19")

```python
ALLOWED_HOSTS = ['*']
```

### **Após a alteração, a linha 28 deve ficar assim.

![Alt text](images/cloud9-20.png?raw=true "Cloud9-20")

## 4. Executar a aplicação pela primeira vez

### 4.1 Inicializar a aplicação

#### Utilize o código abaixo no terminal.
```bash
python manage.py runserver $IP:$PORT
```

### 4.2 Acessar a Aplicação

#### Clique no link no canto inferior direito que foi gerado, ele o levará para a página da aplicação.

![Alt text](images/cloud9-21.png?raw=true "Cloud9-21")

#### Observação: Caso a Url não tenha aparecido ou a janela com a Url tenha fechado, utilize o código no terminal para recuperar sua Url de navegação na aplicação.
```bash
echo https://$C9_PID.vfs.cloud9.us-east-2.amazonaws.com/
```

### 4.3 Tela inicial da Aplicação

![Alt text](images/cloud9-22.png?raw=true "Cloud9-22")

### 4.4 Vamos encerrar a execução da aplicação, para isso, devemos voltar a seleção do terminal principal (o mesmo em que fizemos os comandos iniciais), lembre-se de clicar no interior do terminal para levar o foco até ele, após, use o comando 'Ctrl + C', para interromper a execução.

![Alt text](images/cloud9-22-2.png?raw=true "Cloud9-22-2")

### 4.5 O terminal deve ficar assim após a interrupção da execução.

![Alt text](images/cloud9-22-3.png?raw=true "Cloud9-22-3")


### 4.6 Qual foi o protótipo do projeto

### [https://totvsip.github.io/UNICAMP23-HandsOnDjango-HTMLReference/](https://totvsip.github.io/UNICAMP23-HandsOnDjango-HTMLReference/)


## 5. Executando a aplicação pelo Cloud9, para termos acesso ao debug

### 5.1 Configurando o Debug utilizando o run

#### O Debug é uma ferramenta que permite o programador visualizar o funcionamento do código e identificar problemas, facilitando a correção.

#### Pressione o "RUN" na parte superior do cloud9.

![Alt text](images/cloud9-23.png?raw=true "Cloud9-23")

#### Uma nova janela se abrirá na região inferior.

![Alt text](images/cloud9-24.png?raw=true "Cloud9-24")

### 5.2 Informe o comando a ser utilizado para o "command".

#### Na região do "command", informe o código a seguir.

```bash
djangounicamp/manage.py runserver $IP:$PORT
```
![Alt text](images/cloud9-25.png?raw=true "Cloud9-25")

### 5.3 Habilite o Debug

#### Clique na opção de Debug para habilitá-lo.

![Alt text](images/cloud9-26.png?raw=true "Cloud9-26")

### 5.4 Clique no botão "Run" para executar a aplicação mesmo vazia ainda.

![Alt text](images/cloud9-26-2.png?raw=true "Cloud9-26-2")

### 5.5 A tela do terminal deve ficar assim após a execução.

![Alt text](images/cloud9-26-3.png?raw=true "Cloud9-26-3")

### 5.6 Criar o plano de migraçao e criar o banco de dados
```bash
python manage.py makemigrations

python manage.py migrate
```


### 5.6 Criar um super usuário(Administrador)

```bash
python manage.py createsuperuser
```

## 5.7 Entendendo o admin e os modelos de dados

#### Deve-se adicionar ao arquivo './core/settings.py' o seguinte trecho correspondente ao domínio do projeto:
#### Atente-se que, a Url deve estar sem a '/' final, assim como o exemplo abaixo, altere a Url para a do seu projeto
```python
CSRF_TRUSTED_ORIGINS = ['https://98d9aa5b75664f7689c4149e247f8b25.vfs.cloud9.us-east-2.amazonaws.com',]
```

### 5.8 Após isso, acessar o admin com:
```url
[Url do projeto]/admin
```

## 6. Criar os modelos no arquivo models.py

```python
from datetime import datetime
from django.db import models
from django.db.models import Sum
from django.utils import timezone

tipo_operacao_choices = [("P", "Pagamento"),
                         ("R", "Recebimento")]


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

```
### 6.1 Após adicionar o código anterior, devemos executar dois comandos no terminal, na seguinte ordem:
#### O comando 'makemigrations' serve para prepararmos as migrações das tabelas(modelos) criados anteriormente, ou então em algumas situações para representar as alterações nos modelos.
```bash
python manage.py makemigrations
```

#### O comando 'migrate' serve para aplicar as criações ou alterações feitas nos modelos, responsável por sincronizar os esquemas do banco de dados com o estado atual das tabelas(modelos).
```bash
python manage.py migrate
```
#### Ambos são comandos muito importantes, visto que trabalham diretamente com a estrutura do banco de dados, essencialmente para manter o banco de dados alinhado com a estrutura dos modelos de dados do seu aplicativo.

#### Após a execução dos comandos, devemos obter o seguinte resultado no terminal:
![Alt text](images/cloud9-makemigrations_migrate.png?raw=true "Cloud9-makemigrations_migrate")


### 7. Criar as definições de administração para acessarmos o banco de dados e visualizar nossa estrutura de dados no arquivo admin.py
    
```python
from django.contrib import admin
from django.utils.html import format_html
from app.models import Usuario, Categoria, Movimento, SaldoInicial


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
```

#### Após a adição do código acima, podemos acessar novamente o 'django admin', da mesma forma que acessamos anteriormente.

### 7.1 Convertendo o modelo de Usuário padrão, para um personalizado
#### A criação do nosso super usuário, feito anteriormente usando o comando 'createsuperuser' faz com que, por padrão, o Django salve o usuário em seu modelo original de usuários.

#### Para obtermos mais praticidade, poder de customização e facilidade na criação e gerenciamento de nossos usuários, devemos criar o nosso próprio modelo de Usuário, para isso, adicione o trecho a seguir no arquivo './app/models.py', substituindo também com alguns dos novos imports utilizados.

```python
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

```

### 7.2 Para que o nosso modelo personalizado seja utilizado pelo Django, devemos também atualizar o nosso arquivo './core/settings.py'
#### Devemos incluir no arquivo o seguinte trecho de código:
```python
AUTH_USER_MODEL = 'app.Usuario'
```

#### A partir da criação de nosso modelo de Usuário personalizado, devemos realizar novamente os comandos de migração para aplicar as mudanças feitas. Siga a sequência abaixo e execute no terminal:
```bash
rm db.sqlite3
```

```bash
rm -rf app/migrations
```

```bash
python manage.py makemigrations
```

```bash
python manage.py makemigrations app
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

### 7.3 Assim como devemos atualizar o nosso arquivo './app/admin.py'
#### Dessa forma, o painel de administração do Django irá assumir o uso desse novo modelo que criamos para os usuários, no intuito de termos a capacidade de adicionarmos os campos adicionais que forem necessários.
#### Atualize o arquivo com o novo modelo de Usuário para o admin, assim como também os novos imports necessários:

```python
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
```

## 8. Criar diretórios auxiliares do projeto
```bash
mkdir templates
mkdir -p core/static/img
mkdir -p core/static/js
mkdir uploads
```

![Alt text](images/cloud9-28.png?raw=true "Cloud9-28")

## 9. Alterar o arquivo './core/settings.py' para o nosso projeto

### 9.1 Adicionar o import do módulo "os"

```python
import os
```
![Alt text](images/cloud9-29.png?raw=true "Cloud9-29")

### 9.2 Adicionar a linha abaixo no arquivo './core/settings.py', para utilizar como referência da versão publicada do projeto

```python
# Controle da versão do sistema
APP_VERSION = '0.1.001'
```
![Alt text](images/cloud9-30.png?raw=true "Cloud9-30")

### 9.3 Alterar a Linguagem Padrão e o Fuso Horário no Django, em './core/settings.py'

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

![Alt text](images/cloud9-31.png?raw=true "Cloud9-31")

### 9.4 Alterar os diretórios dos arquivos estáticos e mídia

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Static Files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core/static'),
)
```
### ** Antes das alterações **
![Alt text](images/cloud9-32.png?raw=true "Cloud9-32")

### ** Após as alterações **

![Alt text](images/cloud9-33.png?raw=true "Cloud9-33")

### 9.5 Alterar o diretório dos templates

### ** Antes das alterações **

![Alt text](images/cloud9-34.png?raw=true "Cloud9-34")

```python
'DIRS': [os.path.join(BASE_DIR, 'templates/')],
```

### ** Após as alterações **

![Alt text](images/cloud9-35.png?raw=true "Cloud9-35")


## 10. Configurações de 'STATIC'

### 10.1. Alterar o arquivo '.core/urls.py' para o nosso projeto e criar o arquivo 'urls.py' no diretório './app', para a nossa aplicação.

### Alterando o arquivo '.core/urls.py':
#### Adicionar o import do módulo include

```python
from django.urls import path, include
```

#### Adicionar a linha abaixo para utilizar como padrão um novo modelo de usuário

```python
path('', include('app.urls')),

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### O arquivo core/urls.py deve ficar assim

```python
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('app.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

### Criando o arquivo 'urls.py' em './app'.
#### Para isso, execute o comando no terminal, ou então, clique com o botão direito no diretório './app' e 'New File' com o nome 'urls.py':
```bash
touch ./app/urls.py
```

### Após a criação do arquivo, adicione esse trecho de código para obter os endpoints necessários do projeto:
#### Cada um irá acessar uma determinada view(função), que irá ter um determinado comportamento a partir de uma lógica definida.
```python
from django.urls import path
from . import views as view

urlpatterns = [
    path('', view.home_view, name='home'),
    path('login', view.home_view, name='login'),
    path('entradas', view.home_view, name='entradas'),
    path('saidas', view.home_view, name='saidas'),
    path('config', view.home_view, name='config'),
]
```

#### Por enquanto, iremos utilizar a mesma view(home_view), posteriormente iremos criar as demais funções.

## 11. Definição de 'views.py', devemos acessar o arquivo './app/views.py' e adicionar o seguinte código:
```python
from django.http import HttpResponse


def home_view(request):
    return HttpResponse('Hello, World!')

```

#### Cada uma das 'views' correspondem a um endpoint, que definimos anteriormente no arquivo 'urls.py', dessa forma, quando acessarmos algum desses domínios, automaticamente a função correspondente irá ser executada.
#### No caso, a 'view' demonstrada está renderizando uma tela 'Hello, World!' com o 'HttpResponse', a efeito de exemplo.

### 11.1 Demonstração de outro exemplo com a renderização de uma 'view'
#### Neste caso, vamos atualizar fazendo uso de com algumas tags HTML:
```python
from django.http import HttpResponse


def home_view(request):
    html = "<h1>Hello, World!</h1>"
    html += "<p>Essa é uma das outras maneiras de renderizarmos uma página através de uma view!</p>"
    return HttpResponse(html)

```


### 12. Configurar a sessão de bibliotecas, no arquivo './core/settings.py', para contemplar o arquivo 'templatetags'

### ** Antes das alterações **

![Alt text](images/cloud9-36.png?raw=true "Cloud9-36")

```python
            'libraries': {
                'templatetags': 'app.templatetags',
            }
```
### ** Observação: a configuração deve ser inserida dentro do trecho 'OPTIONS'. **
### ** Após as alterações. **

![Alt text](images/cloud9-37.png?raw=true "Cloud9-37")

### A configuração dos templates deve estar dessa forma no arquivo './core/settings.py'.
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'templatetags': 'app.templatetags',
            }
        },
    },
]
```


### 12.1 Uso de templatetags
### Deve-se criar o arquivo 'templatetags.py', no diretório './app', para isso, há duas formas de fazermos essa criação:
#### Executando o comando no terminal:
```bash
touch ./app/templatetags.py
```

#### As 'templatetags' no Django, são construções utilizadas geralmente com o prefixo '{%  %}', para incorporar lógicas nos modelos HTML.
```html
{% load templatetags %}
{% minha_templatetag parametro1 parametro2 %}
```
E vamos ver isso mais adiante.

#### Ou então, clicar com o botão direito sobre o diretório './app' e em seguida 'New File', com o nome 'templatetags.py':
![Alt text](images/cloud9-new_file_templatetags.png?raw=true "Cloud9-38")

### Após a criação do arquivo, devemos adicionar o seguinte código:
```python templatetags.py
from django.template import Library
from core import settings

register = Library()


@register.simple_tag
def app_version():
    return settings.APP_VERSION

@register.simple_tag
def show_header_menu(request):
    if request.path == '/login':
        return False
    else:
        return True
```
#### As 'templatetags', são uma forma eficaz de adicionarmos lógica ao nossos templates HTML, de forma com que seja de fácil reutilização em outros códigos.


## 13. Templates
### No diretório 'Templates', vamos criar os arquivos HTML a seguir:

### base.html

templates/base.html

```html
{% load static %}
{% load templatetags %}

<!DOCTYPE html>
<html lang="pt-br" data-bs-theme="dark">
<!-- <html lang="pt-br"> -->
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <title>{% block title %}{% endblock %}</title>

    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
            rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
            crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
            crossorigin="anonymous"></script>

    <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"
            integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA=="
            crossorigin="anonymous"
            referrerpolicy="no-referrer"
    />
    <script src="https://unpkg.com/htmx.org@1.6.1/dist/htmx.min.js"></script>

    {% block extra_header_content %}
    {% endblock %}
</head>
<body>
<div class="container">

    {% show_header_menu request as show_menu %}
    {% if show_menu %}
        {% include 'header.html' %}
    {% endif %}

    {% if messages %}
        <div class="messages mt-4 text-right" style="max-width: 300px; margin-left: auto;">
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }}" role="alert">
                    {{ message }}
                </div>
            {% endfor %}
        </div>
    {% endif %}

    <div class="mt-3">
        {% block container_content %}{% endblock %}
    </div>

</div>

<script
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>

{% block extra_body_content %}
{% endblock %}

<!-- Copyright -->
<footer data-bs-theme="dark" class="text-center text-white fixed-bottom">
    <div class="container p-1"></div>

    <div class="text-center p-1 text-small">
        <p class="mt-5 mb-3 text-muted"><small>
            v{% app_version %} © 2023 Copyright
            <a class="text-white" href="https://www.totvs.com.br/" target="_blank">TOTVS IP/TM</a>
        </small></p>
    </div>
</footer>

</body>
</html>

```

### header.html

templates/header.html
```html
{% if user.is_authenticated %}
<div class="mt-2">
    <ul class="container nav nav-pills nav-fill gap-2 p-1 small bg-primary rounded-5 shadow-sm" id="pillNav1"
        style="--bs-nav-link-color: var(--bs-white); --bs-nav-pills-link-active-color: var(--bs-primary); --bs-nav-pills-link-active-bg: var(--bs-white);">
        <!-- Abas no cabeçalho -->
        <li class="nav-item" role="presentation">
            <a class="nav-link rounded-5 {{ is_home_tab_active }}" id="home-tab1" href="{% url 'home' %}">
                <i class="fa-solid fa-building-columns"></i>
                Home</a>
        </li>
        <li class="nav-item" role="presentation">
            <a class="nav-link rounded-5 {{ is_entradas_tab_active }}" id="profile-tab1" href="{% url 'entradas' %}">
                <i class="fa-solid fa-right-to-bracket"></i>
                Entradas</a>
        </li>
        <li class="nav-item" role="presentation">
            <a class="nav-link rounded-5 {{ is_saidas_tab_active }}" id="contact-tab1" href="{% url 'saidas' %}">
                <i class="fa-solid fa-right-from-bracket"></i>
                Saídas</a>
        </li>
        <li class="nav-item" role="presentation">
            <a class="nav-link rounded-5 {{ is_config_tab_active }}" id="setup-tab1" href="{% url 'config' %}">
                <i class="fa-solid fa-gear"></i>
                Config</a>
        </li>
    </ul>
</div>
{% endif %}
```

### home.html

templates/home.html
```html
{% extends 'base.html' %}

{% block title %}TBank - Home{% endblock %}

{% block container_content %}
    <div class="card d-flex flex-wrap">
        <div class="p-3">
            <div class="card" style="background-color: rgb(15, 141, 19)">
                <h5 class="card-header">Entradas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias {{ valor_entrada }}</h5>
                    <button type="button" class="btn btn-primary" hx-get="/salvar_movimento/?tipo_movimento=entrada"
                            hx-target="#modalGenerico">Incluir Nova Entrada
                    </button>
                </div>
            </div>
        </div>

        <div class="p-3">
            <div class="card" style="background-color: rgb(221, 23, 23)">
                <h5 class="card-header">Saídas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias {{ valor_saida }}</h5>
                    <button type="button" class="btn btn-primary" hx-get="/salvar_movimento/?tipo_movimento=saida"
                            hx-target="#modalGenerico">Incluir Nova Saída
                    </button>
                </div>
            </div>
        </div>

        <div class="p-3">
            <div class="card" style="background-color: rgb(33, 6, 204)">
                <h5 class="card-header">Balanço</h5>
                <div class="card-body">
                    <h5 class="card-title">Balanço geral nos últimos 4 meses.</h5>
                    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modChart">
                        Analisar
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal Genérico -->
    <div id="modal" class="modal fade">
        <div id="modalGenerico" class="modal-dialog" hx-target="#this">
        </div>
    </div>
    <!-- Final Modal Genérico -->

    <!-- Modal Gráfico -->
    <div class="modal fade" id="modChart" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Gráfico</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <canvas id="canvas" width="80%" height="80%"></canvas>
                </div>
            </div>
        </div>
    </div>
    <!-- Final Modal Gráfico -->
{% endblock %}


{% block extra_body_content %}
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
        {# GRÁFICO #}
        ;(function () {
            const ctx = document.getElementById("canvas").getContext("2d")
            const myChart = new Chart(ctx, {
                type: "bar",
                data: {
                    labels: ["Jul", "Ago", "Set", "Out"],
                    datasets: [
                        {
                            label: "Entradas",
                            data: [6, 7, 6, 8],
                            backgroundColor: "rgb(15, 141, 19)",
                            borderColor: "rgb(15, 141, 19)",
                            borderWidth: 1,
                        },
                        {
                            label: "Saídas",
                            data: [5, 11, 5, 5],
                            backgroundColor: "rgb(221, 23, 23)",
                            borderColor: "rgb(221, 23, 23)",
                            borderWidth: 1,
                        },
                    ],
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                        },
                    },
                },
            })
        })()
    </script>

{% endblock %}
```


### login.html

templates/login.html
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}TBank - Login{% endblock %}

{% block container_content %}
    <div class="text-center">
  <img
    alt=""
    class="mb-4 mt-5"
    height="100"
    width="100"
    src="{% static 'img/totvs_logo_branco.png' %}"
  />
  <form class="form-signin" method="post" action="{% url 'login' %}">
      {% csrf_token %}
    <h1 class="h3 mb-4 font-weight-normal">Faça o seu login</h1>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">
          <span class="fa fa-user"></span>
      </span>
      <input id="username" name="username" type="text" class="form-control" placeholder="Usuário"/>
    </div>

    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">
          <span class="fa fa-lock"></span>
      </span>
      <input id="password" name="password" type="password" class="form-control" placeholder="Senha"/>
    </div>

    <div class="d-grid gap-1 mt-5">
      <button class="btn btn-primary" href="{% url 'login' %}" type="submit">Login</button>
    </div>

  </form>

</div>

{% endblock %}
```

### entradas.html

templates/entradas.html

```html
{% extends 'base.html' %}

{% block title %}TBank - Entradas{% endblock %}

{% include 'header.html' %}

{% block container_content %}
    <div class="card d-flex flex-wrap">

        <div class="p-3">
            <div class="card" style="background-color: rgb(15, 141, 19);">
                <h5 class="card-header">Entradas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias {{ valor_total }}</h5>
                    <a href="nav_tabs_base.html" class="btn btn-primary">Incluir nova Entrada</a>
                </div>
            </div>
        </div>

        <table class="table">
            <thead>
            <tr>
                <th scope="col">Data</th>
                <th scope="col">Categoria</th>
                <th scope="col">Descrição</th>
                <th class="text-end" scope="col">Valor</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">{{ valor }}</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">{{ valor }}</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">{{ valor }}</td>
            </tr>
            </tbody>
        </table>

    </div>
{% endblock %}
```


### saidas.html

templates/saidas.html

```html
{% extends 'base.html' %}

{% block title %}TBank - Saídas{% endblock %}

{% include 'header.html' %}

{% block container_content %}
    <div class="card d-flex flex-wrap">

        <div class="p-3">
            <div class="card" style="background-color: rgb(221, 23, 23);">
                <h5 class="card-header">Saídas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias {{ valor_total }}</h5>
                    <a href="nav_tabs_base.html" class="btn btn-primary">Incluir nova Saída</a>
                </div>
            </div>
        </div>

        <table class="table">
            <thead>
            <tr>
                <th scope="col">Data</th>
                <th scope="col">Categoria</th>
                <th scope="col">Descrição</th>
                <th class="text-end" scope="col">Valor</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">{{ valor }}</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">{{ valor }}</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">{{ valor }}</td>
            </tr>
            </tbody>
        </table>

    </div>
{% endblock %}

```


### config.html

templates/config.html
```html
{% extends 'base.html' %}
{% block title %}TBank - Config{% endblock %}
{% block container_content %}

<div class="card">
    <div class="card-body">
        <h1 class="card-title">Usuário</h1>

        <form class="form-signin" method="post" action="{% url 'config' %}">
            {% csrf_token %}
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa fa-user"></span>
                </span>
                <input id="primeiro_nome" name="primeiro_nome" type="text" required class="form-control"
                    placeholder="Primeiro nome" value="{{ primeiro_nome }}" />
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa fa-signature"></span>
                </span>
                <input id="segundo_nome" name="segundo_nome" type="text" required class="form-control"
                    placeholder="Segundo nome" value="{{ segundo_nome }}" />
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa-solid fa-envelopes-bulk"></span>
                </span>
                <input id="cep" name="cep" type="text" required class="form-control" maxlength="9" placeholder="CEP"
                    value="{{ cep }}" onkeyup="trataCep(event)" onfocusout="buscaCep()">
                <span class="input-group-text"> <a class="fa fa-search" onclick="buscaCep()"></a></span>
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa-solid fa-road"></span>
                </span>
                <input id="rua" name="rua" type="text" required class="form-control" placeholder="Rua"
                    value="{{ rua }}" />
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa-solid fa-hashtag"></span>
                </span>
                <input id="numero" name="numero" type="text" required class="form-control" placeholder="Numero"
                    value="{{ numero }}" />
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa-solid fa-map-location-dot"></span>
                </span>
                <input id="complemento" name="complemento" type="text" class="form-control" placeholder="Complemento"
                    value="{{ complemento }}" />
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa-solid fa-tree-city"></span>
                </span>
                <input id="bairro" name="bairro" type="text" required class="form-control" readonly="true"
                    placeholder="Bairro" value="{{ bairro }}" />
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa-solid fa-city"></span>
                </span>
                <input id="cidade" name="cidade" type="text" required class="form-control" readonly="true"
                    placeholder="Cidade" value="{{ cidade }}" />
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa-brands fa-usps"></span>
                </span>
                <input id="estado" name="estado" type="text" required class="form-control" readonly="true"
                    placeholder="Estado" value="{{ estado }}" />
            </div>

            <!-- Senhas -->
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa fa-lock"></span>
                </span>
                <input id="id_password1" name="password1" type="password" class="form-control" placeholder="Senha"
                       oninput="validatePasswords()"/>
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">
                    <span class="fa fa-lock"></span>
                </span>
                <input id="id_password2" name="password2" type="password" class="form-control"
                    placeholder="Confirmação da Senha" oninput="validatePasswords()"/>
            </div>
            <span id="senha-2-error" class="error-message"></span>
            <!-- Final Senhas -->

            <div class="d-grid gap-1 mt-5">
                <button id="salvar" class="btn btn-success" type="submit">Salvar</button>
                <a id="cancelar" class="btn btn-primary" href="{% url 'home' %}">Cancelar</a>
                <a id="logout" class="btn btn-danger" href="{% url 'logout' %}">Logout</a>
                <div class="d-grid gap-1 mt-5">
                    <p></p>
                </div>
            </div>
        </form>
    </div>
</div>
<div class="d-grid gap-1 mt-5">
    <p></p>
</div>

{# TODO: Validar porque o trecho nao funciona no main.js #}
<script>

const limpaFormCep = () => {
    document.getElementById("rua").value = "";
    document.getElementById("bairro").value = "";
    document.getElementById("cidade").value = "";
    document.getElementById("uf").value = "";
};

const trataCep = (event) => {
    let input = event.target;
    input.value = mascaraDoCep(input.value);
};

const mascaraDoCep = (value) => {
    if (!value) return "";
    value = value.replace(/\D/g, "");
    value = value.replace(/(\d{5})(\d)/, "$1-$2");
    return value;
};

const meu_retorno = (conteudo) => {
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById("rua").value = conteudo.logradouro;
        document.getElementById("bairro").value = conteudo.bairro;
        document.getElementById("cidade").value = conteudo.localidade;
        document.getElementById("estado").value = conteudo.uf;
    } //end if.
    else {
        //CEP não Encontrado.
        limpaFormCep();
        alert("CEP não encontrado.");
    }
};

const buscaCep = () => {
    //Nova variável "cep" somente com dígitos.
    let cep = document.getElementById("cep").value.replace(/\D/g, "");

    //Verifica se campo cep possui valor informado.
    if (cep != "") {
        //Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if (validacep.test(cep)) {
            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById("rua").value = "...";
            document.getElementById("bairro").value = "...";
            document.getElementById("cidade").value = "...";
            document.getElementById("estado").value = "...";

            //Cria um elemento javascript.
            var script = document.createElement("script");

            //Sincroniza com o callback.
            script.src =
                "https://viacep.com.br/ws/" + cep + "/json/?callback=meu_retorno";

            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);
        } //end if.
        else {
            //cep é inválido.
            limpaFormCep();
            alert("Formato de CEP inválido.");
        }
    } //end if.
    else {
        //cep sem valor, limpa formulário.
        limpaFormCep();
    }
};

</script>

{% endblock %}

```

#### Os templates fazem uso de 'template tags' do Django, não somente como criamos o arquivo 'templatetags.py', mas, também no sentido de podermos trabalhar com lógica de forma mais fácil entre os templates e as 'views', assim como usamos as tags '{{ }}' (exemplo: "{{ valor }}"), para exibição de um determinado dado, enviado por contexto por uma view.

### Antes de entrarmos nos conceitos de valores dinâmicos, vamos ver rapidamente, os efeitos dessa alterações:
```python
def home_view(request):
    context = {
        "valor_entrada": "R$ 8.726,92",
        "valor_saida": "R$ 3.736,19"
    }
    return render(request, './home.html', context)
```


## 14. Exibição de valores do banco de dados de forma dinâmica
#### Até então, trabalhamos com valores estáticos enviados pelas views para os templates, a seguir, vamos detalhar os passos para obtermos os valores que estão salvos no nosso banco de dados.

### 14.1 Alteração em './app/urls.py', altere o código para o correspondente abaixo
#### Dessa forma, agora, temos os demais endpoints definidos, contando com: login/logout, entradas/saídas, configuração, salvamento/exclusão/edição, além de uma view adicional para outros testes.

```python
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
]
```


### 14.2 Alteração em './app/views.py', altere o código para o correspondente abaixo
#### Após as alterações em nossas 'urls', nas nossas novas 'views', iremos trabalhar em conjunto com os dados que estão salvos no banco de dados, os exibindo de forma inteligente e de fácil manutenção, tendo a possibilidade de aplicar filtros de diversas maneiras em nossas consultas.

```python
# --- COM DADOS OBTIDOS DO BANCO DE DADOS, DE FORMA DINÂMICA ---

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse


def login_view(request):
    context = {'is_show_header': 'false'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                return redirect('home')
            else:
                return redirect('login', context)
        else:
            return redirect('login', context)

    else:
        return render(request, 'login.html', context)


@login_required
def home_view(request):
    context = {
        "is_home_tab_active": "active",
    }
    return render(request, 'home.html', context)


@login_required
def entradas_view(request):
    movimentos_entrada = Movimento.objects.filter(usuario=request.user, categoria__tipo='R')
    context = {
        "is_entradas_tab_active": "active",
        "movimentos_entrada": movimentos_entrada,
    }
    return render(request, 'entradas.html', context)


@login_required
def saidas_view(request):
    movimentos_saida = Movimento.objects.filter(usuario=request.user, categoria__tipo='P')
    context = {
        "is_saidas_tab_active": "active",
        "movimentos_saida": movimentos_saida,
    }
    return render(request, 'saidas.html', context)


@login_required
def config_view(request):
    # Do jeito difícil
    if request.method == 'POST':
        usuario = Usuario.objects.get(id=request.user.id)
        usuario.first_name =  request.POST['primeiro_nome']
        usuario.last_name = request.POST['segundo_nome']
        usuario.cep = request.POST['cep']
        usuario.rua = request.POST['rua']
        usuario.numero = request.POST['numero']
        usuario.complemento = request.POST['complemento']
        usuario.bairro = request.POST['bairro']
        usuario.cidade = request.POST['cidade']
        usuario.estado = request.POST['estado']
        if request.POST['password1'] != '':
            usuario.password = make_password(request.POST['password1'])
        usuario.save()
        messages.success(request, 'Usuário atualizado com sucesso!')
        return redirect('config')

    elif request.method == 'GET':

        if request.user.is_authenticated:
            usuario = Usuario.objects.get(id=request.user.id)
            context = {"is_config_tab_active": "active",
                       "primeiro_nome": usuario.first_name,
                       "segundo_nome": usuario.last_name,
                       "cep": usuario.cep,
                       "rua": usuario.rua,
                       "numero": usuario.numero,
                       "complemento": usuario.complemento,
                       "bairro": usuario.bairro,
                       "cidade": usuario.cidade,
                       "estado": usuario.estado,
                       }

            return render(request, 'config.html', context)
        else:
            return redirect('login')


def salvar_movimento(request):
    if request.method == 'POST':
        form = MovimentoForm(request.POST)
        if form.is_valid():
            novo_movimento = form.save(commit=False)
            novo_movimento.usuario = request.user
            novo_movimento.save()

            messages.success(request, 'Item adicionado com sucesso!')
        else:
            messages.warning(request, 'Houve um problema na criação!')

        # Faz o redirecionamento de página usando HTMX, de acordo com o movimento e mostrando a mensagem.
        response = HttpResponse()
        if form.instance.categoria.tipo == 'R':
            response['HX-Redirect'] = '/entradas'
        else:
            response['HX-Redirect'] = '/saidas'

        return response
    else:
        # Parâmetros de inicialização de formulário
        form = MovimentoForm(initial_value=request.GET['tipo_movimento'])

    context = {
        'form': form,
    }
    return render(request, 'modals/modal_salvar_movimentos.html', context)


def editar_movimento(request, movimento_id):
    movimento = get_object_or_404(Movimento, pk=movimento_id)
    if request.method == 'POST':
        form = MovimentoForm(request.POST, instance=movimento)
        if form.is_valid():
            form.save()
            response = HttpResponse()
            if form.instance.categoria.tipo == 'R':
                response['HX-Redirect'] = '/entradas'
            else:
                response['HX-Redirect'] = '/saidas'

            return response
    else:
        form = MovimentoForm(instance=movimento, initial_value=movimento.categoria.tipo)
    return render(request, 'modals/modal_salvar_movimentos.html', {'form': form})


@csrf_exempt
def excluir_movimento(request, movimento_id):
    movimento = get_object_or_404(Movimento, id=movimento_id)

    if movimento.usuario == request.user:
        movimento.delete()

    response = HttpResponse()
    if movimento.categoria.tipo == 'R':
        response['HX-Redirect'] = '/entradas'
    else:
        response['HX-Redirect'] = '/saidas'

    return response

# --- COM DADOS OBTIDOS DO BANCO DE DADOS, DE FORMA DINÂMICA ---

# --- LOGOUT ---
@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
# --- LOGOUT ---


def qualquer_requisicao(request):
    to_return = {'status': 'ok'}
    json = JsonResponse(to_return)
    return json
```

#### O código atualizado inclui consultas ao banco de dados para recuperar os valores previamente salvos e também incorpora novas funcionalidades que serão aplicadas posteriormente ao longo do nosso projeto. Esses valores são enviados por contexto da mesma maneira que anteriormente. No entanto, como próximo passo, precisamos atualizar nossos templates para garantir a exibição dos dados enviados.

### Lembre-se, para executar o projeto, execute esse comando:
```bash
python manage.py runserver $IP:$PORT
```
## 15. Criação do main.js para abrir e fechar modal e para validação da senha

```bash
touch ./core/static/main.js

```

#### Acesse o arquivo main.js criado e informe o código abaixo

>main.js
```js
// Abertura dos modals
document.addEventListener("DOMContentLoaded", function () {
    const modal = new bootstrap.Modal(document.getElementById("modal"));

    htmx.on("htmx:afterSwap", function (e) {
        modal.show();
    });

    htmx.on("htmx:afterRequest", function (e) {
        modal.hide();
    });
});
// Abertura dos modals

// Validação das senhas
    function validatePasswords() {
        var senha1 = document.getElementById('id_password1').value;
        var senha2 = document.getElementById('id_password2').value;
        var errorSpan = document.getElementById('senha-2-error');

        if (senha1 !== senha2) {
            document.getElementById('id_password2').classList.add('is-invalid'); // Adiciona classe de erro ao campo
            document.getElementById('salvar').classList.add('disabled'); // Desativa o botão de salvar
        } else {
            document.getElementById('id_password2').classList.remove('is-invalid'); // Remove a classe de erro do campo
            document.getElementById('salvar').classList.remove('disabled'); // Ativa o botão de salvar
        }
    }

    document.getElementById('id_password1').addEventListener('input', validatePasswords);
    document.getElementById('id_password2').addEventListener('input', validatePasswords);
// Validação das senhas
```

### 15.1 Upload de imagem para o diretório './core/static/img'
#### Salve a imagem a seguir e adicione-a dentro do diretório de imagens:

![Alt text](images/totvs_logo_branco.png?raw=true "totvs_logo_branco")

#### Siga os passos para realizar a adição da imagem ao diretório:
#### Selecione o diretório
![Alt text](images/selecionar_diretorio_img.png?raw=true "selecionar_diretorio_img")

#### Upload Local Files
![Alt text](images/upload_local_files.png?raw=true "upload_local_files")

#### Adicione a imagem
![Alt text](images/adicionando_imagem.png?raw=true "adicionando_imagem")

#### Ao final, ficará assim
![Alt text](images/final_imagem.png?raw=true "final_imagem")

## 16. Alteração nos templates dinâmicos, de acordo com as alterações nas 'views'
### Altere os templates com os códigos atualizados a seguir:

### home.html

templates/home.html

```html
{% extends 'base.html' %}

{% block title %}TBank - Home{% endblock %}

{% block container_content %}
    <div class="card d-flex flex-wrap">
        <div class="p-3">
            <div class="card" style="background-color: rgb(15, 141, 19)">
                <h5 class="card-header">Entradas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias {{ request.user.get_entradas_total_30_dias }}</h5>
                    <button type="button" class="btn btn-primary" hx-get="/salvar_movimento/?tipo_movimento=entrada"
                            hx-target="#modalGenerico">Incluir Nova Entrada
                    </button>
                </div>
            </div>
        </div>

        <div class="p-3">
            <div class="card" style="background-color: rgb(221, 23, 23)">
                <h5 class="card-header">Saídas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias {{ request.user.get_saidas_total_30_dias }}</h5>
                    <button type="button" class="btn btn-primary" hx-get="/salvar_movimento/?tipo_movimento=saida"
                            hx-target="#modalGenerico">Incluir Nova Saída
                    </button>
                </div>
            </div>
        </div>

        <div class="p-3">
            <div class="card" style="background-color: rgb(33, 6, 204)">
                <h5 class="card-header">Balanço</h5>
                <div class="card-body">
                    <h5 class="card-title">Balanço geral nos últimos 4 meses.</h5>
                    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modChart">
                        Analisar
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal Genérico -->
    <div id="modal" class="modal fade">
        <div id="modalGenerico" class="modal-dialog" hx-target="#this">
        </div>
    </div>
    <!-- Final Modal Genérico -->

    <!-- Modal Gráfico -->
    <div class="modal fade" id="modChart" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Gráfico</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <canvas id="canvas" width="80%" height="80%"></canvas>
                </div>
            </div>
        </div>
    </div>
    <!-- Final Modal Gráfico -->
{% endblock %}


{% block extra_body_content %}
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
        {# GRÁFICO #}
        ;(function () {
            const ctx = document.getElementById("canvas").getContext("2d")
            const myChart = new Chart(ctx, {
                type: "bar",
                data: {
                    labels: ["Jul", "Ago", "Set", "Out"],
                    datasets: [
                        {
                            label: "Entradas",
                            data: [6, 7, 6, 8],
                            backgroundColor: "rgb(15, 141, 19)",
                            borderColor: "rgb(15, 141, 19)",
                            borderWidth: 1,
                        },
                        {
                            label: "Saídas",
                            data: [5, 11, 5, 5],
                            backgroundColor: "rgb(221, 23, 23)",
                            borderColor: "rgb(221, 23, 23)",
                            borderWidth: 1,
                        },
                    ],
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                        },
                    },
                },
            })
        })()
    </script>

{% endblock %}
```

### entradas.html

templates/entradas.html
```html
{% extends 'base.html' %}

{% block title %}TBank - Entradas{% endblock %}

{% include 'header.html' %}

{% block container_content %}
    <div class="card d-flex flex-wrap">
        <div class="p-3">
            <div class="card" style="background-color: rgb(15, 141, 19);">
                <h5 class="card-header">Entradas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias {{ request.user.get_entradas_total_30_dias }}</h5>
                    <button type="button" class="btn btn-primary" hx-get="/salvar_movimento/?tipo_movimento=entrada" hx-target="#modalGenerico">Incluir Nova Entrada</button>
                </div>
            </div>
        </div>

        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Data</th>
                    <th scope="col">Categoria</th>
                    <th scope="col">Descrição</th>
                    <th class="text-end" scope="col">Valor</th>
                    <th class="text-end" scope="col">Ações</th>
                </tr>
            </thead>
            <tbody>
                {% for movimento in movimentos_entrada %}
                    <tr>
                        <th scope="row">{{ movimento.data_movimento }}</th>
                        <td>{{ movimento.categoria.descricao }}</td>
                        <td>{{ movimento.descricao }}</td>
                        <td class="text-end">R$ {{ movimento.valor }}</td>
                        <td class="text-end">
                            <a type="button" class="btn btn-primary btn-sm" hx-get="{% url 'editar_movimento' movimento.id %}" hx-trigger="click" hx-target="#modalGenerico"><i class="fa-solid fa-pen-to-square"></i></a>
                            <a type="button" class="btn btn-danger btn-sm" hx-delete="/excluir_movimento/{{ movimento.id }}/" hx-confirm="Tem certeza de que deseja excluir este movimento?"><i class="fa-solid fa-x"></i></a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

    <!-- Modal Genérico -->
    <div id="modal" class="modal fade">
        <div id="modalGenerico" class="modal-dialog" hx-target="#this">
        </div>
    </div>
    <!-- Final Modal Genérico -->

{% endblock %}
```

### saidas.html

templates/saidas.html
```html
{% extends 'base.html' %}

{% block title %}TBank - Saídas{% endblock %}

{% include 'header.html' %}

{% block container_content %}
    <div class="card d-flex flex-wrap">
        <div class="p-3">
            <div class="card" style="background-color: rgb(221, 23, 23);">
                <h5 class="card-header">Saídas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias {{ request.user.get_saidas_total_30_dias }}</h5>
                    <button type="button" class="btn btn-primary" hx-get="/salvar_movimento/?tipo_movimento=saida" hx-target="#modalGenerico">Incluir Nova Saída</button>
                </div>
            </div>
        </div>

        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Data</th>
                    <th scope="col">Categoria</th>
                    <th scope="col">Descrição</th>
                    <th class="text-end" scope="col">Valor</th>
                    <th class="text-end" scope="col">Ações</th>
                </tr>
            </thead>
            <tbody>
                {% for movimento in movimentos_saida %}
                    <tr>
                        <th scope="row">{{ movimento.data_movimento }}</th>
                        <td>{{ movimento.categoria.descricao }}</td>
                        <td>{{ movimento.descricao }}</td>
                        <td class="text-end">R$ {{ movimento.valor }}</td>
                        <td class="text-end">
                            <a type="button" class="btn btn-primary btn-sm" hx-get="{% url 'editar_movimento' movimento.id %}" hx-trigger="click" hx-target="#modalGenerico"><i class="fa-solid fa-pen-to-square"></i></a>
                            <a type="button" class="btn btn-danger btn-sm" hx-delete="/excluir_movimento/{{ movimento.id }}/" hx-confirm="Tem certeza de que deseja excluir este movimento?"><i class="fa-solid fa-x"></i></a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

    <!-- Modal Genérico -->
    <div id="modal" class="modal fade">
        <div id="modalGenerico" class="modal-dialog" hx-target="#this">
        </div>
    </div>
    <!-- Final Modal Genérico -->

{% endblock %}
```
#### Dessa forma, estamos utilizando os dados que foram salvos no banco de dados, em vez dos valores estáticos.
#### Nesses códigos atualizados, estamos utilizando também os métodos 'get_entradas_total_30_dias' e 'get_saidas_total_30_dias', com a template tag '{{ request.user.MÉTODO_USADO }}'(request.user equivale ao usuário com sessão ativa no momento). Essa utilização se dá por dois métodos aplicados aos nossos modelos, em './app/models.py', no sentido de facilitarmos a reutilização do código, ou até mesmo uma manutenção simplificada.


### 17 Criação do template para o modal(criação, exclusão e edição)
#### Assim como já feito anteriormente, podemos criar o diretório dos modals, juntamente com o template, da seguinte forma em nosso terminal:
```bash
mkdir ./templates/modals
touch ./templates/modals/modal_salvar_movimento.html
```
#### ** Lembre-se, caso seu projeto esteja sendo executado, clique no terminal e com 'Ctrl + C' o interrompa, para poder digitar os comandos acima. **

### Após a criação do template, cole o código a seguir:
```html
{% load crispy_forms_tags %}

<div class="modal-content rounded-4 shadow-lg">
    <form hx-post="{{ request.path }}" hx-target="#modalGenerico" hx-swap="outerHTML">
        {% csrf_token %}
        <div class="modal-header border-bottom-0">
            <h5 class="modal-title fs-5">TESTE</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            </button>
        </div>

        <div class="modal-body">
            <!-- Campos do formulário -->
                {% crispy form %}
            <!-- Campos do formulário -->
            <div class="modal-footer flex-column align-items-stretch w-100 gap-2 pb-3 border-top-0">
                <div class="row">
                    <div class="col-md-6 d-grid gap-2">
                        <button type="submit" class="btn btn-lg btn-success btn-block">Salvar</button>
                    </div>
                    <div class="col-md-6 d-grid gap-2">
                        <button type="button" class="btn btn-lg btn-danger btn-block" data-bs-dismiss="modal">Cancelar</button>
                    </div>
                </div>
            </div>
        </div>
    </form>
</div>
```
#### O modal acima, conta com alguns recursos diferentes muito utilizados em projetos Django, como o Django-HTMX e Django-Crispy-Forms, que são melhor explicados abaixo.
#### Django-HTMX: se trata de uma extensão que podemos utilizar juntamente com o HTML, no sentido de criar interfaces de usuário interativas e dinâmicas sem a necessidade de escrevermos muito código JavaScript, baseando-se essencialmente nas tecnologias de AJAX e WebSockets.
#### Django-Crispy-Forms: simplifica a criação e personalização de formulários, tornando o código mais limpo e legível, muitas das vezes evitando até a repetição de alguns formulários. Também trabalha em conjunto com o 'crispy_bootstrap5'(pacotes de templates que, desde a versão 2.0 estão em pacotes separados), ou de acordo com a versão do bootstrap usada, em nosso caso, vamos usar o 'crispy_bootstrap5'.

### 17.2 Instalação e uso do Django-HTMX e Django-Crispy-Forms(crispy_bootstrap5)
#### Para utilizar essas bibliotecas em nosso projeto, podemos instalar dessa forma:
```bash
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install django-htmx
```

#### Assim como as colocar em nosso 'INSTALLED_APPS', em './core/settings.py':
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_htmx',
]

# Adicione essas linhas para definir os pacotes de templates
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```


### 17.3 Uso do arquivo 'forms.py'
#### Para fazermos uso de formulários no Django, geralmente usamos um arquivo chamado 'forms.py', devemos criar o arquivo assim como já feito anteriormente:
```bash
touch ./app/forms.py
```

#### Após a criação do arquivo, aplique o código a seguir:
```python
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

```
#### Aqui definimos um formulário que vamos usar tanto para criação e edição de movimentos.
#### Há possibilidade de personalizar e adicionar campos de acordo com a necessidade, assim como também a definição de campos que serão exibidos em 'Meta' e, sequencialmente, em '__init__' a definição de valores iniciais no formulário.


#### Dessa forma, estamos utilizando os dados que foram salvos no banco de dados, em vez dos valores estáticos.
#### Nesses códigos atualizados, estamos utilizando também os métodos 'get_entradas_total_30_dias' e 'get_saidas_total_30_dias', com a template tag '{{ request.user.MÉTODO_USADO }}'(request.user equivale ao usuário com sessão ativa no momento). Essa utilização se dá por dois métodos aplicados aos nossos modelos, em './app/models.py', no sentido de facilitarmos a reutilização do código, ou até mesmo uma manutenção simplificada.


### Você concluiu o tutorial, parabéns!


### Brincadeiras com o console do navegador
```js

fetch('http://127.0.0.1:8000/qualquer_requisicao')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erro:', error));


fetch('https://viacep.com.br/ws/01001000/json/')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erro:', error));
  
```


# EM CASO DE EMERGÊNCIA


### [https://github.com/matheusnogueira/unicamp-master-django](https://github.com/matheusnogueira/unicamp-master-django)