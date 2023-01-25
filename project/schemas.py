#fastapi se ayuda de pydantic para validar los datos de entrada y salida
#aqui definimos n cantidad de modelos para validar datos
from pydantic import BaseModel
from pydantic import validator
from pydantic.utils import GetterDict

from typing import Any

from peewee import ModelSelect


#La clase permite convertir el objeto de tipo model de peewee a un diccionario tipo UserResponseModel
class PeeweeGetterDict(GetterDict):
    def get(self,key:Any, default: Any=None ):
        res = getattr(self._obj,key, default)
        if isinstance(res, ModelSelect):
            return list(res)

        return res

class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

#--------------------------- USER ----------------------------------------

#al crear un objeto este debe complir con todos los parametros y las validaciones
class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('La longitud debe encontrarse entre 3 y 50 caracteres')

        return username

class UserResponseModel(ResponseModel):
    id: int
    username: str

#------------------- MOVIE ----------------------------------------

class MovieResponseModel(ResponseModel):
    id:int
    title:str

#------------------- REVIEW ----------------------------------------

class ReviewValidator():

    @validator('score')
    def score_validator(cls, score):
        if score < 1 or score > 5:
            raise ValueError('El valor debe ser entre 1 y 5')

        return score



class ReviewRequestModel(BaseModel, ReviewValidator):
    user_id : int
    movie_id : int
    review : str
    score : int



class ReviewResponseModel(ResponseModel):
    id: int
    movie : MovieResponseModel
    review : str
    score : int

class ReviewRequestPutModel(BaseModel,ReviewValidator):
    review : str
    score : int


