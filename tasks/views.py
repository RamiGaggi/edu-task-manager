from django.http import HttpResponse
from tasks.logger import logger


def index(request):
    """Index page."""
    logger.info('OK')
    return HttpResponse('Добро пожаловать!!!!')
