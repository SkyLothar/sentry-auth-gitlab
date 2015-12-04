from __future__ import absolute_import

from requests.exceptions import RequestException
from sentry import http
from sentry.utils import json

from .constants import API_BASE_URL


class GitLabApiError(Exception):
    def __init__(self, message='', status=None):
        super(GitLabApiError, self).__init__(message)
        self.status = status


class GitLabClient(object):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.http = http.build_session()

    def _request(self, path, access_token):
        headers = {'Authorization': 'Bearer {0}'.format(access_token)}
        url = '{0}/{1}'.format(API_BASE_URL, path.lstrip('/'))

        try:
            req = self.http.get(url, headers=headers)
        except RequestException as e:
            raise GitLabApiError(unicode(e), status=e.status_code)
        return json.loads(req.content)

    def get_user(self, access_token):
        return self._request('user', access_token)
