from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import os

template = os.path.join(os.path.dirname(__file__), 'templates')
front = APIRouter()
templates = Jinja2Templates(directory=template)


@front.get('/')
async def index(r: Request):
    return templates.TemplateResponse('index.html', {'request': r})
