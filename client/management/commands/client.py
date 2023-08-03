from django.core.management.base import BaseCommand

from client.models import Client
class Command(BaseCommand):
    def handle(self, *args, **options):
        Client.objects.all().delete()

        Client.objects.create(first_name="Феликс", last_name="Зимин", second_name="Юлианович",
                              email="germanstarinenko@gmail.com")
        Client.objects.create(first_name="Георгий", last_name="Евсеев", second_name="Семёнович",
                              email="germanstarinenko2001@gmail.com")
        Client.objects.create(first_name="Анатолий", last_name="Пестов", second_name="Романович",
                              email="margoonavt@yandex.ru")
        Client.objects.create(first_name="Никифор", last_name="Меркушев", second_name="Аристархович",
                              email="uiquoimasoitro-5785@yopmail.com")
        Client.objects.create(first_name="Виктор", last_name="Щербаков", second_name="Платонович",
                              email="o@outlook.com")
