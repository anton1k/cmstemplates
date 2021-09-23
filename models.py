# coding: utf-8

from django.core.cache import cache
import  datetime
import uuid
import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(datetime.datetime.now().strftime('%Y/%m/%d'), filename)

class TemplateZone(models.Model):
    name = models.CharField(_('Zone name'), max_length=255)
    description = models.TextField(_('Short description'), blank=True)

    class Meta:
        verbose_name = _('Template zone')
        verbose_name_plural = _('Template zones')

    def __str__(self):
        return '%s - %s' % (self.name, self.description)

    def save(self, *args, **kwargs):
        """Обнуляет кэш шаблонов для зоны."""
        super(TemplateZone, self).save(*args, **kwargs)
        cache.delete('cmstemplates:%s' % self.name)


class TemplateFile(models.Model):
    name = models.CharField(_('Template name'), max_length=255, help_text=_('Template name, for example, "headline"'))
    zone = models.ForeignKey(TemplateZone, verbose_name=_('Zone'), related_name='files', on_delete=models.CASCADE)
    weight = models.IntegerField(_('Output order'), default=0)
    template_filename = models.CharField(_('Template file name'), max_length=500, blank=True)
    use_content = models.BooleanField(_('Use template text'), default=False)
    template_content = models.TextField(_('Template text'), blank=True)
    is_active = models.BooleanField(_('Active'), default=True)
    only_for_superuser = models.BooleanField(_('Only for superuser'), default=False)

    class Meta:
        verbose_name = _('Template file')
        verbose_name_plural = _('Template files')
        ordering = ['weight']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Обнуляет кэш шаблонов для зоны."""
        super(TemplateFile, self).save(*args, **kwargs)
        cache.delete('cmstemplates:%s' % self.zone.name)

    def source_path(self):
        """Источник шаблона для админки."""
        return self.template_filename if not self.use_content else _('template text')
    source_path.short_description = _('Source')


class Recomendet(models.Model):
    name = models.CharField(u'Название', max_length=200)
    url = models.URLField(u'Ссылка')
    icon = models.ImageField(u'Иконка', upload_to=get_file_path)
    is_active = models.BooleanField(u'Активно', default=True)

    class Meta:
        verbose_name = u'Рекомендация'
        verbose_name_plural = u'Рекомендации'

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(u'Название', max_length=200)
    logo = models.ImageField(u'Изображение', upload_to=get_file_path)
    url = models.URLField(u'Ссылка')
    is_active = models.BooleanField(u'Активно', default=True)
    sorting = models.IntegerField(u'Сортировка', default=100, blank=True)

    class Meta:
        verbose_name = u'Спецпроект'
        verbose_name_plural = u'Спецпроекты'
        ordering = ['sorting', 'pk']

    def __str__(self):
        return self.name
