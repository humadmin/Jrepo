# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

import logging
from awx import __version__ as tower_version

# Prepare the AWX environment.
from awx import prepare_env, MODE
prepare_env()

from django.core.wsgi import get_wsgi_application  # NOQA

"""
WSGI config for AWX project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

if MODE == 'production':
    logger = logging.getLogger('awx.main.models.jobs')
    try:
        fd = open("/var/lib/awx/.tower_version", "r")
        if fd.read().strip() != tower_version:
            raise Exception()
    except Exception:
        logger.error("Missing or incorrect metadata for Tower version.  Ensure Tower was installed using the setup playbook.")
        raise Exception("Missing or incorrect metadata for Tower version.  Ensure Tower was installed using the setup playbook.")

# Return the default Django WSGI application.
application = get_wsgi_application()