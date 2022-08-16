
from django.core.management import BaseCommand

from weather.models import Provience


class Command(BaseCommand):
 
    def handle(self, *args, **options):
        p = Provience(name = "Mugla",provienceId = 48)
        p.save()
        p.town_set.create(name = "Ortaca")
        p.town_set.create(name="Dalaman")
        p.save()

