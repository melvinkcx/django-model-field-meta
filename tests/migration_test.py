"""
Test the migration files generated
"""
import glob

from django.core import management
from django.test import TestCase


class MigrationFileTestSuite(TestCase):
    def test_migrations_are_not_regenerated_unintentionally(self):
        migration_files = glob.glob("./tests/migrations/00*.*")
        self.assertEqual(len(migration_files), 1)

        for _ in range(1, 5):
            management.call_command("makemigrations", "tests")

        migration_files = glob.glob("./tests/migrations/00*.*")
        self.assertEqual(len(migration_files), 1)
