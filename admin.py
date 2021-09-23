# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.conf import settings
from django.contrib.admin import register

from .models import Recomendet, TemplateZone, TemplateFile, Projects

USE_CODEMIRROR = getattr(settings, 'ZONE_TEMPLATE_USE_CODEMIRROR', False)


class TemplateFileAdminForm(forms.ModelForm):
    """Форма с валидацией сохранения файла шаблона."""
    model = TemplateFile

    def __init__(self, *args, **kwargs):
        super(TemplateFileAdminForm, self).__init__(*args, **kwargs)

        if USE_CODEMIRROR:
            from codemirror import CodeMirrorTextarea

            self.fields['template_content'].widget = CodeMirrorTextarea(
                mode='htmlmixed',
                dependencies=('javascript', 'xml', 'css')
            )

    def clean(self):
        """Проверяет чтобы нужные поля небыли пустыми."""
        cleaned_data = super(TemplateFileAdminForm, self).clean()

        template_filename = cleaned_data.get('template_filename')
        use_content = cleaned_data.get('use_content')
        template_content = cleaned_data.get('template_content')

        if use_content:
            if not template_content:
                raise forms.ValidationError(u'Невозможно использовать пустой текст шаблона')
        else:
            if not template_filename:
                raise forms.ValidationError(u'Укажите имя файла шаблона')

        return cleaned_data


class TemplateZoneAdmin(admin.ModelAdmin):
    list_display = ['name']


class TemplateFileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'source_path', 'zone', 'weight', 'is_active']
    list_editable = ['weight', 'is_active']
    list_filter = ['zone__name', 'use_content']
    save_on_top = True
    search_fields = ['id', 'zone__name', 'weight', 'template_filename', 'template_content']
    form = TemplateFileAdminForm


class RecomendetAdmin(admin.ModelAdmin):
    pass


@register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recomendet, RecomendetAdmin)
admin.site.register(TemplateZone, TemplateZoneAdmin)
admin.site.register(TemplateFile, TemplateFileAdmin)
