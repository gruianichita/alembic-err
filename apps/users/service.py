from apps.db import Session


class UserService:
    @staticmethod
    async def retrieve(session: Session, user_id: int) -> dict:
        return {'lol': 'kek', 'user_id': user_id}