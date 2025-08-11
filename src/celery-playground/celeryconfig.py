import os

rabbitmq_username = os.environ.get("RABBITMQ_USERNAME", "guest")
rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD", "guest")
rabbitmq_host = os.environ.get("RABBITMQ_HOST", "localhost")
rabbitmq_port = os.environ.get("RABBITMQ_PORT", "5672")
rabbitmq_virtual_host = os.environ.get("RABBITMQ_VIRTUAL_HOST", "/")

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = os.environ.get("REDIS_PORT", "6379")
redis_database = os.environ.get("REDIS_DATABASE", "0")

broker_url = f"amqp://{rabbitmq_username}:{rabbitmq_password}@{rabbitmq_host}:{rabbitmq_port}/{rabbitmq_virtual_host}"
result_backend = f"redis://{redis_host}:{redis_port}/{redis_database}"
# broker_url = "amqp://guest:guest@localhost:5672//"
# result_backend = "redis://localhost:6379/0"
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "UTC"
enable_utc = True
