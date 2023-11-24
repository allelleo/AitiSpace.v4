import jwt

from app import config

type Token = str


class AuthenticationProvider(object):
    @staticmethod
    async def encode_token(data: dict) -> Token:
        try:
            return jwt.encode(data, config.jwt_private.encode('utf-8'), algorithm=config.algorithm)
        except Exception as e:
            raise e

    @staticmethod
    async def decode_token(token: str):
        try:
            return jwt.decode(token, config.jwt_public.encode('utf-8'), algorithms=[config.algorithm], verify=True)
        except Exception as e:
            raise e
