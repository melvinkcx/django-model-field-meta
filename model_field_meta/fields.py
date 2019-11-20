class FieldWithMeta:
    def __init__(self, **kwargs):
        if 'meta' in kwargs:
            self._meta = kwargs['meta']
            del kwargs["meta"]
        super(self.__class__, self).__init__(**kwargs)

    def get_meta(self):
        return self._meta

    def deconstruct(self):
        """
        Makemigrations resolves the base classes of model fields using this.
        Without this, CharField() will be resolved
        to `model_field_meta.wrapper.CharField` instead of `django.db.models.fields.CharField`
        """
        base_class = self.__class__.__bases__[0]
        base_class_path = "{}.{}".format(base_class.__module__, base_class.__qualname__)
        (field_name, _, args, kwargs) = super(self.__class__, self).deconstruct()

        # The lines below are taken from Django source code: django.db.models.fields.Field.deconstruct()
        if base_class_path.startswith("django.db.models.fields.related"):
            base_class_path = base_class_path.replace("django.db.models.fields.related", "django.db.models")
        elif base_class_path.startswith("django.db.models.fields.files"):
            base_class_path = base_class_path.replace("django.db.models.fields.files", "django.db.models")
        elif base_class_path.startswith("django.db.models.fields.proxy"):
            base_class_path = base_class_path.replace("django.db.models.fields.proxy", "django.db.models")
        elif base_class_path.startswith("django.db.models.fields"):
            base_class_path = base_class_path.replace("django.db.models.fields", "django.db.models")

        return field_name, base_class_path, args, kwargs
