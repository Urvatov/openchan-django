#!/usr/bin/env python

import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openchan.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(  
        ) from exc
    
    
    execute_from_command_line(sys.argv)


def run_server():
    if 'runserver' not in sys.argv:
        sys.argv.append('runserver')

def cmd():
    #python manage.py runserver
    #python manage.py makemigrations
    #python manage.py migrate
    pass

if __name__ == '__main__':
    run_server()
    main()
