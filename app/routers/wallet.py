from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse

from starlette import status
from starlette.responses import JSONResponse

from app.dependencies import templates


router = APIRouter(
    prefix='/wallet',
    tags=['wallet'],
    responses={404: {'descriptions': 'Not Found'}},
)


@router.get("/add", response_class=HTMLResponse)
async def add_page(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})


@router.post("/add")
async def add(data: str = Form(...)):
    return JSONResponse({
        'result': {
            'data': data,
            'msg': 'Wallet add!'
        },
        'status': 'OK',
    })


@router.get("/create", response_class=HTMLResponse)
async def create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})


@router.post("/create")
async def create(data: str = Form(...)):
    return JSONResponse({
        'result': {
            'data': data,
            'msg': 'Wallet create!'
        },
        'status': 'OK',
    })
