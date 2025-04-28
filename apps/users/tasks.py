from celery import shared_task
from django.core.mail import send_mail

from core import settings


@shared_task
def send_email():
    send_mail(
        subject="Hello",
        message=f"Hello!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['azimkulovarita019@gmail.com', 'dastiw1910@gmail.com'],
        fail_silently=False,
    )
