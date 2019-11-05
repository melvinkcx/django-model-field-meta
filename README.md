# django-model-field-meta

A wrapper module of `django.db.models` to allow optional metadata of model fields.

## Example

```python
from model_field_meta import models


class MyModel(models.Model):
    my_field = models.TextField(meta={"key": "value"})
```

```python
model_obj = MyModel.objects.first()

model_obj.get_meta("my_field")
# {"key": "value"}
```


s