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
