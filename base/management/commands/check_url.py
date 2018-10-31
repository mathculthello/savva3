from django.core.management.base import BaseCommand, CommandError
from base.models import Url
import requests
from bs4 import BeautifulSoup as bs

class Command(BaseCommand):
    help = 'Check urls in base'

    def handle(self, *args, **options):
        try:
            urls = Url.objects.all()
            for url in urls:
                try:
                    response=requests.get(url.url)
                    code = response.status_code
                    url.status_code = code
                    if code == 200:
                        url.url=response.url
                        url.title=bs(response.text,'html.parser').title.text
                    url.save()
                    self.stdout.write(self.style.SUCCESS('%s %s' % (url.status_code,url.url)))
                except:
                    pass

        except Url.DoesNotExist:
            raise CommandError('Poll "%s" does not exist' % poll_id)
