from fastapi import FastAPI

from api.v1.routers import user,post

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
