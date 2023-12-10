import smtplib
from email.message import EmailMessage

from celery import Celery

from core.config import settings


celery = Celery("tasks", broker="redis://localhost:6379")


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email["Subject"] = "Thanx for using my service"
    email["From"] = settings.MAIL_FROM
    email["To"] = settings.MAIL_USERNAME

    email.set_content(
        "<div>"
        f'<h1 style="color: red;">Здравствуйте, {username}, спасибо что Вы с нами 😊</h1>'
        '<img src="https://chert-poberi.ru/wp-content/uploads/proga/111/images1/201705/igor7-25051719443344_39.jpg'
        "-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app"
        '-mobile-free-vector.jpg" width="600">'
        "</div>",
        subtype="html",
    )
    return email


@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(settings.MAIL_SERVER, settings.MAIL_PORT) as server:
        server.login(settings.MAIL_USERNAME, settings.GOOGLE_API_PASS)
        server.send_message(email)


@celery.task
async def get_file(data: str):
    with open("text.txt", "w", encoding="UTF-8") as file:
        file.write(data)
    return {"message": 'Ok'}
