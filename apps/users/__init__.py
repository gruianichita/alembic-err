from .model import User
from .schema import UserSchema

BASE_ROUTE = "users"


def register_routes(app, root="api"):
    from .controller import router as users_router
    app.include_router(users_router, prefix=f"/{root}/{BASE_ROUTE}")
