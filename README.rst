GitLab Auth for Sentry
======================

An SSO provider for Sentry which enables GitLab Login

Install
-------

::

    $ pip install https://github.com/skylothar/sentry-auth-gitlab/archive/master.zip

Setup
-----

Create a new application under your GitLab.
Enter the **Authorization callback URL** as the prefix to your Sentry installation:

::

    http(s?)://sentry.example.com/


Once done, grab your API keys and drop them in your ``sentry.conf.py:

.. code-block:: python

    GITLAB_APP_ID = "APP-ID"
    GITLAB_APP_SECRET = "APP-SECRET"
    GITLAB_BASE_DOMAIN = "git.example.com"


Optionally you may also specify the api version and scheme:

.. code-block:: python

    GITLAB_API_VERSION = 3
    GITLAB_HTTP_SCHEME = "https"
