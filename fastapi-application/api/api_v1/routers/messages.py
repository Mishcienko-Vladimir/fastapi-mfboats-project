from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from api.api_v1.routers.fastapi_users import (
    current_active_user,
    current_active_superuser,
)

from core.config import settings
from core.models import User
from core.schemas.user import UserRead


router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],
)


@router.get("/error")
def view_may_raise_error(
    raise_error: bool = False,
):
    """Для проверки обработчика ошибок, ValidationError"""
    if raise_error:
        # 1 / 0
        UserRead.model_validate(None)
    return {"ok": True}


@router.get("")
def get_user_messages(
    user: Annotated[
        User,
        Depends(current_active_user),
    ],
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[
        User,
        Depends(current_active_superuser),
    ],
):
    return {
        "messages": ["secret-m1", "secret-m2", "secret-m3"],
        "user": UserRead.model_validate(user),
    }
