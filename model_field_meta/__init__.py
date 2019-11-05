"""
model_field_meta.models

This module is meant to wrap over django.db.models

Goals:
1. Add metadata to model fields:

    models.TextField(meta={"key":"value"})  # Consider to seal the value of meta

2. Accessing field meta:

    > <ModelObj>.<field>._meta
    {"key": "value"}

    OR
s
    > <ModelObj>.get_meta(<field>)
    {"key": "value"}

"""
from model_field_meta.wrapper import WrappedDjangoModels

models = WrappedDjangoModels()

__all__ = ["models"]
