from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.template import loader, Context
from server.utils.commandline import Popen, pretty_print
import os, subprocess


CONFIG_OPTIONS = {
    'settings': settings
}


def remove_symlink(src):
    try:
        os.unlink(src)
    except:
        pass

class Command(BaseCommand):
    help = "Strop project"

    def handle(self, *args, **options):

        remove_symlink(settings.SUPERVISOR_PATH)
        remove_symlink(settings.NGINX_PATH)
        remove_symlink(settings.UWSGI_PATH)

        _, out, _ = Popen("sudo supervisorctl reread")
        _, out, _ = Popen("sudo supervisorctl update")

        for p in settings.PROCESSES:
            _, out, _ = Popen("sudo supervisorctl stop %s" %(settings.PROJECT_NAME))
            pretty_print(out, info='Stop:')

        subprocess.check_call("service %s restart" %(settings.WEBSERVER), shell=True)
