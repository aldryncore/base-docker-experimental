FROM python:3.5.1

ENV PYTHONUNBUFFERED=1\
    PIP_REQUIRE_VIRTUALENV=false\
    PATH=/virtualenv/bin:/root/.local/bin:$PATH\
    PROCFILE_PATH=/app/Procfile\
    LC_ALL=C.UTF-8\
    LANG=C.UTF-8

COPY stack /stack/base
RUN DEBIAN_FRONTEND=noninteractive /stack/base/install.sh

RUN virtualenv --no-site-packages /virtualenv

ENTRYPOINT ["/tini", "-g", "--"]

ADD Procfile /app/Procfile
CMD ["start", "web"]
