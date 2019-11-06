from django.test import TestCase

from model_field_meta import models


class FieldMetaTestSuite(TestCase):
    def test_empty_meta(self):
        field = models.TextField()
        self.assertFalse(field.get_meta())

    def test_simple_meta(self):
        field = models.TextField(meta="a simple value")
        self.assertEqual(field.get_meta(), "a simple value")

    def test_complex_meta(self):
        class Options:
            food_options = (
                ("1", "Pizza"),
                ("2", "Sushi"),
                ("3", "Ratatouille"),
            )

        field = models.TextField(meta={"options": Options.food_options})
        self.assertDictEqual(field.get_meta(), {"options": Options.food_options})
