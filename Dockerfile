FROM python:3.7.9 AS poetry
RUN pip install poetry==1.1.4
WORKDIR /app

FROM poetry AS python-environment
COPY *.toml *.lock ./
RUN poetry config virtualenvs.create false && poetry install

FROM python-environment AS app
COPY . .
ENTRYPOINT ["python3", "app.py"]