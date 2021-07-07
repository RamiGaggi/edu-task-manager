from django.http import HttpResponse


def index(request):
    """Index page."""
    return HttpResponse('Добро пожаловать!!!!')
