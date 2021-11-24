from django.shortcuts import render
from django.http import HttpResponse
from challenges.models import Challenge
import os
import subprocess
import re
import random
from django.contrib.auth.decorators import login_required
from time import strftime


@login_required()
def index(request):
    return render(request, 'whiteBoxHacking/index.html')

@login_required()
def showViews(request):
    return render(request, 'views.py')

BLACKLIST = [
        "ash", "awk", "bash", "bc", "bunzip2", "bzip2", "chgrp", "chmod",
        "chown", "chsh", "compress", "cp", "cpio", "dash", "du", "env",
        "factor", "finger", "fish", "grep", "gunzip", "gzip", "ifconfig", "ip",
        "iwconfig", "journalctl", "ksh", "locate", "mkdir", "mount", "mv",
        "netcat", "netstat", "nmap", "ping", "python", "python2", "python3",
        "reboot", "rm", "rmdir", "sed", "sh", "shutdown", "sleep", "systemctl",
        "tar", "telinit", "touch", "tree", "umount", "unzip", "xxd", "xz",
        "zip", "zsh",
        ]

WHITELIST = ['echo', 'printf', 'pwd', 'tty', 'cal', 'figlet']

NOOP = ["true", "false", "cd", "fg", "bg", "jobs", "pushd", "popd"]

NOT_A_TTY = [
        "emacs", "joe", "less", "man", "more", "nano", "nethack", "nvim", "pg",
        "vi", "vim",
        ]

FORTUNES = [
"""Twenty percent of all input forms filled out by people contain bad data.

    -- Vic Vyssotsky
       Bell Labs""",

"""Each new user of a new system uncovers a new class of bugs.

    -- Brian Kernighan
       Bell Labs""",

"""When in doubt, use brute force.

    -- Ken Thompson
       Bell Labs""",

"""The structure of a system reflects the structure of the organization that built it.

    -- Richard E. Fairley
       Wang Institute""",

"""Whenever possible, steal code.

    -- Tom Duff
       Bell Labs""",

"""If you lie to the computer, it will get you.

    -- Perry Farrar
       Germantown, Maryland""",

"""Furious activity is no substitute for understanding.

    -- H. H. Williams
       Oakland, California
       September 1985""",
        ]

CWD = 'whiteBoxHacking'
HOSTNAME = "docker-l-4vcpu-7gb-slc13-37"
UID = 1337
USERNAME = "hackerman"

# !!! SECURITY NOTICE !!!
# 'shell' should ALWAYS be False; otherwise, students can inject extra commands after ";", "&", etc.
OPTS = {'shell': False, 'cwd': CWD, 'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}

@login_required()
def unix(request):
    if request.GET and 'unix' in request.GET:
        cmdline = request.GET['unix']

        print(f"\n>>> UNIX: Running '{cmdline}' <<<")  # DELETE ME

        if cmdline == "":
            return HttpResponse("<pre>bash: : command not found</pre>")

        # filter out empty arguments found after splitting the command line on whitespace
        args = list(filter(None, re.split('\s+', cmdline)))
        cmd = args.pop(0)
        print(f">>> UNIX: cmd='{cmd}' args={args} <<<\n")  # DELETE ME

        if cmd in NOOP:
            return HttpResponse(f"<pre></pre>")

        elif "../" in cmd or cmd.startswith("/"):
            return HttpResponse(f"<pre>bash: {cmd}: command not found</pre>")

        elif cmd == 'ls':
            args = filter(lambda s: not s.startswith('/') and '..' not in s, args)
            result = subprocess.run([cmd, *args], **OPTS)
            return HttpResponse(f"<pre>{result.stdout.decode('utf-8') + result.stderr.decode('utf-8')}</pre>")

        elif cmd == "cat":
            if len(args) == 1 and args[0] == '.env':
                challenge7 = Challenge.objects.get(templateValue=7)
                return HttpResponse(f"<pre>Challenge 7 Flag: {challenge7.flag}</pre>")
            else:
                args = filter(lambda s: not s.startswith('/') and '..' not in s, args)
                result = subprocess.run([cmd, *args], **OPTS)
                return HttpResponse(f"<pre>{result.stdout.decode('utf-8') + result.stderr.decode('utf-8')}</pre>")

        elif cmd in WHITELIST:
            args = filter(lambda s: not s.startswith('/') and '..' not in s, args)
            result = subprocess.run([cmd, *args], **OPTS)
            return HttpResponse(f"<pre>{result.stdout.decode('utf-8') + result.stderr.decode('utf-8')}</pre>")

        elif cmd in BLACKLIST:
            return HttpResponse(f"<pre>bash: {cmd}: Permission denied</pre>")

        elif cmd in NOT_A_TTY:
            return HttpResponse(f"<pre>{cmd}: stdin is not a tty</pre>")

        # fake command output
        elif cmd == 'df':
            return HttpResponse("<pre>Filesystem     1K-blocks     Used Available Use% Mounted on<br/>/dev/vda1       25226960 18668320   6542256  75% /</pre>")

        elif cmd == 'fortune': # Encourage students with a random hint
            # F strings freaked out at a backslash. This is a hacky way to combat this
            newlineCharacter = '\n'
            return HttpResponse(f"<pre>{re.sub('{newlineCharacter}', '<br/>', random.choice(FORTUNES))}</pre>")

        elif cmd == 'free':
            return HttpResponse("<pre> total        used        free      shared  buff/cache   available<br/>Mem:        1004892      486940       87752        3372      430200      347140<br/>Swap:             0           0           0                    </pre>")

        elif cmd == 'hostname':
            if args != []:
                return HttpResponse(f"<pre>{HOSTNAME}</pre>")
            else:
                return HttpResponse(f"<pre>hostname: you must be root to change the host name</pre>")

        elif cmd == 'id':
            return HttpResponse(f"<pre>uid={UID}({USERNAME}) gid={UID}({USERNAME}) groups={UID}({USERNAME})</pre>")

        elif cmd == 'sudo':
            return HttpResponse(f"<pre>{USERNAME} is not in the sudoers file.   This incident will be reported.</pre>")

        elif cmd == 'uptime':
            return HttpResponse(f"<pre>{strftime('%H:%M:%S')} up 1337 days, 13:37,  3 users,  load average: 0.05, 0.02, 0.01</pre>")

        elif cmd == 'whoami' or cmd == 'who':
            return HttpResponse(f"<pre>{USERNAME}</pre>")

        else:
            return HttpResponse(f"<pre>bash: {cmd}: command not found</pre>")
    else:
        return HttpResponse("<pre>bash: : command not found</pre>")


@login_required()
def cookieValidation(request):
    challenge = Challenge.objects.get(templateValue=9)
    if request.COOKIES.get('FORSPARTA!') == "HYAAAAAA!HYAAAAAA!HYAAAAAA!":
        return HttpResponse(f"<pre>{challenge.flag}</pre>")
    else:
        return HttpResponse("<h2>Not Authorized</h2><p>Go back and try again</p>")
