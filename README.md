# django-model-field-meta

![](https://github.com/melvinkcx/django-model-field-meta/workflows/tests/badge.svg)

An easy-to-use plugin to allow optional metadata of model fields. 

Compatible with `django-model-utils`, `safedelete`, etc.

Tested on Python 3+, Django 2.1+.

## Example

### Inserting metadata:

```python
from django.db import models   # Remove this 
from model_field_meta import models, FieldMetaMixin

class MyModel(FieldMetaMixin, models.Model):  # Add FieldMetaMixin
    my_field = models.TextField(meta={"key": "value"})
```

Accessing metadata:
```python
model_obj = MyModel.objects.first()

model_obj.get_field_meta("my_field")
# {"key": "value"}
```

Or, 

```python
MyModel.get_field_meta("my_field")
# {"key": "value"}
```

## Installation 

Install from PiPy:

```sh
pip install django-model-field-meta
```

or, if you are using Pipenv:

```sh
pipenv install django-model-field-meta
```

## Why metadata in model field?

In one of my Django projects, I needed to supply extra information about our model fields. 

For my purpose, `help_text` is too limited. Using code comments is not feasible as I need to use those information programatically.

Hence, `django_model_field_meta` package is created. 

## Compatibility with third-party packages

In my project, I use:
 
 * `django-model-utils` for its `InheritanceManager`.
 * `safedelete` for its `SafeDeleteModel`
 
So far, I haven't encounter any issue. Feel free to report if you do. 
 

## Issues 

If you have questions or issues using it, please create a Github issue at:

[https://github.com/melvinkcx/django-model-field-meta/issues](https://github.com/melvinkcx/django-model-field-meta/issues)



