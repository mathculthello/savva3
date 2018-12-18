from django.db import models
import abc

JOKES = 'jokes.Joke'
TYPE_CHOICES = (
    (JOKES, 'Jokes'),
)

class RatingBase(models.Model):
    __metaclass__ = abc.ABCMeta
    rating = models.IntegerField(default=0)

    @abc.abstractmethod
    def update_rating(self, inc_value):
        self.rating = self.rating + inc_value
        self.save()

    @abc.abstractmethod
    def get_rating(self):
        # rating = Rating.objects.get(
        #     rating_type='{}.{}'.format(self.)
        # )
        # self.rating = self.rating + inc_value
        return 0

    class Meta:
        abstract = True

class Rating(models.Model):
    rating_type = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES,
        verbose_name="Тип"
    )
    iid = models.IntegerField(
        verbose_name="Внешний ключ"
    )
    ip = models.CharField(
        max_length=20,
        verbose_name="IP адрес"
    )
    value = models.IntegerField(
        default=1,
        verbose_name="Голос"
    )
    date = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата голосования"
    )

    @classmethod
    def create(cls, rating_type, iid, value, ip):
        rating = Rating(
            rating_type=rating_type, 
            iid=iid,
            value=value,
            ip=ip,
        )

        rating.save()
        return rating

    def __str__(self):
        return '{} {} {} {} {}'.format(self.rating_type, self.iid, self.value, self.ip, self.date)
