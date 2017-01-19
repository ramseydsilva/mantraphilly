from django.conf import settings
from subprocess import check_call, Popen, PIPE, STDOUT
import subprocess, os


try:
    from subprocess import DEVNULL # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')

no_output_kwargs= {'shell': True, 'stdout': PIPE, 'stderr': PIPE}
with_output_kwargs = {'shell': True}

def run_command(command):
    return check_call(command, **kwargs)

def Popen(command, no_output=True):
    kwargs = no_output_kwargs if no_output else with_output_kwargs
    process = subprocess.Popen(command, **kwargs)
    out, err = process.communicate()
    return process, out, err

def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

def pretty_print(out, info='Info:', replace_lines=True):
    out = out.decode('utf-8')
    if replace_lines:
        out = out.replace("\n", "")
    if info:
        print(info, out)
    else:
        print(out)
