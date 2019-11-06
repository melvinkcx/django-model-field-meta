import tempfile

TEMP_DIR = tempfile.TemporaryDirectory().name

INSTALLED_APPS = (
    'model_field_meta',
    'tests',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': TEMP_DIR,
    }
}

SECRET_KEY = 'THIS IS A SECRET KEY'
