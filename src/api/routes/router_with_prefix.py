from fastapi import APIRouter, Depends


router = APIRouter(prefix='/prefix_in_router')


@router.get('/test')
async def router_with_prefix():
    return 'PREFIX IN ROUTER', 200
