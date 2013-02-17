from django.core.paginator import Paginator, EmptyPage

from pagination.constants import (ITEMS_PER_PAGE_CACHE_SUFFIX,
    ITEMS_PER_PAGE_CHOICES)


def get_cache_key(cache_prefix):
    return '{0}{1}'.format(cache_prefix, ITEMS_PER_PAGE_CACHE_SUFFIX)


def paginate_items(items, cache_prefix, request):
    cache_key = get_cache_key(cache_prefix)
    items_per_page = request.session.get(cache_key,
        ITEMS_PER_PAGE_CHOICES[0][1])
    page = request.GET.get('page', 1)

    paginator = Paginator(items, items_per_page)

    try:
        paginator_page = paginator.page(page)
    except EmptyPage:
        paginator_page = paginator.page(paginator.num_pages)

    return paginator_page
