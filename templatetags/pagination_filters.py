from django import template

register = template.Library()


@register.filter
def getvars(value):
    """
    Accepts a request.GET QueryDict and strips off the 'page' parameter
    if it exists and returns any other values present
    """
    request_vars = value.copy()
    if 'page' in request_vars:
        del request_vars['page']

    if request_vars.items():
        concatenator = '&'
    else:
        concatenator = ''

    return '{0}{1}'.format(concatenator, request_vars.urlencode())
