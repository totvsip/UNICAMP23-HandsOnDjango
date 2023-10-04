# --- COM DADOS ESTÁTICOS ---

# from django.shortcuts import render
#
#
# def login_view(request):
#     context = {'is_show_header': 'false'}
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         usuario = authenticate(username=username, password=password)
#         if usuario is not None:
#             if usuario.is_active:
#                 login(request, usuario)
#                 return redirect('home')
#             else:
#                 return redirect('login', context)
#         else:
#             return redirect('login', context)
#
#     else:
#         return render(request, 'login.html', context)
#
# def home_view(request):
#     context = {"is_home_tab_active": "active",
#                "valor": f'R$ {2500:,.2f}'}
#     return render(request, 'home.html', context)
#
# def entradas_view(request):
#     context = {"is_entradas_tab_active": "active",
#                "valor": f'R$ {125:,.2f}',
#                "valor_total": f'R$ {2500:,.2f}'}
#     return render(request, 'entradas.html', context)
#
# def saidas_view(request):
#     context = {"is_saidas_tab_active": "active",
#                "valor": f'R$ {125:,.2f}',
#                "valor_total": f'R$ {2500:,.2f}'}
#     return render(request, 'saidas.html', context)
#
# def config_view(request):
#     context = {"is_config_tab_active": "active",
#                }
#     return render(request, 'config.html', context)

# --- COM DADOS ESTÁTICOS ---


# --- COM DADOS OBTIDOS DO BANCO DE DADOS, DE FORMA DINÂMICA ---

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
import calendar


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
    return render(request, './templates_dinamicos/home_dinamico_02.html', context)


@login_required
def home_view(request):
    # Obter os meses com registros de movimento
    meses_com_registros = Movimento.objects.filter(usuario=request.user).dates('data_movimento', 'month').distinct()

    # Extrair os nomes dos meses
    nomes_meses = [calendar.month_name[mes.month] for mes in meses_com_registros]

    # Calcular a soma dos valores de entradas para cada mês
    entradas_por_mes = []
    for mes in meses_com_registros:
        valor_entradas_mes = Movimento.objects.filter(
            usuario=request.user,
            categoria__tipo='R',
            data_movimento__year=mes.year,
            data_movimento__month=mes.month
        ).aggregate(Sum('valor'))['valor__sum'] or 0
        entradas_por_mes.append(float(valor_entradas_mes))

    # Calcular a soma dos valores de saídas para cada mês
    saidas_por_mes = []
    for mes in meses_com_registros:
        valor_saidas_mes = Movimento.objects.filter(
            usuario=request.user,
            categoria__tipo='P',
            data_movimento__year=mes.year,
            data_movimento__month=mes.month
        ).aggregate(Sum('valor'))['valor__sum'] or 0
        saidas_por_mes.append(float(valor_saidas_mes))

    context = {
        "is_home_tab_active": "active",
        "meses_labels": nomes_meses,
        "entradas_por_mes": entradas_por_mes,
        "saidas_por_mes": saidas_por_mes,
    }
    return render(request, './templates_dinamicos/home_dinamico_02.html', context)


@login_required
def entradas_view(request):
    movimentos_entrada = Movimento.objects.filter(usuario=request.user, categoria__tipo='R')
    context = {
        "is_entradas_tab_active": "active",
        "movimentos_entrada": movimentos_entrada,
    }
    return render(request, 'templates_dinamicos/entradas_dinamico.html', context)



@login_required
def saidas_view(request):
    movimentos_saida = Movimento.objects.filter(usuario=request.user, categoria__tipo='P')
    context = {
        "is_saidas_tab_active": "active",
        "movimentos_saida": movimentos_saida,
    }
    return render(request, 'templates_dinamicos/saidas_dinamico.html', context)


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