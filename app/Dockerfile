FROM python:3.7.9 AS poetry
RUN pip install poetry==1.1.4

FROM poetry AS python-environment
COPY *.toml *.lock ./
RUN poetry config virtualenvs.create false && poetry install

FROM python-environment AS app
WORKDIR /app
COPY . .
