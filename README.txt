Установка:

1. Добавить 'cmstemplates' в INSTALLED_APPS
2. Добавить 'cmstemplates.loaders.Loader' в конец TEMPLATE_LOADERS
3. Указать директорию с шаблонами:

ZONE_TEMPLATES_DIR = os.path.join(BASE_DIR, 'zone_templates')

4. Создать директорию 'zone_templates' рядом с файлом settings.py
5. Выполнить ./manage.py migrate cmstemplates
6. Зайти в админку и создать зону шаблона
7. В шаблон зону можно добавить таким образом:
{% include "<название зоны>" %}

Если хочется использовать codemirror:

В настройки добавить и установить зависимости:
ZONE_TEMPLATE_USE_CODEMIRROR = True

Установка зависимостей:

1. source env/bin/activate
2. pip install django-codemirror-widget
3. cd project_name/static/vendor
4. wget http://codemirror.net/codemirror.zip
5. unzip codemirror.zip
6. mv codemirror-4.2 codemirror
7. Добавить в SETTINGS.py:

CODEMIRROR_PATH = 'vendor/codemirror'
CODEMIRROR_THEME = 'default'
CODEMIRROR_CONFIG = {'lineNumbers': True}


Итоговые настройки должны выглядеть как-то так:

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    'cmstemplates.loaders.Loader',
)

# cmstemplates
ZONE_TEMPLATES_DIR = os.path.join(BASE_DIR, 'zone_templates')
ZONE_TEMPLATE_USE_CODEMIRROR = True

# codemirror
CODEMIRROR_PATH = 'vendor/codemirror'
CODEMIRROR_THEME = 'default'
CODEMIRROR_CONFIG = {'lineNumbers': True}
