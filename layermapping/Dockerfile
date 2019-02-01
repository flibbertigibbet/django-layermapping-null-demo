FROM ubuntu:xenial

ENV PG_MAJOR 10

# Add repo for python 3 on 16.04
RUN set -ex; \
	apt-get update && \
        apt-get install -y software-properties-common wget && \
        add-apt-repository ppa:deadsnakes/ppa && \
        apt-get update && \
        apt-get install -y python3.7-dev

# point python3 to 3.7 (not 3.5)
RUN set -ex; \
	update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1 && \
	update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2 && \
	update-alternatives --config python3

RUN echo "PYTHON VERSION"; python3 --version

# pip
RUN set -ex; \
	wget https://bootstrap.pypa.io/get-pip.py && \
	python3 get-pip.py && \
	rm get-pip.py && \
	python3 -m pip install pip --upgrade && \
	python3 -m pip install wheel

RUN set -ex; \
  if ! command -v gpg > /dev/null; then \
    apt-get update && apt-get upgrade	 \
    apt-get install -y --no-install-recommends \
      dirmngr \
      gnupg \
    ; \
  fi

RUN set -ex; \
# pub   4096R/ACCC4CF8 2011-10-13 [expires: 2019-07-02]
#       Key fingerprint = B97B 0AFC AA1A 47F0 44F2  44A0 7FCC 7D46 ACCC 4CF8
# uid                  PostgreSQL Debian Repository
	key='B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8'; \
	export GNUPGHOME="$(mktemp -d)"; \
  ( gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --no-tty --recv-keys "$key" \
  || gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --no-tty --recv-keys "$key" \
  || gpg --keyserver keyserver.pgp.com --no-tty --recv-keys "$key" ); \
	gpg --batch --export "$key" > /etc/apt/trusted.gpg.d/postgres.gpg; \
	rm -rf "$GNUPGHOME"; \
	apt-key list

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main $PG_MAJOR" > /etc/apt/sources.list.d/pgdg.list

RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
      build-essential \
      libpq-dev \
      enchant \
      git \
      gdal-bin \
      gettext \
      postgis \
      postgresql-client-$PG_MAJOR \
    ; \
    rm -rf /var/lib/apt/lists/*;

COPY requirements.txt /tmp
RUN set -ex \
    && python3 -m pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

RUN python3 --version && python3 -m pip --version

RUN set -ex \
    && python3 -m pip install --no-cache-dir \
        --force-reinstall -U --no-clean --src /usr/local/src \
        --user \
        -e git+git://github.com/flibbertigibbet/django.git@master#egg=Django

RUN set -ex \
    && python3 -m pip install --no-cache-dir -r \
    /usr/local/src/django/tests/requirements/py3.txt

RUN mkdir -p /usr/src
COPY ./ /usr/src
COPY ./test_postgis.py /usr/local/src/django
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
