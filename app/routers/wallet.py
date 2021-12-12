from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
# from web3 import Web3

from starlette import status
from starlette.responses import JSONResponse

from app.dependencies import templates


router = APIRouter(
    prefix='/wallet',
    tags=['wallet'],
    responses={404: {'descriptions': 'Not Found'}},
)


@router.get("/check_wallet")
async def check_wallet(wallet):
    return JSONResponse({
        'result': {
            'msg': 'Checked'
        },
        'status': 'OK'
    })


@router.get("/add", response_class=HTMLResponse)
async def add_page(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})


@router.post("/add")
async def add(data: str = Form(...)):
    # infura_url = 'https://mainnet.infura.io/v3/55a3b0d210fc4136afda985e9063e805'
    # web3 = Web3(Web3.HTTPProvider(infura_url))
    # addres_user = data
    # balance = web3.fromWei(web3.eth.get_balance(addres_user), 'ether')
    # print("addres_user: ->", addres_user, "balance_user: ->", balance)
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
