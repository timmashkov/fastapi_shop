from email.mime.text import MIMEText
from smtplib import SMTP_SSL

from celery import Celery
from fastapi import BackgroundTasks
from pydantic import BaseConfig

from core.config import settings
from fastapi_mail import ConnectionConfig, MessageSchema, FastMail

celery = Celery("tasks", broker="redis://localhost:6379")


