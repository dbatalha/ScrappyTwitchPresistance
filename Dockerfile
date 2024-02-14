FROM python:3.12.1-slim-bookworm

RUN mkdir /scrappy-db
COPY . /scrappy-db
COPY pyproject.toml /scrappy-db

WORKDIR /scrappy-db
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["poetry", "run", "scrappy-db"]