from django import template

register = template.Library()


@register.filter
def getvars(value):
    """
    Accepts a request.GET QueryDict and strips off the 'page' parameter
    if it exists and returns any other values present
    """
    request_vars = value.copy()

    # if 'page' is already in the request_vars, remove it, as it will be
    # added later. This prevents duplicate 'page' parameters being included
    # in the return value
    if 'page' in request_vars.dict():
        del request_vars['page']

    if request_vars.dict():
        concatenator = '&'
    else:
        concatenator = ''

    return '{0}{1}'.format(concatenator, request_vars.urlencode())
