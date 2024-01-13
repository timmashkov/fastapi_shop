from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from apps.auth import current_user
from apps.tasks.mail import send_email_report_dashboard
from core.config import logger

router = APIRouter(prefix="/tasks")


@router.get("/sending_mail", description="Sending thanxgivin email to user")
@cache(expire=60)
def sending_mail(user=Depends(current_user)):
    try:
        send_email_report_dashboard.delay(user.username)
        return {"status": 200, "data": "Email has been sent", "details": None}
    except Exception as e:
        logger.error(f"Error {e} has been raised")
