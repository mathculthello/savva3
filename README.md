# Развертывание для разработки

```
# Клонируем репозиторий
git clone https://github.com/aeifn/savva3

# Создаем виртуальное питон-окружение
virtualenv -ppython3 venv
source ./venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
npm install

# Создание базы данных
./manage.py migrate

# Создание пользователя:
./manage.py createsuperuser

npm run dev

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

# Фронтенд

Чтобы собрать фронтенд:
```
npm install
npm run dev
```

# TODO

[TODO](TODO.md)

# Что где находится

шаблоны в папках templates.

стили в папке webpack-src/scss.

yarn ставит JS зависимости в директорию node_modules

(зависимости описаны в файлах package.json и yarn.lock)

webpack из разрозненных файлов в директории webpack-src генерирует единый файл со стилями и JS, который подключается к шаблонам

настройки webpack находятся в файле webpack.config.js

директории allmath base events features jokes questions содержат приложения (это условно говоря, код разных разделов сайта)

директория  savva3  - это основное (связующее) приложение. там хранятся все настройки проекта и конфигурация адресов страниц

webpack надо запускать после каждого изменения в коде фронтенда. но можно и запустить его в режиме отслеживания изменений: webpack --mode=development -w
