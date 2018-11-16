from django.utils.translation import gettext as _
from django.shortcuts import reverse



TOP_MENU = [

	{
	'title': 'Лекции',
	'url': reverse('events:events'),
	'hint': 'Открытые лекции Алексея Савватеева',
	},

	{
	'title': 'Видеозаписи',
	'url': reverse('base:videos'),
	'hint': 'Видеозаписи лекций',
	},

	{
	'title': 'Книги',
	'url': reverse('base:books'),
	'hint': 'Рекомендуемые книги по математике, физике',
	},

	{
	'title': 'Анекдоты',
	'url': reverse('jokes:index'),
	'hint': 'Замечательная подборка математических шуток',
	},

	{
	'title': 'Савватеев',
	'url': reverse('savvateev'),
	'hint': 'Кто такой Савватеев?'
	},

	{
	'title': 'Математика для гуманитариев',
	'url': '/book/',
	'hint': 'Книга Алексея Савватеева для представителей гуманитарных специальностей'
	},
]


BOTTOM_MENU = [
	{
	'title': 'Участие',
	'hint': 'Как поучаствовать в проекте',
	'url': reverse('participate'),
	},

	{
	'title': 'Команда',
	'hint': 'Кто делает проект?',
	'url': reverse('team'),

	},

	{
	'title': 'Благодарности',
	'hint': 'Спасибо всем!',
	'url': reverse('credits'),
	},

	{
	'title': 'Карта сайта',
	'hint': 'Чтобы не потеряться!',
	'url': '/sitemap/',
	}

]