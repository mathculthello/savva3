from django.urls import reverse_lazy as reverse



TOP_MENU = [

	{
	'title': 'Лекции',
	'url': reverse('events:events'),
	'hint': 'Открытые лекции Алексея Савватеева',
	'changefreq': "weekly",
    'priority': 0.8,
	},

	{
	'title': 'Видеозаписи',
	'url': reverse('base:videos'),
	'hint': 'Взять и изучить!',
	'changefreq': 'weekly',
	'priority': 0.8
	},

	{
	'title': 'Книги',
	'url': reverse('base:books'),
	'hint': 'Рекомендуемые книги по математике, физике',
	'changefreq': 'monthly',
	'priority': 0.5
	},

	{
	'title': 'Анекдоты',
	'url': reverse('jokes:index'),
	'hint': 'Замечательная подборка математических шуток',
	'rel': 'nofollow',
	'changefreq': 'monthly',
	'priority': 0.5
	},

	{
	'title': 'Савватеев',
	'url': reverse('savvateev'),
	'hint': 'Кто такой Савватеев?',
	'changefreq': 'monthly',
	'priority': 0.9,
	'template': 'pages/savvateev.html'
	},

	{
	'title': 'Математика для гуманитариев',
	'url': '/book/',
	'hint': 'Книга Алексея Савватеева для представителей гуманитарных специальностей (скачать)',
	'changefreq': 'yearly',
	'priority': 0.8
	},
]


BOTTOM_MENU = [
	{
	'title': 'Участие',
	'hint': 'Как поучаствовать в проекте',
	'url': reverse('participate'),
	'changefreq': 'monthly',
	'priority': 0.5
	},

	{
	'title': 'Команда',
	'hint': 'Кто делает проект?',
	'url': reverse('team'),
	'changefreq': 'monthly',
	'priority': 0.5
	},

	{
	'title': 'Благодарности',
	'hint': 'Спасибо всем!',
	'url': reverse('credits'),
	'changefreq': 'monthly',
	'priority': 0.5
	},

	{
	'title': 'Карта сайта',
	'hint': 'Чтобы не потеряться!',
	'url': reverse('sitemap'),
	'changefreq': 'monthly',
	'priority': 0.5
	}

]