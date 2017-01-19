from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Restart project"

    def handle(self, *args, **options):
        #call_command('stop', interactive=False)
        call_command('start', interactive=False)

