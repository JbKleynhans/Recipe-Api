from django.core.management import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError



class Command(BaseCommand):
    def handle(self, *args, **options):
        #entry point for command
        self.stdout.write("waiting for database")
        db_up = False
        while db_up==False:
            try:
                self.check(databases=["default"])
                db_up = True

            except (Psycopg2Error,OperationalError):
                self.stdout.write("database unavailable,waiting one second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("database available"))
