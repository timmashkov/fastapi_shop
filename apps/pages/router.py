from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from apps.users.views import show_users

router = APIRouter(
    prefix="/pages",
)

templates = Jinja2Templates(directory="apps/templates")


@router.get('/base')
def get_base(request: Request):
    return templates.TemplateResponse("base.html", context={"request": request})


@router.get('/search/{id}')
def get_search(request: Request, users=Depends(show_users)):
    return templates.TemplateResponse("search.html",
                                      context={"request": request,
                                               "users": users})
