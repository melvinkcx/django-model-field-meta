import os

import django
from django.core import management

os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
django.setup()

management.call_command("makemigrations", "tests")
management.call_command("migrate")
