FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    pip install --upgrade pip && \
    pip install poetry && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock* /code/

RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

COPY . /code

EXPOSE 8000
