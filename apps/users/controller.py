from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from apps.db import Session, get_sql_db
from apps.users.service import UserService

router = InferringRouter()


@cbv(router)
class UserController:
    session: Session = Depends(get_sql_db)
    user_service: UserService = Depends(UserService)

    @router.get("/{user_id}")
    async def retrieve(self, user_id: int) -> dict:
        res: dict = await self.user_service.retrieve(self.session, user_id)
        return res
