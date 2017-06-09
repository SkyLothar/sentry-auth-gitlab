from __future__ import absolute_import, print_function

from django.conf import settings

CLIENT_ID = getattr(settings, 'GITLAB_APP_ID', None)
CLIENT_SECRET = getattr(settings, 'GITLAB_APP_SECRET', None)

BASE_DOMAIN = getattr(settings, 'GITLAB_BASE_DOMAIN', None)
SCHEME = getattr(settings, 'GITLAB_HTTP_SCHEME', 'https')
API_VERSION = getattr(settings, 'GITLAB_API_VERSION', 3)

ACCESS_TOKEN_URL = '{0}://{1}/oauth/token'.format(SCHEME, BASE_DOMAIN)
AUTHORIZE_URL = '{0}://{1}/oauth/authorize'.format(SCHEME, BASE_DOMAIN)
API_BASE_URL = '{0}://{1}/api/v{2}'.format(SCHEME, BASE_DOMAIN, API_VERSION)

SCOPE = 'api'
