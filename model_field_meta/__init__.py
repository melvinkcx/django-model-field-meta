from model_field_meta.mixins import FieldMetaMixin
from model_field_meta.wrapper import WrappedDjangoModels

models = WrappedDjangoModels()

__all__ = ["models", "FieldMetaMixin"]
