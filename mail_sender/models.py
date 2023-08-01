from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}

CHOICES_STATUS = (
    ('CR', 'Created'),
    ('IP', 'In Progress'),
    ('CL', 'Closed'),
)

FREQUENCY_SEND = (
    ('OD', 'Once a day'),
    ('OW', 'Once a week'),
    ('OM', 'Once a month'),
)

# TIME_SEND = (
#     ('00:00', '00:00:00'),
#     ('08:00', '08:00:00'),
#     ('10:00', '10:00:00'),
#     ('12:00', '12:00:00'),
#     ('14:00', '14:00:00'),
#     ('16:00', '16:00:00'),
# )


class Customer(models.Model):
    email = models.CharField(max_length=150, verbose_name='e-mail')
    full_name = models.CharField(max_length=150, verbose_name='фио', **NULLABLE)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    is_blocked = models.BooleanField(default=False, verbose_name='заблокирован')

    def delete(self, *args, **kwargs):
        self.is_blocked = True
        self.save()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'


class ContentEmail(models.Model):
    headliner = models.CharField(max_length=150, verbose_name='тема письма')
    text = models.TextField(verbose_name='текст письма')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Добавлено', **NULLABLE)

    def __str__(self):
        return f'{self.headliner}'

    class Meta:
        verbose_name = 'письмо для рассылки'
        verbose_name_plural = 'письма для рассылки'


class SendSettings(models.Model):

    name = models.CharField(max_length=150, verbose_name='название рассылки')
    send_time = models.TimeField(verbose_name='Время отправки')
    period = models.CharField(max_length=2, choices=FREQUENCY_SEND, default='OM', verbose_name='Частота рассылки')
    status = models.CharField(max_length=2, choices=CHOICES_STATUS, default='CR', verbose_name='Статус')
    message = models.ForeignKey(ContentEmail, on_delete=models.CASCADE, verbose_name='Текст рассылки', **NULLABLE)
    customer = models.ManyToManyField(Customer, verbose_name='Клиенты', **NULLABLE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Добавлено', **NULLABLE)

    def delete(self, *args, **kwargs):
        self.status = 'CL'
        self.save()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылок'


class EmailLogs(models.Model):
    data_last_sent = models.DateTimeField(verbose_name='дата последней рассылки')
    status_issue = models.BooleanField(default=False, verbose_name='статус попытки')
    server_respond = models.CharField(max_length=50, verbose_name='ответ сервера', **NULLABLE)
    sender = models.ForeignKey(SendSettings, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.server_respond}'
