from fastapi import APIRouter

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int


router = APIRouter(
    prefix="/users", tags=["Users"], responses={404: {"message": "No encontrado"}}
)
# PARA INICIAR EL SERVIDOR python -m uvicorn users:app --reload
# DOCUMENTACION http://127.0.0.1:8000/redoc o http://127.0.0.1:8000/docs#/ (esta ultima es swagger)

users_list = [
    User(id=1, name="giuliano", surname="pisarra", age=29),
    User(id=2, name="guido", surname="pisarra", age=35),
]


@router.get("/")
async def users():
    return users_list


@router.get("/{id}")
async def user(id: int):
    return search_user(id)


@router.get("/")
async def user(id: int):
    return search_user(id)


@router.post("/", response_model=User, status_code=201)
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(
            status_code=404, detail="Usuario existente"
        )  # CUIDADO CAMBIAR EL ERROR

    users_list.append(user)
    return user


@router.put("/")
async def update_user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
        return user
    if not found:
        return {"error": "No se actualizo el usuario"}


@router.delete("/{id}")
async def delete_user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return {"message": "Usuario eliminado"}
    if not found:
        return {"error": "No se eliminó el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "usuario inexistente"
