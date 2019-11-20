from django.db import models as django_models
from django.db.models.fields import __all__ as django_fields

from model_field_meta.fields import FieldWithMeta


class WrappedDjangoModels:
    new_classes = {}

    def __init__(self):
        """
        Why not also wrap `django.db.models.Model` here?
        """

        # Model fields
        for field in django_fields:
            if field.endswith("Field") and field != "Field":
                self.new_classes[field] = type(field, (getattr(django_models, field),), {
                    "__init__": FieldWithMeta.__init__,
                    "_meta": None,
                    "get_meta": FieldWithMeta.get_meta,
                    "deconstruct": FieldWithMeta.deconstruct,
                })

    def __getattr__(self, attr):
        if attr in self.new_classes:
            return self.new_classes[attr]
        return getattr(django_models, attr)
