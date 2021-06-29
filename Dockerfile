FROM python:3.7.9 AS base
RUN pip install poetry==1.1.4

FROM base AS python-environment
WORKDIR /app
COPY *.toml *.lock ./
RUN poetry config virtualenvs.create false && poetry install
ENV PATH=/usr/local/bin:$PATH

FROM python-environment AS app
COPY . .
ENTRYPOINT ["python3", "app.py"]