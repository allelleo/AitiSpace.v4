from fastapi import HTTPException
from starlette.status import (
    HTTP_409_CONFLICT, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
)

from app.enums import LogCode
from app.logger import get_logger

logger = get_logger()


class UniqueUsername(HTTPException):
    def __init__(self):
        logger.INFO(message='Unique username', code=LogCode.register_unique_username)
        super().__init__(
            status_code=HTTP_409_CONFLICT,
            detail={
                'code': 1,
                'message': 'Unique username'
            }
        )


class UniqueEmail(HTTPException):
    def __init__(self):
        logger.INFO(message='Unique email', code=LogCode.register_unique_email)
        super().__init__(
            status_code=HTTP_409_CONFLICT,
            detail={
                'code': 2,
                'message': 'Unique email'
            }
        )


class NotFoundAuthTypeProvider(HTTPException):
    def __init__(self):
        logger.CRITICAL(message='Not found default auth type provider!')
        super().__init__(
            status_code=HTTP_404_NOT_FOUND,
            detail={
                'code': 3,
                'message': 'Not found auth type provider'
            }
        )


class DBConnection(HTTPException):
    def __init__(self):
        logger.CRITICAL(message='Cannot connect to database!')
        super().__init__(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                'code': 4,
                'message': 'Cannot connect to database'
            }
        )


class TransactionManagement(HTTPException):
    def __init__(self):
        logger.CRITICAL('Transaction Management Error!')
        super().__init__(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                'code': 5,
                'message': 'Database transaction error'
            }
        )


class Unknown(HTTPException):
    def __init__(self, e):
        logger.CRITICAL(f'Unknown exception: {e}')
        super().__init__(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                'code': 6,
                'message': 'Unknown error'
            }
        )


class UserNotFoundByEmail(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTP_404_NOT_FOUND,
            detail={
                'code': 7,
                'message': 'User not found by email'
            }
        )


class WrongPassword(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTP_404_NOT_FOUND,
            detail={
                'code': 9,
                'message': 'Wrong user password'
            }
        )
