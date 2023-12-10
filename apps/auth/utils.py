import smtplib
from email.message import EmailMessage

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.database import vortex
from core.models import User


async def get_user_db(
    session: AsyncSession = Depends(vortex.session_dependency),
):
    """
    Func for working with database
    :param session:
    :return:
    """
    yield SQLAlchemyUserDatabase(session, User)


def get_email(username: str):
    email = EmailMessage()
    email["Subject"] = "Thanx for using my service"
    email["From"] = settings.MAIL_FROM
    email["To"] = settings.MAIL_USERNAME

    email.set_content(
        "<div>"
        f'<h1 style="color: red;">Здравствуйте, {username}, спасибо что Вы с нами 😊</h1>'
        '<img src="https://ic.pics.livejournal.com/dymontiger/54234047/32891743/32891743_original.jpg'
        "-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app"
        '-mobile-free-vector.jpg" width="600">'
        "</div>",
        subtype="html",
    )
    return email


def send_email(username: str):
    email = get_email(username)
    with smtplib.SMTP_SSL(settings.MAIL_SERVER, settings.MAIL_PORT) as server:
        server.login(settings.MAIL_USERNAME, settings.GOOGLE_API_PASS)
        server.send_message(email)
