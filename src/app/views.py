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

