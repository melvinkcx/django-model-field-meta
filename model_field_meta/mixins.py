class FieldMetaMixin:
    @classmethod
    def get_field_meta(cls, field_name):
        return cls._meta.get_field(field_name).get_meta()

    @classmethod
    def has_field_meta(cls, field_name):
        return hasattr(cls._meta.get_field(field_name), "_meta") \
               and cls.get_field_meta(field_name) is not None
