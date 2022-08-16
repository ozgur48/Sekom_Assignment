import time
import traceback
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand

class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_ready = False
        while not db_ready:
            try:
                db_conn = connections['default']
                cursor = db_conn.cursor()
                cursor.execute("SELECT count(*) FROM pg_database where datname='wheather'")
                row = cursor.fetchone()
                if row is not None:
                    db_ready = True
            except OperationalError:
                self.stdout.write('Database unavailable, waititng 1 second...')
                time.sleep(1)
            finally:
                try: cursor.close()
                except: pass
                try: db_conn.close()
                except: pass

        self.stdout.write(self.style.SUCCESS('Database available!'))