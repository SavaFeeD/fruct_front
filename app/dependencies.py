from fastapi import Header, HTTPException
from fastapi.templating import Jinja2Templates

from typing import Optional


templates = Jinja2Templates(directory='./app/templates')


async def get_token_header(x_token: Optional[str] = Header(None)):
    if x_token != 'sushka':
        raise HTTPException(status_code=400, detail='X-Token header invalid')


async def get_query_token(token: str):
    if token != 'alex':
        raise HTTPException(status_code=400, detail='No Alex token provided')
