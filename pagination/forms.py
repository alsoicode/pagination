from django import forms

from pagination.constants import ITEMS_PER_PAGE_CHOICES


class ItemsPerPageForm(forms.Form):
    number = forms.ChoiceField(initial=ITEMS_PER_PAGE_CHOICES[0][1],
        choices=ITEMS_PER_PAGE_CHOICES)

    def __init__(self, *args, **kwargs):
        cache_prefix = kwargs.pop('cache_prefix', None)
        super(ItemsPerPageForm, self).__init__(*args, **kwargs)
        self.fields['cache_prefix'] = forms.CharField(
            widget=forms.HiddenInput(),
            initial=cache_prefix)


class PageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        paginator = kwargs.pop('paginator')
        try:
            page = int(kwargs.pop('page'))
        except ValueError:
            page = 1

        page_range = paginator.page_range
        choices = zip(page_range, page_range)
        super(PageForm, self).__init__(*args, **kwargs)

        self.fields['page'] = forms.ChoiceField(
            choices=choices, initial=page,
            widget=forms.Select(attrs={'class': 'span1'}))
