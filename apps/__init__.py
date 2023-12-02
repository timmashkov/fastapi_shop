from fastapi import APIRouter
from .products.views import router as products_router
from .users.views import router as users_router
from .profiles.views import router as profiles_router
from .posts.views import router as posts_router

router = APIRouter(prefix="/apps")

router.include_router(router=products_router, tags=["Products"])
router.include_router(router=users_router, tags=["Users"])
router.include_router(router=profiles_router, tags=["Profiles"])
router.include_router(router=posts_router, tags=["Posts"])
