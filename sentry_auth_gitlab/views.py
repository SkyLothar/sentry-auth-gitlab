from __future__ import absolute_import

from sentry.auth.view import AuthView

from .client import GitLabClient


class FetchUser(AuthView):
    def handle(self, request, helper):
        access_token = helper.fetch_state('data')['access_token']
        user = GitLabClient().get_user(access_token)
        helper.bind_state('user', user)
        return helper.next_step()
