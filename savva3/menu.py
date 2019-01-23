from django.urls import reverse_lazy as reverse
from events.models import Event
from base.models import Video, Book, Course
from jokes.models import Joke
from savva3.utils import template_mtime, model_mtime



MATHERIALS = [

	{
	'title': 'Видеозаписи',
	'url': reverse('base:videos'),
	'hint': 'Взять и изучить!',
	'changefreq': 'weekly',
	'priority': 0.8,
	'lastmod': model_mtime(Video)
	},

	{
	'title': 'Книги',
	'url': reverse('base:books'),
	'hint': 'Рекомендуемые книги по математике, физике',
	'changefreq': 'monthly',
	'priority': 0.5,
	'lastmod': model_mtime(Book)
	},

	{
	'title': 'Курсы',
	'url': reverse('base:courses'),
	'hint': 'Полномасштабные видеокурсы',
	'changefreq': 'monthly',
	'priority': 0.5,
	'lastmod': model_mtime(Course)
	},

        {
            'title': 'Курсы лекций',
            'url': reverse('list'),
            'hint': 'Курсы лекций',
            'changefreq': 'yearly',
            'priority': 0.5,
        }
]



TOP_MENU = [

	{
	'title': 'Лекции',
        # Переадресация происходит в events/views.py
	'url': reverse('events:events'),
        #'url': 'https://wiki.savvateev.xyz/doku.php?id=лекции',
        'target': '_blank',
	'hint': 'Открытые лекции Алексея Савватеева',
	'changefreq': "weekly",
	'priority': 0.8,
	'lastmod': model_mtime(Event)
	},

	{
	'title': 'Материалы',
	'submenu': MATHERIALS,
	},

	{
	'title': '100 уроков',
	'url': reverse('100lessons'),
	'hint': '100 уроков математики',
	'changefreq': 'monthly',
	'priority': 0.5,
	},


	{
	'title': 'Юмор',
	'url': reverse('jokes:index'),
	'hint': 'Замечательная подборка математических шуток',
	'rel': 'nofollow',
	'changefreq': 'monthly',
	'priority': 0.5,
	'lastmod': model_mtime(Joke)
	},

	{
	'title': 'Савватеев',
	'url': reverse('savvateev'),
	'hint': 'Кто такой Савватеев?',
	'changefreq': 'monthly',
	'priority': 0.9,
	'lastmod': template_mtime('pages/savvateev.html'),
	},

	{
	'title': 'Математика для гуманитариев',
	'url': reverse('savva_book'),
	'hint': 'Книга Алексея Савватеева для представителей гуманитарных специальностей (скачать)',
	'changefreq': 'yearly',
	'priority': 0.8,
	'lastmod': template_mtime('pages/savva_book.html')
	},

        {
                'title': 'Вики',
                'url': 'https://wiki.savvateev.xyz/',
                'hint': 'Публичная вики',
        },

	{
	'title': 'Пригласить',
	'url': reverse('events:invite'),
	'hint': 'Пригласить Алексея Савватеева с лекцией в ваш город',
	'changefreq': 'yearly',
	'priority': 0.8,
	'lastmod': template_mtime('events/invite.html'),
	'class': 'ml-1 btn btn-outline-warning my-0'
	}
]


BOTTOM_MENU = [
	{
	'title': 'Участие',
	'hint': 'Как поучаствовать в проекте',
	'url': reverse('participate'),
	'changefreq': 'monthly',
	'priority': 0.5,
	'lastmod': template_mtime('pages/participate.html')
	},

	{
	'title': 'Команда',
	'hint': 'Кто делает проект?',
        'url': reverse('team'),
        'target': '_blank',
#	'changefreq': 'monthly',
#	'priority': 0.5,
#	'lastmod': template_mtime('pages/team.html')
	},

	{
	'title': 'Благодарности',
	'hint': 'Спасибо всем!',
	'url': reverse('credits'),
	'changefreq': 'monthly',
	'priority': 0.5,
	'lastmod': template_mtime('pages/credits.html')
	},

	{
	'title': 'Карта сайта',
	'hint': 'Чтобы не потеряться!',
	'url': reverse('sitemap'),
	'changefreq': 'monthly',
	'priority': 0.5
	}

]

