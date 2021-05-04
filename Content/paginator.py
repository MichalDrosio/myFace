

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import request


def pag(request, date):
    paginator = Paginator(date, 3)
    page = request.GET.get('page', 1)
    try:
        date = paginator.page(page)
    except PageNotAnInteger:
        date = paginator.page(1)
    except EmptyPage:
        date = paginator.page(paginator.num_pages)
    return date