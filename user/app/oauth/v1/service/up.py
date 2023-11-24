from tortoise.exceptions import DoesNotExist, DBConnectionError, TransactionManagementError
from tortoise.transactions import in_transaction

from app.exceptions import Unknown, TransactionManagement, DBConnection, NotFoundAuthTypeProvider, UniqueEmail, \
    UniqueUsername
from app.logger import get_logger
from app.models import (
    User,
    Profile,
    Rating,
    RatingPerWeek,
    RatingPerMonth,
    AuthType,
    AuthTypeProvider
)
from app.providers import AuthenticationProvider
from app.schemas import SignUp, SignUpOutput
from app.utils.unique import check_unique_email, check_unique_username

logger = get_logger()


async def task(email, uuid):
    print(f"Task email {email} with uuid {uuid}")


async def service_sign_up(data: SignUp) -> SignUpOutput:
    if not await check_unique_email(user_model=User, email=data.email):
        raise UniqueEmail
    if not await check_unique_username(user_model=User, username=data.username):
        raise UniqueUsername

    try:
        async with in_transaction() as transaction:
            auth_provider = await AuthTypeProvider.get(title='default')

            profile = await Profile.create(using_db=transaction)
            rating = await Rating.create(using_db=transaction)
            rating_per_week = await RatingPerWeek.create(using_db=transaction)
            rating_per_month = await RatingPerMonth.create(using_db=transaction)

            auth = await AuthType.create(type=auth_provider, using_db=transaction)

            user: User = User(
                username=data.username,
                first_name=data.first_name,
                last_name=data.last_name,
                email=data.email,

                profile=profile,
                rating=rating,
                rating_per_week=rating_per_week,
                rating_per_month=rating_per_month,
                auth_type=auth
            )
            await user.set_password(data.password)
            await user.save()
            email, uuid = await user.get_data_for_validate_email()
            await task(email, uuid)

            token = await AuthenticationProvider.encode_token({
                'user_id': user.id
            })

            logger.INFO(f'Register user with id: {user.id}')

            return SignUpOutput(token=token)
    except DoesNotExist:
        raise NotFoundAuthTypeProvider
    except DBConnectionError:
        raise DBConnection
    except TransactionManagementError:
        raise TransactionManagement
    except Exception as e:
        raise Unknown(str(e))
