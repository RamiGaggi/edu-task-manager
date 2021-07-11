from django.shortcuts import render
from tasks.logger import logger


def index(request):
    """Index page."""
    logger.info('OK')
    return render(request, 'tasks/index.html')
