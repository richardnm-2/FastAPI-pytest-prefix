from fastapi import FastAPI
from api.routes.router_without_prefix import router as router_without_prefix
from api.routes.router_with_prefix import router as router_with_prefix

app = FastAPI(
    title='PYTEST PREFIX'
)

app.include_router(
    router_with_prefix,
    tags=['PYTEST PREFIX']
)

app.include_router(
    router_without_prefix,
    prefix='/prefix_in_include',
    tags=['PYTEST PREFIX']
)
