from fastapi import APIRouter

router = APIRouter(
    prefix="/discord",
    tags=["discord"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def test():
    return 'asdf'