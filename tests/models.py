from model_field_meta import models, FieldMetaMixin


class Coffee(FieldMetaMixin, models.Model):
    packaging_meta = {"choices": {
        "kg": (0.5, 1, 2, 5, 10, 15, 20),
    }}

    brand = models.CharField(max_length=512)
    blend = models.CharField(max_length=512, meta=None)
    packaging = models.TextField(meta=packaging_meta)
