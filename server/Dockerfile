FROM python:3.11-slim-bullseye as build-stage

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN apt-get update -y \
  && apt-get install curl -y \
  && curl -sSL https://install.python-poetry.org | python3 - \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev \
  && apt-get remove curl -y

COPY src/ /app/

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080 || exit 1

CMD ["gunicorn", "app:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "-b", ":8080"]