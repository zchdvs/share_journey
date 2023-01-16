from fastapi import APIRouter

router = APIRouter(
    prefix="/midjourney",
    tags=["midjourney"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def test():
    return 'asdf'