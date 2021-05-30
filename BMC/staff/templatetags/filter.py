from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
register = template.Library()


def pagination(request,modelobj):
    page = request.GET.get('page', 1)
    paginator = Paginator(modelobj, 5)
    try:
        pageobj = paginator.page(page)
    except PageNotAnInteger:
        pageobj = paginator.page(1)
    except EmptyPage:
        pageobj = paginator.page(paginator.num_pages)
    return pageobj

@register.simple_tag
def getempsearchname(request)->str:
    search = request.GET.get('emp_search','')
    return search


