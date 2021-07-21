from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Unicode,
    func,
)

from apps.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, nullable=False, server_default=func.now())
    last_login_date = Column(DateTime, server_default=func.now())
    email = Column(String(250), nullable=False)

    name = Column(Unicode(250, collation="utf8mb4_unicode_ci"), nullable=False)
    phone_number = Column(String(250), nullable=True)
    address = Column(Unicode(1500, collation="utf8mb4_unicode_ci"), nullable=True)
    cognito_username = Column(String(250), nullable=True)
    hubspot_contact_id = Column(String(250), nullable=True)
    country = Column(String(80), nullable=True)
