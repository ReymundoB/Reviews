from fastapi import FastAPI
from fastapi import APIRouter

from project.database import database as connection
from project.database import User,Movie,UserReview


from project.routers import user_router
from project.routers import review_router


app=FastAPI(title='Proyecto para reseñar peliculas',
            description='En este proyecto podremos crear, leer, actualizar y eliminar reseñas. Aplica para usuarios'
                        ' autenticados y anónimos',
            version='1.0.0')

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)

app.include_router(api_v1)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables([User,Movie,UserReview])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

#
# @app.get('/')
# async def index():
#     return 'Hola mundo, desde un servidor API'
#
# @app.get('/test')
# async def test():
#     return 'Hola mundo, desde un test'


