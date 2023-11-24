from tortoise.exceptions import DoesNotExist

from app.exceptions import UserNotFoundByEmail, WrongPassword
from app.models import User
from app.providers import AuthenticationProvider
from app.schemas import SignIn, SignInOutput


async def service_sign_in(data: SignIn) -> SignInOutput:
    try:
        user: User = await User.get(email=data.email)
    except DoesNotExist:
        raise UserNotFoundByEmail

    if user.check_password(data.password):
        token = await AuthenticationProvider.encode_token({
            'user_id': user.id
        })
        return SignInOutput(token=token)

    raise WrongPassword
