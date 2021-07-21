from fastapi import FastAPI

from .routes import register_routes


def create_app(config="dev"):
    app = FastAPI(title="Api")

    register_routes(app)

    @app.get("/health")
    def health():
        return {"status": "healthy"}

    return app
