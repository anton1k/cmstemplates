from cmstemplates.models import (Projects, Recomendet, TemplateFile,
                                 TemplateZone)
from django import template
from django.conf import settings
from django.core.cache import cache
from django.template import TemplateDoesNotExist
from django.utils._os import safe_join
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def get_recomendet():
    return Recomendet.objects.filter(is_active=True)


@register.simple_tag()
def get_projects():
    return Projects.objects.filter(is_active=True)