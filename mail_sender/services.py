from datetime import datetime, timedelta

from django.core.cache import cache
from django.core.mail import send_mail
from smtplib import SMTPException

from config import settings
from mail_sender.models import SendSettings, EmailLogs


def get_period_days(code):
    table_periods = {
        'OD': 1,
        'OW': 7,
        'OM': 30,
    }
    return table_periods.get(code)


def get_cache(key, model):
    """функция для создания кэша для модели"""
    if settings.CACHE_ENABLED:
        current_cache = cache.get(key)
        if current_cache is None:
            current_cache = model
            cache.set(key, current_cache)
    else:
        current_cache = model
    return current_cache


def check_mail_sender():
    """функция для проверки активных рассылок и создания записи в логах"""
    send_settings = SendSettings.objects.all()
    send_settings = SendSettings.objects.filter(status='CR')
    send_settings = SendSettings.objects.filter(send_time__lte=datetime.now())

    for setting in send_settings:
        #  проверка существования предыдущих записей в логах по каждой рассылке
        try:
            current_log = EmailLogs.objects.get(sender=setting)
            next_send_day = current_log.data_last_sent + timedelta(days=get_period_days(setting.period))
        except:
            current_log = None
            next_send_day = None

        #  если запись есть и указанный период еще не закончился, то пропускаем итерацию
        if current_log and next_send_day.date() > datetime.now().date():
            continue

        subject = setting.message.headliner
        message = setting.message.text
        recipient_list = [customer.email for customer in setting.customer.all()]

        #  блок отправки письма указанным адресатам
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipient_list
                )
            server_respond = 'success'
            print(f'Рассылка "{setting}" успешно отправлена')
        except SMTPException as msg:
            server_respond = f'error code: {msg}'
        except:
            server_respond = f'unknown error'

        status_issue = True if server_respond == 'success' else False

        #  блок обновления или создание записи в логах
        if current_log:
            current_log.data_last_sent = datetime.now()
            current_log.status_issue = status_issue
            current_log.server_respond = server_respond
            current_log.save()
        else:
            EmailLogs.objects.create(data_last_sent=datetime.now(), status_issue=status_issue, server_respond=server_respond, sender=setting)

