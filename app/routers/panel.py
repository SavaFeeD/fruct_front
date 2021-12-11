from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from starlette import status
from starlette.responses import JSONResponse

from app.dependencies import templates


router = APIRouter(
    prefix='/panel',
    tags=['panel'],
    responses={404: {'descriptions': 'Not Found'}},
)


@router.get("/", response_class=HTMLResponse)
async def panel(request: Request):
    return templates.TemplateResponse("panel.html", {
        "request": request,
        "wallet": {
            "hash": "dqwdadsdsad",
            "balance": "0.03123"
        }
    })

