# Celery playground

This project is a playground for learning Celery.

## Get started

Create and activate a Python virtual environment:

```shell
uv venv -p 3.13 .venv
. .venv/bin/activate
```

Install project dependencies

```shell
uv sync --no-install-project --all-extras --all-group
```

Reuse a template for Compose environment variables:

```shell
cp compose/.env.template compose/.env
```

Start broker, result backend and flower using Docker Compose:

```shell
docker compose -f compose/compose.yaml up -d
```

Assuming using the default values in the `.env` file, you can access
those URLs:

- Celery Flower: [http://localhost:5555](http://localhost:5555)
- RabbitMQ management: [http://localhost:15672](http://localhost:15672)

Connection URL to services:

- RabbitMQ (broker): `amqp://guest:guest@localhost:5672//`
- Redis (result backend): `redis://localhost:6379/0`

Assert the `src` directory is in your `PYTHONPATH`:

```shell
export PYTHONPATH=$PYTHONPATH:"${PWD}/src"
```

Locally start a worker:

```shell
celery -A celery-playground.worker worker --loglevel=info
```

Locally start a Python module that send a workflow to Celery:

```shell
python -m celery-playground
```

To stop services:

```shell
docker compose -f compose/compose.yaml down -v
```

## TODO

- Find a way to automatically set the `PYTHONPATH` (uv/_pyproject.toml_?),
- Create Compose services for the worker and the workflow creation script,
- Add black and ruff configurations (_pyproject.toml_).
