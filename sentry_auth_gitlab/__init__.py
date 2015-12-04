from __future__ import absolute_import

from sentry.auth import register

from .provider import GitLabOAuth2Provider

register('gitlab', GitLabOAuth2Provider)
