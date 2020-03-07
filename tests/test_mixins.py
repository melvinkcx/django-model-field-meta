from django.test import TestCase

from tests.models import Coffee


class FieldMetaMixinTestCase(TestCase):
    def setUp(self):
        Coffee.objects.all().delete()

    def _create_coffee(self):
        return Coffee.objects.create(brand="Malongo", blend="Arabica", packaging="0.5kg")

    def test_instance_get_meta(self):
        malongo_arabica = self._create_coffee()
        meta = malongo_arabica.get_field_meta("packaging")
        self.assertDictEqual(meta, Coffee.packaging_meta)

    def test_class_get_meta(self):
        meta = Coffee.get_field_meta("packaging")
        self.assertDictEqual(meta, Coffee.packaging_meta)

    def test_instance_has_meta(self):
        malongo_arabica = self._create_coffee()
        self.assertFalse(malongo_arabica.has_field_meta("brand"))
        self.assertFalse(malongo_arabica.has_field_meta("blend"))
        self.assertTrue(malongo_arabica.has_field_meta("packaging"))

    def test_class_has_meta(self):
        self.assertFalse(Coffee.has_field_meta("brand"))
        self.assertFalse(Coffee.has_field_meta("blend"))
        self.assertTrue(Coffee.has_field_meta("packaging"))
