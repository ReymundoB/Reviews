from fastapi import Cookie
from fastapi import Response
from fastapi import HTTPException, APIRouter

from fastapi.security import HTTPBasicCredentials

from ..database import User

from ..schemas import UserResponseModel, ReviewResponseModel
from ..schemas import UserRequestModel

from typing import List

router = APIRouter(prefix='/users')


                    #aqui indicamos que la respuesta sera serializada, que es el modelo. (serializado=json)
@router.post('', response_model=UserResponseModel)
async def create_user(user:UserRequestModel):

    if User.select().where(User.username == user.username).exists():
        raise  HTTPException(409,'El username se encuentra en uso.')

    hash_password=User.create_password(user.password)

    user=User.create(
        username=user.username,
        password=hash_password
    )

    return user


@router.post('/login', response_model=UserResponseModel)
async def login(credentials:HTTPBasicCredentials, response:Response):
    user = User.select().where(User.username == credentials.username).first()
    if user is None:
        raise  HTTPException(404,'No se encuentra el usuario.')
    if user.password!= User.create_password(credentials.password):
        raise  HTTPException(404,'Contraseña incorrecta.')

    #cracion y asignacion de cookies
    response.set_cookie(key='user_id', value=user.id)

    return  user

@router.get('/reviews',response_model=List[ReviewResponseModel])
async def get_reviews(user_id:int = Cookie(None)):

    user = User.select().where(User.id == user_id).first()
    if user is None:
        raise HTTPException(404,'No se encuentra el usuario.')


    return [user_review for user_review in user.reviews]
