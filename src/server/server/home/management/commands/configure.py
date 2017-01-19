from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.template import loader, Context
import os, subprocess


CONFIG_OPTIONS = {
    'settings': settings
}

class Command(BaseCommand):
    args = '<config_file>'
    help = "Configure project for deployment"

    def config_file(self, root, f):
        config_file = os.path.join(settings.CONFIG_BUILD_DIR, f)
        t = loader.get_template("config/" + f)
        c = Context(CONFIG_OPTIONS)
        rendered = t.render(c)
        with open(config_file, "w") as text_file:
            text_file.write(rendered)

    def handle(self, *args, **options):

        if len(args):
            self.config_file(settings.CONFIG_TEMPLATE_DIR, args[0])
        else:
            # Create config build dir
            subprocess.check_call("mkdir -p %s" %(settings.CONFIG_BUILD_DIR), shell=True)
            for f in os.listdir(settings.CONFIG_TEMPLATE_DIR):
                if os.path.isfile(os.path.join(settings.CONFIG_TEMPLATE_DIR, f)):
                    self.config_file(settings.CONFIG_TEMPLATE_DIR, f)
