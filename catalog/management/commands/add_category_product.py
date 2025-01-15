from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'create category and product'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('load fixture'))
