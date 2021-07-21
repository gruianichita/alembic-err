from typing import Optional

from apps.base import CamelModel


class UserSchema(CamelModel):
    """User schema"""

    id: Optional[int]
    created_date: str
    last_login_date: Optional[str]
    email: str
    name: str
    phone_number: Optional[str]
    address: Optional[str]
    cognito_username: Optional[str]
    hubspot_contact_id: Optional[str]
    country: Optional[str]
