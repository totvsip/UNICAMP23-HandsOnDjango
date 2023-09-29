UNICAMP - HANDS ON

# HANDS ON DJANGO FRAMEWORK by TOTVS IP/TM

## 1. Acessar nosso ambiente de desenvolvimento na nuvem

### 1.1 Acesse o link abaixo

[//]: # (```url)

[//]: # (https://console.aws.amazon.com)

[//]: # (```)
### [https://console.aws.amazon.com](https://console.aws.amazon.com)

### 1.2 Selecione a opção "Usuário do IAM" e informe o ID da conta
![Alt text](images/cloud9-01.png?raw=true "cloud9-01")

### 1.3 Insira seu usuário e senha para acessar o AWS
![Alt text](images/cloud9-02.png?raw=true "cloud9-02")

### 1.4 Clique na barra de pesquisa(Search) na parte superior da página

![Alt text](images/cloud9-03.png?raw=true "cloud9-03")

### 1.5 Escreva 'cloud9' e selecione a primeira opção

![Alt text](images/cloud9-04.png?raw=true "cloud9-04")

### 1.6 Acesse o 'cloud9' e expanda o menu lateral
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

### 2.5 (Não use o código abaixo, ele serve apenas para exemplo) Nesse momento o, ideal seria criar um ambiente virtual, que poderia ser feito da forma abaixo, no entando, vamos utilizar o ambiente do Cloud9 para que o Debug seja mais simples.
            
            ```bash
            python3 -m venv venv
            ```
            
            ## Ativar o ambiente virtual
            
            ```bash
            source venv/bin/activate
            ```

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


## 6 Criar diretórios auxiliares do projeto
```bash
mkdir templates
mkdir core/static
mkdir uploads
```

![Alt text](images/cloud9-diretorios_auxiliares.png?raw=true "Cloud9-diretorios_auxiliares")
#### Para isso, deve-se voltar a seleção do terminal principal (o mesmo em que fizemos os comandos iniciais), lembre-se de clicar no interior do terminal para levar o foco até ele, após, use o comando 'Ctrl + C', para interromper a execução.
#### Dessa forma, é possível voltarmos a digitar os comandos necessários, no caso, crie os diretórios informados acima, com os comandos 'mkdir'.


![Alt text](images/cloud9-28.png?raw=true "Cloud9-28")

### 7. Alterar o arquivo './core/settings.py' para o nosso projeto

### 7.1 Adicionar o import do módulo "os"

```python
import os
```
![Alt text](images/cloud9-29.png?raw=true "Cloud9-29")

### 7.2 Adicionar a linha abaixo no arquivo './core/settings.py', para definir um novo modelo de usuário como padrão

```python
AUTH_USER_MODEL = 'app.Usuario'
```

### 7.3 Adicionar a linha abaixo no arquivo './core/settings.py', para utilizar como referência da versão publicada do projeto

```python
# Controle da versão do sistema
APP_VERSION = '0.1.001'
```
![Alt text](images/cloud9-30.png?raw=true "Cloud9-30")

### 7.4 Alterar a Linguagem Padrão e o Fuso Horário no Django, em './core/settings.py'

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

![Alt text](images/cloud9-31.png?raw=true "Cloud9-31")

### 7.5 Alterar os diretórios dos arquivos estáticos e mídia

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

### 7.6 Alterar o diretório dos templates

### ** Antes das alterações **

![Alt text](images/cloud9-34.png?raw=true "Cloud9-34")

```python
'DIRS': [os.path.join(BASE_DIR, 'templates/')],
```

### ** Após as alterações **

![Alt text](images/cloud9-35.png?raw=true "Cloud9-35")

### 7.7 Configurar a sessão de bibliotecas, no arquivo './core/settings.py', para contemplar o arquivo 'templatetags'

### ** Antes das alterações **

![Alt text](images/cloud9-35.png?raw=true "Cloud9-35")

```python
            'libraries': {
                'templatetags': 'app.templatetags',
            }
```
### ** Observação: a configuração deve ser inserida dentro do trecho 'OPTIONS'. **
### ** Após as alterações.

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

### 7.8 Uso de templatetags
#### As 'templatetags' no Django, são construções utilizadas geralmente com o prefixo '{%  %}', para incorporar lógicas nos modelos HTML.
```html
{% load templatetags %}
{% minha_templatetag parametro1 parametro2 %}
```

### Deve-se criar o arquivo 'templatetags.py', no diretório './app', para isso, há duas formas de fazermos essa criação:
#### Executando o comando no terminal:
```bash
touch ./app/templatetags.py
```

#### Ou então, clicar com o botão direito sobre o diretório './app' e em seguida 'New File', com o nome 'templatetags.py':
![Alt text](images/cloud9-new_file_templatetags.png?raw=true "Cloud9-new_file_templatetags")

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

## Alterar o arquivo '.core/urls.py' para o nosso projeto e criar o arquivo 'urls.py' no diretório './app', para a nossa aplicação.

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
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Criando o arquivo 'urls.py' em './app', para isso, podemos seguir o mesmo passo do arquivo 'templatetags.py', criado anteriormente.
#### Executando o comando no terminal, ou então, clique com o botão direito no diretório './app' e 'New File' com o nome 'urls.py':
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
    path('login', view.login_view, name='login'),
    path('entradas', view.entradas_view, name='entradas'),
    path('saidas', view.saidas_view, name='saidas'),
    path('config', view.config_view, name='config'),
]
```

## Definição de 'views.py', devemos acessar o arquivo './app/views.py' e adicionar o seguinte código:
```python
from django.shortcuts import render


def login_view(request):
    context = {'is_show_header': 'false'}
    return render(request, 'login.html', context)

def home_view(request):
    context = {"is_home_tab_active": "active",
               }
    return render(request, 'home.html', context)

def entradas_view(request):
    context = {"is_entradas_tab_active": "active",
               }
    return render(request, 'entradas.html', context)

def saidas_view(request):
    context = {"is_saidas_tab_active": "active",
               }
    return render(request, 'saidas.html', context)

def config_view(request):
    context = {"is_config_tab_active": "active",
               }
    return render(request, 'config.html', context)
```

#### Cada uma das 'views' correspondem a um endpoint, que definimos anteriormente no arquivo 'urls.py', dessa forma, quando acessarmos algum desses domínios, automaticamente a função correspondente irá ser executada.
#### No caso, as 'views' demonstradas estão renderizando os templates HTML e enviando um contexto(Um dicionário Python que contém dados que serão passados de uma view para um template HTML).


## Criar o modelo de usuário e os demais modelos também no arquivo models.py

```python
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

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


class Categoria(models.Model):
    class Meta:
        verbose_name_plural = "Categoria"
        verbose_name = "Categorias"

    tipo = models.CharField('Tipo', max_length=1, choices=tipo_operacao_choices, default="P")
    descricao = models.CharField('Descrição', max_length=100)
    data_criacao = models.DateField('Data de Inclusão', default=datetime.now, blank=True)

    def __str__(self):
        return '%s - (%s)', self.tipo, self.descricao


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
        return '%s - %s (%s)', self.categoria.descricao, self.descricao, self.valor
```
### Após adicionar o código anterior, devemos executar dois comandos no terminal, na seguinte ordem:
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

## Criar as definições de administração para acessarmos o banco de dados e visualizar nossa estrutura de dados no arquivo admin.py
    
```python
from django.contrib import admin

from app.models import Usuario, Categoria, Movimento


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'cidade')
    list_filter = ('estado',)
    # search_fields = ('firt_name', 'last_name', 'cidade', 'estado')
    list_per_page = 30
    ordering = ('first_name',)


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

```

## Criar um super usuário

```bash
python manage.py createsuperuser
```

## Entendendo o admin e os modelos de dados

### Deve-se adicionar ao arquivo './core/settings.py' o seguinte trecho correspondente ao domínio do projeto:
#### Atente-se que, a Url deve estar sem a '/' final, assim como o exemplo abaixo, altere a Url para a do seu projeto
```python
CSRF_TRUSTED_ORIGINS = ['https://98d9aa5b75664f7689c4149e247f8b25.vfs.cloud9.us-east-2.amazonaws.com',]
```

### Execute a aplicação com:
```bash
python manage.py runserver $IP:$PORT
```

### Após isso, acessar o admin com:
```url
[Url do projeto]/admin
```

## Templates
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

    <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"
            integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA=="
            crossorigin="anonymous"
            referrerpolicy="no-referrer"
    />

    {% block extra_header_content %}
    {% endblock %}
</head>
<body>
<div class="container">

    {% show_header_menu request as show_menu %}
    {% if show_menu %}
        {% include 'header.html' %}
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
{% block title %}TBank Entradas{% endblock %}

{% block container_content %}
    <div class="card d-flex flex-wrap">

        <div class="p-3">
            <div class="card" style="background-color: rgb(15, 141, 19);">
                <h5 class="card-header">Entradas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias R$ 8.922,93</h5>
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
                <td class="text-end">R$ 123,87</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">R$ 123,87</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">R$ 123,87</td>
            </tr>
            </tbody>
        </table>

    </div>
{% endblock %}
```

### home.html

templates/home.html
```html
{% extends 'base.html' %}

{% block title %}TBank{% endblock %}

{% block container_content %}
    <div class="card d-flex flex-wrap">
        <div class="p-3">
            <div class="card" style="background-color: rgb(15, 141, 19)">
                <h5 class="card-header">Entradas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias R$ 8.922,93</h5>
                    <a href="nav_tabs_base.html" class="btn btn-primary"
                    >Incluir nova Entrada</a
                    >
                </div>
            </div>
        </div>

        <div class="p-3">
            <div class="card" style="background-color: rgb(221, 23, 23)">
                <h5 class="card-header">Saídas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias R$ 8.922,93</h5>
                    <a href="nav_tabs_base.html" class="btn btn-primary"
                    >Incluir nova Saída</a
                    >
                </div>
            </div>
        </div>

        <div class="p-3">
            <div class="card" style="background-color: rgb(33, 6, 204)">
                <h5 class="card-header">Balanço</h5>
                <div class="card-body">
                    <h5 class="card-title">Balanço geral nos útumos 30 dias.</h5>
                    <a href="nav_tabs_base.html" class="btn btn-primary">Analisar</a>
                </div>
            </div>
        </div>
    </div>

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
  <form class="form-signin">
    <h1 class="h3 mb-4 font-weight-normal">Faça o seu login</h1>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1"
        ><span class="fa fa-user"></span
      ></span>
      <input
        type="text"
        class="form-control"
        placeholder="Usuário"
        aria-label="Usuário"
        aria-describedby="basic-addon1"
      />
    </div>

    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1"
        ><span class="fa fa-lock"></span
      ></span>

      <input
        type="text"
        class="form-control"
        placeholder="Senha"
        aria-label="Username"
        aria-describedby="basic-addon1"
      />
    </div>

    <div class="d-grid gap-1 mt-5">
      <a class="btn btn-primary" href="{% url 'home' %}" type="button">Login</a>
    </div>

  </form>

</div>

{% endblock %}
```

### entradas.html

templates/entradas.html

```html
{% extends 'base.html' %}

{% block title %}TBank Entradas{% endblock %}

{% block container_content %}
    <div class="card d-flex flex-wrap">

        <div class="p-3">
            <div class="card" style="background-color: rgb(15, 141, 19);">
                <h5 class="card-header">Entradas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias R$ 8.922,93</h5>
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
                <td class="text-end">R$ 123,87</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">R$ 123,87</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">R$ 123,87</td>
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

{% block title %}TBank Saídas{% endblock %}

{% block container_content %}
    <div class="card d-flex flex-wrap">

        <div class="p-3">
            <div class="card" style="background-color: rgb(221, 23, 23);">
                <h5 class="card-header">Saídas</h5>
                <div class="card-body">
                    <h5 class="card-title">Total nos últimos 30 dias R$ 8.922,93</h5>
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
                <td class="text-end">R$ 123,87</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">R$ 123,87</td>
            </tr>
            <tr>
                <th scope="row">10/10/10</th>
                <td>Alimentação</td>
                <td>Almoço</td>
                <td class="text-end">R$ 123,87</td>
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


            <form class="form-signin">

                <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">
          <span class="fa fa-user"></span>
        </span>
                    <input
                            type="text"
                            class="form-control"
                            placeholder="Usuário"
                            readonly="true"
                            value="Usuário Teste"
                    />
                </div>

                <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">
          <span class="fa-solid fa-envelopes-bulk"></span>
        </span>
                    <input
                            type="text"
                            class="form-control"
                            placeholder="CEP"
                    />
                </div>

                <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">
          <span class="fa-solid fa-road"></span>
        </span>
                    <input
                            type="text"
                            class="form-control"
                            readonly="true"
                            placeholder="Rua"
                    />
                </div>

                <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">
          <span class="fa-solid fa-hashtag"></span>
        </span>
                    <input
                            type="text"
                            class="form-control"
                            placeholder="Numero"
                    />
                </div>

                <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">
          <span class="fa-solid fa-map-location-dot"></span>
        </span>
                    <input
                            type="text"
                            class="form-control"
                            placeholder="Complemento"
                    />
                </div>

                <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">
          <span class="fa-solid fa-city"></span>
        </span>
                    <input
                            type="text"
                            class="form-control"
                            readonly="true"
                            placeholder="Cidade"
                    />
                </div>

                <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">
          <span class="fa-brands fa-usps"></span>
        </span>
                    <input
                            type="text"
                            class="form-control"
                            readonly="true"
                            placeholder="Estado"
                    />
                </div>

                <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">
          <span class="fa fa-lock"></span>
        </span>
                    <input
                            type="password"
                            class="form-control"
                            placeholder="Senha"
                    />
                </div>

                <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">
          <span class="fa fa-lock"></span>
        </span>
                    <input
                            type="password"
                            class="form-control"
                            placeholder="Confirmação da Senha"
                    />
                </div>

                <div class="d-grid gap-1 mt-5">
                    <a class="btn btn-success" href="#" type="submit">Salvar</a>
                    <a class="btn btn-primary" href="{% url 'home' %}" type="submit">Cancelar</a>
                    <a class="btn btn-danger" href="{% url 'login' %}" type="submit">Logout</a>
                </div>
            </form>
        </div>
    </div>

    <p class="mt-5 mb-3 text-muted">TOTVS IP/TM ©2023</p>

{% endblock %}
```

## Caso não esteja executando, executar a aplicação e obter o resultado final

```bash
python manage.py runserver $IP:$PORT
```

## Você concluiu o tutorial, parabéns!
