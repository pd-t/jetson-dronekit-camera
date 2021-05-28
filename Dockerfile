FROM python:3.7.9 AS base
RUN apt-get update \
&& apt-get install -y --no-install-recommends git \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/* \
&& pip install poetry==1.1.4
WORKDIR /app

FROM base AS python-environment
COPY *.toml *.lock ./
RUN poetry config virtualenvs.create false && poetry install

FROM python-environment AS app
COPY . .
