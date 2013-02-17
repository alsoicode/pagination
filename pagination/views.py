from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from pagination.utils import get_cache_key


@csrf_exempt
def set_items_per_page(request):
    if request.method == 'POST':
        cache_prefix = request.POST.get('cache_prefix', None)
        number = request.POST.get('number', None)
        if cache_prefix and number:
            cache_key = get_cache_key(cache_prefix)
            request.session[cache_key] = number

        return HttpResponseRedirect(request.META['HTTP_REFERER'])
