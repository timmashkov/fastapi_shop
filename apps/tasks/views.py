from fastapi import APIRouter, BackgroundTasks, Depends, Form
from fastapi_cache.decorator import cache

from apps.auth import current_user
from apps.tasks.mail import send_email_report_dashboard, get_file

router = APIRouter(prefix="/tasks")


@router.get("/dashboard")
@cache(expire=60)
def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    # 1400 ms - Клиент ждет
    send_email_report_dashboard(user.username)
    # 500 ms - Задача выполняется на фоне FastAPI в event loop'е или в другом треде
    background_tasks.add_task(send_email_report_dashboard, user.username)
    # 600 ms - Задача выполняется воркером Celery в отдельном процессе
    send_email_report_dashboard.delay(user.username)
    return {"status": 200, "data": "Письмо отправлено", "details": None}


@router.post("/add_file")
async def add_file(text: str):
    return await get_file(data=text)
