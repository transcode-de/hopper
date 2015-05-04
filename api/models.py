# encoding: utf-8
from __future__ import unicode_literals

import json

from django.conf import settings
from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

from .forms import HopperForm


@python_2_unicode_compatible
class FormData(models.Model):
    """Represents an complete Form with meta data and form elements"""
    GET = 'GET'
    POST = 'POST'
    FORM_METHODS = (
        (GET, 'GET'),
        (POST, 'POST')
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author')
    title = models.TextField(verbose_name='Form title')
    date_created = models.DateTimeField(verbose_name='Date created', editable=False)
    date_updated = models.DateTimeField(verbose_name='Date updated', editable=False)
    action = models.TextField(verbose_name='Form action')
    enctype = models.TextField(verbose_name='Form enctype', default='multipart/form-data')
    method = models.CharField(choices=FORM_METHODS, max_length=4, verbose_name='Field method',
        default=GET)
    help_text = models.TextField(verbose_name='Help text', null=True, blank=True)
    css_classes = models.TextField(verbose_name='Form CSS classes', default='')
    elements = HStoreField()
    elements_css_classes = models.TextField(verbose_name='Field CSS classes', default='')
    html = models.TextField(default=None, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.html = HopperForm(model=self).render_as_form()
        self.elements = self.convert_values_to_string(self.elements)
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(FormData, self).save(*args, **kwargs)

    @classmethod
    def convert_to_dict(cls, elements):
        """Converts flat dict to normal dict
        The current implementation of hstore only allows flat
        dictionaries, all values of nested dicts are strings and have to
        convert to python objects."""
        converted_elements = {}
        if type(elements) != dict:
            converted_elements = json.loads(elements)
        else:
            for key, element in elements.items():
                if type(element) == str:
                    converted_elements[key] = json.loads(element)
                else:
                    converted_elements[key] = elements[key]
        return converted_elements

    @classmethod
    def convert_values_to_string(cls, elements):
        """Converts normal dict to flat dict
        The current implementation of hstore only allows flat
        dictionaries, all values of nested dicts have to convert to
        string."""
        converted_elements = {}
        for key, element in elements.items():
            converted_elements[key] = json.dumps(element)
        return converted_elements
