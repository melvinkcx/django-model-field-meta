class FieldMetaMixin:
    @classmethod
    def get_field_meta(cls, field_name):
        return cls._meta.get_field(field_name).get_meta()
