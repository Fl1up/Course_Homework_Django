from django.core.management.base import BaseCommand

from mailing.models import Message


class Command(BaseCommand):
    def handle(self, *args, **options):
        Message.objects.all().delete()

        Message.objects.create(theme="Важно",
                               body="123444")