from django.core.management.base import BaseCommand
from django.conf import settings
from server.utils.commandline import Popen, pretty_print
import os, re, subprocess


class Command(BaseCommand):
    help = "Isac status"

    def handle(self, *args, **options):
        _, out, _ = Popen("sudo supervisorctl status")
        pretty_print(out, info='', replace_lines=False)
