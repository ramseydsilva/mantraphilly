from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.template import loader, Context
from server.utils.commandline import Popen, pretty_print
import os, subprocess, time


CONFIG_OPTIONS = {
    'settings': settings
}


def create_symlink(src, dest):
    if not os.path.exists(dest):
        os.symlink(src, dest)

class Command(BaseCommand):
    help = "Start project"

    def handle(self, *args, **options):

        call_command('configure', interactive=False)
        call_command('stop', interactive=False)

        create_symlink(os.path.join(settings.CONFIG_BUILD_DIR, "supervisor"), settings.SUPERVISOR_PATH)
        create_symlink(os.path.join(settings.CONFIG_BUILD_DIR, "nginx"), settings.NGINX_PATH)
        create_symlink(os.path.join(settings.CONFIG_BUILD_DIR, "uwsgi.ini"), settings.UWSGI_PATH)

        # build docs
        # subprocess.check_call("cd %s/docs && rm -rf build && make html" %(settings.PROJECT_PATH), shell=True)

        _, out, _ = Popen("sudo supervisorctl reload")
        time.sleep(5)
        for p in settings.PROCESSES:
            _, out, _ = Popen("supervisorctl stop %s" %(p))
            pretty_print(out, info='Stop:')
            _, out, _ = Popen("sudo supervisorctl start %s" %(p))
            pretty_print(out, info='Start:')

        subprocess.check_call("service %s restart" %(settings.WEBSERVER), shell=True)
