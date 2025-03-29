# Skystore

## Описание
Skystore — это интернет-магазин для продажи плагинов и примеров кода. Проект создан на Django и использует Bootstrap для стилизации страниц.

## Функциональность
- Главная страница с информацией о сервисе.
- Страница контактов с формой обратной связи.
- Обработка формы обратной связи и вывод сообщения об успешной отправке.
- Подключение статических файлов (Bootstrap стили и скрипты).

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/ValeriiVolynchikov/DjangoProjects.git
   
   ```
2. Создайте и активируйте виртуальное окружение (рекомендуется):
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   poetry install
   ```
4. Запустите сервер разработки:
   ```sh
   python manage.py runserver
   ```
5. Откройте в браузере: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Структура проекта
```
DjangoProjects/
├── config/                # Конфигурация Django-проекта
│   ├── settings.py        # Основные настройки проекта
│   ├── urls.py            # Основные маршруты проекта
│   ├── wsgi.py            # Точка входа для WSGI
│
├── catalog/               # Приложение интернет-магазина
│   ├── templates/         # HTML-шаблоны
│   │   ├── home.html      # Главная страница
│   │   ├── contacts.html  # Страница контактов
│   ├── migrations.py      # Директория приложения файлов миграции СБД
│   ├── views.py           # Контроллеры (обработка страниц и формы)
│   ├── urls.py            # Маршруты приложения
│   ├── photo/             # Папка хранения изображений продуктов
│   ├── management/        # Пакет приложения кастомной команды
│   ├───__init__.py
│       └───commands/
│           ├───__init__.py
│           └───add_products.py
├── static/                # Статические файлы (CSS, JS, изображения)
│   ├── css/bootstrap.min.css
|   ├── js/bootstrap.min.css
├── screenchots/           # Скриншоты выполнения Django shell
│
├── manage.py              # Основной файл управления Django-проектом
├── .env                   # Файл для хранения переменных среды и конфиденциальной информации
├── requirements.txt       # Список зависимостей
├── README.md              # Документация проекта
```

## Использование
- Перейдите на `/home/` для просмотра главной страницы.
- Перейдите на `/contacts/` для формы обратной связи.
- Заполните форму и отправьте сообщение, система уведомит об успешной отправке.

## Требования
- Python 3.8+
- Django 4+
- Bootstrap (подключается через статические файлы)

## Лицензия
Проект распространяется под свободной лицензией.
