from datetime import datetime
from typing import Optional
from pydantic import BaseModel, HttpUrl
from enum import Enum
from fastapi import Query


class BankName(str, Enum):
    ros = 'ros-bank'
    sber = 'sber-bank'


class Banks(BaseModel):
    name: str
    connect: HttpUrl


class User(BaseModel):
    email: str
    password: str
    name: str
    description: Optional[str] = None
