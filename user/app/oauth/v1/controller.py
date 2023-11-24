from fastapi import APIRouter, Request

from app.oauth.v1.descriptions import sign_up_description
from app.oauth.v1.service.up import service_sign_up
from app.oauth.v1.service.sin import service_sign_in
from app.schemas import SignUp, SignUpOutput, SignIn, SignInOutput

oauth_v1 = APIRouter()


@oauth_v1.post('/sign-up', description=sign_up_description)
async def sign_up(r: Request, data: SignUp) -> SignUpOutput:
    return await service_sign_up(data)


@oauth_v1.post('/sign-up/vk')
async def sign_up_vk(r: Request):
    return


@oauth_v1.post('/sign-up/google')
async def sign_up_google(r: Request):
    return


@oauth_v1.post('/sign-in')
async def sign_in(r: Request, data: SignIn) -> SignInOutput:
    return await service_sign_in(data)


@oauth_v1.post('/sign-in/vk')
async def sign_in(r: Request):
    return


@oauth_v1.post('/sign-in/google')
async def sign_in(r: Request):
    return
