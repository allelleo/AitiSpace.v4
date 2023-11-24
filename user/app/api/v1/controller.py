from fastapi import APIRouter

from app.models import User

api_v1 = APIRouter()


@api_v1.post('/get_user')
async def get_user(user_id: int):
    user = await User.get(id=user_id)
    return await user.json()
