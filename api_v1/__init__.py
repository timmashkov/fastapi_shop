from fastapi import APIRouter
from .products.views import router as products_router
from .users.views import router as users_router
from .profiles.views import router as profile_router

router = APIRouter(
    prefix='/api_v1'
)

router.include_router(router=products_router)
router.include_router(router=users_router)
router.include_router(router=profile_router)
