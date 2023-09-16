from fastapi import FastAPI, APIRouter

app = FastAPI()


router = APIRouter(
    prefix='',
    responses={404: {'description': 'Not found'}}
)


app.include_router(router)
