from fastapi import APIRouter

from pydantic import BaseModel

router = APIRouter(
    prefix="/products", tags=["Products"], responses={404: {"message": "No encontrado"}}
)


@router.get("/")
async def products():
    return "users_list"
