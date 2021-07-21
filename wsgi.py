import os

from apps import create_app

app = create_app(config=os.getenv("ENV") or "test")

