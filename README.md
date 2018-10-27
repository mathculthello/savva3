# Развертывание для разработки

```
git clone https://github.com/aeifn/savva3
virtualenv -ppython3 venv
. venv/bin/activate
cd savva3/
pip install -r requirements.txt
cp savva3/env_settings.py.example savva3/env_settings.py
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
