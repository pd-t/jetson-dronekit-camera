FROM dustynv/jetson-inference:r32.5.0 AS base
RUN python3 -m pip install -U pip \
&& pip3 install poetry==1.1.7

FROM base AS python-environment
ENV LANG C.UTF-8
WORKDIR /app
COPY *.toml *.lock ./
RUN poetry config virtualenvs.create false \
&& poetry install --no-interaction --no-ansi

FROM python-environment AS app
COPY . .
ENTRYPOINT ["python3", "app.py"]