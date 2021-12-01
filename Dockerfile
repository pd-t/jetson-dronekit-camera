FROM dustynv/jetson-inference:r32.5.0 AS base
RUN python3 -m pip install -U pip \
&& pip3 install poetry==1.1.7

FROM base AS python-environment
ENV LANG C.UTF-8

COPY *.toml *.lock ./
RUN poetry config virtualenvs.create false \
&& poetry install --no-interaction --no-ansi

FROM python-environment AS app
COPY app /app/app
WORKDIR /app
CMD PYTHONPATH="." python3 app/main.py