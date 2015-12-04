test:
	pip install -e .
	pip install "file://`pwd`#egg=sentry-auth-gitlab[tests]"
	py.test -x
