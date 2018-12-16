FROM python:3.6-slim-stretch

RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
      binutils \
      build-essential \
      enchant \
      git \
      gdal-bin \
      gettext \
      libproj-dev \
      sqlite3 \
      python-gdal \
      libspatialite-dev \
      spatialite-bin \
      libsqlite3-mod-spatialite \
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
        -e git+git://github.com/flibbertigibbet/django.git@feature/add-null-layermapping-support-master#egg=Django

RUN set -ex \
    && pip install --no-cache-dir -r /usr/local/src/django/tests/requirements/py3.txt

RUN mkdir -p /usr/src
COPY ./ /usr/src
COPY ./test_spatialite.py /usr/local/src/django
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
