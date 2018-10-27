# Развертывание для разработки

```
git clone https://github.com/aeifn/savva3

# Создаем виртуальное питон-окружение
virtualenv -ppython3 venv
. venv/bin/activate

# Установка зависимостей
cd savva3/
pip install -r requirements.txt

# Тестовые настроки
cp savva3/env_settings.py.example savva3/env_settings.py

# Создание базы данных
./manage.py migrate
```

Создание пользователя:

```
./manage.py createsuperuser
```

Теперь сайт можно запустить:

```
./manage.py runserver
```

В браузере:

http://localhost/

http://localhost/admin
