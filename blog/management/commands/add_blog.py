from django.core.management.base import BaseCommand

from blog.models import Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        Article.objects.all().delete(),


        # fruits = Blog.objects.create(title='фрукты')
        # vegetables = Blog.objects.create(title='овощи')
        # berry = Blog.objects.create(title='ягоды')
        # meet = Blog.objects.create(title='мясо')
        # fish = Blog.objects.create(title='рыба')

        Article.objects.create(title='банан', content='Желтый', img="/Банан.png")
        Article.objects.create(title='помидор', content='Красный', img='/Помидор.png')
        Article.objects.create(title='орех', content='Коричневый',  img='/Орех.png')
        Article.objects.create(title='баранина', content='Кровавая', img='/Баранина.png')
        Article.objects.create(title='курица', content='Пернатая', img='/Курица.png')
        Article.objects.create(title='килька', content='Скользкая', img='/Рыба.png')
        Article.objects.create(title='черешня', content='Красненькая', img='/Черешня.png')
        Article.objects.create(title='клубника', content='Розовая', img='/Клубника.png')






