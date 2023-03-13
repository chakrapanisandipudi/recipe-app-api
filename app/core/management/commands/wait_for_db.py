"""
Django command to wait for database to be available
"""

from django.core.management import BaseCommand
import time

from django.db.utils import OperationalError
from psycopg2 import OperationalError as psycopg2Error


class Command(BaseCommand):
    """  Django command wait for database connection  """

    def handle(self, *args, **options):
        """ Entrypoint to command """

        self.stdout.write('Waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waitig 1 second')
                time.sleep()
        self.stdout.write(self.style.SUCCESS('Database Available..'))
