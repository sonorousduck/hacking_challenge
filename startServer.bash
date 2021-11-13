#!/bin/bash
uwsgi --socket hacking_challenge.sock --module hacking_challenge.wsgi --chmod-socket=666
