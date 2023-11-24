from app.types import TUser


async def check_unique_username(user_model: TUser, username: str) -> bool:
    if await user_model.exists(username=username):
        return False
    return True


async def check_unique_email(user_model: TUser, email: str) -> bool:
    if await user_model.exists(email=email):
        return False
    return True
