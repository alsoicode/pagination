from django.conf import settings


ITEMS_PER_PAGE_CHOICES = getattr(settings,
    'PAGINATION_ITEMS_PER_PAGE_CHOICES',
    (
        ('10', 10),
        ('25', 25),
        ('50', 50),
        ('100', 100),
    )
)

DEFAULT_ITEMS_PER_PAGE_START_INDEX = getattr(settings,
    'PAGINATION_DEFAULT_ITEMS_PER_PAGE_START_INDEX', 0)

ITEMS_PER_PAGE_CACHE_SUFFIX = '_items_per_page'
