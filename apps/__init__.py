from fastapi import APIRouter
from .products.views import router as products_router
from .users.views import router as users_router
from .profiles.views import router as profiles_router
from .posts.views import router as posts_router
from .orders.views import router as orders_router
from .auth import router as auth_router
from .tasks.views import router as task_router

router = APIRouter(prefix="/apps")

router.include_router(router=products_router, tags=["Products"])
router.include_router(router=users_router, tags=["Users"])
router.include_router(router=profiles_router, tags=["Profiles"])
router.include_router(router=posts_router, tags=["Posts"])
router.include_router(router=orders_router, tags=["Orders"])
router.include_router(router=auth_router, tags=["Auth"])
router.include_router(router=task_router, tags=["Tasks"])
