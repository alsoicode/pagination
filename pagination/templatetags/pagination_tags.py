from django import template

from pagination.constants import (ITEMS_PER_PAGE_CHOICES,
    DEFAULT_ITEMS_PER_PAGE_START_INDEX)
from pagination.forms import ItemsPerPageForm, PageForm
from pagination.templatetags.pagination_filters import getvars
from pagination.utils import get_cache_key

register = template.Library()


@register.inclusion_tag('pagination/items-per-page-form.html',
    takes_context=True)
def items_per_page_form(context, cache_prefix, items):
    """
    `items` is expected to be a django Paginator.Page instance
    """
    request = context.get('request')

    cache_key = get_cache_key(cache_prefix)

    try:
        items_per_page = request.session.get(cache_key,
            ITEMS_PER_PAGE_CHOICES[DEFAULT_ITEMS_PER_PAGE_START_INDEX][1])
    except IndexError:
        items_per_page = ITEMS_PER_PAGE_CHOICES[0][1]

    form = ItemsPerPageForm(request.POST or None,
        cache_prefix=cache_prefix, initial={'number': items_per_page})
    return {'form': form, 'items': items}


@register.inclusion_tag('pagination/paginator.html', takes_context=True)
def paginator(context, items):
    """
    `items` is expected to be a django Paginator.Page instance
    """
    request = context.get('request')

    form = PageForm(request.POST or None, paginator=items.paginator,
        page=request.GET.get('page', 1))

    return {'items': items, 'form': form, 'request': request}


@register.simple_tag
def form_action(request):
    return '{}?{}'.format(request.path, getvars(request.GET)[1:])
