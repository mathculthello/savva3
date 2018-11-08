# Развертывание для разработки

```
# Создаем виртуальное питон-окружение
virtualenv -ppython3 venv
. venv/bin/activate

# Клонируем репозиторий
git clone https://github.com/aeifn/savva3

# Установка зависимостей
cd savva3/
pip install -r requirements.txt

# Тестовые настроки
cp savva3/env_settings.py.example savva3/env_settings.py

# Создание базы данных
./manage.py migrate

# Загружаем тестовые данные в базу данных
./manage.py loaddata dump.json

# Создание пользователя:
./manage.py createsuperuser

#Теперь сайт можно запустить:
./manage.py runserver
```

В браузере:

http://localhost/

http://localhost/admin


Jupyter notebook:

```
./manage.py shell_plus --notebook
```

открыть файл playground.ipynb




# Фронтенд

чтобы собрать фронтенд: yarn add; webpack





# Дополнительно (как что работает)

шаблоны в папках templates

стили в папке webpack/scss

yarn ставит JS зависимости в директорию node_modules

(они описаны в файлах package.json и yarn.lock)

webpack из разрозненных файлов в директории webpacksrc генерирует единый файл со стилями и JS, который подключается к HTML

настройки webpack находятся в файле webpack.config.js

директории allmath base events  features jokes questions содержат приложения (это условно говоря, код разных разедлов сайта)

директория  savva3  - это основное (связующее) приложение. там хранятся все настройки проекта и конфигурация адресов страниц

webpack надо запускать после каждого изменения в коде фронтенда. но можно и запустить его в режиме отслеживания изменений: webpack --mode=development -w
