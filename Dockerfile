# Generate the requeriments.txt with Poetry
FROM python:3.10.5-slim-bullseye as builder

RUN pip install poetry

COPY ./pyproject.toml ./
COPY ./poetry.lock ./

RUN poetry export --without-hashes --dev --format requirements.txt -o /requirements.txt

#----------------------------
FROM python:3.10.5-slim-bullseye

RUN apt-get update
RUN apt-get -y install gcc

# Set env
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip

WORKDIR /code
COPY --from=builder requirements.txt /tmp/

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY ./src /code/src
COPY ./tests /code/tests/
COPY ./pyproject.toml /code/pyproject.toml
