FROM ubuntu:bionic

RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
      build-essential \
      libpq-dev \
      enchant \
      git \
      gdal-bin \
      gettext \
      default-libmysqlclient-dev \
      default-mysql-client \
      python-dev \
      python-pip \
      python-setuptools \
    ; \
    rm -rf /var/lib/apt/lists/*;

COPY requirements.txt /tmp
RUN set -ex \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

RUN set -ex \
    && pip install --no-cache-dir \
        --force-reinstall -U --no-clean --src /usr/local/src \
        --user \
        -e git+git://github.com/flibbertigibbet/django.git@feature/add-null-layermapping-support#egg=Django

RUN set -ex \
    && pip install --no-cache-dir -r /usr/local/src/django/tests/requirements/py2.txt \
    && pip install --no-cache-dir -r /usr/local/src/django/tests/requirements/mysql.txt

RUN mkdir -p /usr/src
COPY ./ /usr/src
COPY ./test_mysql.py /usr/local/src/django
WORKDIR /usr/src

CMD ["--workers=4", \
     "--timeout=60", \
     "--bind=0.0.0.0:8080", \
     "--log-level=info", \
     "--access-logfile=-", \
     "--access-logformat=%({X-Forwarded-For}i)s %(h)s %(l)s %(u)s %(t)s \"%(r)s\" %(s)s %(b)s \"%(f)s\" \"%(a)s\"", \
     "--error-logfile=-", \
     "-kgevent", \
     "layermapping.wsgi"]

ENTRYPOINT ["/usr/local/bin/gunicorn"]
