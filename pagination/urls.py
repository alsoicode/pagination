from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pagination.views',
    url(r'^set-items-per-page/$', 'set_items_per_page',
        name='set_items_per_page'),
)
