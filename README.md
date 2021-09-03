# Questionnaire
Документация API (автодокументирование на swagger (drf-yasg) доступно по адресу http://127.0.0.1:8000/swagger/ )


Окружение проекта:
python 3.9
Django 3.2.6
djangorestframework
Склонируйте репозиторий с помощью git

https://github.com/MaximGST/Questionnaire.git
Перейти в папку:

cd Questionnaire

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Выполнить следующие команды:


Команда для создания миграций приложения для базы данных

python manage.py makemigrations

python manage.py migrate
Создание суперпользователя
python manage.py createsuperuser
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль: по умолчанию почта speccy.rom@yandex.ru пароль: 123456

Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
Команда для запуска приложения
python manage.py runserver
