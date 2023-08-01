from django.core.management import BaseCommand

from mail_sender.services import check_mail_sender


class Command(BaseCommand):

    def handle(self, *args, **options):
        check_mail_sender()