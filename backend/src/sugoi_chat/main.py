from fastapi import FastAPI
from tortoise import Tortoise

from api.router import router


def create_app():
    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()


@app.on_event('startup')
async def init():
    await Tortoise.init(
        db_url='postgres://sugoi:sugoi@localhost:5432/sugoi',
        modules={'models': ['auth.models']}
    )
    await Tortoise.generate_schemas()
