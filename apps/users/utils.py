from fastapi.templating import Jinja2Templates
import smtplib
from email.message import EmailMessage
from core.config import settings

from celery import Celery

templates = Jinja2Templates(directory="apps/users/templates")


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery("users", broker="redis://localhost:6379")


def get_email(username: str):
    email = EmailMessage()
    email["Subject"] = 'Fastapi'
    email["From"] = settings.smtp_user
    email["To"] = settings.smtp_user
    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
async def send_mail(username: str):
    email = get_email(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(settings.smtp_user, settings.smtp_pass)
        server.send_message(email)
