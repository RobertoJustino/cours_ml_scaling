from fastapi import FastAPI

from proj.celery_utils import create_celery   # new

def create_app() -> FastAPI:
    app = FastAPI()

    # do this before loading routes              # new
    app.celery_app = create_celery()             # new

    from proj.users import users_router                # new
    app.include_router(users_router)                      # new

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app