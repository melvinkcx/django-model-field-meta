from typing import Iterable

from django.db import models as django_models
from django.db.models.fields import __all__ as django_fields

from model_field_meta.fields import FieldWithMeta


class WrappedDjangoModels:
    new_classes = {}

    def __init__(self):
        # Model fields
        for field in django_fields:
            if field.endswith("Field") and field != "Field":
                base_class = getattr(django_models, field)
                self.new_classes[field] = type(field, (base_class,), {
                    "__init__": FieldWithMeta.__init__,
                    "_meta": None,
                    "get_meta": FieldWithMeta.get_meta,
                    "deconstruct": FieldWithMeta.deconstruct,
                    "__module__": base_class.__module__,
                })

    def __getattr__(self, attr):
        if attr in self.new_classes:
            return self.new_classes[attr]
        return getattr(django_models, attr)

    def __dir__(self) -> Iterable[str]:
        return django_fields
