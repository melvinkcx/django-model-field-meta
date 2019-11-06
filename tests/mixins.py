from django.test import TestCase

from tests.models import Coffee


class FieldMetaMixinTestCase(TestCase):
    def test_instance_get_meta(self):
        malongo_arabica = Coffee.objects.create(brand="Malongo", blend="Arabica", packaging="0.5kg")
        meta = malongo_arabica.get_field_meta("packaging")
        self.assertDictEqual(meta, Coffee.packaging_meta)

    def test_class_get_meta(self):
        meta = Coffee.get_field_meta("packaging")
        self.assertDictEqual(meta, Coffee.packaging_meta)
