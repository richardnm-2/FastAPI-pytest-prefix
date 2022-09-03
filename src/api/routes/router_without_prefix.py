from fastapi import APIRouter, Depends


router = APIRouter()


@router.get('/test')
async def router_with_prefix():
    return 'PREFIX IN INCLUDE ROUTER', 200
