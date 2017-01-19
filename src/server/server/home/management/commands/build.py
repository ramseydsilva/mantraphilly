from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.template import loader, Context
import os, subprocess


class Command(BaseCommand):
    help = "Build project"

    def handle(self, *args, **options):
        call_command('collectstatic', interactive=False)
        call_command('migrate', interactive=False)

        if os.path.exists(os.path.join(settings.PROJECT_PATH + "/fixtures")):
            subprocess.check_call('%s/bin/%s loaddata %s/fixtures/*' %(settings.PROJECT_NAME, settings.PROJECT_ROOT, settings.PROJECT_PATH), shell=True)

        # build docs
        if os.path.exists(os.path.join(settings.PROJECT_ROOT + "/src/docs")):
            subprocess.check_call("cd %s/src/docs && rm -rf build && make html" %(settings.PROJECT_ROOT), shell=True)

        # build js
        if os.path.exists(os.path.join(settings.PROJECT_ROOT + "/src/web/web/package.json")):
            subprocess.check_call("cd %s/src/web/web && npm install" %(settings.PROJECT_ROOT), shell=True)
            subprocess.check_call("cd %s/src/web/web && ./node_modules/grunt-cli/bin/grunt build" %(settings.PROJECT_ROOT), shell=True)
