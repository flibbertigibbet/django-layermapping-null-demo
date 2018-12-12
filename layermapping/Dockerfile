FROM python:3.6-slim-stretch

ENV PG_MAJOR 10
ENV PG_VERSION 10.6-1.pgdg90+1

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY ./layermapping/ /usr/src

COPY requirements.txt /tmp

RUN set -ex; \
	if ! command -v gpg > /dev/null; then \
		apt-get update; \
		apt-get install -y --no-install-recommends \
      git \
			gnupg \
			dirmngr \
		; \
		rm -rf /var/lib/apt/lists/*; \
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

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main $PG_MAJOR" > /etc/apt/sources.list.d/pgdg.list

RUN set -ex \
    && buildDeps=" \
       build-essential \
       libpq-dev \
    " \
    && deps=" \
       gdal-bin \
       gettext \
       postgis \
       postgresql-client-$PG_MAJOR=$PG_VERSION \
    " \
    && apt-get update && apt-get install -y $buildDeps $deps --no-install-recommends \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && apt-get purge -y --auto-remove $buildDeps \
       $(! command -v gpg > /dev/null || echo 'gnupg dirmngr') \
    && rm -rf /tmp/requirements.txt /var/lib/apt/lists/*

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
