from fastapi import APIRouter, Depends

from app.dependencies import get_token_header

from starlette import status
from starlette.responses import JSONResponse

from app.schemes import BankName

from app.mock import banks_mock


router = APIRouter(
    prefix='/bank',
    tags=['bank'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'descriptions': 'Not Found'}},
)


@router.get("/all")
async def get_bank(offset: int = 0, limit: int = 10):
    return JSONResponse(banks_mock.banks[offset: limit])


@router.get("/{bank_name}")
async def get_bank(bank_name: BankName):
    return JSONResponse({'name': bank_name})


@router.get("/connect")
async def connect_bank(bank: str):
    if len(
            set.intersection(
                {x["name"] for x in banks_mock.banks},
                {bank}
            )
    ) > 0:
        return JSONResponse({
            'status': status.HTTP_200_OK,
            'msg': 'OK'
        })
    else:
        return JSONResponse({
            'status': status.HTTP_404_NOT_FOUND,
            'msg': 'Not Found'
        })