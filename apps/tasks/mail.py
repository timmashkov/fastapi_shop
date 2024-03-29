import smtplib
from email.message import EmailMessage

from celery import Celery

from core.config import settings, logger

celery = Celery("tasks", broker=f"redis://{settings.redis_host}:{settings.redis_port}")


def get_email_template_dashboard(username: str) -> EmailMessage:
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
def send_email_report_dashboard(username: str) -> None:
    logger.info("Celery task works")
    try:
        email = get_email_template_dashboard(username)
        with smtplib.SMTP_SSL(settings.MAIL_SERVER, settings.MAIL_PORT) as server:
            server.login(settings.MAIL_USERNAME, settings.GOOGLE_API_PASS)
            server.send_message(email)
        logger.info(f"Message to {username} has been sent")
    except Exception as e:
        logger.error(f"Error {e} has been raised")
