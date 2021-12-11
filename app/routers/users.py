from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse

from starlette import status
from starlette.responses import JSONResponse

from app.schemes import User
from app.dependencies import templates


router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={404: {'descriptions': 'Not Found'}},
)


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    return JSONResponse({
        'result': {
            'user': {'email': email, 'password': password},
            'msg': 'Complete!'
        },
        'status': 'OK',
    })


@router.get("/register", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
async def login(email: str = Form(...), password: str = Form(...)):
    return JSONResponse({
        'result': {
            'user': {'email': email, 'password': password},
            'msg': 'Complete!'
        },
        'status': 'OK',
    })
