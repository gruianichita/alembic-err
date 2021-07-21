def register_routes(app, root="api"):
    from apps.users import register_routes as attach_users

    # Add routes
    attach_users(app)