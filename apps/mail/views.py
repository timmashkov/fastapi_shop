from fastapi import APIRouter, BackgroundTasks, UploadFile, File, Form
from fastapi_mail import MessageSchema, MessageType, FastMail
from pydantic import EmailStr
from starlette.responses import JSONResponse

from apps.mail.data import conf
from apps.mail.schemas import EmailSchema
from core.config import logger

router = APIRouter(prefix="/mail")


@router.post("/email", description="Just sending email")
async def simple_send(email: EmailSchema, text: str) -> JSONResponse:
    html = f"""<p>{text}</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.model_dump().get("email"),
        body=html,
        subtype=MessageType.html,
    )

    fm = FastMail(conf)
    try:
        await fm.send_message(message)
        logger.info(f"Message {message} has been sent")
        return JSONResponse(status_code=200, content={"message": "email has been sent"})
    except Exception as e:
        logger.error(f"Error {e} has been raised")


# as background task
@router.post("/email_background", description="Sending email as background")
async def send_in_background(
    background_tasks: BackgroundTasks, email: EmailSchema
) -> JSONResponse:
    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=email.model_dump().get("email"),
        body="Simple background task",
        subtype=MessageType.plain,
    )

    fm = FastMail(conf)
    try:
        background_tasks.add_task(fm.send_message, message)
        logger.info(f"Message {message} has been sent")
        return JSONResponse(status_code=200, content={"message": "email has been sent"})
    except Exception as e:
        logger.error(f"Error {e} has been raised")


@router.post("/file", description="Sending file via email")
async def send_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    email: EmailStr = Form(...),
) -> JSONResponse:
    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=[email],
        body="Simple background task",
        subtype=MessageType.html,
        attachments=[file],
    )

    fm = FastMail(conf)
    try:
        background_tasks.add_task(fm.send_message, message)
        logger.info(f"Message {message} has been sent")
        return JSONResponse(status_code=200, content={"message": "email has been sent"})
    except Exception as e:
        logger.error(f"Error {e} has been raised")
